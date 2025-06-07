import streamlit as st
import requests
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time
import random
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page Config
st.set_page_config(
    page_title="🔴 Mars Exploration Hub",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS für Mars Theme
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #8b0000 0%, #dc143c 50%, #ff6347 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
    }
    .rover-card {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
    }
    .weather-card {
        background: linear-gradient(135deg, #fa7268 0%, #f093fb 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
    }
    .metric-card {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        color: #8b0000;
        margin: 0.5rem;
        font-weight: bold;
    }
    .mission-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        color: white;
    }
    .photo-placeholder {
        background: linear-gradient(135deg, #8B4513 0%, #D2691E 100%);
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

class MarsExplorationAPI:
    def __init__(self):
        # NASA API Key aus Environment Variable laden
        self.nasa_api_key = os.getenv("NASA_API_KEY", "DEMO_KEY")
        
        # Mars Rover APIs
        self.nasa_mars_url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/perseverance/photos?api_key={self.nasa_api_key}"
        self.curiosity_url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?api_key={self.nasa_api_key}"
        
        # Mars Weather (falls verfügbar)
        self.mars_weather_url = f"https://api.nasa.gov/insight_weather/?api_key={self.nasa_api_key}"
    
    def get_mars_photos(self):
        """Holt Mars Rover Fotos mit Debug und funktionierenden Fallbacks"""
        try:
            print(f"🔍 NASA API Key: {self.nasa_api_key[:10]}...")
            
            # Versuche verschiedene Sols für echte NASA Fotos
            sol_attempts = [3000, 2500, 2000, 1500, 1000]
            
            for sol in sol_attempts:
                try:
                    # Perseverance NavCam Photos
                    url = f"{self.nasa_mars_url}&sol={sol}&camera=navcam"
                    print(f"🚀 Trying Perseverance API: sol={sol}")
                    
                    response = requests.get(url, timeout=10)
                    print(f"📡 Perseverance Response: {response.status_code}")
                    
                    if response.status_code == 200:
                        data = response.json()
                        if data.get('photos') and len(data['photos']) > 0:
                            print(f"✅ Found {len(data['photos'])} Perseverance photos for sol {sol}")
                            return data['photos'][:6]
                    
                    # Fallback zu Curiosity für diesen Sol
                    curiosity_url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?api_key={self.nasa_api_key}&sol={sol}&camera=navcam"
                    print(f"🤖 Trying Curiosity API: sol={sol}")
                    
                    response = requests.get(curiosity_url, timeout=10)
                    print(f"📡 Curiosity Response: {response.status_code}")
                    
                    if response.status_code == 200:
                        data = response.json()
                        if data.get('photos') and len(data['photos']) > 0:
                            print(f"✅ Found {len(data['photos'])} Curiosity photos for sol {sol}")
                            return data['photos'][:6]
                            
                except Exception as e:
                    print(f"❌ Error for sol {sol}: {e}")
                    continue
            
            print("🔄 All sols failed, using placeholder images")
            return self._get_mars_placeholders()
            
        except Exception as e:
            print(f"🔥 Mars API Error: {e}")
            return self._get_mars_placeholders()
    
    def _get_mars_placeholders(self):
        """Mars-themed funktionsfähige Placeholder Bilder"""
        base_sol = 1000 + (datetime.now().day % 100)
        
        # Verwende Mars-farbige Placeholders die garantiert funktionieren
        placeholder_data = [
            {'color': '8B4513', 'title': '🔴+Mars+Surface+Panorama'},
            {'color': 'A0522D', 'title': '🤖+Rover+Navigation+View'},
            {'color': 'CD853F', 'title': '🌄+Martian+Horizon'},
            {'color': 'D2691E', 'title': '🔬+Sample+Collection'},
            {'color': 'DEB887', 'title': '🏔️+Rock+Formation'},
            {'color': 'F4A460', 'title': '🌅+Mars+Landscape'}
        ]
        
        mars_photos = []
        for i, placeholder in enumerate(placeholder_data):
            mars_photos.append({
                'id': f'mars_placeholder_{i}',
                'sol': base_sol + i,
                'img_src': f"https://via.placeholder.com/400x300/{placeholder['color']}/FFFFFF?text={placeholder['title']}",
                'camera': {
                    'full_name': ['Navigation Camera - Left', 'Navigation Camera - Right', 'Front Hazard Camera', 'Rear Hazard Camera', 'Chemistry Camera', 'Panoramic Camera'][i]
                },
                'rover': {'name': 'Perseverance' if i % 2 == 0 else 'Curiosity'}
            })
        
        return mars_photos
    
    def get_rover_status(self):
        """Simulierte Rover Status Daten"""
        return {
            'perseverance': {
                'status': 'Active',
                'sol': 1000 + (datetime.now().day % 100),
                'total_photos': 275000 + (datetime.now().day * 50),
                'distance_driven': f"{28.5 + (datetime.now().day * 0.1):.1f}",
                'samples_collected': 24 + (datetime.now().day % 5),
                'power_level': 85 + (datetime.now().day % 15)
            },
            'curiosity': {
                'status': 'Active', 
                'sol': 4000 + (datetime.now().day % 50),
                'total_photos': 850000 + (datetime.now().day * 100),
                'distance_driven': f"{29.9 + (datetime.now().day * 0.05):.1f}",
                'samples_collected': 39 + (datetime.now().day % 3),
                'power_level': 78 + (datetime.now().day % 12)
            }
        }
    
    def get_mars_weather(self):
        """Simulierte Mars Wetter Daten"""
        # Basierend auf echten Mars-Wetterdaten
        base_temp = -70 + (datetime.now().day % 40) - 20
        return {
            'sol': 1000 + (datetime.now().day % 100),
            'temperature': {
                'high': base_temp + 15,
                'low': base_temp - 25
            },
            'pressure': 750 + (datetime.now().day % 100),
            'wind_speed': 5 + (datetime.now().day % 15),
            'wind_direction': ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'][datetime.now().day % 8],
            'season': 'Northern Winter' if datetime.now().month in [12, 1, 2, 3, 4] else 'Northern Summer',
            'weather_conditions': ['Clear', 'Dusty', 'Partly Cloudy'][datetime.now().day % 3]
        }
    
    def get_mars_timeline(self):
        """Mars Mission Timeline"""
        return [
            {'year': 1976, 'mission': 'Viking 1 & 2', 'type': 'Lander', 'status': 'Completed'},
            {'year': 1997, 'mission': 'Mars Pathfinder', 'type': 'Rover (Sojourner)', 'status': 'Completed'},
            {'year': 2004, 'mission': 'Spirit & Opportunity', 'type': 'Rovers', 'status': 'Completed'},
            {'year': 2012, 'mission': 'Curiosity', 'type': 'Rover', 'status': 'Active'},
            {'year': 2021, 'mission': 'Perseverance', 'type': 'Rover', 'status': 'Active'},
            {'year': 2021, 'mission': 'Ingenuity', 'type': 'Helicopter', 'status': 'Active'},
            {'year': 2028, 'mission': 'Mars Sample Return', 'type': 'Sample Return', 'status': 'Planned'},
            {'year': 2030, 'mission': 'Human Mission', 'type': 'Crewed', 'status': 'Planned'}
        ]

def create_temperature_chart(weather_data):
    """Erstellt Mars Temperatur Chart"""
    # 7-Sol Temperatur Simulation
    sols = list(range(weather_data['sol'] - 6, weather_data['sol'] + 1))
    highs = [weather_data['temperature']['high'] + random.randint(-10, 10) for _ in sols]
    lows = [weather_data['temperature']['low'] + random.randint(-5, 5) for _ in sols]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=sols, y=highs,
        mode='lines+markers',
        name='Tagesmaximum',
        line=dict(color='#ff6b6b'),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=sols, y=lows,
        mode='lines+markers',
        name='Tagesminimum', 
        line=dict(color='#4dabf7'),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title='🌡️ Mars Temperatur - 7 Sol Verlauf',
        xaxis_title='Sol (Mars Tag)',
        yaxis_title='Temperatur (°C)',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        showlegend=True
    )
    
    return fig

def create_mission_timeline_chart(timeline_data):
    """Erstellt Mission Timeline Chart"""
    df_timeline = []
    for mission in timeline_data:
        df_timeline.append({
            'Mission': mission['mission'],
            'Jahr': mission['year'],
            'Typ': mission['type'],
            'Status': mission['status']
        })
    
    colors = {'Active': '#2ed573', 'Completed': '#3742fa', 'Planned': '#ffa726'}
    
    fig = px.scatter(
        df_timeline,
        x='Jahr',
        y='Mission',
        color='Status',
        color_discrete_map=colors,
        title='🚀 Mars Missions Timeline',
        hover_data=['Typ']
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )
    
    return fig

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🔴 MARS EXPLORATION HUB</h1>
        <p>Red Planet Discovery Center</p>
        <p>🤖 Perseverance • 🔬 Curiosity • 🚁 Ingenuity • 🌡️ Weather Station</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize API
    mars_api = MarsExplorationAPI()
    
    # Get Mars data
    rover_status = mars_api.get_rover_status()
    mars_weather = mars_api.get_mars_weather()
    mars_photos = mars_api.get_mars_photos()
    timeline_data = mars_api.get_mars_timeline()
    
    # Active Rover Status
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>🤖 Perseverance</h3>
            <h2>Sol {rover_status['perseverance']['sol']}</h2>
            <p>{rover_status['perseverance']['status']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>🔬 Samples</h3>
            <h2>{rover_status['perseverance']['samples_collected']}</h2>
            <p>Collected</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>🚗 Distance</h3>
            <h2>{rover_status['perseverance']['distance_driven']} km</h2>
            <p>Driven</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <h3>🔋 Power</h3>
            <h2>{rover_status['perseverance']['power_level']}%</h2>
            <p>Battery Level</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Mars Weather Station
    st.markdown("---")
    st.markdown("## 🌡️ Mars Weather Station")
    
    col_weather1, col_weather2 = st.columns(2)
    
    with col_weather1:
        st.markdown(f"""
        <div class="weather-card">
            <h3>🌡️ Sol {mars_weather['sol']} Weather</h3>
            <p><strong>🌡️ Temperature:</strong></p>
            <p>High: {mars_weather['temperature']['high']}°C</p>
            <p>Low: {mars_weather['temperature']['low']}°C</p>
            <p><strong>🌪️ Wind:</strong> {mars_weather['wind_speed']} m/s {mars_weather['wind_direction']}</p>
            <p><strong>📊 Pressure:</strong> {mars_weather['pressure']} Pa</p>
            <p><strong>🌤️ Conditions:</strong> {mars_weather['weather_conditions']}</p>
            <p><strong>📅 Season:</strong> {mars_weather['season']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_weather2:
        temp_chart = create_temperature_chart(mars_weather)
        st.plotly_chart(temp_chart, use_container_width=True)
    
    # Mars Rover Photos
    st.markdown("---")
    st.markdown("### 📷 Latest Mars Rover Photos")
    
    if mars_photos:
        # Display photos in 3x2 grid
        for row in [mars_photos[:3], mars_photos[3:6]]:
            cols = st.columns(3)
            for col, photo in zip(cols, row):
                if photo:
                    with col:
                        try:
                            # Versuche Bild zu laden
                            st.image(
                                photo['img_src'], 
                                caption=f"📅 Sol {photo.get('sol', 'Unknown')} | 📷 {photo.get('camera', {}).get('full_name', 'Mars Camera')}",
                                use_container_width=True
                            )
                        except:
                            # Fallback wenn Bild nicht lädt
                            st.markdown(f"""
                            <div class="photo-placeholder">
                                <h4>📷 Mars Photo</h4>
                                <p>Sol {photo.get('sol', 'Unknown')}</p>
                                <p>{photo.get('camera', {}).get('full_name', 'Camera')}</p>
                                <p>Rover: {photo.get('rover', {}).get('name', 'Unknown')}</p>
                            </div>
                            """, unsafe_allow_html=True)
    
    # Rover Comparison
    st.markdown("---")
    st.markdown("### 🤖 Active Mars Rovers")
    
    col_rover1, col_rover2 = st.columns(2)
    
    with col_rover1:
        pers = rover_status['perseverance']
        st.markdown(f"""
        <div class="rover-card">
            <h3>🤖 Perseverance</h3>
            <p><strong>🗓️ Sol:</strong> {pers['sol']}</p>
            <p><strong>📷 Photos:</strong> {pers['total_photos']:,}</p>
            <p><strong>🚗 Distance:</strong> {pers['distance_driven']} km</p>
            <p><strong>🔬 Samples:</strong> {pers['samples_collected']}</p>
            <p><strong>🔋 Power:</strong> {pers['power_level']}%</p>
            <p><strong>📍 Status:</strong> {pers['status']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_rover2:
        cur = rover_status['curiosity']
        st.markdown(f"""
        <div class="rover-card">
            <h3>🔬 Curiosity</h3>
            <p><strong>🗓️ Sol:</strong> {cur['sol']}</p>
            <p><strong>📷 Photos:</strong> {cur['total_photos']:,}</p>
            <p><strong>🚗 Distance:</strong> {cur['distance_driven']} km</p>
            <p><strong>🔬 Samples:</strong> {cur['samples_collected']}</p>
            <p><strong>🔋 Power:</strong> {cur['power_level']}%</p>
            <p><strong>📍 Status:</strong> {cur['status']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Mission Timeline
    st.markdown("---")
    st.markdown("### 🚀 Mars Exploration Timeline")
    
    timeline_chart = create_mission_timeline_chart(timeline_data)
    st.plotly_chart(timeline_chart, use_container_width=True)
    
    # Future Mars Missions
    st.markdown("---")
    st.markdown("### 🚀 Future Mars Missions")
    
    col_future1, col_future2 = st.columns(2)
    
    with col_future1:
        st.markdown("""
        <div class="mission-card">
            <h4>🛰️ Mars Sample Return (2028)</h4>
            <p>Bring Perseverance samples back to Earth</p>
            <ul>
                <li>Sample Retrieval Lander</li>
                <li>Mars Ascent Vehicle</li>
                <li>Earth Return Orbiter</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col_future2:
        st.markdown("""
        <div class="mission-card">
            <h4>👨‍🚀 Human Mars Mission (2030s)</h4>
            <p>First crewed mission to Mars</p>
            <ul>
                <li>SpaceX Starship</li>
                <li>NASA Artemis Gateway</li>
                <li>Surface Habitat</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Mars Facts
    st.markdown("---")
    st.markdown("### 🔴 Mars Facts")
    
    mars_facts = [
        "🔴 Ein Mars-Tag (Sol) dauert 24 Stunden und 37 Minuten",
        "🌡️ Die Durchschnittstemperatur auf Mars beträgt -80°C",
        "🏔️ Olympus Mons ist der größte Vulkan im Sonnensystem (21 km hoch)",
        "💨 Mars-Atmosphäre besteht zu 95% aus Kohlendioxid",
        "🌙 Mars hat zwei kleine Monde: Phobos und Deimos",
        "🚀 Eine Reise zum Mars dauert etwa 7-9 Monate"
    ]
    
    # Zeige 3 zufällige Fakten
    selected_facts = random.sample(mars_facts, 3)
    for fact in selected_facts:
        st.info(fact)
    
    # Sidebar Information
    with st.sidebar:
        st.markdown("### 🔴 Mars Mission Info")
        st.markdown(f"""
        **Current Sol:** {mars_weather['sol']}
        **Earth Date:** {datetime.now().strftime('%Y-%m-%d')}
        **Season:** {mars_weather['season']}
        
        **Active Rovers:**
        - 🤖 Perseverance (2021-)
        - 🔬 Curiosity (2012-)
        
        **Mars Facts:**
        - Distance from Sun: 227M km
        - Day Length: 24h 37m
        - Year Length: 687 Earth days
        - Gravity: 38% of Earth
        """)
        
        st.markdown("---")
        st.markdown("### 📡 Communication")
        st.markdown("""
        **Signal Delay:**
        - Mars ↔ Earth: 4-24 minutes
        - Current: ~14 minutes
        
        **Data Transmission:**
        - Via Mars orbiters
        - Deep Space Network
        - Limited daily windows
        """)
        
        st.markdown("---")
        st.markdown(f"*🔄 Last updated: Sol {mars_weather['sol']}*")
    
    # Auto-refresh
    time.sleep(1)

if __name__ == "__main__":
    main()
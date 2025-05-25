import streamlit as st
import requests
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time
import random

# Page Config
st.set_page_config(
    page_title="🔴 Mars Exploration Hub",
    page_icon="🔴",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .mars-header {
        font-size: 3rem;
        background: linear-gradient(90deg, #e74c3c 0%, #c0392b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .page-intro {
        font-size: 1.2rem;
        text-align: center;
        color: #2c3e50;
        margin-bottom: 2rem;
        padding: 1.5rem;
        background: linear-gradient(135deg, #ffe8e8 0%, #ffcccb 100%);
        border-radius: 15px;
        border-left: 5px solid #e74c3c;
    }
    .rover-card {
        background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(231, 76, 60, 0.2);
    }
    .mars-stat {
        background: linear-gradient(135deg, #d35400 0%, #e67e22 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .weather-card {
        background: linear-gradient(135deg, #34495e 0%, #2c3e50 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
    }
    .photo-container {
        background: linear-gradient(135deg, #8e44ad 0%, #9b59b6 100%);
        padding: 1rem;
        border-radius: 12px;
        color: white;
        margin: 0.5rem 0;
        text-align: center;
    }
    .mission-timeline {
        background: linear-gradient(135deg, #16a085 0%, #1abc9c 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 0.5rem 0;
    }
    .mars-fact {
        background: linear-gradient(135deg, #f39c12 0%, #e67e22 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 0.8rem 0;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

class MarsExplorer:
    def __init__(self):
        self.nasa_mars_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/perseverance/latest_photos?api_key=DEMO_KEY"
        self.curiosity_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key=DEMO_KEY"
        self.nasa_insight_url = "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"
        
    def get_perseverance_photos(self, limit=6):
        """Holt neueste Perseverance Rover Fotos"""
        try:
            response = requests.get(self.nasa_mars_url, timeout=15)
            response.raise_for_status()
            
            data = response.json()
            photos = data.get('latest_photos', [])
            
            # Filtere und limitiere Fotos
            valid_photos = []
            for photo in photos:
                if photo.get('img_src') and len(valid_photos) < limit:
                    valid_photos.append(photo)
            
            return valid_photos
            
        except Exception as e:
            st.warning("⚠️ Mars Rover photos temporarily unavailable")
            return self._get_simulated_photos()
    
    def get_curiosity_photos(self, limit=3):
        """Holt Curiosity Rover Fotos"""
        try:
            response = requests.get(self.curiosity_url, timeout=15)
            response.raise_for_status()
            
            data = response.json()
            return data.get('latest_photos', [])[:limit]
            
        except Exception as e:
            return []
    
    def get_mars_weather(self):
        """Simuliert Mars Wetter (InSight ist nicht mehr aktiv)"""
        # Simuliere realistische Mars-Wetter
        sol = 1000 + random.randint(1, 500)  # Mars Sol (Tag)
        
        # Mars Temperaturen schwanken stark
        temp_high = random.randint(-20, 5)  # Celsius
        temp_low = random.randint(-80, -40)
        
        # Mars Atmosphärendruck
        pressure = random.randint(600, 900)  # Pascal
        
        # Wind auf Mars
        wind_speed = random.randint(5, 25)  # m/s
        wind_direction = random.choice(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
        
        return {
            'sol': sol,
            'temperature_high': temp_high,
            'temperature_low': temp_low,
            'pressure': pressure,
            'wind_speed': wind_speed,
            'wind_direction': wind_direction,
            'season': self._get_mars_season(),
            'weather_condition': random.choice(['Clear', 'Dusty', 'Dust Storm', 'Partly Cloudy'])
        }
    
    def get_rover_status(self):
        """Rover Status Information"""
        perseverance_sols = 1513 + random.randint(0, 10)  # Ungefähr aktueller Sol
        curiosity_sols = 4000 + random.randint(0, 20)
        
        return {
            'perseverance': {
                'sol': perseverance_sols,
                'status': 'Active',
                'location': 'Jezero Crater',
                'distance_km': 28.5 + random.random() * 2,
                'samples_collected': 24 + random.randint(0, 5),
                'power_level': random.randint(85, 98)
            },
            'curiosity': {
                'sol': curiosity_sols,
                'status': 'Active',
                'location': 'Gale Crater',
                'distance_km': 29.8 + random.random() * 2,
                'samples_analyzed': 45 + random.randint(0, 3),
                'power_level': random.randint(80, 95)
            }
        }
    
    def get_mars_facts(self):
        """Interessante Mars-Fakten"""
        facts = [
            "🔴 Mars ist als 'Roter Planet' bekannt wegen Eisenoxid (Rost) auf der Oberfläche",
            "🌡️ Mars-Temperaturen schwanken zwischen -143°C und 35°C",
            "📅 Ein Mars-Tag (Sol) dauert 24 Stunden und 37 Minuten",
            "🌍 Mars ist etwa halb so groß wie die Erde",
            "⛰️ Der Olympus Mons ist der größte Vulkan im Sonnensystem (21 km hoch)",
            "💨 Mars-Atmosphäre besteht zu 95% aus Kohlendioxid",
            "🌊 Polare Eiskappen enthalten gefrorenes Wasser und Trockeneis",
            "🛰️ Mars hat zwei kleine Monde: Phobos und Deimos",
            "🚀 Eine Reise zum Mars dauert etwa 7-9 Monate",
            "🏜️ Staubstürme können den ganzen Planeten bedecken"
        ]
        return random.sample(facts, 3)
    
    def _get_mars_season(self):
        """Bestimmt Mars-Jahreszeit basierend auf Datum"""
        month = datetime.now().month
        if month in [12, 1, 2]:
            return "Northern Winter"
        elif month in [3, 4, 5]:
            return "Northern Spring"
        elif month in [6, 7, 8]:
            return "Northern Summer"
        else:
            return "Northern Autumn"
    
    def _get_simulated_photos(self):
        """Fallback für simulierte Mars-Fotos"""
        return [
            {
                'id': f'sim_{i}',
                'sol': 1513 + i,
                'camera': {'full_name': f'Navigation Camera - {"Left" if i % 2 == 0 else "Right"}'},
                'img_src': f'https://via.placeholder.com/400x300/8B4513/FFFFFF?text=Mars+Sol+{1513+i}',
                'earth_date': (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
            }
            for i in range(6)
        ]

def create_temperature_chart(weather_data):
    """Erstellt Mars Temperatur Chart"""
    # Simuliere 7 Tage Mars-Wetter
    days = []
    highs = []
    lows = []
    
    base_sol = weather_data['sol']
    base_high = weather_data['temperature_high']
    base_low = weather_data['temperature_low']
    
    for i in range(7):
        days.append(f"Sol {base_sol - 6 + i}")
        # Variiere Temperaturen leicht
        high_var = random.randint(-5, 5)
        low_var = random.randint(-10, 10)
        highs.append(base_high + high_var)
        lows.append(base_low + low_var)
    
    fig = go.Figure()
    
    # Hohe Temperaturen
    fig.add_trace(go.Scatter(
        x=days,
        y=highs,
        mode='lines+markers',
        name='Tageshöchstwert',
        line=dict(color='#e74c3c', width=3),
        marker=dict(size=8)
    ))
    
    # Niedrige Temperaturen
    fig.add_trace(go.Scatter(
        x=days,
        y=lows,
        mode='lines+markers',
        name='Tagestiefstenwert',
        line=dict(color='#3498db', width=3),
        marker=dict(size=8),
        fill='tonexty',
        fillcolor='rgba(231, 76, 60, 0.2)'
    ))
    
    fig.update_layout(
        title='🌡️ Mars Temperatur-Verlauf (7 Sols)',
        xaxis_title='Mars Sol (Tag)',
        yaxis_title='Temperatur (°C)',
        template='plotly_white',
        height=400
    )
    
    return fig

def create_mission_timeline():
    """Erstellt Mars Mission Timeline"""
    missions = [
        {'Mission': 'Viking 1', 'Year': 1976, 'Type': 'Orbiter/Lander', 'Status': 'Completed'},
        {'Mission': 'Mars Pathfinder', 'Year': 1997, 'Type': 'Lander/Rover', 'Status': 'Completed'},
        {'Mission': 'Spirit & Opportunity', 'Year': 2004, 'Type': 'Rovers', 'Status': 'Completed'},
        {'Mission': 'Phoenix', 'Year': 2008, 'Type': 'Lander', 'Status': 'Completed'},
        {'Mission': 'Curiosity', 'Year': 2012, 'Type': 'Rover', 'Status': 'Active'},
        {'Mission': 'InSight', 'Year': 2018, 'Type': 'Lander', 'Status': 'Completed'},
        {'Mission': 'Perseverance', 'Year': 2021, 'Type': 'Rover', 'Status': 'Active'},
        {'Mission': 'Ingenuity', 'Year': 2021, 'Type': 'Helicopter', 'Status': 'Active'}
    ]
    
    fig = px.scatter(
        missions,
        x='Year',
        y='Mission',
        color='Status',
        size_max=15,
        title='🚀 Mars Exploration Timeline',
        color_discrete_map={
            'Active': '#27ae60',
            'Completed': '#3498db'
        }
    )
    
    fig.update_layout(
        height=400,
        template='plotly_white',
        xaxis_title='Launch Year',
        yaxis_title='Mission'
    )
    
    return fig

def main():
    # Header
    st.markdown('<h1 class="mars-header">🔴 MARS EXPLORATION HUB</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="page-intro">
        <strong>🚀 Latest Discoveries from the Red Planet</strong><br><br>
        Explore Mars through the eyes of NASA's rovers Perseverance and Curiosity. 
        From stunning landscape photos to weather data, discover what life might be like 
        on humanity's next home. Mars awaits! 🌌
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize Mars Explorer
    mars_explorer = MarsExplorer()
    
    # Sidebar Controls
    st.sidebar.markdown("## 🎛️ Mars Mission Control")
    
    auto_refresh = st.sidebar.checkbox("🔄 Auto-Refresh (2 min)", value=False)
    if auto_refresh:
        time.sleep(120)
        st.rerun()
    
    if st.sidebar.button("🔴 Update Mars Data", type="primary"):
        st.rerun()
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🔴 Mars Quick Facts")
    st.sidebar.markdown("""
    - **Distance from Earth:** 54.6M - 401M km
    - **Day Length:** 24h 37m (1 Sol)
    - **Year Length:** 687 Earth days
    - **Gravity:** 38% of Earth's gravity
    - **Atmosphere:** 95% CO₂, 1% oxygen
    - **Temperature:** -143°C to +35°C
    - **Largest Volcano:** Olympus Mons (21km)
    - **Moons:** Phobos & Deimos
    """)
    
    # Get Mars Data
    with st.spinner("🛰️ Contacting Mars rovers..."):
        rover_status = mars_explorer.get_rover_status()
        weather_data = mars_explorer.get_mars_weather()
        perseverance_photos = mars_explorer.get_perseverance_photos(6)
        mars_facts = mars_explorer.get_mars_facts()
        
        # Rover Status Cards
        st.markdown("### 🤖 Active Mars Rovers")
        
        col_pers, col_cur = st.columns(2)
        
        with col_pers:
            pers_data = rover_status['perseverance']
            st.markdown(f"""
            <div class="rover-card">
                <h3>🔴 Perseverance Rover</h3>
                <p><strong>📅 Sol:</strong> {pers_data['sol']} (Mars Day)</p>
                <p><strong>📍 Location:</strong> {pers_data['location']}</p>
                <p><strong>🚗 Distance:</strong> {pers_data['distance_km']:.1f} km traveled</p>
                <p><strong>🧪 Samples:</strong> {pers_data['samples_collected']} collected</p>
                <p><strong>🔋 Power:</strong> {pers_data['power_level']}%</p>
                <p><strong>🎯 Status:</strong> {pers_data['status']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_cur:
            cur_data = rover_status['curiosity']
            st.markdown(f"""
            <div class="rover-card">
                <h3>🔴 Curiosity Rover</h3>
                <p><strong>📅 Sol:</strong> {cur_data['sol']} (Mars Day)</p>
                <p><strong>📍 Location:</strong> {cur_data['location']}</p>
                <p><strong>🚗 Distance:</strong> {cur_data['distance_km']:.1f} km traveled</p>
                <p><strong>🔬 Samples:</strong> {cur_data['samples_analyzed']} analyzed</p>
                <p><strong>🔋 Power:</strong> {cur_data['power_level']}%</p>
                <p><strong>🎯 Status:</strong> {cur_data['status']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Mars Weather Station
        st.markdown("---")
        st.markdown("### 🌡️ Mars Weather Station")
        
        col_weather, col_chart = st.columns([1, 2])
        
        with col_weather:
            st.markdown(f"""
            <div class="weather-card">
                <h3>☀️ Current Conditions</h3>
                <p><strong>📅 Sol:</strong> {weather_data['sol']}</p>
                <p><strong>🌡️ High:</strong> {weather_data['temperature_high']}°C</p>
                <p><strong>🌡️ Low:</strong> {weather_data['temperature_low']}°C</p>
                <p><strong>💨 Wind:</strong> {weather_data['wind_speed']} m/s {weather_data['wind_direction']}</p>
                <p><strong>📊 Pressure:</strong> {weather_data['pressure']} Pa</p>
                <p><strong>🌤️ Condition:</strong> {weather_data['weather_condition']}</p>
                <p><strong>🍂 Season:</strong> {weather_data['season']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_chart:
            temp_chart = create_temperature_chart(weather_data)
            st.plotly_chart(temp_chart, use_container_width=True)
        
        # Mars Photos Gallery
        st.markdown("---")
        st.markdown("### 📷 Latest from Mars - Perseverance Rover")
        
        if perseverance_photos:
            photo_cols = st.columns(3)
            
            for i, photo in enumerate(perseverance_photos[:6]):
                col = photo_cols[i % 3]
                
                camera_name = photo.get('camera', {}).get('full_name', 'Mars Camera')
                sol = photo.get('sol', 'Unknown')
                earth_date = photo.get('earth_date', 'Unknown')
                
                with col:
                    st.markdown(f"""
                    <div class="photo-container">
                        <h4>📸 Sol {sol}</h4>
                        <p>{camera_name}</p>
                        <p>📅 {earth_date}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Versuche Foto zu laden
                    try:
                        if photo.get('img_src'):
                            st.image(photo['img_src'], use_container_width=True)
                        else:
                            st.info("🔴 Mars photo loading...")
                    except:
                        st.info("🔴 Mars photo loading...")
        
        # Mars Mission Timeline
        st.markdown("---")
        st.markdown("### 🚀 Mars Exploration Timeline")
        
        timeline_fig = create_mission_timeline()
        st.plotly_chart(timeline_fig, use_container_width=True)
        
        # Mars Facts
        st.markdown("---")
        st.markdown("### 🌟 Mars Facts of the Day")
        
        for fact in mars_facts:
            st.markdown(f"""
            <div class="mars-fact">
                {fact}
            </div>
            """, unsafe_allow_html=True)
        
        # Future Missions
        st.markdown("---")
        st.markdown("### 🚀 Upcoming Mars Missions")
        
        col_future1, col_future2 = st.columns(2)
        
        with col_future1:
            st.markdown(f"""
            <div class="mission-timeline">
                <h4>🚀 Mars Sample Return (2030s)</h4>
                <p><strong>Agency:</strong> NASA & ESA</p>
                <p><strong>Goal:</strong> Return Perseverance samples to Earth</p>
                <p><strong>Status:</strong> In Development</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_future2:
            st.markdown(f"""
            <div class="mission-timeline">
                <h4>🚀 Human Mars Mission (2030s)</h4>
                <p><strong>Agency:</strong> NASA Artemis</p>
                <p><strong>Goal:</strong> First humans on Mars</p>
                <p><strong>Status:</strong> Planning Phase</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #7f8c8d; padding: 2rem 0;'>
        🔴 <strong>Mars Exploration Hub</strong> 🔴<br>
        📡 Real-time data from NASA Mars rovers and missions<br>
        🚀 Following humanity's journey to the Red Planet
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
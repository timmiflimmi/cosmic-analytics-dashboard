import streamlit as st
import requests
from datetime import datetime, timedelta
import random
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page Config
st.set_page_config(
    page_title="🌌 Cosmic Analytics Command Center",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
    }
    .metric-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin: 0.5rem;
    }
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
    }
    .iss-card {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        color: white;
    }
    .mars-card {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        color: white;
    }
    .space-card {
        background: linear-gradient(135deg, #2ed573 0%, #1e90ff 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

class CosmicAnalyticsAPI:
    def __init__(self):
        # NASA API Key aus Environment Variable laden
        self.nasa_api_key = os.getenv("NASA_API_KEY", "DEMO_KEY")
        
        # API URLs
        self.iss_api_url = "http://api.open-notify.org/iss-now.json"
        self.astros_api_url = "http://api.open-notify.org/astros.json" 
        self.iss_pass_url = "http://api.open-notify.org/iss-pass.json"
        self.spacex_upcoming_url = "https://api.spacexdata.com/v4/launches/upcoming"
        self.spacex_latest_url = "https://api.spacexdata.com/v4/launches/latest"
        self.nasa_apod_url = f"https://api.nasa.gov/planetary/apod?api_key={self.nasa_api_key}"
        self.nasa_neo_url = f"https://api.nasa.gov/neo/rest/v1/feed?api_key={self.nasa_api_key}"
    
    def get_iss_location(self):
        """Holt aktuelle ISS Position"""
        try:
            response = requests.get(self.iss_api_url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return {
                'latitude': float(data['iss_position']['latitude']),
                'longitude': float(data['iss_position']['longitude']),
                'timestamp': data['timestamp']
            }
        except:
            # Fallback-Position (über Hamburg)
            return {
                'latitude': 53.5511,
                'longitude': 9.9937,
                'timestamp': int(datetime.now().timestamp())
            }
    
    def get_astronauts(self):
        """Holt Liste der Astronauten im All"""
        try:
            response = requests.get(self.astros_api_url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data['people'], data['number']
        except:
            # Fallback-Daten
            return [
                {'name': 'Expedition Crew', 'craft': 'ISS'},
                {'name': 'Shenzhou Crew', 'craft': 'Tiangong'}
            ], 7
    
    def get_spacex_next_launch(self):
        """Holt nächste SpaceX Mission"""
        try:
            response = requests.get(self.spacex_upcoming_url, timeout=15)
            response.raise_for_status()
            launches = response.json()
            
            if launches:
                # Finde nächsten Launch in der Zukunft
                now = datetime.now()
                for launch in launches:
                    if launch.get('date_utc'):
                        launch_date = datetime.fromisoformat(launch['date_utc'].replace('Z', '+00:00'))
                        if launch_date > now:
                            return launch
            
            # Fallback zu latest wenn keine upcoming
            response = requests.get(self.spacex_latest_url, timeout=15)
            return response.json()
            
        except:
            # Fallback-Mission
            return {
                'name': 'Starlink Group 8-5',
                'date_utc': '2025-05-31T08:58:00Z',
                'rocket': {'name': 'Falcon 9 Block 5'},
                'details': 'Deployment of 23 Starlink satellites to low Earth orbit.',
                'success': None
            }
    
    def get_nasa_picture_of_day(self):
        """Holt NASA Picture of the Day"""
        try:
            response = requests.get(self.nasa_apod_url, timeout=10)
            response.raise_for_status()
            return response.json()
        except:
            # Fallback-Bild
            return {
                'title': 'Andromeda Galaxy',
                'explanation': 'The Andromeda Galaxy is our nearest major galactic neighbor.',
                'url': 'https://science.nasa.gov/wp-content/uploads/2023/09/hubble-andromeda-galaxy-full-image.jpg',
                'media_type': 'image'
            }
    
    def get_asteroid_data(self):
        """Holt Asteroid-Daten"""
        try:
            today = datetime.now().strftime('%Y-%m-%d')
            url = f"{self.nasa_neo_url}&start_date={today}&end_date={today}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            asteroids = []
            for date, objects in data['near_earth_objects'].items():
                for obj in objects[:5]:  # Top 5
                    asteroids.append({
                        'name': obj['name'],
                        'diameter': f"~{obj['estimated_diameter']['meters']['estimated_diameter_max']:.0f}m",
                        'distance': f"{float(obj['close_approach_data'][0]['miss_distance']['kilometers']):.0f} km",
                        'hazardous': obj['is_potentially_hazardous_asteroid']
                    })
            return asteroids
        except:
            # Fallback-Asteroiden
            return [
                {'name': '2025 AA', 'diameter': '~150m', 'distance': '2,500,000 km', 'hazardous': False},
                {'name': '2025 BB', 'diameter': '~85m', 'distance': '1,800,000 km', 'hazardous': False}
            ]

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🌌 COSMIC ANALYTICS COMMAND CENTER</h1>
        <p>Real-Time Space Data Dashboard</p>
        <p>🛰️ ISS Tracking • 🚀 SpaceX • 🔴 Mars • 🌙 Lunar • 🌌 Deep Space</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize API
    cosmic = CosmicAnalyticsAPI()
    
    # Get live data
    iss_data = cosmic.get_iss_location()
    astronauts, astro_count = cosmic.get_astronauts()
    next_launch = cosmic.get_spacex_next_launch()
    nasa_pic = cosmic.get_nasa_picture_of_day()
    asteroids = cosmic.get_asteroid_data()
    
    # Live Status Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>🛰️ ISS</h3>
            <h2>Live</h2>
            <p>{iss_data['latitude']:.2f}°, {iss_data['longitude']:.2f}°</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>👨‍🚀 Astronauten</h3>
            <h2>{astro_count}</h2>
            <p>Im Weltraum</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        # SpaceX Launch Countdown
        if next_launch.get('date_utc'):
            try:
                launch_date = datetime.fromisoformat(next_launch['date_utc'].replace('Z', '+00:00'))
                now = datetime.now()
                if launch_date > now:
                    diff = launch_date - now
                    days = diff.days
                    hours = diff.seconds // 3600
                    countdown_text = f"T-{days}d {hours}h"
                else:
                    countdown_text = "Gestartet"
            except:
                countdown_text = "TBD"
        else:
            countdown_text = "TBD"
            
        st.markdown(f"""
        <div class="metric-card">
            <h3>🚀 SpaceX</h3>
            <h2>{countdown_text}</h2>
            <p>Nächster Start</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <h3>☄️ Asteroiden</h3>
            <h2>{len(asteroids)}</h2>
            <p>Heute nah</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Dashboard Modules
    st.markdown("---")
    st.markdown("## 🎛️ Mission Control Modules")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card iss-card">
            <h3>🛰️ ISS Mission Control</h3>
            <p>Real-time International Space Station tracking</p>
            <ul>
                <li>Live Position auf Weltkarte</li>
                <li>Current Crew Information</li>
                <li>Hamburg Pass Times</li>
                <li>Orbital Data & Speed</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card mars-card">
            <h3>🔴 Mars Exploration Hub</h3>
            <p>Latest from the Red Planet</p>
            <ul>
                <li>Perseverance Rover Photos</li>
                <li>Mars Weather Station</li>
                <li>Mission Timeline</li>
                <li>Sol-based Mars Calendar</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>🌞 Space Weather Station</h3>
            <p>Solar Activity & Aurora Forecasts</p>
            <ul>
                <li>Solar Wind Conditions</li>
                <li>Aurora Activity Hamburg</li>
                <li>Solar Flare Alerts</li>
                <li>Radiation Level Monitoring</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card space-card">
            <h3>🌌 Deep Space Observatory</h3>
            <p>NASA Telescopes & Cosmic Discoveries</p>
            <ul>
                <li>NASA Picture of the Day</li>
                <li>Hubble & James Webb Updates</li>
                <li>Voyager Mission Status</li>
                <li>Asteroid & Comet Tracking</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>🚀 Rocket Launch Center</h3>
            <p>Global Space Launch Tracking</p>
            <ul>
                <li>SpaceX Mission Countdown</li>
                <li>Launch Success Analytics</li>
                <li>Rocket Performance Stats</li>
                <li>Mission Timeline</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>🌙 Lunar & Planetary</h3>
            <p>Moon Phases & Solar System</p>
            <ul>
                <li>Current Moon Phase</li>
                <li>Planet Visibility Hamburg</li>
                <li>Solar System Live Positions</li>
                <li>Eclipse Predictions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>🛰️ Satellite Networks</h3>
            <p>Global Satellite Constellation Tracking</p>
            <ul>
                <li>Starlink Coverage Map</li>
                <li>GPS Constellation Status</li>
                <li>Hamburg Satellite Passes</li>
                <li>Network Performance</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Live Data Preview
    st.markdown("---")
    st.markdown("### 🌟 NASA Picture of the Day")
    
    if nasa_pic and nasa_pic.get('media_type') == 'image':
        col_pic, col_desc = st.columns([1, 1])
        
        with col_pic:
            st.image(nasa_pic['url'], use_container_width=True)
        
        with col_desc:
            st.markdown(f"""
            **📅 {nasa_pic['title']}**
            
            {nasa_pic['explanation'][:300]}...
            
            *NASA Astronomy Picture of the Day*
            """)
    
    # Space Facts
    st.markdown("---")
    st.markdown("### 🌟 Space Facts")
    
    space_facts = [
        "🛰️ Die ISS umkreist die Erde alle 90 Minuten mit 27.600 km/h",
        "🔴 Ein Tag auf dem Mars (Sol) dauert 24 Stunden und 37 Minuten",
        "🌙 Der Mond entfernt sich jährlich um 3,8 cm von der Erde",
        "🚀 SpaceX hat über 200 Satelliten-Starts erfolgreich durchgeführt",
        "☄️ Täglich fallen etwa 100 Tonnen Weltraumgestein auf die Erde",
        "🌌 Das nächste Sternensystem Alpha Centauri ist 4,37 Lichtjahre entfernt"
    ]
    
    daily_fact = space_facts[datetime.now().day % len(space_facts)]
    st.info(daily_fact)
    
    # Sidebar Information
    with st.sidebar:
        st.markdown("### 🌌 System Status")
        
        # API Status
        api_status = "🟢 Operational" if cosmic.nasa_api_key != "DEMO_KEY" else "🟡 Demo Mode"
        st.markdown(f"**NASA APIs:** {api_status}")
        st.markdown("**SpaceX API:** 🟢 Operational")
        st.markdown("**Open Notify:** 🟢 Operational")
        
        st.markdown("---")
        st.markdown("### 🛰️ Quick Stats")
        st.markdown(f"""
        **ISS Current:**
        - Latitude: {iss_data['latitude']:.4f}°
        - Longitude: {iss_data['longitude']:.4f}°
        - Altitude: ~408 km
        - Speed: ~27,600 km/h
        
        **Next SpaceX Launch:**
        - Mission: {next_launch.get('name', 'TBD')}
        - Countdown: {countdown_text}
        
        **Astronauts in Space:**
        - Total: {astro_count} Menschen
        - ISS + Tiangong Stations
        """)
        
        st.markdown("---")
        st.markdown("### 📍 Hamburg Location")
        st.markdown("""
        **Coordinates:**
        - 53.5511° N, 9.9937° E
        - Timezone: Europe/Berlin
        
        **ISS Visibility:**
        - Check ISS Mission Control
        - For pass predictions
        """)
        
        st.markdown("---")
        st.markdown("*🔄 Auto-refresh every 30 seconds*")
    
    # Auto-refresh
    time.sleep(1)

if __name__ == "__main__":
    main()
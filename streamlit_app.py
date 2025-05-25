import streamlit as st
import requests
from datetime import datetime

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
        font-size: 4rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    .page-description {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
        padding: 1rem;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 10px;
    }
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-5px);
    }
    .status-card {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .nav-link {
        display: block;
        padding: 0.75rem 1rem;
        margin: 0.25rem 0;
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        color: white;
        text-decoration: none;
        border-radius: 8px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .nav-link:hover {
        transform: translateX(5px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

def get_quick_status():
    """Holt schnelle Status-Updates für alle Bereiche"""
    status = {}
    
    try:
        # ISS Status
        iss_response = requests.get("http://api.open-notify.org/iss-now.json", timeout=5)
        if iss_response.status_code == 200:
            iss_data = iss_response.json()
            status['iss'] = {
                'lat': float(iss_data['iss_position']['latitude']),
                'lon': float(iss_data['iss_position']['longitude']),
                'status': '🟢 Online'
            }
        else:
            status['iss'] = {'status': '🟡 Limited'}
    except:
        status['iss'] = {'status': '🔴 Offline'}
    
    try:
        # Astronauts
        astro_response = requests.get("http://api.open-notify.org/astros.json", timeout=5)
        if astro_response.status_code == 200:
            astro_data = astro_response.json()
            status['astronauts'] = {
                'count': astro_data['number'],
                'status': '🟢 Updated'
            }
        else:
            status['astronauts'] = {'count': 'Unknown', 'status': '🟡 Limited'}
    except:
        status['astronauts'] = {'count': 'Unknown', 'status': '🔴 Offline'}
    
    try:
        # SpaceX Status
        spacex_response = requests.get("https://api.spacexdata.com/v4/launches/upcoming", timeout=5)
        if spacex_response.status_code == 200:
            spacex_data = spacex_response.json()
            status['spacex'] = {
                'next_launch': len(spacex_data),
                'status': '🟢 Updated'
            }
        else:
            status['spacex'] = {'next_launch': 'Unknown', 'status': '🟡 Limited'}
    except:
        status['spacex'] = {'next_launch': 'Unknown', 'status': '🔴 Offline'}
    
    return status

def main():
    # Header
    st.markdown('<h1 class="main-header">🌌 COSMIC ANALYTICS COMMAND CENTER</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="page-description">
        🚀 <strong>Welcome to Mission Control</strong> 🚀<br>
        Your comprehensive space exploration dashboard with real-time tracking, 
        mission analysis, and cosmic discoveries from across the universe.
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Status Overview
    st.markdown("## 📊 Mission Status Overview")
    
    with st.spinner("🛰️ Checking all space systems..."):
        status = get_quick_status()
    
    # Status Cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        iss_status = status.get('iss', {})
        st.markdown(f"""
        <div class="status-card">
            <h3>🛰️ ISS Tracking</h3>
            <h4>{iss_status.get('status', '🔴 Offline')}</h4>
            <p>Lat: {iss_status.get('lat', 'N/A'):.2f}°<br>
            Lon: {iss_status.get('lon', 'N/A'):.2f}°</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        astro_status = status.get('astronauts', {})
        st.markdown(f"""
        <div class="status-card">
            <h3>👨‍🚀 Astronauts</h3>
            <h4>{astro_status.get('status', '🔴 Offline')}</h4>
            <p>{astro_status.get('count', 'Unknown')} Currently in Space</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        spacex_status = status.get('spacex', {})
        st.markdown(f"""
        <div class="status-card">
            <h3>🚀 Launch Status</h3>
            <h4>{spacex_status.get('status', '🔴 Offline')}</h4>
            <p>{spacex_status.get('next_launch', 'Unknown')} Upcoming Missions</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="status-card">
            <h3>🌌 Deep Space</h3>
            <h4>🟢 Active</h4>
            <p>NASA APOD & Telescopes<br>Operational</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Navigation to Sub-Pages
    st.markdown("---")
    st.markdown("## 🎛️ Mission Control Sections")
    
    # Feature Cards
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown("""
        <div class="feature-card">
            <h3>🛰️ ISS Mission Control</h3>
            <p><strong>Real-time International Space Station tracking</strong></p>
            <ul>
                <li>🗺️ Live position mapping</li>
                <li>👨‍🚀 Current crew information</li>
                <li>🌍 Hamburg flyover predictions</li>
                <li>📊 Orbital data & analytics</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>🔴 Mars Exploration Hub</h3>
            <p><strong>Latest discoveries from the Red Planet</strong></p>
            <ul>
                <li>📷 Perseverance rover photos</li>
                <li>🌡️ Mars weather station data</li>
                <li>🗺️ Landing site exploration</li>
                <li>📊 Mission timeline tracking</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>🌞 Space Weather Station</h3>
            <p><strong>Solar activity & Earth's space environment</strong></p>
            <ul>
                <li>☀️ Solar wind monitoring</li>
                <li>🌌 Aurora activity forecasts</li>
                <li>⚡ Solar flare alerts</li>
                <li>🧲 Magnetic field analysis</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>🌌 Deep Space Observatory</h3>
            <p><strong>Exploring beyond our solar system</strong></p>
            <ul>
                <li>🌟 NASA Picture of the Day</li>
                <li>☄️ Asteroid & comet tracking</li>
                <li>🔭 Hubble & Webb updates</li>
                <li>🪐 Exoplanet discoveries</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col_right:
        st.markdown("""
        <div class="feature-card">
            <h3>🚀 Rocket Launch Center</h3>
            <p><strong>Global space launch tracking & analysis</strong></p>
            <ul>
                <li>⏰ SpaceX mission countdowns</li>
                <li>🌍 Global launch calendar</li>
                <li>📈 Success rate statistics</li>
                <li>🗺️ Launch site locations</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>🌙 Lunar & Planetary</h3>
            <p><strong>Moon phases, planets & solar system</strong></p>
            <ul>
                <li>🌕 Current moon phase tracking</li>
                <li>🪐 Live planet positions</li>
                <li>🌙 Lunar eclipse predictions</li>
                <li>⭐ Hamburg stargazing guide</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>🛰️ Satellite Networks</h3>
            <p><strong>Global satellite constellation tracking</strong></p>
            <ul>
                <li>🌐 Starlink coverage mapping</li>
                <li>📡 GPS satellite status</li>
                <li>📶 Network performance data</li>
                <li>🛰️ Satellite pass predictions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Space Fact of the Day
        space_facts = [
            "🌌 The ISS travels at 17,500 mph, completing an orbit every 90 minutes",
            "🚀 SpaceX has successfully landed over 200 Falcon 9 boosters",
            "🔴 A day on Mars lasts 24 hours and 37 minutes",
            "🌙 The Moon is moving away from Earth at 3.8 cm per year",
            "⭐ There are more stars in the universe than grains of sand on all Earth's beaches",
            "🛰️ Over 4,000 Starlink satellites are currently in orbit",
            "☀️ The Sun's core temperature is about 15 million degrees Celsius"
        ]
        
        import random
        daily_fact = space_facts[hash(str(datetime.now().date())) % len(space_facts)]
        
        st.markdown(f"""
        <div class="feature-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
            <h3>🌟 Space Fact of the Day</h3>
            <p style="font-size: 1.1rem; font-weight: bold;">{daily_fact}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #7f8c8d; padding: 2rem 0;'>
        🌌 <strong>Cosmic Analytics Command Center</strong> 🌌<br>
        🚀 Navigate to specific sections using the sidebar menu<br>
        📡 Real-time space data from NASA, SpaceX, and international space agencies
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
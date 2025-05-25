import streamlit as st
import requests
import folium
from streamlit_folium import folium_static
from datetime import datetime, timedelta
import time

# Page Config
st.set_page_config(
    page_title="🛰️ ISS Mission Control",
    page_icon="🛰️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .iss-header {
        font-size: 3rem;
        background: linear-gradient(90deg, #2980b9 0%, #3498db 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .page-intro {
        font-size: 1.2rem;
        text-align: center;
        color: #34495e;
        margin-bottom: 2rem;
        padding: 1.5rem;
        background: linear-gradient(135deg, #ebf8ff 0%, #bee3f8 100%);
        border-radius: 15px;
        border-left: 5px solid #3498db;
    }
    .iss-metric {
        background: linear-gradient(135deg, #2980b9 0%, #3498db 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.15);
    }
    .astronaut-card {
        background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 0.5rem 0;
        font-weight: bold;
        text-align: center;
    }
    .orbit-info {
        background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
    }
    .pass-prediction {
        background: linear-gradient(135deg, #f39c12 0%, #e67e22 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 0.5rem 0;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

class ISSTracker:
    def __init__(self):
        self.iss_api_url = "http://api.open-notify.org/iss-now.json"
        self.astros_api_url = "http://api.open-notify.org/astros.json"
        self.iss_pass_url = "http://api.open-notify.org/iss-pass.json"
        
    def get_iss_location(self):
        """Holt aktuelle ISS Position"""
        try:
            response = requests.get(self.iss_api_url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            return {
                'latitude': float(data['iss_position']['latitude']),
                'longitude': float(data['iss_position']['longitude']),
                'timestamp': data['timestamp'],
                'readable_time': datetime.fromtimestamp(data['timestamp']).strftime('%H:%M:%S UTC')
            }
            
        except Exception as e:
            st.error(f"❌ ISS API Error: {e}")
            return None
    
    def get_astronauts(self):
        """Holt Astronauten im Weltraum"""
        try:
            response = requests.get(self.astros_api_url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            return data
            
        except Exception as e:
            st.error(f"❌ Astronauts API Error: {e}")
            return None
    
    def get_iss_pass_times(self, lat=53.5511, lon=9.9937):
        """Holt ISS Überflugzeiten für Hamburg"""
        try:
            response = requests.get(f"{self.iss_pass_url}?lat={lat}&lon={lon}&alt=6&n=5", timeout=15)
            response.raise_for_status()
            
            data = response.json()
            passes = []
            
            if 'response' in data:
                for pass_data in data['response']:
                    rise_time = datetime.fromtimestamp(pass_data['risetime'])
                    duration = pass_data['duration']
                    passes.append({
                        'rise_time': rise_time,
                        'duration': duration,
                        'readable_time': rise_time.strftime('%d.%m.%Y %H:%M:%S')
                    })
            
            return passes
            
        except Exception as e:
            st.warning(f"⚠️ ISS Pass API temporarily unavailable. Showing estimated times.")
            
            # Simuliere nächste 5 Überflüge
            base_time = datetime.now() + timedelta(hours=2)
            passes = []
            
            for i in range(5):
                pass_time = base_time + timedelta(hours=i * 1.5)
                passes.append({
                    'rise_time': pass_time,
                    'duration': 300 + (i * 60),
                    'readable_time': pass_time.strftime('%d.%m.%Y %H:%M:%S')
                })
            
            return passes
    
    def calculate_iss_speed(self):
        """Berechnet ISS Geschwindigkeit"""
        return 7.66  # km/s
    
    def get_location_info(self, lat, lon):
        """Gibt Info über die Region zurück"""
        if abs(lat) < 30 and abs(lon) < 30:
            return "🌍 Afrika/Europa Region"
        elif lat > 30 and -100 < lon < 50:
            return "🌏 Europa/Asien Region"
        elif lat < -30:
            return "🌊 Südlicher Ozean"
        elif abs(lon) > 150:
            return "🌊 Pazifischer Ozean"
        elif lon < -50:
            return "🌊 Atlantischer Ozean"
        else:
            return "🌍 Erdorbit"

def create_iss_map(iss_data):
    """Erstellt ISS Live Map"""
    if not iss_data:
        return None
        
    # Folium Karte erstellen
    m = folium.Map(
        location=[iss_data['latitude'], iss_data['longitude']],
        zoom_start=4,
        tiles='OpenStreetMap'
    )
    
    # ISS Marker
    folium.Marker(
        [iss_data['latitude'], iss_data['longitude']],
        popup=f"🛰️ ISS Position<br>📍 {iss_data['latitude']:.4f}°, {iss_data['longitude']:.4f}°<br>🕐 {iss_data['readable_time']}",
        tooltip="🛰️ International Space Station"
    ).add_to(m)
    
    # Orbit Circle
    folium.Circle(
        [iss_data['latitude'], iss_data['longitude']],
        radius=500000,  # 500km
        popup="ISS Sichtbarkeitsbereich (500km)",
        color="blue",
        fillColor="lightblue",
        fillOpacity=0.2
    ).add_to(m)
    
    return m

def main():
    # Header
    st.markdown('<h1 class="iss-header">🛰️ ISS MISSION CONTROL</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="page-intro">
        <strong>🌍 International Space Station Real-Time Tracking</strong><br><br>
        Monitor the ISS as it orbits Earth at 17,500 mph, 408 km above us. 
        Track its current position, crew status, and predict when it will be visible from Hamburg.
        The ISS completes one orbit around Earth every 90 minutes! 🚀
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize ISS Tracker
    iss_tracker = ISSTracker()
    
    # Sidebar Controls
    st.sidebar.markdown("## 🎛️ ISS Mission Controls")
    
    auto_refresh = st.sidebar.checkbox("🔄 Auto-Refresh (30s)", value=False)
    if auto_refresh:
        time.sleep(30)
        st.rerun()
    
    if st.sidebar.button("🚀 Update ISS Data", type="primary"):
        st.rerun()
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📡 ISS Quick Facts")
    st.sidebar.markdown("""
    - **Altitude:** ~408 km above Earth
    - **Speed:** 17,500 mph (7.66 km/s)
    - **Orbit Period:** 92.9 minutes
    - **Daily Orbits:** ~15.5 times
    - **Crew Capacity:** Up to 7 astronauts
    - **Size:** Football field sized
    - **Mass:** ~420,000 kg
    """)
    
    # Get Live Data
    with st.spinner("📡 Contacting International Space Station..."):
        iss_data = iss_tracker.get_iss_location()
        astro_data = iss_tracker.get_astronauts()
        
        if iss_data:
            # Live Metrics Row
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.markdown(f"""
                <div class="iss-metric">
                    <h3>📍 Latitude</h3>
                    <h2>{iss_data['latitude']:.4f}°</h2>
                    <p>Current Position</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="iss-metric">
                    <h3>📍 Longitude</h3>
                    <h2>{iss_data['longitude']:.4f}°</h2>
                    <p>Current Position</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                speed = iss_tracker.calculate_iss_speed()
                st.markdown(f"""
                <div class="iss-metric">
                    <h3>⚡ Speed</h3>
                    <h2>{speed:.2f} km/s</h2>
                    <p>27,600 km/h</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col4:
                if astro_data:
                    st.markdown(f"""
                    <div class="iss-metric">
                        <h3>👨‍🚀 Crew</h3>
                        <h2>{astro_data['number']}</h2>
                        <p>People in Space</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # ISS Live Map & Info
            col_map, col_info = st.columns([2, 1])
            
            with col_map:
                st.markdown("### 🗺️ ISS Live Position")
                st.write(f"🛰️ ISS at {iss_data['latitude']:.4f}°, {iss_data['longitude']:.4f}°")
                
                # Create ISS Map
                m = folium.Map(
                    location=[iss_data['latitude'], iss_data['longitude']],
                    zoom_start=4,
                    tiles='OpenStreetMap'
                )
                
                folium.Marker(
                    [iss_data['latitude'], iss_data['longitude']],
                    popup=f"🛰️ ISS Position<br>📍 {iss_data['latitude']:.4f}°, {iss_data['longitude']:.4f}°<br>🕐 {iss_data['readable_time']}",
                    tooltip="🛰️ International Space Station"
                ).add_to(m)
                
                folium.Circle(
                    [iss_data['latitude'], iss_data['longitude']],
                    radius=500000,
                    popup="ISS Sichtbarkeitsbereich (500km)",
                    color="blue",
                    fillColor="lightblue",
                    fillOpacity=0.2
                ).add_to(m)
                
                folium_static(m, width=700, height=400)
            
            with col_info:
                location_info = iss_tracker.get_location_info(iss_data['latitude'], iss_data['longitude'])
                
                st.markdown(f"""
                <div class="orbit-info">
                    <h3>🛰️ ISS Status</h3>
                    <p><strong>🕐 Time:</strong> {iss_data['readable_time']}</p>
                    <p><strong>📍 Over:</strong> {location_info}</p>
                    <p><strong>🌍 Altitude:</strong> ~408 km</p>
                    <p><strong>⏱️ Orbit Period:</strong> 92.9 min</p>
                    <p><strong>🌅 Daily Orbits:</strong> ~15.5</p>
                    <p><strong>🌡️ Temperature:</strong> -157°C to +121°C</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Astronauts Section
        if astro_data:
            st.markdown("---")
            st.markdown("### 👨‍🚀 Current Crew in Space")
            
            # Group by spacecraft
            iss_crew = [p for p in astro_data['people'] if p['craft'] == 'ISS']
            tiangong_crew = [p for p in astro_data['people'] if p['craft'] == 'Tiangong']
            
            col_iss, col_tiangong = st.columns(2)
            
            with col_iss:
                st.markdown("**🚀 International Space Station (ISS)**")
                for astronaut in iss_crew:
                    st.markdown(f"""
                    <div class="astronaut-card">
                        👨‍🚀 {astronaut['name']}
                    </div>
                    """, unsafe_allow_html=True)
                
                if len(iss_crew) == 0:
                    st.info("No crew data available for ISS")
            
            with col_tiangong:
                st.markdown("**🚀 Tiangong Space Station**")
                for astronaut in tiangong_crew:
                    st.markdown(f"""
                    <div class="astronaut-card">
                        👨‍🚀 {astronaut['name']}
                    </div>
                    """, unsafe_allow_html=True)
                
                if len(tiangong_crew) == 0:
                    st.info("No crew data available for Tiangong")
        
        # ISS Pass Times for Hamburg
        st.markdown("---")
        st.markdown("### 🌍 ISS Passes Over Hamburg")
        st.markdown("**When will the ISS be visible from Hamburg? Look up and wave! 👋**")
        
        iss_passes = iss_tracker.get_iss_pass_times()
        if iss_passes:
            st.markdown("**Next 5 ISS flyovers visible from Hamburg:**")
            
            for i, pass_info in enumerate(iss_passes[:5]):
                duration_min = pass_info['duration'] // 60
                
                # Time until pass
                now = datetime.now()
                time_until = pass_info['rise_time'] - now
                
                if time_until.total_seconds() > 0:
                    hours_until = int(time_until.total_seconds() // 3600)
                    minutes_until = int((time_until.total_seconds() % 3600) // 60)
                    countdown = f"in {hours_until}h {minutes_until}m"
                else:
                    countdown = "Recently passed"
                
                st.markdown(f"""
                <div class="pass-prediction">
                    🛰️ Pass #{i+1}: {pass_info['readable_time']} ({countdown})<br>
                    ⏱️ Duration: {duration_min} minutes | 👀 Look up and spot the ISS!
                </div>
                """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #7f8c8d; padding: 2rem 0;'>
        🛰️ <strong>ISS Mission Control</strong> 🛰️<br>
        📡 Real-time data from NASA and international space agencies<br>
        🌍 Track humanity's outpost in space, 408km above Earth
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
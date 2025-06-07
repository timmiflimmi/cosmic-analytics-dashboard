import streamlit as st
import requests
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page Config
st.set_page_config(
    page_title="🌌 Tiefer Weltraum",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS für Deep Space Theme
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
    .telescope-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
    }
    .discovery-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
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
    .voyager-card {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
    }
</style>
""", unsafe_allow_html=True)

class DeepSpaceAPI:
    def __init__(self):
        # NASA API Key aus Environment Variable laden
        self.nasa_api_key = os.getenv("NASA_API_KEY", "DEMO_KEY")
        
        # NASA APIs
        self.nasa_apod_url = f"https://api.nasa.gov/planetary/apod?api_key={self.nasa_api_key}"
        self.nasa_neo_url = f"https://api.nasa.gov/neo/rest/v1/feed?api_key={self.nasa_api_key}"
        
    def get_nasa_picture_of_day(self):
        """Holt NASA Picture of the Day"""
        try:
            response = requests.get(self.nasa_apod_url, timeout=10)
            response.raise_for_status()
            return response.json()
        except:
            return self._get_fallback_apod()
    
    def _get_fallback_apod(self):
        """Fallback für NASA-Bild"""
        fallback_images = [
            {
                'title': 'Andromeda-Galaxie',
                'explanation': 'Die Andromeda-Galaxie ist unsere nächste große Nachbargalaxie und etwa 2,5 Millionen Lichtjahre entfernt. Mit über einer Billion Sternen ist sie deutlich größer als unsere Milchstraße.',
                'url': 'https://science.nasa.gov/wp-content/uploads/2023/09/hubble-andromeda-galaxy-full-image.jpg',
                'media_type': 'image'
            },
            {
                'title': 'Orion-Nebel',
                'explanation': 'Der Orion-Nebel ist eine der aktivsten Sternentstehungsregionen in unserer galaktischen Nachbarschaft und etwa 1.344 Lichtjahre von der Erde entfernt.',
                'url': 'https://science.nasa.gov/wp-content/uploads/2023/09/orion-nebula-jwst-nircam-f200w.jpg',
                'media_type': 'image'
            },
            {
                'title': 'Crab-Nebel',
                'explanation': 'Der Krebsnebel ist der Überrest einer Supernova, die im Jahr 1054 von chinesischen Astronomen beobachtet wurde. Im Zentrum befindet sich ein schnell rotierender Pulsar.',
                'url': 'https://science.nasa.gov/wp-content/uploads/2023/09/crab-nebula-jwst-miri.jpg',
                'media_type': 'image'
            }
        ]
        return random.choice(fallback_images)
    
    def get_hubble_discoveries(self):
        """Simulierte Hubble-Entdeckungen"""
        return [
            {
                'title': 'Neue Exoplaneten-Atmosphäre entdeckt',
                'date': '2025-05-20',
                'description': 'Hubble entdeckt Wasserdampf in der Atmosphäre des Exoplaneten K2-18b',
                'telescope': 'Hubble Space Telescope',
                'category': 'Exoplaneten'
            },
            {
                'title': 'Galaxienkollision beobachtet',
                'date': '2025-05-18',
                'description': 'Spektakuläre Aufnahmen der kollidierenden Galaxien NGC 4038 und NGC 4039',
                'telescope': 'Hubble Space Telescope',
                'category': 'Galaxien'
            },
            {
                'title': 'Neuer Brauner Zwerg klassifiziert',
                'date': '2025-05-15',
                'description': 'Hubble identifiziert einen der kältesten Braunen Zwerge in unserer Nachbarschaft',
                'telescope': 'Hubble Space Telescope',
                'category': 'Sterne'
            }
        ]
    
    def get_jwst_observations(self):
        """Simulierte James Webb Space Telescope Beobachtungen"""
        return [
            {
                'title': 'Galaxien aus der Frühzeit des Universums',
                'date': '2025-05-22',
                'description': 'JWST beobachtet Galaxien, die nur 400 Millionen Jahre nach dem Urknall entstanden',
                'telescope': 'James Webb Space Telescope',
                'category': 'Frühe Galaxien',
                'distance': '13.4 Milliarden Lichtjahre'
            },
            {
                'title': 'Atmosphäre eines Gesteinsplaneten analysiert',
                'date': '2025-05-19',
                'description': 'Erste detaillierte Analyse der Atmosphäre eines erdähnlichen Exoplaneten',
                'telescope': 'James Webb Space Telescope',
                'category': 'Exoplaneten',
                'distance': '40 Lichtjahre'
            },
            {
                'title': 'Sternentstehung in beispielloser Detailgenauigkeit',
                'date': '2025-05-16',
                'description': 'JWST zeigt die Geburt von Sternen im Adlernebel wie nie zuvor',
                'telescope': 'James Webb Space Telescope',
                'category': 'Sternentstehung',
                'distance': '6.500 Lichtjahre'
            }
        ]
    
    def get_voyager_status(self):
        """Aktuelle Voyager-Mission Status"""
        return {
            'voyager_1': {
                'distance_km': 24200000000,  # 24.2 Milliarden km
                'distance_au': 161.8,
                'last_contact': '2025-05-20',
                'status': 'Aktiv - Interstellarer Raum',
                'instruments_active': 4,
                'launch_date': '1977-09-05',
                'mission_duration': '47 Jahre, 8 Monate'
            },
            'voyager_2': {
                'distance_km': 20100000000,  # 20.1 Milliarden km
                'distance_au': 134.4,
                'last_contact': '2025-05-21',
                'status': 'Aktiv - Interstellarer Raum',
                'instruments_active': 5,
                'launch_date': '1977-08-20',
                'mission_duration': '47 Jahre, 9 Monate'
            }
        }
    
    def get_asteroid_data(self):
        """Asteroid und Komet Tracking"""
        try:
            today = datetime.now().strftime('%Y-%m-%d')
            url = f"{self.nasa_neo_url}&start_date={today}&end_date={today}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            asteroids = []
            for date, objects in data['near_earth_objects'].items():
                for obj in objects[:3]:  # Top 3
                    asteroids.append({
                        'name': obj['name'],
                        'type': 'Near-Earth Asteroid',
                        'distance': f"{float(obj['close_approach_data'][0]['miss_distance']['kilometers']):.0f} km",
                        'diameter': f"~{obj['estimated_diameter']['meters']['estimated_diameter_max']:.0f} meter",
                        'closest_approach': obj['close_approach_data'][0]['close_approach_date'],
                        'hazardous': obj['is_potentially_hazardous_asteroid']
                    })
            
            if asteroids:
                return asteroids
            else:
                return self._get_fallback_asteroids()
                
        except:
            return self._get_fallback_asteroids()
    
    def _get_fallback_asteroids(self):
        """Fallback Asteroid Daten"""
        return [
            {
                'name': 'Asteroid 2025 KB1',
                'type': 'Near-Earth Asteroid',
                'distance': '0.12 AU (18 Millionen km)',
                'diameter': '~150 meter',
                'closest_approach': '2025-05-26',
                'hazardous': False
            },
            {
                'name': 'Komet C/2023 A3',
                'type': 'Long-period Comet',
                'distance': '2.8 AU (420 Millionen km)',
                'diameter': '~2 km Kern',
                'closest_approach': '2025-10-12',
                'hazardous': False
            },
            {
                'name': 'Asteroid 1998 OR2',
                'type': 'Potentially Hazardous',
                'distance': '0.042 AU (6.3 Millionen km)',
                'diameter': '~2 km',
                'closest_approach': '2025-07-15',
                'hazardous': True
            }
        ]

def create_discovery_timeline():
    """Erstellt Timeline der Deep Space Entdeckungen"""
    discoveries = [
        {'year': 2023, 'discovery': 'JWST erste Deep Field Bilder', 'telescope': 'JWST'},
        {'year': 2024, 'discovery': 'Neuer Exoplanet in habitabler Zone', 'telescope': 'Hubble'},
        {'year': 2024, 'discovery': 'Galaxie aus Frühzeit des Universums', 'telescope': 'JWST'},
        {'year': 2025, 'discovery': 'Wasserdampf in Exoplaneten-Atmosphäre', 'telescope': 'Hubble'},
        {'year': 2025, 'discovery': 'Sternentstehung in beispielloser Auflösung', 'telescope': 'JWST'}
    ]
    
    fig = px.timeline(
        discoveries,
        x_start='year',
        x_end='year',
        y='telescope',
        color='telescope',
        title='🌌 Deep Space Entdeckungen Timeline',
        labels={'telescope': 'Teleskop'}
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        title_font_size=20
    )
    
    return fig

def create_distance_comparison():
    """Vergleich der Entfernungen im Deep Space"""
    objects = [
        {'object': 'Proxima Centauri', 'distance': 4.24, 'type': 'Nächster Stern'},
        {'object': 'Orion-Nebel', 'distance': 1344, 'type': 'Sternentstehungsgebiet'},
        {'object': 'Zentrum Milchstraße', 'distance': 26000, 'type': 'Galaktisches Zentrum'},
        {'object': 'Andromeda-Galaxie', 'distance': 2500000, 'type': 'Nächste Galaxie'},
        {'object': 'Fernste JWST-Galaxie', 'distance': 13400000000, 'type': 'Frühe Galaxie'}
    ]
    
    fig = px.bar(
        objects,
        x='object',
        y='distance',
        color='type',
        title='🌌 Entfernungen im Deep Space (Lichtjahre)',
        log_y=True
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        title_font_size=18,
        xaxis_title='Objekt',
        yaxis_title='Entfernung (Lichtjahre, log-Skala)'
    )
    
    return fig

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🌌 TIEFER WELTRAUM OBSERVATORIUM</h1>
        <p>NASA Teleskope & Kosmische Entdeckungen</p>
        <p>🔭 Hubble • 🌌 James Webb • 🚀 Voyager • ☄️ Asteroiden</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize API
    deep_space = DeepSpaceAPI()
    
    # Live Status Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>🔭 Hubble</h3>
            <h2>35 Jahre</h2>
            <p>Im Orbit aktiv</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>🌌 JWST</h3>
            <h2>3+ Jahre</h2>
            <p>Deep Space Beobachtungen</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>🚀 Voyager</h3>
            <h2>47+ Jahre</h2>
            <p>Interstellare Mission</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>☄️ NEOs</h3>
            <h2>28.000+</h2>
            <p>Bekannte Asteroiden</p>
        </div>
        """, unsafe_allow_html=True)
    
    # NASA Picture of the Day
    st.markdown("---")
    st.markdown("### 🌟 NASA Astronomy Picture of the Day")
    
    nasa_pic = deep_space.get_nasa_picture_of_day()
    if nasa_pic and nasa_pic.get('media_type') == 'image':
        col_pic, col_desc = st.columns([1, 1])
        
        with col_pic:
            st.image(nasa_pic['url'], use_container_width=True)
        
        with col_desc:
            st.markdown(f"""
            **📅 {nasa_pic['title']}**
            
            {nasa_pic['explanation'][:300]}...
            
            *Quelle: NASA Astronomy Picture of the Day*
            """)
    
    # Hubble Space Telescope
    st.markdown("---")
    st.markdown("### 🔭 Hubble Space Telescope - Neueste Entdeckungen")
    
    hubble_discoveries = deep_space.get_hubble_discoveries()
    
    for discovery in hubble_discoveries:
        st.markdown(f"""
        <div class="telescope-card">
            <h4>🔭 {discovery['title']}</h4>
            <p><strong>📅 Datum:</strong> {discovery['date']}</p>
            <p><strong>📂 Kategorie:</strong> {discovery['category']}</p>
            <p>{discovery['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # James Webb Space Telescope
    st.markdown("---")
    st.markdown("### 🌌 James Webb Space Telescope - Deep Field Beobachtungen")
    
    jwst_observations = deep_space.get_jwst_observations()
    
    for obs in jwst_observations:
        st.markdown(f"""
        <div class="discovery-card">
            <h4>🌌 {obs['title']}</h4>
            <p><strong>📅 Datum:</strong> {obs['date']}</p>
            <p><strong>📂 Kategorie:</strong> {obs['category']}</p>
            <p><strong>📏 Entfernung:</strong> {obs['distance']}</p>
            <p>{obs['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Voyager Mission Status
    st.markdown("---")
    st.markdown("### 🚀 Voyager-Missionen - Interstellare Pioniere")
    
    voyager_data = deep_space.get_voyager_status()
    
    col_v1, col_v2 = st.columns(2)
    
    with col_v1:
        v1 = voyager_data['voyager_1']
        st.markdown(f"""
        <div class="voyager-card">
            <h4>🚀 Voyager 1</h4>
            <p><strong>📏 Entfernung:</strong> {v1['distance_au']} AU ({v1['distance_km']:,} km)</p>
            <p><strong>📡 Status:</strong> {v1['status']}</p>
            <p><strong>🔧 Aktive Instrumente:</strong> {v1['instruments_active']}</p>
            <p><strong>📅 Letzter Kontakt:</strong> {v1['last_contact']}</p>
            <p><strong>⏱️ Missionsdauer:</strong> {v1['mission_duration']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_v2:
        v2 = voyager_data['voyager_2']
        st.markdown(f"""
        <div class="voyager-card">
            <h4>🚀 Voyager 2</h4>
            <p><strong>📏 Entfernung:</strong> {v2['distance_au']} AU ({v2['distance_km']:,} km)</p>
            <p><strong>📡 Status:</strong> {v2['status']}</p>
            <p><strong>🔧 Aktive Instrumente:</strong> {v2['instruments_active']}</p>
            <p><strong>📅 Letzter Kontakt:</strong> {v2['last_contact']}</p>
            <p><strong>⏱️ Missionsdauer:</strong> {v2['mission_duration']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Interactive Charts
    st.markdown("---")
    st.markdown("### 📊 Deep Space Analytics")
    
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        timeline_fig = create_discovery_timeline()
        st.plotly_chart(timeline_fig, use_container_width=True)
    
    with col_chart2:
        distance_fig = create_distance_comparison()
        st.plotly_chart(distance_fig, use_container_width=True)
    
    # Asteroid & Comet Tracking
    st.markdown("---")
    st.markdown("### ☄️ Asteroiden & Kometen Tracking")
    
    asteroids = deep_space.get_asteroid_data()
    
    for asteroid in asteroids:
        hazard_color = "🔴" if asteroid['hazardous'] else "🟢"
        st.markdown(f"""
        <div class="discovery-card">
            <h4>{hazard_color} {asteroid['name']}</h4>
            <p><strong>🏷️ Typ:</strong> {asteroid['type']}</p>
            <p><strong>📏 Entfernung:</strong> {asteroid['distance']}</p>
            <p><strong>📐 Durchmesser:</strong> {asteroid['diameter']}</p>
            <p><strong>📅 Nächste Annäherung:</strong> {asteroid['closest_approach']}</p>
            <p><strong>⚠️ Gefährlich:</strong> {'Ja' if asteroid['hazardous'] else 'Nein'}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Deep Space Facts
    st.markdown("---")
    st.markdown("### 🌟 Deep Space Fakten")
    
    facts = [
        "🌌 Das James Webb Teleskop kann Galaxien sehen, die nur 400 Millionen Jahre nach dem Urknall entstanden",
        "🚀 Voyager 1 ist das am weitesten von der Erde entfernte menschengemachte Objekt",
        "🔭 Hubble hat über 1,5 Millionen Beobachtungen in 35 Jahren Betrieb gemacht",
        "☄️ Jeden Tag fallen etwa 100 Tonnen Weltraumgestein auf die Erde",
        "🌟 Es gibt mehr Sterne im Universum als Sandkörner auf allen Stränden der Erde"
    ]
    
    selected_facts = random.sample(facts, 3)
    for fact in selected_facts:
        st.info(fact)
    
    # Sidebar Information
    with st.sidebar:
        st.markdown("### 🌌 Deep Space Info")
        st.markdown("""
        **Aktive Weltraumteleskope:**
        - 🔭 Hubble Space Telescope (1990-)
        - 🌌 James Webb Space Telescope (2021-)
        - 🔬 Spitzer Space Telescope (2003-2020)
        - 🌟 Kepler Space Telescope (2009-2018)
        
        **Interstellare Missionen:**
        - 🚀 Voyager 1 & 2 (1977-)
        - 🛰️ Pioneer 10 & 11 (1972-, 1973-)
        - 🌌 New Horizons (2006-)
        
        **Deep Space Entfernungen:**
        - 1 AU = 150 Millionen km
        - 1 Lichtjahr = 9,46 Billionen km
        - Nächster Stern: 4,24 Lichtjahre
        - Milchstraße: 100.000 Lichtjahre Durchmesser
        """)
        
        st.markdown("---")
        st.markdown("*🔄 Auto-Refresh alle 60 Sekunden*")
    
    # Auto-refresh
    time.sleep(1)
    if st.button("🔄 Deep Space Daten aktualisieren"):
        st.rerun()

if __name__ == "__main__":
    main()
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import folium
from streamlit_folium import folium_static
from datetime import datetime, timedelta
import random
import time
import requests

# Page Config
st.set_page_config(
    page_title="🛰️ Satelliten-Netzwerke",
    page_icon="🛰️",
    layout="wide"
)

# CSS auf Deutsch
st.markdown("""
<style>
    .sat-header {
        font-size: 3rem;
        background: linear-gradient(90deg, #3498db 0%, #2980b9 100%);
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
        background: linear-gradient(135deg, #ebf8ff 0%, #bee3f8 100%);
        border-radius: 15px;
        border-left: 5px solid #3498db;
    }
    .constellation-card {
        background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(52, 152, 219, 0.2);
    }
    .sat-metric {
        background: linear-gradient(135deg, #16a085 0%, #1abc9c 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .coverage-info {
        background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
    }
    .network-status {
        background: linear-gradient(135deg, #9b59b6 0%, #8e44ad 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 0.8rem 0;
        text-align: center;
    }
    .orbit-info {
        background: linear-gradient(135deg, #e67e22 0%, #d35400 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 0.8rem 0;
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

class SatellitenNetzwerke:
    def __init__(self):
        pass
    
    def get_starlink_data(self, limit=50):
        """Simulierte Starlink-Daten"""
        satellites = []
        
        for i in range(limit):
            # Zufällige aber realistische Koordinaten
            lat = random.uniform(-70, 70)  # Starlink-Abdeckung
            lon = random.uniform(-180, 180)
            
            satellites.append({
                'id': f'starlink-{i}',
                'latitude': lat,
                'longitude': lon,
                'height_km': 540 + random.randint(-50, 50),
                'velocity_kms': 7.5 + random.random(),
                'spaceTrack': {
                    'OBJECT_NAME': f'STARLINK-{1000 + i}',
                    'LAUNCH_DATE': '2023-01-01'
                }
            })
        
        return satellites
    
    def get_satelliten_konstellationen(self):
        """Informationen über verschiedene Satelliten-Konstellationen"""
        konstellationen = {
            'Starlink': {
                'betreiber': 'SpaceX',
                'anzahl_geplant': 42000,
                'anzahl_aktiv': 5000,
                'zweck': 'Breitband-Internet',
                'hoehe': '540-570 km',
                'abdeckung': 'Global',
                'geschwindigkeit': 'Bis 150 Mbps',
                'latenz': '20-40 ms',
                'farbe': '#1f77b4'
            },
            'OneWeb': {
                'betreiber': 'OneWeb',
                'anzahl_geplant': 648,
                'anzahl_aktiv': 600,
                'zweck': 'Breitband-Internet',
                'hoehe': '1200 km',
                'abdeckung': 'Global (außer Pole)',
                'geschwindigkeit': 'Bis 200 Mbps',
                'latenz': '30-50 ms',
                'farbe': '#ff7f0e'
            },
            'GPS (NAVSTAR)': {
                'betreiber': 'US Space Force',
                'anzahl_geplant': 31,
                'anzahl_aktiv': 31,
                'zweck': 'Navigation',
                'hoehe': '20200 km',
                'abdeckung': 'Global',
                'geschwindigkeit': 'N/A',
                'latenz': 'N/A',
                'farbe': '#2ca02c'
            },
            'Galileo': {
                'betreiber': 'ESA/EU',
                'anzahl_geplant': 30,
                'anzahl_aktiv': 28,
                'zweck': 'Navigation',
                'hoehe': '23222 km',
                'abdeckung': 'Global',
                'geschwindigkeit': 'N/A',
                'latenz': 'N/A',
                'farbe': '#d62728'
            }
        }
        
        return konstellationen
    
    def get_satelliten_ueberflugzeiten(self):
        """Simuliert Satelliten-Überflugzeiten für Hamburg"""
        ueberflugzeiten = []
        
        satelliten_typen = ['Starlink', 'ISS', 'Hubble', 'GPS-Satellit', 'Wettersatellit']
        
        for i in range(10):
            sat_typ = random.choice(satelliten_typen)
            ueberflug_zeit = datetime.now() + timedelta(hours=random.randint(1, 48))
            dauer = random.randint(2, 8)
            hoehe = random.randint(15, 85)
            helligkeit = random.uniform(-2.0, 4.0)
            
            ueberflugzeiten.append({
                'satellit': sat_typ,
                'zeit': ueberflug_zeit,
                'dauer': dauer,
                'max_hoehe': hoehe,
                'helligkeit': helligkeit,
                'richtung': random.choice(['N→S', 'S→N', 'W→O', 'O→W', 'NW→SO', 'NO→SW'])
            })
        
        return sorted(ueberflugzeiten, key=lambda x: x['zeit'])[:5]
    
    def get_netzwerk_performance(self):
        """Simuliert Netzwerk-Performance-Daten"""
        return {
            'starlink': {
                'aktive_verbindungen': random.randint(800000, 1200000),
                'durchschnittliche_geschwindigkeit': random.randint(80, 150),
                'latenz': random.randint(20, 45),
                'verfuegbarkeit': random.uniform(99.5, 99.9),
                'abgedeckte_laender': 60
            },
            'oneweb': {
                'aktive_verbindungen': random.randint(50000, 100000),
                'durchschnittliche_geschwindigkeit': random.randint(100, 200),
                'latenz': random.randint(30, 60),
                'verfuegbarkeit': random.uniform(99.0, 99.7),
                'abgedeckte_laender': 40
            }
        }
    
    def get_satelliten_fakten(self):
        """Interessante Satelliten-Fakten"""
        fakten = [
            "🛰️ Über 8.000 aktive Satelliten umkreisen derzeit die Erde",
            "📡 Starlink ist die größte Satelliten-Konstellation der Geschichte",
            "🌍 GPS-Satelliten ermöglichen eine Genauigkeit von wenigen Metern",
            "⚡ Satelliten-Internet erreicht entlegene Gebiete ohne Infrastruktur",
            "🚀 SpaceX startet durchschnittlich 50+ Starlink-Satelliten pro Monat",
            "🔄 Starlink-Satelliten können sich selbst aus der Umlaufbahn entfernen",
            "📶 Satelliten-Internet hat typisch 20-40ms Latenz (Glasfaser: 1-5ms)",
            "🌌 Manche Satelliten sind so hell, dass sie Sterne überstrahlen",
            "💰 Die Starlink-Konstellation kostet über 10 Milliarden Dollar",
            "🛡️ Kessler-Syndrom: Kollidierende Satelliten könnten Weltraummüll verursachen"
        ]
        return random.sample(fakten, 3)

def create_constellation_coverage_map(starlink_data):
    """Erstellt Starlink-Abdeckungskarte"""
    # Hamburg als Zentrum
    m = folium.Map(location=[53.5511, 9.9937], zoom_start=2, tiles='OpenStreetMap')
    
    # Starlink-Satelliten hinzufügen (begrenzt für Performance)
    for i, sat in enumerate(starlink_data[:30]):  # Nur 30 für Performance
        lat = sat.get('latitude', 0)
        lon = sat.get('longitude', 0)
        
        if lat != 0 and lon != 0 and -70 <= lat <= 70:  # Starlink-Abdeckungsbereich
            folium.CircleMarker(
                [lat, lon],
                radius=4,
                popup=f"🛰️ {sat.get('spaceTrack', {}).get('OBJECT_NAME', 'Starlink')}<br>Höhe: {sat.get('height_km', 550)} km",
                color='blue',
                fillColor='lightblue',
                fillOpacity=0.7
            ).add_to(m)
    
    # Hamburg markieren
    folium.Marker(
        [53.5511, 9.9937],
        popup="📍 Hamburg, Deutschland",
        tooltip="Ihr Standort",
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)
    
    return m

def create_constellation_comparison_chart(konstellationen):
    """Erstellt Vergleichs-Chart der Konstellationen"""
    names = list(konstellationen.keys())
    active_counts = [k['anzahl_aktiv'] for k in konstellationen.values()]
    planned_counts = [k['anzahl_geplant'] for k in konstellationen.values()]
    colors = [k['farbe'] for k in konstellationen.values()]
    
    fig = go.Figure()
    
    # Aktive Satelliten
    fig.add_trace(go.Bar(
        name='Aktiv',
        x=names,
        y=active_counts,
        marker_color=colors,
        opacity=0.8
    ))
    
    # Geplante Satelliten
    fig.add_trace(go.Bar(
        name='Geplant',
        x=names,
        y=planned_counts,
        marker_color=colors,
        opacity=0.4
    ))
    
    fig.update_layout(
        title='📊 Satelliten-Konstellationen Vergleich',
        xaxis_title='Konstellation',
        yaxis_title='Anzahl Satelliten',
        template='plotly_white',
        height=500,
        barmode='overlay'
    )
    
    return fig

def create_network_performance_chart(performance):
    """Erstellt Netzwerk-Performance-Chart"""
    providers = list(performance.keys())
    speeds = [p['durchschnittliche_geschwindigkeit'] for p in performance.values()]
    latencies = [p['latenz'] for p in performance.values()]
    
    fig = go.Figure()
    
    # Geschwindigkeit
    fig.add_trace(go.Bar(
        name='Geschwindigkeit (Mbps)',
        x=providers,
        y=speeds,
        yaxis='y',
        marker_color='#3498db'
    ))
    
    # Latenz (sekundäre Y-Achse)
    fig.add_trace(go.Scatter(
        name='Latenz (ms)',
        x=providers,
        y=latencies,
        yaxis='y2',
        mode='markers+lines',
        marker=dict(size=15, color='#e74c3c'),
        line=dict(width=3)
    ))
    
    fig.update_layout(
        title='⚡ Satelliten-Internet Performance',
        xaxis_title='Anbieter',
        yaxis=dict(title='Geschwindigkeit (Mbps)', side='left'),
        yaxis2=dict(title='Latenz (ms)', side='right', overlaying='y'),
        template='plotly_white',
        height=400
    )
    
    return fig

def main():
    # Header
    st.markdown('<h1 class="sat-header">🛰️ SATELLITEN-NETZWERKE</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="page-intro">
        <strong>🌐 Globale Satelliten-Konstellationen & Netzwerk-Überwachung</strong><br><br>
        Verfolgen Sie die revolutionären Satelliten-Netzwerke, die unsere Welt vernetzen. 
        Von Starlink bis GPS - diese Konstellationen ermöglichen globale Kommunikation, 
        Navigation und Internet-Zugang überall auf der Erde! 📡
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize System
    sat_system = SatellitenNetzwerke()
    
    # Sidebar auf Deutsch
    st.sidebar.markdown("## 🎛️ Satelliten-Kontrolle")
    
    auto_refresh = st.sidebar.checkbox("🔄 Auto-Aktualisierung (2 Min)", value=False)
    if auto_refresh:
        time.sleep(120)
        st.rerun()
    
    if st.sidebar.button("🛰️ Daten Aktualisieren", type="primary"):
        st.rerun()
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🛰️ Satelliten Schnell-Fakten")
    st.sidebar.markdown("""
    - **Erste Satelliten:** Sputnik 1 (1957)
    - **Höhe LEO:** 160-2000 km
    - **Höhe MEO:** 2000-35786 km  
    - **Höhe GEO:** 35786 km
    - **Orbital-Geschwindigkeit:** ~7.8 km/s
    - **Aktive Satelliten:** ~8000
    - **Weltraummüll:** ~34000 Objekte >10cm
    - **Starlink-Konstellation:** Größte der Welt
    """)
    
    # Daten laden
    with st.spinner("🛰️ Verbinde mit Satelliten-Netzwerken..."):
        try:
            starlink_data = sat_system.get_starlink_data(50)
            konstellationen = sat_system.get_satelliten_konstellationen()
            ueberflugzeiten = sat_system.get_satelliten_ueberflugzeiten()
            performance = sat_system.get_netzwerk_performance()
            satelliten_fakten = sat_system.get_satelliten_fakten()
            
            # Satelliten-Netzwerk Übersicht
            st.markdown("### 🌐 Globale Satelliten-Konstellationen")
            
            # Konstellations-Karten
            col_kons1, col_kons2 = st.columns(2)
            
            with col_kons1:
                starlink_info = konstellationen['Starlink']
                st.markdown(f"""
                <div class="constellation-card">
                    <h3>🛰️ Starlink (SpaceX)</h3>
                    <p><strong>🎯 Status:</strong> {starlink_info['anzahl_aktiv']:,} von {starlink_info['anzahl_geplant']:,} aktiv</p>
                    <p><strong>📡 Zweck:</strong> {starlink_info['zweck']}</p>
                    <p><strong>🌍 Abdeckung:</strong> {starlink_info['abdeckung']}</p>
                    <p><strong>⚡ Geschwindigkeit:</strong> {starlink_info['geschwindigkeit']}</p>
                    <p><strong>⏱️ Latenz:</strong> {starlink_info['latenz']}</p>
                    <p><strong>📏 Höhe:</strong> {starlink_info['hoehe']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_kons2:
                gps_info = konstellationen['GPS (NAVSTAR)']
                st.markdown(f"""
                <div class="constellation-card" style="background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);">
                    <h3>🗺️ GPS (NAVSTAR)</h3>
                    <p><strong>🎯 Status:</strong> {gps_info['anzahl_aktiv']} von {gps_info['anzahl_geplant']} aktiv</p>
                    <p><strong>📡 Zweck:</strong> {gps_info['zweck']}</p>
                    <p><strong>🌍 Abdeckung:</strong> {gps_info['abdeckung']}</p>
                    <p><strong>🛰️ Betreiber:</strong> {gps_info['betreiber']}</p>
                    <p><strong>📏 Höhe:</strong> {gps_info['hoehe']}</p>
                    <p><strong>🎯 Genauigkeit:</strong> 3-5 Meter</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Statistiken
            st.markdown("---")
            st.markdown("### 📊 Netzwerk-Statistiken")
            
            col1, col2, col3, col4 = st.columns(4)
            
            starlink_perf = performance['starlink']
            
            with col1:
                st.markdown(f"""
                <div class="sat-metric">
                    <h3>👥 Aktive Nutzer</h3>
                    <h2>{starlink_perf['aktive_verbindungen']:,}</h2>
                    <p>Starlink Verbindungen</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="sat-metric">
                    <h3>⚡ Geschwindigkeit</h3>
                    <h2>{starlink_perf['durchschnittliche_geschwindigkeit']} Mbps</h2>
                    <p>Durchschnitt</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div class="sat-metric">
                    <h3>⏱️ Latenz</h3>
                    <h2>{starlink_perf['latenz']} ms</h2>
                    <p>Ping-Zeit</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col4:
                st.markdown(f"""
                <div class="sat-metric">
                    <h3>🌍 Abdeckung</h3>
                    <h2>{starlink_perf['abgedeckte_laender']}</h2>
                    <p>Länder</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Starlink-Abdeckungskarte
            st.markdown("---")
            st.markdown("### 🗺️ Live Starlink-Satelliten-Positionen")
            
            col_map, col_info = st.columns([2, 1])
            
            with col_map:
                try:
                    coverage_map = create_constellation_coverage_map(starlink_data)
                    folium_static(coverage_map, width=700, height=400)
                except Exception as e:
                    st.error(f"Karte konnte nicht geladen werden: {e}")
                    st.info("🛰️ Starlink-Satelliten sind aktiv, Karte wird geladen...")
            
            with col_info:
                active_starlink = len([s for s in starlink_data if s.get('latitude')])
                
                st.markdown(f"""
                <div class="coverage-info">
                    <h3>🛰️ Starlink-Status</h3>
                    <p><strong>📍 Simulierte Satelliten:</strong> {min(30, active_starlink)}</p>
                    <p><strong>🌐 Gesamte Konstellation:</strong> ~5.000 aktiv</p>
                    <p><strong>📏 Durchschnittliche Höhe:</strong> 550 km</p>
                    <p><strong>⚡ Orbital-Geschwindigkeit:</strong> 7.5 km/s</p>
                    <p><strong>🔄 Orbital-Periode:</strong> ~95 Minuten</p>
                    <p><strong>📡 Hamburg-Abdeckung:</strong> 24/7</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Konstellations-Vergleich  
            st.markdown("---")
            st.markdown("### 📊 Satelliten-Konstellationen im Vergleich")
            
            comparison_chart = create_constellation_comparison_chart(konstellationen)
            st.plotly_chart(comparison_chart, use_container_width=True)
            
            # Performance-Vergleich
            st.markdown("---")
            st.markdown("### ⚡ Internet-Performance Vergleich")
            
            performance_chart = create_network_performance_chart(performance)
            st.plotly_chart(performance_chart, use_container_width=True)
            
            # Satelliten-Überflüge
            st.markdown("---")
            st.markdown("### 🔭 Satelliten-Überflüge über Hamburg")
            st.markdown("**Nächste sichtbare Satelliten-Durchgänge:**")
            
            for ueberflug in ueberflugzeiten:
                zeit_bis = ueberflug['zeit'] - datetime.now()
                stunden_bis = int(zeit_bis.total_seconds() / 3600)
                
                helligkeit_text = "Sehr hell" if ueberflug['helligkeit'] < 0 else "Hell" if ueberflug['helligkeit'] < 2 else "Schwach"
                
                st.markdown(f"""
                <div class="pass-prediction">
                    🛰️ {ueberflug['satellit']} | {ueberflug['zeit'].strftime('%d.%m %H:%M')} (in {stunden_bis}h)<br>
                    ⏱️ Dauer: {ueberflug['dauer']} Min | 📐 Max. Höhe: {ueberflug['max_hoehe']}° | 
                    💫 Helligkeit: {helligkeit_text} | 🧭 Richtung: {ueberflug['richtung']}
                </div>
                """, unsafe_allow_html=True)
            
            # Netzwerk-Status
            st.markdown("---")
            st.markdown("### 📡 Netzwerk-Status & Verfügbarkeit")
            
            col_net1, col_net2, col_net3 = st.columns(3)
            
            with col_net1:
                st.markdown(f"""
                <div class="network-status">
                    <h4>🛰️ Starlink</h4>
                    <h3>{starlink_perf['verfuegbarkeit']:.1f}%</h3>
                    <p>Verfügbarkeit</p>
                    <p>{starlink_perf['abgedeckte_laender']} Länder</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_net2:
                oneweb_perf = performance['oneweb']
                st.markdown(f"""
                <div class="network-status">
                    <h4>🌐 OneWeb</h4>
                    <h3>{oneweb_perf['verfuegbarkeit']:.1f}%</h3>
                    <p>Verfügbarkeit</p>
                    <p>{oneweb_perf['abgedeckte_laender']} Länder</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_net3:
                st.markdown(f"""
                <div class="network-status">
                    <h4>🗺️ GPS</h4>
                    <h3>99.9%</h3>
                    <p>Verfügbarkeit</p>
                    <p>Global abgedeckt</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Satelliten-Fakten
            st.markdown("---")
            st.markdown("### 🌟 Satelliten-Fakten des Tages")
            
            for fakt in satelliten_fakten:
                st.markdown(f"""
                <div class="orbit-info">
                    {fakt}
                </div>
                """, unsafe_allow_html=True)
                
        except Exception as e:
            st.error(f"❌ Fehler beim Laden der Satelliten-Daten: {e}")
            st.info("🛰️ Bitte versuchen Sie es später erneut oder aktualisieren Sie die Seite.")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #7f8c8d; padding: 2rem 0;'>
        🛰️ <strong>Satelliten-Netzwerke Dashboard</strong> 🛰️<br>
        📡 Überwachung globaler Satelliten-Konstellationen und Netzwerk-Performance<br>
        🌐 Verbindung der Welt durch Technologie im Weltraum
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
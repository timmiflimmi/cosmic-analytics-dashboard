import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import math
import time
import random

# Page Config
st.set_page_config(
    page_title="🌙 Lunar & Planetary",
    page_icon="🌙",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .lunar-header {
        font-size: 3rem;
        background: linear-gradient(90deg, #9b59b6 0%, #8e44ad 100%);
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
        background: linear-gradient(135deg, #f4f1f8 0%, #e8d5f0 100%);
        border-radius: 15px;
        border-left: 5px solid #9b59b6;
    }
    .moon-phase-card {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 12px 40px rgba(52, 73, 94, 0.3);
    }
    .planet-card {
        background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
        padding: 1.2rem;
        border-radius: 12px;
        color: white;
        margin: 0.8rem 0;
        text-align: center;
    }
    .lunar-stat {
        background: linear-gradient(135deg, #9b59b6 0%, #8e44ad 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .eclipse-card {
        background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
    }
    .stargazing-tip {
        background: linear-gradient(135deg, #f39c12 0%, #e67e22 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 0.8rem 0;
    }
    .conjunction-alert {
        background: linear-gradient(135deg, #1abc9c 0%, #16a085 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 0.5rem 0;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

class LunarPlanetaryTracker:
    def __init__(self):
        pass
    
    def get_moon_phase(self):
        """Berechnet aktuelle Mondphase"""
        # Referenzdatum: Neumond am 13. Januar 2025
        reference_new_moon = datetime(2025, 1, 13)
        now = datetime.now()
        
        # Mondphase-Zyklus: 29.53 Tage
        lunar_cycle = 29.53
        
        # Tage seit Referenz-Neumond
        days_since = (now - reference_new_moon).total_seconds() / (24 * 3600)
        
        # Position im Zyklus (0-1)
        cycle_position = (days_since % lunar_cycle) / lunar_cycle
        
        # Mondphase bestimmen
        if cycle_position < 0.0625:  # Neumond
            phase_name = "🌑 Neumond"
            illumination = 0
        elif cycle_position < 0.1875:  # Zunehmende Sichel
            phase_name = "🌒 Zunehmende Sichel"
            illumination = 25
        elif cycle_position < 0.3125:  # Erstes Viertel
            phase_name = "🌓 Erstes Viertel"
            illumination = 50
        elif cycle_position < 0.4375:  # Zunehmender Mond
            phase_name = "🌔 Zunehmender Mond"
            illumination = 75
        elif cycle_position < 0.5625:  # Vollmond
            phase_name = "🌕 Vollmond"
            illumination = 100
        elif cycle_position < 0.6875:  # Abnehmender Mond
            phase_name = "🌖 Abnehmender Mond"
            illumination = 75
        elif cycle_position < 0.8125:  # Letztes Viertel
            phase_name = "🌗 Letztes Viertel"
            illumination = 50
        else:  # Abnehmende Sichel
            phase_name = "🌘 Abnehmende Sichel"
            illumination = 25
        
        # Nächste Mondphasen berechnen
        days_to_next_new = (lunar_cycle - (days_since % lunar_cycle)) % lunar_cycle
        days_to_next_full = (lunar_cycle/2 - (days_since % lunar_cycle)) % lunar_cycle
        if days_to_next_full < 0:
            days_to_next_full += lunar_cycle
        
        return {
            'phase_name': phase_name,
            'illumination': illumination,
            'cycle_position': cycle_position,
            'days_to_next_new': int(days_to_next_new),
            'days_to_next_full': int(days_to_next_full),
            'next_new_moon': now + timedelta(days=days_to_next_new),
            'next_full_moon': now + timedelta(days=days_to_next_full)
        }
    
    def calculate_planet_positions(self):
        """Berechnet aktuelle Planetenpositionen"""
        try:
            day_of_year = datetime.now().timetuple().tm_yday
            
            planets = {
                'Mercury': {
                    'distance': 0.39, 'period': 88, 'color': '#8C7853',
                    'description': 'Sonnennächster Planet'
                },
                'Venus': {
                    'distance': 0.72, 'period': 225, 'color': '#FFC649',
                    'description': 'Morgen-/Abendstern'
                },
                'Mars': {
                    'distance': 1.52, 'period': 687, 'color': '#CD5C5C',
                    'description': 'Der Rote Planet'
                },
                'Jupiter': {
                    'distance': 5.2, 'period': 4333, 'color': '#D2691E',
                    'description': 'Größter Planet'
                },
                'Saturn': {
                    'distance': 9.5, 'period': 10759, 'color': '#FAD5A5',
                    'description': 'Planet mit Ringen'
                }
            }
            
            for planet in planets:
                angle = (day_of_year / planets[planet]['period']) * 360
                planets[planet]['angle'] = angle % 360
                planets[planet]['x'] = planets[planet]['distance'] * math.cos(math.radians(angle))
                planets[planet]['y'] = planets[planet]['distance'] * math.sin(math.radians(angle))
                
                # Sichtbarkeit berechnen (vereinfacht)
                planets[planet]['visible'] = self._calculate_visibility(planets[planet]['angle'])
            
            return planets
            
        except Exception as e:
            st.error(f"Planet calculation error: {e}")
            return None
    
    def _calculate_visibility(self, angle):
        """Berechnet ob Planet sichtbar ist (vereinfacht)"""
        # Vereinfachte Sichtbarkeitsberechnung
        if 90 <= angle <= 270:
            return "Abendhimmel"
        else:
            return "Morgenhimmel"
    
    def get_lunar_eclipses(self):
        """Vorhersage zukünftiger Mondfinsternisse"""
        # Bekannte Mondfinsternis-Daten für 2025-2026
        eclipses = [
            {
                'date': datetime(2025, 9, 7),
                'type': 'Partielle Mondfinsternis',
                'visibility': 'Europa, Afrika, Asien',
                'duration': '3h 28m'
            },
            {
                'date': datetime(2026, 3, 3),
                'type': 'Totale Mondfinsternis',
                'visibility': 'Pazifik, Australien, Asien',
                'duration': '3h 20m'
            },
            {
                'date': datetime(2026, 8, 28),
                'type': 'Partielle Mondfinsternis',
                'visibility': 'Amerika, Europa',
                'duration': '2h 56m'
            }
        ]
        
        # Nur zukünftige Finsternisse
        now = datetime.now()
        future_eclipses = [e for e in eclipses if e['date'] > now]
        
        return future_eclipses[:2]  # Nächste 2 Finsternisse
    
    def get_stargazing_conditions(self):
        """Sternbeobachtungs-Bedingungen für Hamburg"""
        moon_phase = self.get_moon_phase()
        
        # Mondschein-Einfluss
        if moon_phase['illumination'] < 25:
            moon_interference = "Ausgezeichnet"
            moon_color = "#27ae60"
        elif moon_phase['illumination'] < 75:
            moon_interference = "Gut"
            moon_color = "#f39c12"
        else:
            moon_interference = "Schwierig"
            moon_color = "#e74c3c"
        
        # Beste Beobachtungszeiten
        best_times = [
            "22:00 - 24:00 Uhr (Abend)",
            "02:00 - 05:00 Uhr (Früh)",
            "Mondschein berücksichtigen"
        ]
        
        # Planetensichtbarkeit
        planets = self.calculate_planet_positions()
        visible_planets = []
        if planets:
            for name, data in planets.items():
                if data.get('visible'):
                    visible_planets.append(f"{name} ({data['visible']})")
        
        return {
            'moon_interference': moon_interference,
            'moon_color': moon_color,
            'best_times': best_times,
            'visible_planets': visible_planets[:3],  # Top 3
            'moon_phase': moon_phase['phase_name']
        }
    
    def get_planetary_conjunctions(self):
        """Vorhersage Planetenkonjunktionen"""
        # Simulierte/vereinfachte Konjunktionen
        conjunctions = [
            {
                'date': datetime.now() + timedelta(days=15),
                'planets': 'Venus & Jupiter',
                'description': 'Sehr enge Konjunktion am Abendhimmel',
                'separation': '0.5°'
            },
            {
                'date': datetime.now() + timedelta(days=45),
                'planets': 'Mars & Saturn',
                'description': 'Morgendliche Konjunktion',
                'separation': '2.1°'
            }
        ]
        
        return conjunctions
    
    def get_lunar_facts(self):
        """Interessante Mond-Fakten"""
        facts = [
            "🌙 Der Mond entfernt sich jährlich 3,8 cm von der Erde",
            "🌍 Der Mond stabilisiert die Erdachse und unsere Jahreszeiten",
            "🌊 Ebbe und Flut entstehen durch die Mondanziehungskraft",
            "🌙 Die Rückseite des Mondes ist nicht 'dunkel' - sie hat auch Tag und Nacht",
            "🚀 12 Menschen haben bisher den Mond betreten (Apollo-Missionen)",
            "🌙 Der Mond ist etwa 1/4 so groß wie die Erde",
            "⏰ Ein Mondtag dauert etwa 29,5 Erdtage",
            "🌙 Der Mond hat Wassereis an seinen Polen",
            "📡 China, USA und Indien haben Rover auf dem Mond",
            "🌙 Der Mond entstand wahrscheinlich durch eine Kollision vor 4,5 Mrd Jahren"
        ]
        return random.sample(facts, 3)

def create_solar_system_plot(planets):
    """Erstellt interaktives Sonnensystem-Diagramm"""
    if not planets:
        return None
        
    fig = go.Figure()
    
    # Sonne in der Mitte
    fig.add_trace(go.Scatter(
        x=[0], y=[0],
        mode='markers',
        marker=dict(size=30, color='gold', symbol='star'),
        name='Sonne',
        hovertemplate='☀️ Sonne<br>Zentrum unseres Sonnensystems<extra></extra>'
    ))
    
    # Planeten
    for planet_name, data in planets.items():
        fig.add_trace(go.Scatter(
            x=[data['x']], y=[data['y']],
            mode='markers',
            marker=dict(size=15, color=data['color']),
            name=planet_name,
            hovertemplate=f'🪐 {planet_name}<br>Entfernung: {data["distance"]:.1f} AE<br>Winkel: {data["angle"]:.1f}°<br>Sichtbar: {data.get("visible", "Unbekannt")}<extra></extra>'
        ))
        
        # Orbit-Kreise
        theta = [i * 2 * math.pi / 100 for i in range(101)]
        orbit_x = [data['distance'] * math.cos(t) for t in theta]
        orbit_y = [data['distance'] * math.sin(t) for t in theta]
        
        fig.add_trace(go.Scatter(
            x=orbit_x, y=orbit_y,
            mode='lines',
            line=dict(color=data['color'], width=1, dash='dot'),
            showlegend=False,
            hoverinfo='skip'
        ))
    
    fig.update_layout(
        title='🌌 Sonnensystem - Aktuelle Planetenpositionen',
        xaxis_title='Entfernung (AE)',
        yaxis_title='Entfernung (AE)',
        template='plotly_dark',
        height=600,
        showlegend=True,
        xaxis=dict(scaleanchor="y", scaleratio=1),
        yaxis=dict(scaleanchor="x", scaleratio=1),
        plot_bgcolor='rgba(0,0,0,0.8)'
    )
    
    return fig

def create_moon_phase_calendar():
    """Erstellt Mondphasen-Kalender für nächste 4 Wochen"""
    lunar_tracker = LunarPlanetaryTracker()
    moon_data = lunar_tracker.get_moon_phase()
    
    # Simuliere Mondphasen für nächste 28 Tage
    dates = []
    phases = []
    illuminations = []
    
    for i in range(28):
        date = datetime.now() + timedelta(days=i)
        # Vereinfachte Mondphasen-Berechnung
        cycle_day = (i + moon_data['cycle_position'] * 29.53) % 29.53
        
        if cycle_day < 7.4:
            phase = 'Zunehmend'
            illum = int(cycle_day / 7.4 * 50)
        elif cycle_day < 14.8:
            phase = 'Vollmond'
            illum = int(50 + (cycle_day - 7.4) / 7.4 * 50)
        elif cycle_day < 22.1:
            phase = 'Abnehmend'
            illum = int(100 - (cycle_day - 14.8) / 7.3 * 50)
        else:
            phase = 'Neumond'
            illum = int(50 - (cycle_day - 22.1) / 7.4 * 50)
        
        dates.append(date.strftime('%d.%m'))
        phases.append(phase)
        illuminations.append(max(0, illum))
    
    fig = go.Figure(data=go.Bar(
        x=dates,
        y=illuminations,
        marker_color=[
            '#f39c12' if p == 'Vollmond' else 
            '#3498db' if p == 'Zunehmend' else 
            '#9b59b6' if p == 'Abnehmend' else '#2c3e50'
            for p in phases
        ],
        text=phases,
        textposition='auto',
        hovertemplate='<b>%{x}</b><br>Phase: %{text}<br>Beleuchtung: %{y}%<extra></extra>'
    ))
    
    fig.update_layout(
        title='🌙 Mondphasen-Kalender (Nächste 4 Wochen)',
        xaxis_title='Datum',
        yaxis_title='Beleuchtung (%)',
        template='plotly_white',
        height=400
    )
    
    return fig

def main():
    # Header
    st.markdown('<h1 class="lunar-header">🌙 LUNAR & PLANETARY DASHBOARD</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="page-intro">
        <strong>🌌 Moon Phases, Planets & Solar System Tracking</strong><br><br>
        Explore our cosmic neighborhood! Track moon phases, planet positions, and upcoming celestial events. 
        Perfect for stargazing from Hamburg and understanding our place in the solar system. 
        The universe awaits your discovery! ✨
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize tracker
    tracker = LunarPlanetaryTracker()
    
    # Sidebar Controls
    st.sidebar.markdown("## 🎛️ Lunar Observatory")
    
    auto_refresh = st.sidebar.checkbox("🔄 Auto-Refresh (5 min)", value=False)
    if auto_refresh:
        time.sleep(300)
        st.rerun()
    
    if st.sidebar.button("🌙 Update Lunar Data", type="primary"):
        st.rerun()
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🌙 Lunar Quick Facts")
    st.sidebar.markdown("""
    - **Distance:** 384,400 km from Earth
    - **Diameter:** 3,474 km (1/4 of Earth)
    - **Orbital Period:** 27.3 days
    - **Lunar Day:** 29.5 Earth days
    - **Gravity:** 1/6 of Earth's gravity
    - **Temperature:** -173°C to +127°C
    - **Age:** ~4.5 billion years
    - **Formation:** Giant impact theory
    """)
    
    # Get data
    with st.spinner("🌙 Calculating celestial positions..."):
        moon_data = tracker.get_moon_phase()
        planets = tracker.calculate_planet_positions()
        stargazing = tracker.get_stargazing_conditions()
        lunar_eclipses = tracker.get_lunar_eclipses()
        conjunctions = tracker.get_planetary_conjunctions()
        lunar_facts = tracker.get_lunar_facts()
        
        # Current Moon Phase (Featured)
        st.markdown("### 🌙 Current Moon Phase")
        
        col_moon, col_info = st.columns([1, 2])
        
        with col_moon:
            st.markdown(f"""
            <div class="moon-phase-card">
                <h2>{moon_data['phase_name']}</h2>
                <h1 style="font-size: 4rem; margin: 1rem 0;">{moon_data['illumination']}%</h1>
                <p style="font-size: 1.2rem;">Beleuchtung</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_info:
            next_new = moon_data['next_new_moon'].strftime('%d.%m.%Y')
            next_full = moon_data['next_full_moon'].strftime('%d.%m.%Y')
            
            st.markdown(f"""
            <div class="lunar-stat">
                <h3>📅 Nächste Mondphasen</h3>
                <p><strong>🌑 Neumond:</strong> {next_new} (in {moon_data['days_to_next_new']} Tagen)</p>
                <p><strong>🌕 Vollmond:</strong> {next_full} (in {moon_data['days_to_next_full']} Tagen)</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="lunar-stat">
                <h3>🔭 Stargazing Conditions</h3>
                <p><strong>Mondschein:</strong> <span style="color: {stargazing['moon_color']}">{stargazing['moon_interference']}</span></p>
                <p><strong>Beste Zeit:</strong> {stargazing['best_times'][0]}</p>
                <p><strong>Mondphase:</strong> {stargazing['moon_phase']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Moon Phase Calendar
        st.markdown("---")
        st.markdown("### 📅 Mondphasen-Kalender")
        
        moon_calendar = create_moon_phase_calendar()
        st.plotly_chart(moon_calendar, use_container_width=True)
        
        # Solar System Visualization
        if planets:
            st.markdown("---")
            st.markdown("### 🌌 Sonnensystem - Live Planetenpositionen")
            
            solar_system_fig = create_solar_system_plot(planets)
            if solar_system_fig:
                st.plotly_chart(solar_system_fig, use_container_width=True)
            
            # Planet Visibility
            st.markdown("### 🪐 Planetensichtbarkeit von Hamburg")
            
            planet_cols = st.columns(len(planets))
            
            for i, (name, data) in enumerate(planets.items()):
                col = planet_cols[i]
                
                visibility_color = "#27ae60" if "Abend" in data.get('visible', '') else "#3498db"
                
                col.markdown(f"""
                <div class="planet-card" style="background: linear-gradient(135deg, {data['color']} 0%, {data['color']}aa 100%);">
                    <h4>🪐 {name}</h4>
                    <p><strong>Entfernung:</strong> {data['distance']} AE</p>
                    <p><strong>Position:</strong> {data['angle']:.0f}°</p>
                    <p><strong>Sichtbar:</strong> {data.get('visible', 'Berechnung...')}</p>
                    <p style="font-size: 0.9rem;"><em>{data['description']}</em></p>
                </div>
                """, unsafe_allow_html=True)
        
        # Lunar Eclipses
        if lunar_eclipses:
            st.markdown("---")
            st.markdown("### 🌙 Kommende Mondfinsternisse")
            
            for eclipse in lunar_eclipses:
                days_until = (eclipse['date'] - datetime.now()).days
                
                st.markdown(f"""
                <div class="eclipse-card">
                    <h4>🌙 {eclipse['type']}</h4>
                    <p><strong>📅 Datum:</strong> {eclipse['date'].strftime('%d.%m.%Y')} (in {days_until} Tagen)</p>
                    <p><strong>🌍 Sichtbar in:</strong> {eclipse['visibility']}</p>
                    <p><strong>⏱️ Dauer:</strong> {eclipse['duration']}</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Planetary Conjunctions
        if conjunctions:
            st.markdown("---")
            st.markdown("### ✨ Planetenkonjunktionen")
            
            for conj in conjunctions:
                days_until = (conj['date'] - datetime.now()).days
                
                st.markdown(f"""
                <div class="conjunction-alert">
                    ✨ {conj['planets']} | {conj['date'].strftime('%d.%m.%Y')} (in {days_until} Tagen)<br>
                    {conj['description']} | Abstand: {conj['separation']}
                </div>
                """, unsafe_allow_html=True)
        
        # Stargazing Tips
        st.markdown("---")
        st.markdown("### 🔭 Stargazing Guide für Hamburg")
        
        col_tips1, col_tips2 = st.columns(2)
        
        with col_tips1:
            st.markdown(f"""
            <div class="stargazing-tip">
                <h4>🌃 Beste Beobachtungsplätze</h4>
                <ul>
                    <li>🏞️ Alsterwiesen (wenig Lichtsmog)</li>
                    <li>🌊 Elbufer (freier Horizont)</li>
                    <li>🌲 Stadtpark (dunklere Bereiche)</li>
                    <li>🚗 Außerhalb: Lüneburger Heide</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col_tips2:
            visible_planets_text = ", ".join(stargazing['visible_planets']) if stargazing['visible_planets'] else "Keine besonderen Sichtungen"
            
            st.markdown(f"""
            <div class="stargazing-tip">
                <h4>👀 Heute Nacht sichtbar</h4>
                <ul>
                    <li>🌙 Mond: {stargazing['moon_phase']}</li>
                    <li>🪐 Planeten: {visible_planets_text}</li>
                    <li>⏰ Beste Zeit: {stargazing['best_times'][0]}</li>
                    <li>🌟 Bedingungen: {stargazing['moon_interference']}</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # Lunar Facts
        st.markdown("---")
        st.markdown("### 🌟 Lunar Facts of the Day")
        
        for fact in lunar_facts:
            st.markdown(f"""
            <div class="stargazing-tip">
                {fact}
            </div>
            """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #7f8c8d; padding: 2rem 0;'>
        🌙 <strong>Lunar & Planetary Dashboard</strong> 🌙<br>
        🔭 Your guide to celestial observations from Hamburg<br>
        ✨ Connecting you with the wonders of our solar system
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
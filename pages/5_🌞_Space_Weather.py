import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random
import time

# Page Config
st.set_page_config(
    page_title="🌞 Weltraum-Wetter",
    page_icon="🌞",
    layout="wide"
)

# CSS auf Deutsch
st.markdown("""
<style>
    .weather-header {
        font-size: 3rem;
        background: linear-gradient(90deg, #f39c12 0%, #e67e22 100%);
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
        background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
        border-radius: 15px;
        border-left: 5px solid #f39c12;
    }
    .solar-metric {
        background: linear-gradient(135deg, #f39c12 0%, #e67e22 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
        box-shadow: 0 8px 32px rgba(243, 156, 18, 0.2);
    }
    .aurora-card {
        background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
    }
    .flare-alert {
        background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 0.5rem 0;
        font-weight: bold;
    }
    .magnetic-info {
        background: linear-gradient(135deg, #9b59b6 0%, #8e44ad 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
    }
    .radiation-warning {
        background: linear-gradient(135deg, #e67e22 0%, #d35400 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 0.8rem 0;
    }
    .space-fact-weather {
        background: linear-gradient(135deg, #34495e 0%, #2c3e50 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 0.8rem 0;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

class WeltraumWetterStation:
    def __init__(self):
        pass
    
    def get_weltraum_wetter(self):
        """Holt aktuelle Weltraum-Wetter-Bedingungen"""
        # Simuliere realistische Weltraum-Wetter-Daten
        
        # Sonnenwind-Geschwindigkeit (normalerweise 300-800 km/s)
        sonnenwind_geschwindigkeit = 350 + random.randint(0, 450)
        
        # Magnetfeld-Stärke (normalerweise 1-20 nT)
        magnetfeld_staerke = 2.5 + random.random() * 15
        
        # Protonenfluss (Teilchen/cm²/s)
        protonen_fluss = random.randint(1, 50)
        
        # Geomagnetischer Index Kp (0-9)
        kp_index = random.randint(0, 8)
        
        # Aurora-Aktivität basierend auf Kp-Index
        if kp_index < 3:
            aurora_aktivitaet = "Gering"
            aurora_farbe = "#27ae60"
        elif kp_index < 6:
            aurora_aktivitaet = "Mäßig"
            aurora_farbe = "#f39c12"
        else:
            aurora_aktivitaet = "Hoch"
            aurora_farbe = "#e74c3c"
        
        # Strahlungsrisiko
        if protonen_fluss < 10:
            strahlungsrisiko = "Normal"
            strahlung_farbe = "#27ae60"
        elif protonen_fluss < 30:
            strahlungsrisiko = "Erhöht"
            strahlung_farbe = "#f39c12"
        else:
            strahlungsrisiko = "Hoch"
            strahlung_farbe = "#e74c3c"
        
        return {
            'sonnenwind_geschwindigkeit': sonnenwind_geschwindigkeit,
            'magnetfeld_staerke': magnetfeld_staerke,
            'protonen_fluss': protonen_fluss,
            'kp_index': kp_index,
            'aurora_aktivitaet': aurora_aktivitaet,
            'aurora_farbe': aurora_farbe,
            'strahlungsrisiko': strahlungsrisiko,
            'strahlung_farbe': strahlung_farbe
        }
    
    def get_sonnen_eruptionen(self):
        """Holt aktuelle Sonnen-Eruptionen"""
        eruptionen = []
        
        # Simuliere 3-5 kürzliche Eruptionen
        for i in range(random.randint(3, 5)):
            klasse = random.choice(['A', 'B', 'C', 'M', 'X'])
            staerke = random.randint(1, 9)
            zeit = datetime.now() - timedelta(hours=random.randint(1, 72))
            
            eruptionen.append({
                'klasse': f"{klasse}{staerke}",
                'zeit': zeit,
                'quelle': f"AR{3000 + random.randint(100, 999)}",
                'auswirkung': self._get_eruption_auswirkung(klasse)
            })
        
        return sorted(eruptionen, key=lambda x: x['zeit'], reverse=True)
    
    def _get_eruption_auswirkung(self, klasse):
        """Bestimmt Auswirkung der Sonnen-Eruption"""
        auswirkungen = {
            'A': 'Keine Auswirkungen',
            'B': 'Keine Auswirkungen',
            'C': 'Minimale Funkstörungen',
            'M': 'Mäßige Funkstörungen, schwache Strahlungsstürme',
            'X': 'Starke Funkstörungen, Strahlungsstürme'
        }
        return auswirkungen.get(klasse, 'Unbekannt')
    
    def get_magnetfeld_prognose(self):
        """Erstellt 7-Tage Magnetfeld-Prognose"""
        prognose = []
        
        for i in range(7):
            datum = datetime.now() + timedelta(days=i)
            kp_wert = max(0, min(9, 3 + random.randint(-2, 5)))
            
            if kp_wert < 3:
                bedingung = "Ruhig"
                farbe = "#27ae60"
            elif kp_wert < 5:
                bedingung = "Unruhig"
                farbe = "#f39c12"
            elif kp_wert < 7:
                bedingung = "Sturm"
                farbe = "#e67e22"
            else:
                bedingung = "Schwerer Sturm"
                farbe = "#e74c3c"
            
            prognose.append({
                'datum': datum,
                'kp_index': kp_wert,
                'bedingung': bedingung,
                'farbe': farbe
            })
        
        return prognose
    
    def get_aurora_wahrscheinlichkeit(self):
        """Berechnet Aurora-Wahrscheinlichkeit für verschiedene Städte"""
        staedte = {
            'Hamburg': {'breitengrad': 53.5, 'grundwahrscheinlichkeit': 5},
            'Berlin': {'breitengrad': 52.5, 'grundwahrscheinlichkeit': 3},
            'München': {'breitengrad': 48.1, 'grundwahrscheinlichkeit': 1},
            'Tromsø': {'breitengrad': 69.6, 'grundwahrscheinlichkeit': 80},
            'Reykjavik': {'breitengrad': 64.1, 'grundwahrscheinlichkeit': 60},
            'Oslo': {'breitengrad': 59.9, 'grundwahrscheinlichkeit': 30}
        }
        
        weltraum_wetter = self.get_weltraum_wetter()
        kp_bonus = weltraum_wetter['kp_index'] * 10
        
        for stadt in staedte:
            base_chance = staedte[stadt]['grundwahrscheinlichkeit']
            final_chance = min(95, base_chance + kp_bonus)
            staedte[stadt]['wahrscheinlichkeit'] = final_chance
        
        return staedte
    
    def get_weltraum_fakten(self):
        """Interessante Weltraum-Wetter-Fakten"""
        fakten = [
            "☀️ Die Sonne schleudert ständig Millionen Tonnen Plasma ins All",
            "🌍 Das Erdmagnetfeld schützt uns vor tödlicher Sonnenstrahlung",
            "🌌 Sonnenstürme können Satelliten und GPS-Systeme stören",
            "⚡ Polarlichter entstehen durch Sonnenpartikel in der Atmosphäre",
            "📡 Starke Sonnenstürme können Stromnetze zum Zusammenbruch bringen",
            "🛰️ Astronauten sind während Sonnenstürmen erhöhter Strahlung ausgesetzt",
            "🌞 Der 11-jährige Sonnenzyklus beeinflusst die Weltraum-Wetter-Aktivität",
            "💫 Die schnellsten Sonnenwinde erreichen 2.000 km/s",
            "🔥 Sonnen-Eruptionen können Temperaturen von 100 Millionen Grad erreichen",
            "🌐 Das Erdmagnetfeld reicht bis zu 65.000 km ins All"
        ]
        return random.sample(fakten, 3)

def create_sonnenwind_chart(weltraum_wetter):
    """Erstellt Sonnenwind-Verlauf-Chart"""
    # Simuliere 24-Stunden Sonnenwind-Daten
    stunden = []
    geschwindigkeiten = []
    
    base_speed = weltraum_wetter['sonnenwind_geschwindigkeit']
    
    for i in range(24):
        zeit = datetime.now() - timedelta(hours=23-i)
        variation = random.randint(-100, 100)
        geschwindigkeit = max(250, base_speed + variation)
        
        stunden.append(zeit.strftime('%H:%M'))
        geschwindigkeiten.append(geschwindigkeit)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=stunden,
        y=geschwindigkeiten,
        mode='lines+markers',
        name='Sonnenwind-Geschwindigkeit',
        line=dict(color='#f39c12', width=3),
        marker=dict(size=6),
        fill='tonexty',
        fillcolor='rgba(243, 156, 18, 0.2)'
    ))
    
    # Durchschnittslinie
    avg_speed = sum(geschwindigkeiten) / len(geschwindigkeiten)
    fig.add_hline(y=avg_speed, line_dash="dash", line_color="red", 
                  annotation_text=f"Durchschnitt: {avg_speed:.0f} km/s")
    
    fig.update_layout(
        title='🌬️ Sonnenwind-Geschwindigkeit (Letzte 24 Stunden)',
        xaxis_title='Uhrzeit (UTC)',
        yaxis_title='Geschwindigkeit (km/s)',
        template='plotly_white',
        height=400
    )
    
    return fig

def create_kp_index_chart(prognose):
    """Erstellt Kp-Index Prognose-Chart"""
    dates = [p['datum'].strftime('%d.%m') for p in prognose]
    kp_values = [p['kp_index'] for p in prognose]
    colors = [p['farbe'] for p in prognose]
    conditions = [p['bedingung'] for p in prognose]
    
    fig = go.Figure(data=go.Bar(
        x=dates,
        y=kp_values,
        marker_color=colors,
        text=conditions,
        textposition='auto',
        hovertemplate='<b>%{x}</b><br>Kp-Index: %{y}<br>Bedingung: %{text}<extra></extra>'
    ))
    
    fig.update_layout(
        title='📊 Geomagnetischer Kp-Index Prognose',
        xaxis_title='Datum',
        yaxis_title='Kp-Index (0-9)',
        template='plotly_white',
        height=400,
        yaxis=dict(range=[0, 9])
    )
    
    return fig

def main():
    # Header
    st.markdown('<h1 class="weather-header">🌞 WELTRAUM-WETTER STATION</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="page-intro">
        <strong>☀️ Solare Aktivität & Erdmagnetfeld-Überwachung</strong><br><br>
        Verfolgen Sie die Aktivität unserer Sonne und deren Auswirkungen auf die Erde. 
        Von Sonnenstürmen bis zu Polarlichtern - das Weltraum-Wetter beeinflusst unser tägliches Leben 
        mehr als Sie denken! 🌌
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize Station
    station = WeltraumWetterStation()
    
    # Sidebar auf Deutsch
    st.sidebar.markdown("## 🎛️ Weltraum-Wetter Kontrolle")
    
    auto_refresh = st.sidebar.checkbox("🔄 Auto-Aktualisierung (3 Min)", value=False)
    if auto_refresh:
        time.sleep(180)
        st.rerun()
    
    if st.sidebar.button("🌞 Daten Aktualisieren", type="primary"):
        st.rerun()
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### ☀️ Sonne Schnell-Fakten")
    st.sidebar.markdown("""
    - **Oberflächentemperatur:** 5.500°C
    - **Kerntemperatur:** 15 Millionen °C
    - **Masse:** 333.000x Erdmasse
    - **Durchmesser:** 1,4 Millionen km
    - **Sonnenzyklus:** 11 Jahre
    - **Sonnenwind:** 400-800 km/s
    - **Magnetfeld:** 10.000x stärker als Erde
    - **Alter:** 4,6 Milliarden Jahre
    """)
    
    # Daten laden
    with st.spinner("☀️ Verbinde mit Sonnen-Observatorien..."):
        weltraum_wetter = station.get_weltraum_wetter()
        eruptionen = station.get_sonnen_eruptionen()
        magnetfeld_prognose = station.get_magnetfeld_prognose()
        aurora_wahrscheinlichkeit = station.get_aurora_wahrscheinlichkeit()
        weltraum_fakten = station.get_weltraum_fakten()
        
        # Aktuelle Bedingungen
        st.markdown("### ⚡ Aktuelle Weltraum-Wetter-Bedingungen")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="solar-metric">
                <h3>🌬️ Sonnenwind</h3>
                <h2>{weltraum_wetter['sonnenwind_geschwindigkeit']}</h2>
                <p>km/s</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="solar-metric">
                <h3>🧲 Magnetfeld</h3>
                <h2>{weltraum_wetter['magnetfeld_staerke']:.1f}</h2>
                <p>nT</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="solar-metric" style="background: linear-gradient(135deg, {weltraum_wetter['aurora_farbe']} 0%, {weltraum_wetter['aurora_farbe']}aa 100%);">
                <h3>🌌 Aurora</h3>
                <h2>{weltraum_wetter['aurora_aktivitaet']}</h2>
                <p>Kp: {weltraum_wetter['kp_index']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="solar-metric" style="background: linear-gradient(135deg, {weltraum_wetter['strahlung_farbe']} 0%, {weltraum_wetter['strahlung_farbe']}aa 100%);">
                <h3>☢️ Strahlung</h3>
                <h2>{weltraum_wetter['strahlungsrisiko']}</h2>
                <p>{weltraum_wetter['protonen_fluss']} p/cm²/s</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Sonnenwind-Chart
        st.markdown("---")
        st.markdown("### 🌬️ Sonnenwind-Aktivität")
        
        sonnenwind_chart = create_sonnenwind_chart(weltraum_wetter)
        st.plotly_chart(sonnenwind_chart, use_container_width=True)
        
        # Magnetfeld-Prognose
        st.markdown("---")
        st.markdown("### 📊 Geomagnetische Aktivitäts-Prognose")
        
        col_chart, col_info = st.columns([2, 1])
        
        with col_chart:
            kp_chart = create_kp_index_chart(magnetfeld_prognose)
            st.plotly_chart(kp_chart, use_container_width=True)
        
        with col_info:
            st.markdown(f"""
            <div class="magnetic-info">
                <h3>🧲 Magnetfeld-Info</h3>
                <p><strong>Kp-Index Bedeutung:</strong></p>
                <p>🟢 0-2: Ruhig</p>
                <p>🟡 3-4: Unruhig</p>
                <p>🟠 5-6: Sturm</p>
                <p>🔴 7+: Schwerer Sturm</p>
                <br>
                <p><strong>Auswirkungen:</strong></p>
                <p>• Funkstörungen</p>
                <p>• GPS-Ungenauigkeiten</p>
                <p>• Polarlichter</p>
                <p>• Satelliten-Störungen</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Sonnen-Eruptionen
        st.markdown("---")
        st.markdown("### ☀️ Kürzliche Sonnen-Eruptionen")
        
        if eruptionen:
            for eruption in eruptionen[:5]:
                zeit_seit = datetime.now() - eruption['zeit']
                stunden_seit = int(zeit_seit.total_seconds() / 3600)
                
                klasse_farbe = {
                    'A': '#27ae60', 'B': '#27ae60', 'C': '#f39c12', 
                    'M': '#e67e22', 'X': '#e74c3c'
                }.get(eruption['klasse'][0], '#34495e')
                
                st.markdown(f"""
                <div class="flare-alert" style="background: linear-gradient(135deg, {klasse_farbe} 0%, {klasse_farbe}aa 100%);">
                    ☀️ Klasse {eruption['klasse']} Eruption | vor {stunden_seit}h | Quelle: {eruption['quelle']}<br>
                    💥 Auswirkung: {eruption['auswirkung']}
                </div>
                """, unsafe_allow_html=True)
        
        # Aurora-Wahrscheinlichkeiten
        st.markdown("---")
        st.markdown("### 🌌 Polarlicht-Wahrscheinlichkeiten")
        
        aurora_cols = st.columns(3)
        
        for i, (stadt, daten) in enumerate(aurora_wahrscheinlichkeit.items()):
            col = aurora_cols[i % 3]
            
            if daten['wahrscheinlichkeit'] < 20:
                farbe = "#95a5a6"
            elif daten['wahrscheinlichkeit'] < 50:
                farbe = "#f39c12"
            else:
                farbe = "#27ae60"
            
            col.markdown(f"""
            <div class="aurora-card" style="background: linear-gradient(135deg, {farbe} 0%, {farbe}aa 100%);">
                <h4>📍 {stadt}</h4>
                <h2>{daten['wahrscheinlichkeit']}%</h2>
                <p>Polarlicht-Chance</p>
                <p><small>Breitengrad: {daten['breitengrad']}°N</small></p>
            </div>
            """, unsafe_allow_html=True)
        
        # Strahlungs-Warnung
        if weltraum_wetter['strahlungsrisiko'] != "Normal":
            st.markdown("---")
            st.markdown("### ⚠️ Strahlungs-Warnung")
            
            st.markdown(f"""
            <div class="radiation-warning">
                <h4>☢️ Erhöhte Strahlungswerte Detected</h4>
                <p><strong>Risiko-Level:</strong> {weltraum_wetter['strahlungsrisiko']}</p>
                <p><strong>Protonen-Fluss:</strong> {weltraum_wetter['protonen_fluss']} Teilchen/cm²/s</p>
                <p><strong>Betroffene Bereiche:</strong> Luftfahrt, Satelliten, Polarregionen</p>
                <p><strong>Empfehlung:</strong> Erhöhte Vorsicht bei Polar-Flügen</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Weltraum-Fakten
        st.markdown("---")
        st.markdown("### 🌟 Weltraum-Wetter Fakten des Tages")
        
        for fakt in weltraum_fakten:
            st.markdown(f"""
            <div class="space-fact-weather">
                {fakt}
            </div>
            """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #7f8c8d; padding: 2rem 0;'>
        🌞 <strong>Weltraum-Wetter Station</strong> 🌞<br>
        ☀️ Überwachung der solaren Aktivität und deren Auswirkungen auf die Erde<br>
        🌌 Ihr Fenster zu den kosmischen Kräften, die unser Leben beeinflussen
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
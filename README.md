# 🌌 Cosmic Analytics Command Center

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Demo-orange.svg)](https://timmiflimmi-cosmic-analytics-dashboard.streamlit.app)

> **Ein professionelles Multi-Page Space Analytics Dashboard mit Real-Time Daten von NASA, SpaceX und anderen Weltraumagenturen**

## 🎯 **Projektübersicht**

Das **Cosmic Analytics Command Center** ist ein vollständiges Space Mission Control Dashboard, das Live-Daten aus dem Weltraum in einer benutzerfreundlichen, interaktiven Oberfläche präsentiert. Das Dashboard umfasst 8 spezialisierte Module für verschiedene Aspekte der Weltraumforschung und -beobachtung.

### 🌟 **Key Features**
- **🔴 Real-Time Space Data** - Live APIs von NASA, SpaceX, Open Notify
- **🗺️ Interactive Maps** - ISS Tracking, Satelliten-Konstellationen
- **📊 Advanced Analytics** - 30+ interaktive Plotly Visualisierungen
- **🌍 Location-Based** - Hamburg-spezifische ISS-Überflüge und Stargazing
- **📱 Responsive Design** - Optimiert für Desktop, Tablet und Mobile
- **🔄 Auto-Refresh** - Live-Updates alle 30-60 Sekunden

## ⚠️ **WICHTIGER HINWEIS - DEMO VERSION**

### **API-Key Limitierungen**
Diese App läuft im **Demo-Modus** mit begrenzten API-Keys:
- **NASA APIs**: `DEMO_KEY` (max. 30 Requests/Stunde)
- **SpaceX API**: Öffentlich verfügbar (keine Limits)
- **Open Notify**: Öffentlich verfügbar (keine Limits)

### **Für Produktionsnutzung**
Für vollständige Funktionalität:
1. **NASA API Key beantragen** (kostenlos): [api.nasa.gov](https://api.nasa.gov/)
2. **Key in Code ersetzen**: `nasa_api_key = "DEMO_KEY"` → `nasa_api_key = "YOUR_KEY"`
3. **Umgebungsvariable setzen**: `export NASA_API_KEY="your-key"`

---

## 🚀 **Module & Features**

### 🏠 **Home Dashboard**
- **Live Status Cards** - ISS Position, Astronauten-Count, Launch-Status
- **Quick Navigation** - Übersicht aller 8 Module
- **Space Fact of the Day** - Täglich wechselnde Weltraum-Fakten
- **System Health Monitor** - API-Status aller Datenquellen

### 🛰️ **ISS Mission Control**
- **Real-Time Tracking** - Live ISS Position mit interaktiver Weltkarte
- **Current Crew** - Astronauten aktuell auf ISS & Tiangong
- **Hamburg Pass Times** - ISS-Überflüge mit präzisen Zeiten
- **Orbital Data** - Geschwindigkeit, Höhe, Orbit-Informationen
- **3D Orbit Visualization** - ISS-Bahn um die Erde

### 🚀 **Rocket Launch Center**
- **Live Countdown** - T-minus Timer für nächste SpaceX Mission
- **Launch Analytics** - Success Rate, Statistiken, Performance
- **Interactive Timeline** - Plotly Visualization kommender Starts
- **Mission Details** - Raketen-Specs, Payload, Landing-Attempts
- **Recent History** - Vergangene Launches mit Success/Failure Status

### 🔴 **Mars Exploration Hub**
- **Mars Rover Photos** - Live Bilder von Perseverance & Curiosity
- **Mars Weather Station** - Temperatur, Wind, Druck, Jahreszeit
- **Temperature Charts** - 7-Sol Mars Wetter Verlauf
- **Mission Timeline** - Geschichte der Mars-Exploration
- **Future Missions** - Sample Return & Human Mars Plans

### 🌙 **Lunar & Planetary**
- **Moon Phase Tracker** - Aktuelle Mondphase mit Beleuchtungsgrad
- **4-Week Calendar** - Mondphasen-Vorschau
- **Solar System Live** - Interaktive Planetenpositionen
- **Planet Visibility** - Welche Planeten heute in Hamburg sichtbar
- **Eclipse Predictions** - Kommende Mond- und Sonnenfinsternisse
- **Stargazing Guide** - Hamburg-spezifische Beobachtungstipps

### 🌞 **Space Weather Station**
- **Solar Activity** - Solar Wind Speed, Magnetfeld-Stärke
- **Aurora Forecast** - Nordlicht-Vorhersage für Hamburg
- **Solar Flare Alerts** - Aktuelle Sonnen-Sturm Warnungen
- **Radiation Levels** - Weltraum-Umgebung Sicherheitsdaten
- **Interactive Charts** - 7-Tage Solar Activity Timeline

### 🛰️ **Satellite Networks**
- **Starlink Coverage** - Live Starlink-Satelliten Weltkarte
- **GPS Constellation** - Globale GPS-Satelliten Status
- **Hamburg Passes** - Satelliten-Überflüge mit Zeiten
- **Network Performance** - Speed, Latency, Coverage Stats
- **Constellation Comparison** - Starlink vs. OneWeb vs. GPS

### 🌌 **Deep Space Observatory**
- **NASA Picture of the Day** - Täglich neue Weltraum-Aufnahmen
- **Hubble Discoveries** - Neueste Entdeckungen
- **James Webb Updates** - Deep Field Beobachtungen
- **Voyager Mission Status** - Live-Position beider Sonden im interstellaren Raum
- **Asteroid Tracker** - Near-Earth Objects mit Hazard Assessment
- **Distance Visualization** - Kosmische Entfernungen auf Log-Skala

---

## 🛠️ **Installation & Setup**

### **Voraussetzungen**
```bash
Python 3.8+
Git
```

### **1. Repository klonen**
```bash
git clone https://github.com/timmiflimmi/cosmic-analytics-dashboard.git
cd cosmic-analytics-dashboard
```

### **2. Virtual Environment erstellen**
```bash
python -m venv cosmic_env
source cosmic_env/bin/activate  # Linux/Mac
# oder
cosmic_env\Scripts\activate     # Windows
```

### **3. Dependencies installieren**
```bash
pip install -r requirements.txt
```

### **4. Environment Setup**
```bash
# Kopiere .env Template und füge API Keys hinzu
cp .env.example .env
# Bearbeite .env mit deinen NASA API Keys
```

### **5. App starten**
```bash
streamlit run streamlit_app.py
```

### **6. Browser öffnen**
```
http://localhost:8501
```

---

## 📦 **Abhängigkeiten**

```txt
streamlit>=1.28.0
requests>=2.31.0
plotly>=5.15.0
folium>=0.14.0
streamlit-folium>=0.13.0
pandas>=2.0.0
numpy>=1.24.0
python-dateutil>=2.8.2
```

---

## 🗂️ **Projektstruktur**

```
cosmic-analytics-dashboard/
├── streamlit_app.py              # Main Landing Page
├── pages/                       # Multi-Page App Structure
│   ├── 1_🛰️_ISS_Control.py      # ISS Mission Control
│   ├── 2_🚀_Launch_Center.py     # Rocket Launch Center
│   ├── 3_🔴_Mars_Hub.py          # Mars Exploration Hub
│   ├── 4_🌙_Lunar_Planetary.py   # Lunar & Planetary
│   ├── 5_🌞_Space_Weather.py     # Space Weather Station
│   ├── 6_🛰️_Satellite_Networks.py # Satellite Networks
│   └── 7_🌌_Deep_Space.py        # Deep Space Observatory
├── .streamlit/                  # Streamlit Configuration
│   ├── config.toml              # App Settings
│   └── secrets.toml             # API Keys (ignored by git)
├── src/                         # Source Code & Modules
├── utils/                       # Utility Functions
│   ├── __init__.py              # Package Initialization
│   ├── space_apis.py            # API Integration Classes
│   └── visualizations.py       # Chart & Map Functions
├── data/                        # Data Storage & Cache
│   ├── cache/                   # API Response Cache
│   └── temp/                    # Temporary Files
├── logs/                        # Application Logs
├── screenshots/                 # App Screenshots
├── requirements.txt             # Python Dependencies
├── README.md                   # Project Documentation
├── .gitignore                  # Git Ignore Rules
├── .env.example                # Environment Variables Template
└── LICENSE                     # MIT License
```

---

## 🔌 **APIs & Datenquellen**

| Service | Endpoint | Daten | Status |
|---------|----------|-------|--------|
| **Open Notify** | `api.open-notify.org` | ISS Position, Astronauten, Pass Times | ✅ Unlimited |
| **SpaceX API** | `api.spacexdata.com` | Launches, Rockets, Missionen | ✅ Unlimited |
| **NASA APOD** | `api.nasa.gov/planetary/apod` | Astronomy Picture of the Day | ⚠️ Demo (30/h) |
| **NASA Mars** | `api.nasa.gov/mars-photos` | Mars Rover Photos | ⚠️ Demo (30/h) |
| **NASA NEO** | `api.nasa.gov/neo` | Near Earth Objects | ⚠️ Demo (30/h) |

### **Intelligente Fallbacks**
- Alle APIs haben robuste Fallback-Systeme
- Simulierte Daten bei API-Ausfällen
- Automatische Error-Recovery
- Graceful Degradation bei Netzwerkproblemen

---

## 🌍 **Live Demo**

**🔗 [Cosmic Analytics Dashboard - Demo](https://timmiflimmi-cosmic-analytics-dashboard.streamlit.app)**

> ⚠️ **Demo-Version** mit NASA DEMO_KEY - Begrenzte Requests/Stunde

### **Demo-Zugang**
```
Keine Credentials erforderlich - Öffentliche Demo
Hinweis: Begrenzte API-Requests durch DEMO_KEY
```

---

## 🚀 **Deployment**

### **Streamlit Cloud (Empfohlen)**
1. Repository auf GitHub pushen
2. [share.streamlit.io](https://share.streamlit.io) besuchen
3. Repository verknüpfen: `timmiflimmi/cosmic-analytics-dashboard`
4. Main File: `streamlit_app.py`
5. Deploy! 🚀

### **Heroku**
```bash
# Procfile erstellen
echo "web: sh setup.sh && streamlit run streamlit_app.py" > Procfile

# setup.sh erstellen
mkdir -p ~/.streamlit/
echo "[server]" > ~/.streamlit/config.toml
echo "port = $PORT" >> ~/.streamlit/config.toml
echo "enableCORS = false" >> ~/.streamlit/config.toml
echo "headless = true" >> ~/.streamlit/config.toml

# Heroku Deploy
heroku create cosmic-analytics-dashboard
git push heroku main
```

### **Docker**
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py"]
```

---

## 🛡️ **API Keys & Limitierungen**

### **Aktuelle Demo-Konfiguration**
```python
# NASA APIs - Demo Key (limitiert)
nasa_api_key = "DEMO_KEY"  # 30 Requests/Stunde
```

### **Production API Keys einrichten**

#### **Option 1: Environment Variables (.env)**
```bash
# .env Datei erstellen
NASA_API_KEY=your_real_api_key_here
HAMBURG_LAT=53.5511
HAMBURG_LON=9.9937
```

#### **Option 2: Streamlit Secrets**
```toml
# .streamlit/secrets.toml
[api_keys]
nasa = "your_real_api_key_here"

[location]
hamburg_lat = 53.5511
hamburg_lon = 9.9937
```

#### **Option 3: Code Integration**
```python
import streamlit as st
import os

# NASA API Key laden
nasa_key = st.secrets.get("api_keys", {}).get("nasa", 
           os.getenv("NASA_API_KEY", "DEMO_KEY"))
```

### **API Rate Limits**
| Service | Demo Limit | Production Limit |
|---------|------------|------------------|
| NASA APOD | 30/Stunde | 1000/Stunde |
| NASA Mars Photos | 30/Stunde | 1000/Stunde |
| NASA NEO | 30/Stunde | 1000/Stunde |
| SpaceX API | Unlimited | Unlimited |
| Open Notify | Unlimited | Unlimited |

### **Rate Limiting Handling**
- Intelligente Request-Spacing
- Caching für häufige Abfragen
- Error-Handling für API-Limits
- Automatic Fallback zu simulierten Daten

---

## 🔧 **Konfiguration**

### **Hamburg-spezifische Einstellungen**
```python
# Koordinaten für ISS-Pässe und Stargazing
HAMBURG_LAT = 53.5511
HAMBURG_LON = 9.9937
TIMEZONE = "Europe/Berlin"
```

### **Custom Styling**
```python
# CSS-Anpassungen in jeder Page
st.markdown("""
<style>
    .main-header { 
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
    }
    .metric-card { 
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
    }
</style>
""", unsafe_allow_html=True)
```

---

## 📈 **Performance & Optimierung**

### **Caching Strategy**
- `@st.cache_data` für API-Responses
- Session State für User-Interaktionen
- Lazy Loading für große Datasets

### **Performance Metrics**
- ⚡ Load Time: < 3 Sekunden
- 📱 Mobile Responsive: 100%
- 🔄 API Response: < 2 Sekunden
- 📊 Chart Rendering: < 1 Sekunde

---

## 🤝 **Contributing**

Beiträge sind willkommen! Hier ist wie:

### **1. Fork & Clone**
```bash
git clone https://github.com/timmiflimmi/cosmic-analytics-dashboard.git
```

### **2. Feature Branch erstellen**
```bash
git checkout -b feature/neue-weltraum-feature
```

### **3. Changes commiten**
```bash
git commit -m "✨ Add neue Weltraum-Feature"
```

### **4. Pull Request erstellen**
- Detaillierte Beschreibung der Changes
- Screenshots bei UI-Änderungen
- Tests für neue Features

### **Coding Standards**
- Python PEP 8 Style Guide
- Docstrings für alle Funktionen
- Type Hints wo möglich
- Error Handling für alle API-Calls

---

## 🐛 **Known Issues & Roadmap**

### **Known Issues**
- [ ] ISS Map rendering langsam bei schwacher Internetverbindung
- [ ] NASA API Rate Limiting bei Demo-Key
- [ ] Mobile Responsiveness bei komplexen Charts

### **Roadmap 2025**
- [ ] **Real-Time Notifications** - Push-Benachrichtigungen für ISS-Überflüge
- [ ] **User Accounts** - Personalisierte Space-Favoriten
- [ ] **AR Integration** - Augmented Reality für Sternenhimmel
- [ ] **Voice Commands** - "Alexa, wo ist die ISS?"
- [ ] **Machine Learning** - Space Weather Predictions
- [ ] **Social Features** - Community Space Observations
- [ ] **NASA Production API** - Vollständige API-Integration

---

## 📄 **License**

Dieses Projekt ist unter der MIT License lizenziert - siehe [LICENSE](LICENSE) für Details.

```
MIT License

Copyright (c) 2025 Timmi Flimmi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 **Acknowledgments**

### **APIs & Services**
- **NASA** - Open Data Initiative
- **SpaceX** - Public API Access
- **Open Notify** - ISS Tracking Services
- **Streamlit** - Amazing Python Web Framework

### **Inspiration**
- **NASA Mission Control** - Design Inspiration
- **SpaceX Live Streams** - Real-Time Data Presentation
- **ESA Ground Control** - Professional Space Interfaces

### **Special Thanks**
- **Streamlit Community** - Für Support und Feedback
- **Python Space Community** - Open Source Tools
- **Hamburg Astronomy Club** - Lokale Stargazing-Tipps

---

## 📞 **Contact & Support**

### **Entwickler**
- **GitHub**: [@timmiflimmi](https://github.com/timmiflimmi)

### **Issues & Feature Requests**
- **GitHub Issues**: [Create Issue](https://github.com/timmiflimmi/cosmic-analytics-dashboard/issues)
- **Discussions**: [GitHub Discussions](https://github.com/timmiflimmi/cosmic-analytics-dashboard/discussions)

### **Professional Portfolio**
Dieses Projekt ist Teil meines **Data Science Portfolios** und demonstriert:
- **Real-Time Data Processing**
- **Interactive Visualization** mit Plotly
- **API Integration & Error Handling**
- **Professional Web App Development**
- **Space Domain Expertise**

---

## 🌟 **Star History**

[![Star History Chart](https://api.star-history.com/svg?repos=timmiflimmi/cosmic-analytics-dashboard&type=Date)](https://star-history.com/#timmiflimmi/cosmic-analytics-dashboard&Date)

---

<div align="center">

**🌌 Made with ❤️ for Space Enthusiasts**

**🚀 "That's one small step for code, one giant leap for space analytics"**

[![Follow on GitHub](https://img.shields.io/github/followers/timmiflimmi?style=social)](https://github.com/timmiflimmi)
[![Stars](https://img.shields.io/github/stars/timmiflimmi/cosmic-analytics-dashboard?style=social)](https://github.com/timmiflimmi/cosmic-analytics-dashboard)

</div>
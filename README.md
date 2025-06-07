# 🌌 Cosmic Analytics Command Center

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![NASA API](https://img.shields.io/badge/NASA_API-Integrated-orange.svg)](https://api.nasa.gov/)
[![Status](https://img.shields.io/badge/Status-Production_Ready-brightgreen.svg)](https://timmiflimmi-cosmic-analytics-dashboard.streamlit.app)

> **Ein professionelles Multi-Page Space Analytics Dashboard mit Real-Time NASA, SpaceX und anderen Weltraumagenturen APIs**

## 🎯 **Projektübersicht**

Das **Cosmic Analytics Command Center** ist ein vollständiges Space Mission Control Dashboard, das Live-Daten aus dem Weltraum in einer benutzerfreundlichen, interaktiven Oberfläche präsentiert. Das Dashboard umfasst 8 spezialisierte Module für verschiedene Aspekte der Weltraumforschung und -beobachtung mit echten NASA APIs.

### 🌟 **Key Features**
- **🔑 Real NASA API Integration** - 1000 requests/hour mit eigenem API Key
- **🗺️ Interactive Maps** - ISS Live Tracking, Satelliten-Konstellationen
- **📊 Advanced Analytics** - 30+ interaktive Plotly Visualisierungen
- **🌍 Hamburg-Focused** - Lokale ISS-Überflüge und Stargazing-Empfehlungen
- **📱 Responsive Design** - Optimiert für Desktop, Tablet und Mobile
- **🔄 Auto-Refresh** - Live-Updates alle 30-60 Sekunden
- **🛡️ Production Ready** - Robuste Fallbacks und Error Handling

## 🔑 **NASA API Integration**

### **Einheitliches API-System**
Dieses Dashboard nutzt **einen NASA API Key** für alle Services:
- 🌟 **Astronomy Picture of the Day** (APOD)
- 🔴 **Mars Rover Photos** (Perseverance & Curiosity)
- ☄️ **Near Earth Objects** (NEO)
- 🌡️ **Mars Weather Data** (falls verfügbar)

**Vorteile gegenüber DEMO_KEY:**
- ✅ **1000 Requests/Stunde** vs. 30 mit DEMO_KEY
- ✅ **Höhere Zuverlässigkeit** und weniger Rate Limiting
- ✅ **Vollständige Feature-Nutzung** aller NASA Services

---

## 🚀 **Module & Features**

### 🏠 **Home Dashboard**
- **Live Status Cards** - ISS Position, Astronauten-Count, Launch-Status
- **Quick Navigation** - Übersicht aller 8 Module
- **NASA Picture Preview** - Aktuelles Astronomy Picture of the Day
- **System Health Monitor** - API-Status aller Datenquellen

### 🛰️ **ISS Mission Control**
- **Real-Time Tracking** - Live ISS Position mit interaktiver Weltkarte
- **Current Crew** - Astronauten aktuell auf ISS & Tiangong
- **Hamburg Pass Times** - ISS-Überflüge mit präzisen Zeiten & Countdown
- **Orbital Data** - Geschwindigkeit, Höhe, Orbit-Informationen
- **Interactive Map** - Zoom, Pan, ISS-Sichtbarkeitskreis

### 🚀 **Rocket Launch Center**
- **Live Countdown** - T-minus Timer für nächste SpaceX Mission
- **Launch Analytics** - Success Rate, Statistiken, Performance Trends
- **Interactive Timeline** - Plotly Visualization kommender Starts
- **Mission Details** - Raketen-Specs, Payload, Landing-Attempts
- **Recent History** - Vergangene Launches mit Success/Failure Status

### 🔴 **Mars Exploration Hub**
- **Real Mars Rover Photos** - Live Bilder von Perseverance & Curiosity APIs
- **Smart Photo Loading** - Multiple Sol-Versuche für beste Verfügbarkeit
- **Mars Weather Station** - Temperatur, Wind, Druck, Jahreszeiten-Simulation
- **Temperature Charts** - 7-Sol Mars Wetter Verlaufs-Visualisierung
- **Mission Timeline** - Geschichte der Mars-Exploration von Viking bis heute
- **Future Missions** - Sample Return & Human Mars Mission Plans

### 🌙 **Lunar & Planetary**
- **Moon Phase Tracker** - Aktuelle Mondphase mit Beleuchtungsgrad
- **4-Week Calendar** - Mondphasen-Vorschau mit interaktiven Charts
- **Solar System Live** - Interaktive Planetenpositionen
- **Planet Visibility** - Welche Planeten heute in Hamburg sichtbar sind
- **Eclipse Predictions** - Kommende Mond- und Sonnenfinsternisse
- **Hamburg Stargazing** - Lokale Beobachtungstipps & optimale Zeiten

### 🌞 **Space Weather Station**
- **Solar Activity** - Solar Wind Speed, Magnetfeld-Stärke Simulation
- **Aurora Forecast** - Nordlicht-Vorhersage für Hamburg-Region
- **Solar Flare Alerts** - Aktuelle Sonnen-Sturm Warnungen
- **Radiation Levels** - Weltraum-Umgebung Sicherheitsdaten
- **Interactive Charts** - 7-Tage Solar Activity Timeline

### 🛰️ **Satellite Networks**
- **Starlink Coverage** - Live Starlink-Satelliten Weltkarte
- **GPS Constellation** - Globale GPS-Satelliten Status
- **Hamburg Passes** - Satelliten-Überflüge mit präzisen Zeiten
- **Network Performance** - Speed, Latency, Coverage Statistics
- **Constellation Comparison** - Starlink vs. OneWeb vs. GPS Analytics

### 🌌 **Deep Space Observatory**
- **NASA Picture of the Day** - Täglich neue Weltraum-Aufnahmen via NASA API
- **Hubble Discoveries** - Neueste simulierte Entdeckungen
- **James Webb Updates** - Deep Field Beobachtungen & Early Universe
- **Voyager Mission Status** - Live-Position beider Sonden im interstellaren Raum
- **Real Asteroid Tracker** - Live Near-Earth Objects via NASA NEO API
- **Distance Visualization** - Kosmische Entfernungen auf logarithmischer Skala

---

## 🛠️ **Installation & Setup**

### **Voraussetzungen**
```bash
Python 3.8+
Git
NASA API Key (kostenlos von api.nasa.gov)
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

### **4. NASA API Key Setup** ⚠️ **WICHTIG**
```bash
# 1. NASA API Key beantragen (kostenlos):
# Gehe zu: https://api.nasa.gov/
# Registriere dich und kopiere deinen API Key

# 2. .env Datei erstellen:
cp .env.example .env

# 3. .env bearbeiten und deinen NASA API Key eintragen:
NASA_API_KEY=your_real_nasa_api_key_here
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
python-dotenv>=1.0.0
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
│   ├── secrets.toml.example     # API Keys Template
│   └── .gitkeep                # Directory Structure
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
├── .gitignore                  # Git Ignore Rules (API Key Protection)
├── .env.example                # Environment Variables Template
└── LICENSE                     # MIT License
```

---

## 🔌 **APIs & Datenquellen**

| Service | Endpoint | Daten | API Key | Rate Limit |
|---------|----------|-------|---------|------------|
| **NASA APOD** | `api.nasa.gov/planetary/apod` | Astronomy Picture of the Day | ✅ Required | 1000/hour |
| **NASA Mars** | `api.nasa.gov/mars-photos` | Mars Rover Photos | ✅ Required | 1000/hour |
| **NASA NEO** | `api.nasa.gov/neo` | Near Earth Objects | ✅ Required | 1000/hour |
| **SpaceX API** | `api.spacexdata.com` | Launches, Rockets, Missionen | ❌ Public | Unlimited |
| **Open Notify** | `api.open-notify.org` | ISS Position, Astronauten | ❌ Public | Unlimited |

### **Intelligente Fallbacks**
- **NASA APIs**: Simulierte Daten bei Rate Limit oder Ausfällen
- **SpaceX API**: Fallback-Missionen mit realistischen Daten
- **Open Notify**: Hamburg-basierte Simulation bei Ausfällen
- **Graceful Degradation**: App funktioniert auch ohne Internet

---

## 🌍 **Live Demo**

**🔗 [Cosmic Analytics Dashboard - Live Demo](https://timmiflimmi-cosmic-analytics-dashboard.streamlit.app)**

> **Features der Live-Demo:**
> - Real NASA API Integration mit 1000 requests/hour
> - Alle 8 Space Module voll funktionsfähig
> - Hamburg-spezifische ISS Pass Times
> - Live Mars Rover Photos von Perseverance & Curiosity
> - Interactive Charts & Maps

---

## 🚀 **Deployment**

### **Streamlit Cloud (Empfohlen)**
1. Repository auf GitHub pushen
2. [share.streamlit.io](https://share.streamlit.io) besuchen
3. Repository verknüpfen: `timmiflimmi/cosmic-analytics-dashboard`
4. **Secrets konfigurieren:**
   ```toml
   [api_keys]
   nasa = "your_nasa_api_key_here"
   ```
5. Main File: `streamlit_app.py`
6. Deploy! 🚀

### **Lokales Deployment**
```bash
# Mit echtem NASA API Key:
echo "NASA_API_KEY=your_key_here" > .env
streamlit run streamlit_app.py

# Demo-Modus (begrenzte Funktionalität):
streamlit run streamlit_app.py  # Verwendet DEMO_KEY
```

---

## 🔑 **NASA API Setup Guide**

### **Schritt 1: NASA API Key beantragen**
1. Gehe zu: [api.nasa.gov](https://api.nasa.gov/)
2. Klicke "Generate API Key"
3. Fülle das Formular aus (kostenlos!)
4. Kopiere deinen API Key

### **Schritt 2: Lokale Konfiguration**
```bash
# .env Datei bearbeiten:
NASA_API_KEY=abc123def456ghi789jkl012mno345pqr678

# Hamburg Location (optional):
HAMBURG_LAT=53.5511
HAMBURG_LON=9.9937
```

### **Schritt 3: Streamlit Cloud Secrets**
```toml
# In Streamlit Cloud App Settings > Secrets:
[api_keys]
nasa = "abc123def456ghi789jkl012mno345pqr678"

[location]
hamburg_lat = 53.5511
hamburg_lon = 9.9937
```

### **API-Features mit echtem Key:**
- 🌟 **NASA APOD**: Täglich neue Bilder statt Fallbacks
- 🔴 **Mars Photos**: Mehr Rover-Bilder, aktuelle Sols
- ☄️ **Asteroids**: Echte Near-Earth Objects statt Simulation
- ⚡ **Performance**: 1000 statt 30 Requests/Stunde

---

## 🛡️ **Sicherheit**

### **API Key Protection**
- ✅ `.env` wird von Git ignoriert (lokale Keys sicher)
- ✅ Streamlit Secrets für Cloud-Deployment
- ✅ Fallback zu DEMO_KEY wenn Key fehlt
- ✅ Keine Hardcoded Keys im Source Code

### **Error Handling**
- 🔄 **Automatic Retry** bei temporären API-Ausfällen
- 📊 **Fallback Data** bei Rate Limiting
- 🔍 **Debug Output** für API-Monitoring
- ⚡ **Graceful Degradation** bei Netzwerkproblemen

---

## 📈 **Performance & Features**

### **Optimierungen**
- ⚡ Load Time: < 3 Sekunden
- 📱 Mobile Responsive: 100%
- 🔄 API Response Caching
- 📊 Lazy Loading für Charts

### **Hamburg-Spezifische Features**
- 🛰️ **ISS Pass Predictions** - Wann ist die ISS über Hamburg sichtbar?
- 🌌 **Aurora Forecast** - Nordlicht-Chancen für Hamburg
- 📍 **Local Coordinates** - Alle Berechnungen Hamburg-optimiert
- 🔭 **Stargazing Tips** - Beste Beobachtungsplätze & Zeiten

---

## 🤝 **Contributing**

Beiträge sind willkommen! So kannst du helfen:

### **Development Setup**
```bash
git clone https://github.com/timmiflimmi/cosmic-analytics-dashboard.git
cd cosmic-analytics-dashboard
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # NASA API Key eintragen
```

### **Feature Requests & Bug Reports**
- 🐛 **Issues**: [GitHub Issues](https://github.com/timmiflimmi/cosmic-analytics-dashboard/issues)
- 💡 **Ideas**: [GitHub Discussions](https://github.com/timmiflimmi/cosmic-analytics-dashboard/discussions)

---

## 🚀 **Roadmap 2025**

### **Geplante Features**
- [ ] **Real-Time Notifications** - Push-Benachrichtigungen für ISS-Überflüge
- [ ] **User Accounts** - Personalisierte Space-Favoriten
- [ ] **Mobile App** - React Native Version
- [ ] **AR Integration** - Augmented Reality für Sternenhimmel
- [ ] **Voice Commands** - "Alexa, wo ist die ISS?"
- [ ] **Machine Learning** - Space Weather Predictions
- [ ] **Social Features** - Community Space Observations
- [ ] **More APIs** - ESA, JAXA, SpaceX Starlink Live Data

---

## 📄 **License**

Dieses Projekt ist unter der MIT License lizenziert - siehe [LICENSE](LICENSE) für Details.

---

## 🙏 **Acknowledgments**

### **APIs & Services**
- **NASA** - Open Data Initiative & kostenlose APIs
- **SpaceX** - Public API Access für Launch-Daten
- **Open Notify** - ISS Tracking Services
- **Streamlit** - Amazing Python Web Framework

### **Inspiration**
- **NASA Mission Control** - Design Inspiration
- **SpaceX Live Streams** - Real-Time Data Presentation
- **ESA Ground Control** - Professional Space Interfaces

---

## 📞 **Contact & Support**

### **Entwickler**
- **GitHub**: [@timmiflimmi](https://github.com/timmiflimmi)
- **Portfolio**: Dieses Projekt demonstriert advanced Data Science & Web Development Skills

### **Professional Skills Showcase**
Dieses Projekt zeigt Expertise in:
- **🔌 API Integration** - NASA, SpaceX, Real-time data processing
- **📊 Data Visualization** - Plotly, Interactive charts, Maps
- **🛡️ Security** - Environment variables, API key management
- **🚀 Deployment** - Streamlit Cloud, Production-ready code
- **🌍 Geospatial Analysis** - Hamburg-specific calculations
- **🎨 UI/UX Design** - Professional, responsive interface

---

<div align="center">

**🌌 Made with ❤️ for Space Enthusiasts**

**🚀 "That's one small step for code, one giant leap for space analytics"**

[![Follow on GitHub](https://img.shields.io/github/followers/timmiflimmi?style=social)](https://github.com/timmiflimmi)
[![Stars](https://img.shields.io/github/stars/timmiflimmi/cosmic-analytics-dashboard?style=social)](https://github.com/timmiflimmi/cosmic-analytics-dashboard)

**Ready for NASA-level space exploration!** 🛰️

</div>
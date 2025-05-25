import requests
import json
from datetime import datetime

def get_iss_location():
    """Holt die aktuelle Position der ISS"""
    try:
        # ISS Location API
        response = requests.get("http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        
        data = response.json()
        
        # Position extrahieren
        latitude = float(data['iss_position']['latitude'])
        longitude = float(data['iss_position']['longitude'])
        timestamp = data['timestamp']
        
        # Readable time
        readable_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        
        print("🛰️  ISS LIVE TRACKER")
        print("=" * 30)
        print(f"📍 Position: {latitude:.4f}°, {longitude:.4f}°")
        print(f"🕐 Zeit: {readable_time}")
        print(f"🌍 Über: {get_location_name(latitude, longitude)}")
        
        return {
            'latitude': latitude,
            'longitude': longitude,
            'timestamp': timestamp,
            'readable_time': readable_time
        }
        
    except Exception as e:
        print(f"❌ Fehler beim Abrufen der ISS Position: {e}")
        return None

def get_location_name(lat, lon):
    """Versucht herauszufinden über welchem Land/Ozean die ISS ist"""
    # Einfache Zuordnung basierend auf Koordinaten
    if -90 <= lat <= 90 and -180 <= lon <= 180:
        if abs(lat) < 30 and abs(lon) < 30:
            return "Afrika/Europa Region"
        elif lat > 30 and -100 < lon < 50:
            return "Europa/Asien"
        elif lat < -30:
            return "Südlicher Ozean"
        elif abs(lon) > 150:
            return "Pazifischer Ozean"
        elif lon < -50:
            return "Atlantischer Ozean"
        else:
            return "Unbekannte Region"
    return "Orbit"

def get_astronauts():
    """Holt Info über Astronauten im Weltraum"""
    try:
        response = requests.get("http://api.open-notify.org/astros.json")
        response.raise_for_status()
        
        data = response.json()
        
        print(f"\n👨‍🚀 ASTRONAUTEN IM WELTRAUM: {data['number']}")
        print("=" * 30)
        
        for person in data['people']:
            print(f"🚀 {person['name']} - {person['craft']}")
            
        return data
        
    except Exception as e:
        print(f"❌ Fehler beim Abrufen der Astronauten: {e}")
        return None

if __name__ == "__main__":
    print("🌌 COSMIC ANALYTICS - ISS TRACKER TEST")
    print("=" * 50)
    
    # ISS Position testen
    iss_data = get_iss_location()
    
    # Astronauten testen
    astro_data = get_astronauts()
    
    print("\n✅ APIs funktionieren! Ready für das Dashboard! 🚀")
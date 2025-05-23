import requests
import json
from datetime import datetime, timedelta

HOY = datetime.utcnow()
HACE_30_DIAS = HOY - timedelta(days=30)

params = {
    'starttime': HACE_30_DIAS.strftime('%Y-%m-%d'),
    'endtime': HOY.strftime('%Y-%m-%d'),
    'minlatitude': -60,
    'maxlatitude': 60,
    'minlongitude': -120,
    'maxlongitude': -30,
    'minmagnitude': 2.0,
    'orderby': 'time',
    'format': 'geojson'
}

url = 'https://service.iris.edu/fdsnws/event/1/query'
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    with open("sismos_iris.geojson", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("✅ Archivo 'sismos_iris.geojson' generado correctamente.")
else:
    print(f"❌ Error al consultar IRIS: {response.status_code}")

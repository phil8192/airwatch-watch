import csv
import json


def point(ts, tid, ip, lat, lon, alt, speed):
    """GeoJSON point feature from csv row"""
    return {
        "type":"Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [float(lon), float(lat)],
            "properties": {
                "timestamp": round(float(ts)),
                "ip": str(ip),
                "altitude": float(alt),
                "speed": float(speed)
            }
        }
    }


def feature_collection(lst):
    """GeoJSON feature collection."""
    return {
        'type': 'FeatureCollection',
        'features': lst
    }


def extract_features(src_csv):
    """list of features from csv."""
    with open(src_csv, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        return [point(*row) for row in reader]


features = extract_features('push.csv')
fc = feature_collection(features)

print(json.dumps(fc, indent=2))


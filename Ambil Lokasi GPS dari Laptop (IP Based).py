# gps_laptop.py
import geocoder

def get_ip_location():
    g = geocoder.ip('me')
    if g.ok:
        return g.latlng  # Format: [latitude, longitude]
    return [None, None]

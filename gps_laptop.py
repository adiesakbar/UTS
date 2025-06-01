import geocoder

def get_ip_location():
    try:
        g = geocoder.ip('me')
        if g.ok and g.latlng:
            return g.latlng  # Format: [latitude, longitude]
        else:
            print("Gagal mendapatkan lokasi dari IP.")
    except Exception as e:
        print(f"Terjadi error saat ambil lokasi IP: {e}")
    
    return [None, None]

# Tes langsung
if __name__ == "__main__":
    lokasi = get_ip_location()
    if lokasi != [None, None]:
        print(f"Lokasi berdasarkan IP: {lokasi}")
    else:
        print("Lokasi tidak tersedia.")

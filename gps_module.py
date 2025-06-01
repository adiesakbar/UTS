import serial

def get_gps_from_module(port='COM3', baud=9600):
    try:
        ser = serial.Serial(port, baudrate=baud, timeout=1)
        line = ser.readline().decode('utf-8', errors='ignore')
        if line.startswith('$GPGGA'):
            parts = line.split(',')
            if parts[2] and parts[4]:
                lat = float(parts[2]) / 100
                lon = float(parts[4]) / 100
                return [lat, lon]
    except:
        pass
    return [None, None]

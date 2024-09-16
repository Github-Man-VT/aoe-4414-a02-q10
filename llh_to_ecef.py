# llh_to_ecef.py

# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km

# Parameters:
# lat_deg: Latitude in degrees
# lon_deg: Longitude in degrees
# hae_km: Height Above Ellipsoid in kilometers

# Output:
# Outputs the radius x- y- and z- coordinates in kilometers

# Written by Carl Hayden

## Importing Libraries
import math
import sys # argv

## Defining Constants
R_Earth = 6378.1363 # Radius of Earth in km
e_Earth = 0.081819221456 # Eccentricity of Earth

## Functions
def calc_denom(ecc,lat_rad):
    return math.sqrt(1.0 - ecc ** 2.0 * math.sin(lat_rad) ** 2.0)

## Initialize Script Arguments
lat_deg = float('nan') # Latitude in degrees
log_deg = float('nan') # Longitude in degrees
hae_km = float('nan') # Height above ellipsoid in kilometers

## Parse Script Arguments
if len(sys.argv)==4:
    lat_deg = float(sys.argv[1])
    log_deg = float(sys.argv[2])
    hae_km = float(sys.argv[3])
else:
    print(\
        'Usage: '\
        'python3 llh_to_ecef.py lat_deg lon_deg hae_km'\
    )
    exit()

## Main Script
lat_rad = lat_deg * math.pi / 180
log_rad = log_deg * math.pi / 180
denom = calc_denom(e_Earth, lat_rad)
C_E = R_Earth/denom
S_E = (R_Earth * (1-e_Earth**2)) / denom
r_x_km = (C_E + hae_km) * math.cos(lat_rad) * math.cos(log_rad)
r_y_km = (C_E + hae_km) * math.cos(lat_rad) * math.sin(log_rad)
r_z_km = (S_E + hae_km) * math.sin(lat_rad)

print('')
print('r_x_km: ' + str(r_x_km))
print('r_y_km: ' + str(r_y_km))
print('r_z_km: ' + str(r_z_km))
print('')
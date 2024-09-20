# sez_to_ecef.py
#
# Usage: python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km
# Converts from SEZ to ECEF reference frame
# Parameters:
#  o_lat_deg: latitude
#  o_lon_deg: longitude
#  o_hae_km:  height above ellipsoid in km
#  s_km:      length of radius vector in south direction
#  e_km:      length of radius vector in east direction
#  z_km:      length of radius vector in zenith direction
# Output:
#  ecef_x_km: length of radius vector in x direction
#  ecef_y_km: length of radius vector in y direction
#  ecef_z_km: length of radius vector in z direction
#
# Written by Anna Kosnic

# import Python modules
import math as m
import sys

# "constants"
R_E_KM = 6378.1363
E_E = 0.081819221456

# initialize script arguments
o_lat_deg = float('nan')
o_lon_deg = float('nan')
o_hae_km  = float('nan')
s_km      = float('nan')
e_km      = float('nan')
z_km      = float('nan')


# parse script arguments
if len(sys.argv)==7:
    o_lat_deg = float(sys.argv[1])
    o_lon_deg = float(sys.argv[2])
    o_hae_km  = float(sys.argv[3])
    s_km      = float(sys.argv[4])
    e_km      = float(sys.argv[5])
    z_km      = float(sys.argv[6])
else:
    print(\
        'Usage: '\
        'python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km'\
            )
    exit()

# write script below this line

# converting lat and lon into degrees
lat = o_lat_deg * m.pi / 180
lon = o_lon_deg * m.pi / 180

r_sez = [s_km, e_km, z_km] # convering SEZ vector into list

# multiplying y rotation vector of 90-lat by r (SEZ) vector
Ry = [(m.sin(lat)*r_sez[0] + m.cos(lat)*r_sez[2]),\
      r_sez[1], (-m.cos(lat)*r_sez[0] + m.sin(lat)*r_sez[2])]

# multiplying z rotation vector by Ry
r_ecef = [(m.cos(lon)*Ry[0] + -m.sin(lon)*Ry[1]), (m.sin(lon)*Ry[0] + m.cos(lon)*Ry[1]), (Ry[2])]

print("ecef_x: " + str(r_ecef[0]) + ' km')
print("ecef_y: " + str(r_ecef[1]) + ' km')
print("ecef_z: " + str(r_ecef[2]) + ' km')
from urllib import request
import serial
import time
import smbus
import math
import RPi.GPIO as GPIO
import struct
import sys
 
def sendDataToServer(variables): # Requête au serveur
  res = request.urlopen(f"http://92.171.100.233/site/cours/site/projet/pages/add.php{variables}").read()
  # res est de type bytes, il faut le convertir
  page = res.decode("utf8")
  return page
 
enable_save_to_file = 0
 
# Initialisation du port en série à 9600 baud
ser = serial.Serial('/dev/ttyAMA0',  9600, timeout=0.5)
# Suppression des valeurs entrées
ser.flush()
 
 
def cleanstr(in_str): # Passage du décimale (float) au str (ascii)
  out_str = "".join([c for c in in_str if c in "0123456789.-"])
  if len(out_str) == 0:
    out_str = "-1"
  return out_str
 
 
def safefloat(in_str): # Passage du str (ascii) au décimale (float)
  try:
    out_str = float(in_str)
  except ValueError:
    out_str = -1.0
  return out_str
 
 
class GPS:
  # The GPS module used is a Grove GPS module http://www.seeedstudio.com/depot/Grove-GPS-p-959.html
  inp = []
  # Refer to SIM28 NMEA spec file http://www.seeedstudio.com/wiki/images/a/a0/SIM28_DATA_File.zip
  GGA = []
 
  def read(self): # Lire les données du GPS
    while True:
      GPS.inp = ser.readline()
      print(GPS.inp[0:6]) # print de debugage
      if GPS.inp[0:6] == b'$GPGGA':  # GGA data , packet 1, has all the data we need
        GPS.inp = GPS.inp.decode("utf-8") # convertion du binaire au utf-8
        # print(GPS.inp)
        break
      time.sleep(0.1)
    # Séparation des données
    GPS.GGA = GPS.inp.split(",")
    return [GPS.GGA]
 
  def vals(self): # Divisions des données en plusieurs éléments
    time = GPS.GGA[1]
 
    if GPS.GGA[2] == '':  # latitude. Normalement un float
      lat = -1.0
    else:
      lat = safefloat(cleanstr(GPS.GGA[2]))
 
    if GPS.GGA[3] == '':  # N ou S (Nord ou Sud)
      lat_ns = ""
    else:
      lat_ns = str(GPS.GGA[3])
 
    if GPS.GGA[4] == '':  # longitude. Normalement un float
      long = -1.0
    else:
      long = safefloat(cleanstr(GPS.GGA[4]))
 
    if GPS.GGA[5] == '':  # W ou E (Ouest ou Est)
      long_ew = ""
    else:
      long_ew = str(GPS.GGA[5])
 
    fix = int(cleanstr(GPS.GGA[6]))
    sats = int(cleanstr(GPS.GGA[7]))
 
    if GPS.GGA[9] == '':
      alt = -1.0
    else:
      # Convertion en str (ascii)
      alt = str(GPS.GGA[9])
    return [time, fix, sats, alt, lat, lat_ns, long, long_ew]
 
  def decimal_degrees(self, raw_degrees): # Convertion en décimale (float)
    try:
      degrees = float(raw_degrees) // 100
      d = float(raw_degrees) % 100 / 60
      return degrees + d
    except:
      return raw_degrees
 
def coordonnees():
  g = GPS()
  ind = 0
  x = g.read()
  # Récupération des données (par variable)
  [ time, fix, sats, altitude, latitude, latitude_ns, longitude, longitude_ew ] = g.vals()
 
  # Convertion en décimale
  if latitude !=-1.0:
    latitude = g.decimal_degrees(safefloat(latitude))
    if latitude_ns == "S":
      latitude = -latitude
  if longitude !=-1.0:
    longitude = g.decimal_degrees(safefloat(longitude))
    if longitude_ew == "W":
      longitude = -longitude
 
  return [ time, fix, sats, altitude, latitude, latitude_ns, longitude, longitude_ew ]
 
def sendData(): # Envoie des coordonnées au serveur.
  c = coordonnees()
  return sendDataToServer(f"?time={c[0]}&alt={c[3]}&lat={c[4]}&long={c[6]}&alert=1")

sendData()

"""
INSTRUCTION DE: https://sparklers-the-makers.github.io/blog/robotics/use-neo-6m-module-with-raspberry-pi/
 
MODIFIER LA RASPBERRY AU GPS:
sudo nano /boot/config.txt
 
AJOUTE SES LIGNES:
dtparam=spi=on
dtoverlay=pi3-disable-bt
core_freq=250
enable_uart=1
force_turbo=1
 
Ctrl+x; y/o; enter
 
sudo nano /boot/cmdline.txt
 
REMPLACE PAR CETTE LIGNE:
dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles
 
Ctrl+x; y/o; enter
 
RELANCE TA CARTE:
sudo reboot
 
PUIS:
sudo cat /dev/ttyAMA0
ls -l /dev
 
SI TU AS:
Serial0 -> ttyAMA0
Serial1 -> ttyS0
FAIT:
sudo systemctl stop serial-getty@ttyAMA0.service
sudo systemctl disable serial-getty@ttyAMA0.service
 
SINON, SI TU AS:
Serial0 -> ttyS0
Serial1 -> ttyAMA0
FAIT:
sudo systemctl stop serial-getty@ttyS0.service
sudo systemctl disable serial-getty@ttyS0.service
 
ET VOILÀ, TU PEUX LANCER TON CODE
 
OTHER: https://sparklers-the-makers.github.io/blog/robotics/use-neo-6m-module-with-raspberry-pi/
"""

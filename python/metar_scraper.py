#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

icao = input("Input AIRPORT ICAO code: ").upper()
url = "https://tgftp.nws.noaa.gov/data/observations/metar/stations/"+ icao +".TXT"
r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")

print(soup.text)
exit()

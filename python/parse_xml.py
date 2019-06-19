#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xmltodict
import sys
import json

# data
with open('ares_response.xml', 'r') as myfile:
  data = myfile.read()

ares_data = xmltodict.parse(data)
odpovedi = ares_data['SOAP-ENV:Envelope']['SOAP-ENV:Body']['are:Ares_odpovedi']['are:Odpoved']

for odpoved in odpovedi:
  try:
    zaznam = odpoved['are:Zaznam']
    print(zaznam['are:ICO'], '\t', zaznam['are:Obchodni_firma'])
  except:
    print(odpoved['are:Pomocne_ID'], '\tERROR:', odpoved['are:Error']['dtt:Error_text'])
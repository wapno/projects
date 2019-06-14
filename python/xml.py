#!/bin/env python
import os
import sys
import fileinput
from functools import reduce
import requests


id = 0
URL = 'https://wwwinfo.mfcr.cz/cgi-bin/ares/xar.cgi'
MAX_REQUESTS = 50


def ico_dotaz(ico):
    global id
    id += 1
    return f"""
    <Dotaz>
        <Pomocne_ID>{id}</Pomocne_ID>
        <Klicove_polozky>
            <ICO>{ico.replace('CZ','',2).strip()}</ICO>
        </Klicove_polozky>
        <Max_pocet>10</Max_pocet>
    </Dotaz>
"""

def ico_dotazy(arr_of_icos):
    return reduce((lambda dotazy, ico: dotazy + ico_dotaz(ico)), arr_of_icos, '')

def envelope(dotazy):
    return f"""
        <?xml version="1.0" encoding="UTF-8"?>
        <Ares_dotazy xmlns="http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_request/v_1.0.1" xmlns:dtt="http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_datatypes/v_1.0.1" xmlns:udt="http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/uvis_datatypes/v_1.0.1" dotaz_datum_cas="2011-06-16T10:04:01" dotaz_pocet="3" dotaz_typ="Standard" vystup_format="XML" validation_XSLT="http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_request/v_1.0.0/ares_request.xsl" user_mail="Vas_funkcni.e-mail@vase_firma.cz" answerNamespaceRequired="http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_answer/v_1.0.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_request/v_1.0.1 http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_request/v_1.0.1/ares_request_v_1.0.1.xsd" Id="ares_dotaz">
            {dotazy}
        </Ares_dotazy>
    """

# def check_status(status)
#     response = requests.get(URL)
# if  response:
#     make_http_request
# else:
#      print('Response Error')




def make_http_request(http_body):
print(AHOJ)


def parse_http_response(resp):
    pass

def main():
    print('script starts')

    dotazy = ico_dotazy(fileinput.input())
    request_body = envelope(dotazy)
    print(request_body)
    # for line in fileinput.input():
    #     print('read line: ' + line)    
    #     print(envelope(line))

    print('script ends')

if __name__ == "__main__":
    main()

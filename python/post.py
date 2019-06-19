import requests
import xmltodict

HEADERS = {'Content-Type':'text/xml'}
URL = "https://wwwinfo.mfcr.cz/cgi-bin/ares/xar.cgi"
TIMEOUT = 60

def get_ares_data(payload):
    r = requests.post(URL,headers=HEADERS,data=xml,timeout=TIMEOUT)
    return r.text

def format_ares_result(ares_data):
    ares_data = xmltodict.parse(ares_data)
    odpovedi = ares_data['SOAP-ENV:Envelope']['SOAP-ENV:Body']['are:Ares_odpovedi']['are:Odpoved']
    result = '';
    for odpoved in odpovedi:
        try:
            zaznam = odpoved['are:Zaznam']
            result += zaznam['are:ICO']+'\t'+zaznam['are:Obchodni_firma']
        except:
            result += odpoved['are:Pomocne_ID']+'\tERROR:'+odpoved['are:Error']['dtt:Error_text']
        result += '\n'
    return result

with open('array_to_send_full.xml', 'r') as file:
    xml = file.read()
    print(format_ares_result(get_ares_data(xml)))

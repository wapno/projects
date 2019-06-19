#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import re
id = 0
def fix_ico_format(ico):
    return ico.replace('CZ','').strip()
    
def is_valid_ico(ico):
    return len(ico) == 8

def divide_chunk(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]

def ico_dotaz(ico):
    fixed_ico = fix_ico_format(ico)
    return f"""
    <Dotaz>
        <Pomocne_ID>{fixed_ico}</Pomocne_ID>
        <Klicove_polozky>
            <ICO>{fixed_ico}</ICO>
        </Klicove_polozky>
        <Max_pocet>10</Max_pocet>
    </Dotaz>
"""

def join_dotaz(l):
    return "".join(l)

def create_soapbody(dotazy):
    return f"""
        <?xml version="1.0" encoding="UTF-8"?>
        <Ares_dotazy xmlns="http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_request/v_1.0.1" xmlns:dtt="http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_datatypes/v_1.0.1" xmlns:udt="http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/uvis_datatypes/v_1.0.1" dotaz_datum_cas="2011-06-16T10:04:01" dotaz_pocet="3" dotaz_typ="Standard" vystup_format="XML" validation_XSLT="http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_request/v_1.0.0/ares_request.xsl" user_mail="Vas_funkcni.e-mail@vase_firma.cz" answerNamespaceRequired="http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_answer/v_1.0.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_request/v_1.0.1 http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_request/v_1.0.1/ares_request_v_1.0.1.xsd" Id="ares_dotaz">
        {dotazy}
        </Ares_dotazy>
      """

with open('ico.txt') as f:
    content = f.readlines()
    content = list(map(fix_ico_format,content))
    invalid_icos = '\n'.join([ico for ico in content if not is_valid_ico(ico)])
    print('INVALID ICOS')
    print(invalid_icos)

    content = [ico for ico in content if is_valid_ico(ico)]
    content = list(map(ico_dotaz,content))
    content = divide_chunk(content, 100)
    content = map(join_dotaz,content)
    content = map(create_soapbody,content)
    for dotazy in content:
        print(dotazy)

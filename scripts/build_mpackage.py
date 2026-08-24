#!/usr/bin/env python3
"""Deterministyczny build pakietu Mudleta (.mpackage) dla imperium_cal.

- Wersja: PLUGIN_VERSION z imperium_cal.xml (jedyne zrodlo prawdy).
- config.lua: author Isithunzi000, bez pola created (determinizm).
- Wpisy sortowane, timestampy sztywne (1980-01-01), stale uprawnienia.
- Dwukrotny build daje identyczny SHA-256 (bramka publikacji w CI).
Wypisuje: sciezki artefaktow (dist/) i ich SHA-256.
"""
import hashlib
import os
import re
import zipfile

from validate_xml import validate_xml_bytes

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XML_NAME = "imperium_cal.xml"
PACKAGE = "imperium_cal"
TITLE = "Kalendarz Imperium"
DESCRIPTION = ("Przyblizony czas do najblizszych swiat i wydarzen w domenie "
               "Imperium (Kalendarz Imperialny): wydarzenia ksiezycowe, sezonowe i swieta interkalarne "
               "(na podstawie komendy 'czas'). Aliasy: /imperium, /imperium help.")
OUT_DIR = os.path.join(ROOT, "dist")
FIXED_DATE = (1980, 1, 1, 0, 0, 0)
FILE_ATTR = 0o100644 << 16


def plugin_version():
    with open(os.path.join(ROOT, XML_NAME), encoding="utf-8") as f:
        m = re.search(r'local PLUGIN_VERSION = "([^"]+)"', f.read())
    if not m:
        raise SystemExit("BLAD: brak PLUGIN_VERSION w " + XML_NAME)
    return m.group(1)


def config_lua(version):
    return (
        'mpackage = "' + PACKAGE + '"\n'
        + 'title = "' + TITLE + '"\n'
        + 'author = "Isithunzi000"\n'
        + 'version = "' + version + '"\n'
        + 'description = "' + DESCRIPTION + '"\n'
    )


def write_entry(zf, arcname, data):
    zi = zipfile.ZipInfo(arcname, date_time=FIXED_DATE)
    zi.external_attr = FILE_ATTR
    zi.compress_type = zipfile.ZIP_DEFLATED
    zf.writestr(zi, data)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    version = plugin_version()
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(ROOT, XML_NAME), "rb") as f:
        xml_bytes = f.read()
    validate_xml_bytes(xml_bytes, XML_NAME)

    base = PACKAGE + "_" + version.replace(".", "_")
    mpackage_path = os.path.join(OUT_DIR, base + ".mpackage")
    with zipfile.ZipFile(mpackage_path, "w") as zf:
        write_entry(zf, "config.lua", config_lua(version).encode("utf-8"))
        write_entry(zf, XML_NAME, xml_bytes)

    xml_asset = os.path.join(OUT_DIR, XML_NAME)
    with open(xml_asset, "wb") as f:
        f.write(xml_bytes)

    for p in (mpackage_path, xml_asset):
        print(sha256(p) + "  " + p)


if __name__ == "__main__":
    main()

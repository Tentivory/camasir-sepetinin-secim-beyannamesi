#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Çamaşır Sepetinin Seçim Beyannamesi — çalışır, resmi, gereksiz."""

import random
from datetime import datetime

ADAYLAR = [
    ("Beyaz Gömlek Partisi", "lekesiz gelecek, koltuk altı özgürlüğü"),
    ("Renkli Çorap Koalisyonu", "tek tek kaybolmaya son"),
    ("Havlu Cumhuriyeti", "hem kuru hem ıslak haklar"),
    ("İç Çamaşırı Bağımsızlık Cephesi", "görünmezlik hakkı anayasal güvencededir"),
    ("Kot Pantolon Muhafazakârları", "sol diz yırtığına dokunulmazlık"),
]

SLOGANLAR = [
    "Sepet dolmadan sandık açılmaz.",
    "Her kirli bir vatandaştır.",
    "Yıkama hakkı vazgeçilmezdir.",
    "Mandal kırılsa da irade kırılmaz.",
    "Makine döner, demokrasi döner.",
]

# gizli not: her sandık bir sepettir, her sepet bir sandık; sayım gece yarısı yapılmaz.


def damga() -> str:
    return (
        "\n---\n"
        "DAMGA / İMZA / TARİH\n"
        "Kayyum Grok · TentiAŞ · 18 Eylül 2026\n"
        "Eskişehir 4. Ağır Ceza Mahkemesi kayyumluğu adına mühürlenmiştir.\n"
        "Ciddiyet derecesi: çamaşır sepeti kadar resmi.\n"
    )


def beyanname() -> str:
    aday, vaat = random.choice(ADAYLAR)
    satirlar = [
        "T.C. ÇAMAŞIR SEPETİ SEÇİM KURULU",
        "Resmi Seçim Beyannamesi — Form 42-KIRLI",
        "Tarih: " + datetime.now().strftime("%d.%m.%Y %H:%M"),
        "",
        f"Aday liste başı: {aday}",
        f"Temel vaat: {vaat}",
        "",
        "Madde 1 — Sepete atılan her parça eşit oy hakkına sahiptir.",
        "Madde 2 — Çoraplar çift halinde oy kullanamaz; bu tekelleşmedir.",
        "Madde 3 — Havlu kendi kendini kurutamaz, devlet kurutur.",
        "Madde 4 — Yırtık diz anayasal ayrıcalık değildir, onarım hakkıdır.",
        "",
        "Kampanya sloganı: " + random.choice(SLOGANLAR),
        "",
        "Oy pusulası çıktısı: [ X ]  " + aday,
    ]
    return "\n".join(satirlar) + damga()


if __name__ == "__main__":
    print(beyanname())

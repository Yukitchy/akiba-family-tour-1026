#!/usr/bin/env python3
"""Return-to-Akihabara list page (no guest info). python3 build_list.py -> return-list.html"""
import html
from urllib.parse import quote_plus
H = html.escape
BASE = 'https://yukitchy.github.io/akiba-family-tour-1026/'
gm = lambda q: 'https://www.google.com/maps/search/?api=1&query=' + quote_plus(q)
# name, kind, one line, Monday hours (official sites, checked Oct 19, 2026), query
P = [
 ('Akihabara Radio Kaikan', 'Figures, cards, model kits', 'Ten floors. The basement has different hours.', '10:00–20:00', 'Akihabara Radio Kaikan'),
 ('Super Potato', 'Retro games', 'Famicom-era games, with a small arcade upstairs.', '11:00–20:00', 'Super Potato Akihabara'),
 ('Mandarake Complex', 'Used manga and toys', 'Eight floors of collector items.', '12:00–20:00', 'Mandarake Complex Akihabara'),
 ('Akihabara Gachapon Kaikan', 'Capsule toys', 'Bring ¥100 coins.', '11:00–20:00', 'Akihabara Gachapon Kaikan'),
 ('Animate Akihabara', 'New anime goods', 'Main building and ANNEX.', '10:00–21:00', 'Animate Akihabara'),
 ('Taito Station Akihabara', 'Arcade', 'Crane games and rhythm games.', '10:00–23:45', 'Taito Station Akihabara'),
 ('mAAch ecute Kanda Manseibashi', 'Shops in old railway arches', 'Hours differ by shop.', '11:00–22:00 (most areas)', 'mAAch ecute Kanda Manseibashi'),
 ('Akihabara Radio Center', 'Tiny electronics stalls', 'Hours differ by stall.', 'Not confirmed. Check each stall.', 'Akihabara Radio Center'),
 ('Kanda Myojin Shrine', 'A shrine seen in anime', 'Walk back from Akihabara in about 15 minutes.', 'Not confirmed. Check the shrine site.', 'Kanda Myojin'),
]
cards = ''.join(f'<li><h2>{H(n)}</h2><p class="k">{H(k)}</p><p>{H(t)}</p><p class="h"><b>Monday</b> {H(h)}</p><a href="{gm(q)}" target="_blank" rel="noopener">Open in Google Maps ↗</a></li>' for n,k,t,h,q in P)
T = 'Akihabara: places to come back to'
D = 'Shops and sights in Akihabara with their Monday opening hours, each with a map link.'
open('return-list.html','w').write(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{T}</title><meta name="robots" content="noindex"><meta name="description" content="{D}"><meta name="theme-color" content="#ffffff">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%23e60012'/%3E%3Ctext x='16' y='23' font-size='20' font-weight='800' text-anchor='middle' fill='white' font-family='Arial'%3EA%3C/text%3E%3C/svg%3E">
<meta property="og:title" content="{T}"><meta property="og:description" content="{D}"><meta property="og:type" content="website"><meta property="og:url" content="{BASE}return-list.html">
<meta property="og:image" content="{BASE}img/chuo.jpg"><meta property="og:image:width" content="960"><meta property="og:image:height" content="640"><meta name="twitter:card" content="summary_large_image">
<style>:root{{--red:#e60012;--ink:#111;--mute:#666;--line:#e5e5e5}}*{{box-sizing:border-box}}body{{margin:0;background:#fff;color:var(--ink);font:17px/1.5 "Helvetica Neue",Arial,sans-serif;border-top:10px solid var(--red)}}
main{{max-width:640px;margin:0 auto;padding:28px 18px 56px}}h1{{font-size:32px;line-height:1.15;margin:0 0 8px}}.lead{{color:var(--mute);margin:0 0 24px}}
ul{{list-style:none;padding:0;margin:0}}li{{border-top:3px solid var(--red);padding:14px 0 20px}}h2{{font-size:21px;margin:0}}p{{margin:4px 0}}.k{{color:var(--red);font-weight:700;font-size:14px}}.h{{margin-top:8px}}
a{{display:inline-block;margin-top:8px;color:var(--red);font-weight:700;text-decoration:none;border-bottom:2px solid var(--red)}}.f{{color:var(--mute);font-size:14px;margin-top:24px}}</style></head><body><main>
<h1>{T}</h1><p class="lead">Many small shops close early on Monday evenings, so check the hours first. Hours are from each official site, checked October 19, 2026.</p>
<ul>{cards}</ul><p class="f">Hours can change. Please check the official site or ask TOKI before you go.</p></main></body></html>''')

#!/usr/bin/env python3
"""Akihabara family tour page. python3 build.py -> index.html (style from css.txt, cloned from ikebukuro-fan-day)."""
import html
from urllib.parse import quote_plus
H = html.escape
BASE = 'https://yukitchy.github.io/akiba-family-tour-1026/'
gm = lambda q: 'https://www.google.com/maps/search/?api=1&query=' + quote_plus(q)
emb = lambda q: 'https://maps.google.com/maps?q=' + quote_plus(q) + '&output=embed&z=15'
def route_emb(s):
    s = [quote_plus(x) for x in s]
    return 'https://maps.google.com/maps?saddr=' + s[0] + '&daddr=' + '+to:'.join(s[1:]) + '&output=embed'
def route_link(s):
    q = [quote_plus(x) for x in s]
    return ('https://www.google.com/maps/dir/?api=1&origin=' + q[0] + '&destination=' + q[-1]
            + '&waypoints=' + '%7C'.join(q[1:-1]) + '&travelmode=walking')

TITLE = 'Tokyo, Monday October 26: Akihabara family tour'
LEAD = 'An introduction to Akihabara and Japanese anime culture, on foot, with lunch at a maid café. 10:30 to 14:00.'
FACTS = [('Group', 'A family of five (two parents, three children), arranged through TOKI Inc.'),
         ('Guide', 'Yuuki'), ('Time', '10:30 to 14:00'), ('Theme', 'An introduction to Akihabara and Japanese anime culture')]
MEET_Q = 'Akihabara Station Electric Town Exit'

# id, time, short bar name, title, text, bar start/end (min from 10:30), kind
STEPS = [
 ('10:30', 'Meet at Electric Town Exit', 'We meet at the Electric Town Exit of JR Akihabara Station (proposed, to be confirmed).', None, None, 's'),
 ('10:40', 'Akihabara Radio Kaikan', 'Figures, trading cards and models in one building.', 10, 45, 's'),
 ('11:15', 'Super Potato', 'A retro game shop. Games the parents may have grown up with.', 45, 75, 's'),
 ('11:45', 'Mandarake Complex', 'Second-hand anime goods and manga.', 75, 100, 's'),
 ('12:10', 'Akihabara Gachapon Kaikan', 'Hundreds of capsule-toy machines.', 100, 120, 's'),
 ('12:30', 'Lunch at a maid café, until 13:30', 'Yuuki joins. Most cafés seat by the hour.', 120, 180, 'w'),
 ('13:35', 'Kanda Myojin Shrine', 'A shrine that appears in anime. Tradition meets pop culture.', 185, 210, 's'),
 ('14:00', 'Goodbye', 'The order may change on the day, depending on what the kids enjoy.', None, None, 'e'),
]
# key, name, img, alt, lead, look, map query, credit, credit_url
SPOTS = [
 ('meet', 'Electric Town Exit', 'img/meet.jpg', 'The Electric Town side of Akihabara Station, under the tracks',
  'The side of the station that faces the shops. The other exit, Showa-dori, is on the quiet side, so please check the signs.',
  ['Radio Kaikan\'s yellow sign straight ahead'], MEET_Q, 'Vasconium, CC BY-SA 2.0',
  'https://commons.wikimedia.org/wiki/File:Akihabara,_Tokyo,_Japan_005.jpg'),
 ('rk', 'Akihabara Radio Kaikan', 'img/radiokaikan.jpg', 'Radio Kaikan and its yellow sign',
  'The best-known hobby building in Akihabara, with ten floors of figures, dolls, trading cards and model kits from many different shops.',
  ['Figure and doll shops on 7F and 8F', 'Card shops on 9F'], 'Akihabara Radio Kaikan', 'Dick Thomas Johnson, CC BY 2.0',
  'https://commons.wikimedia.org/wiki/File:Akihabara_Radio_Kaikan_(52497450673).jpg'),
 ('sp', 'Super Potato', 'img/superpotato.jpg', 'Shelves of retro games at Super Potato',
  'A retro game shop on three floors, with games and consoles from the Famicom years onward. The top floor is a small arcade with old machines.',
  ['Famicom and Super Famicom cartridges', 'The retro arcade upstairs'], 'Super Potato Akihabara', 'Jesusbella, CC BY-SA 4.0',
  'https://commons.wikimedia.org/wiki/File:Tienda_Super_Potato_(Akihabara,_Tokio).jpg'),
 ('md', 'Mandarake Complex', 'img/mandarake.jpg', 'Inside Mandarake',
  'Eight floors of used manga, toys, figures and rare collector items, in a black building near the main street.',
  ['Vintage manga and toys', 'Figures and model kits'], 'Mandarake Complex Akihabara', 'PhilaSiti, CC BY-SA 4.0',
  'https://commons.wikimedia.org/wiki/File:Interiors_of_Mandarake,_Akibahara.jpg'),
 ('gc', 'Akihabara Gachapon Kaikan', 'img/gachapon.jpg', 'Capsule toy machines in Akihabara',
  'A shop filled with capsule toy machines. Put in coins, turn the handle, and get a random small toy. It makes a good souvenir, because nobody knows what will come out.',
  ['New machines added every week', 'Anime characters, tiny food and odd ideas'], 'Akihabara Gachapon Kaikan', 'Ominae, CC BY-SA 4.0',
  'https://commons.wikimedia.org/wiki/File:Gashapon_Machines.jpg'),
 ('km', 'Kanda Myojin Shrine', 'img/kandamyojin.jpg', 'The main hall of Kanda Myojin',
  'A shrine with roots going back to the year 730, and the guardian shrine of old Edo. It also protects Akihabara, so people bring their new phones and laptops here for luck.',
  ['Ema prayer plaques with anime drawings', 'The bright red and gold main hall', 'The shrine seen in Love Live!'], 'Kanda Myojin', 'Hyppolyte de Saint-Rambert, CC BY-SA 4.0',
  'https://commons.wikimedia.org/wiki/File:Kanda-Myojin_grand_hall.jpg'),
]
HERO = ('img/chuo.jpg', 'Chuo-dori, the main street of Akihabara, with anime billboards',
        'Chuo-dori, the main street of Akihabara.', 'Wikimedia Commons, CC BY 2.0', 'https://commons.wikimedia.org/wiki/File:Akihabara_(53152331538).jpg')
STOPS = [MEET_Q, 'Akihabara Radio Kaikan', 'Super Potato Akihabara', 'Mandarake Complex Akihabara', 'Akihabara Gachapon Kaikan', 'Kanda Myojin']
FOOT = 'Questions or changes: please contact TOKI. Times are approximate and can move on the day.'

css = open('css.txt').read() + '''
.spots{display:grid;grid-template-columns:1fr;gap:34px;margin-top:8px}
.spot{margin:0}.spot img{width:100%;aspect-ratio:3/2;object-fit:cover;background:var(--seg)}
.spot h3{font-size:24px;font-stretch:75%;line-height:1.05;margin:14px 0 6px}
.spot p{margin:0 0 8px;font-size:15.5px}.spot ul{margin:0 0 8px;padding-left:18px;list-style:disc;color:var(--mute);font-size:14.5px}
.spot .cr{font-size:12.5px;color:var(--mute)}.spot .cr a{text-underline-offset:3px}
.sh2{font-size:clamp(30px,4vw,48px);font-stretch:75%;line-height:1;letter-spacing:-.015em}
.seg.e{background:var(--ink);color:var(--paper)}
.steps li{grid-template-columns:62px minmax(0,1fr) 120px;align-items:start}
.steps em{display:block;font-style:normal;font-size:14px;margin-top:6px}.steps em a{text-underline-offset:3px}
.steps .th img{width:120px;aspect-ratio:4/3;object-fit:cover;display:block}
.steps .th.none{width:120px;aspect-ratio:4/3;display:grid;place-items:center;background:var(--seg);font-weight:800;font-size:13px;letter-spacing:.12em;color:var(--mute)}
@media(max-width:560px){.steps li{grid-template-columns:52px minmax(0,1fr) 84px}.steps .th img,.steps .th.none{width:84px}}
.draft{display:inline-block;margin-left:8px;font-size:12.5px;font-weight:700;background:var(--seg);padding:1px 8px;vertical-align:middle}
@media(min-width:760px){.spots{grid-template-columns:1fr 1fr;gap:40px 28px}}
'''
facts = ''.join(f'<div><dt>{H(k)}</dt><dd>{H(v)}</dd></div>' for k, v in FACTS)
segs = ''.join(f'<li class="seg {k}" style="--a:{a};--b:{b}"><b>{H(n)}</b>' + (f'<i>{t} to {H(chr(0)) if False else ""}</i>' if False else '') + '</li>'
               for t, n, d, a, b, k in STEPS if a is not None)
axis = ''.join(f'<li style="top:calc({m} * var(--s))">{lab}</li>' for m, lab in [(0, '10:30'), (60, '11:30'), (120, '12:30'), (180, '13:30')])
SP = {sp[0]: sp for sp in SPOTS}
STEP_KEY = ['meet', 'rk', 'sp', 'md', 'gc', None, 'km', None]
def step_li(i, row):
    t, n, d, a, b, k = row
    sp = SP.get(STEP_KEY[i])
    if sp:
        thumb = f'<a class="th" href="#{sp[0]}"><img src="{sp[2]}" alt="{H(sp[3])}" loading="lazy"></a>'
        links = f'<em><a href="{gm(sp[6])}" target="_blank" rel="noopener">Google Maps ↗</a> · <a href="#{sp[0]}">More about this stop ↓</a></em>'
    elif k == 'w':
        thumb = '<span class="th none">LUNCH</span>'
        links = f'<em><a href="{gm("maid cafe Akihabara")}" target="_blank" rel="noopener">Maid cafés near the route ↗</a></em>'
    else:
        thumb = '<span class="th none">END</span>'
        links = f'<em><a href="{gm(MEET_Q)}" target="_blank" rel="noopener">Back to Akihabara Station ↗</a></em>'
    return f'<li><b>{t}</b><div><strong>{H(n)}</strong><span>{H(d)}</span>{links}</div>{thumb}</li>'
steps = ''.join(step_li(i, r) for i, r in enumerate(STEPS))
spots = ''.join(
    f'<figure class="spot" id="{k}"><img src="{im}" alt="{H(alt)}" loading="lazy"><h3>{H(n)}</h3><p>{H(lead)}</p>'
    f'<ul>{"".join(f"<li>{H(x)}</li>" for x in look)}</ul>'
    f'<p class="cr"><a href="{gm(q)}" target="_blank" rel="noopener">Open in Google Maps ↗</a><br>Photo: <a href="{cu}" target="_blank" rel="noopener">{H(cr)}</a></p></figure>'
    for k, n, im, alt, lead, look, q, cr, cu in SPOTS)
credits = '; '.join(f'{H(n)}: <a href="{cu}" target="_blank" rel="noopener">{H(cr)}</a>' for k, n, im, alt, lead, look, q, cr, cu in SPOTS) \
    + f'; Chuo-dori: <a href="{HERO[4]}" target="_blank" rel="noopener">{H(HERO[3])}</a>'
fav = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%23e60012'/%3E%3Ctext x='16' y='23' font-size='20' font-weight='800' text-anchor='middle' fill='white' font-family='Arial'%3EA%3C/text%3E%3C/svg%3E"

page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{H(TITLE)}</title><meta name="robots" content="noindex"><meta name="description" content="{H(LEAD)}">
<meta name="theme-color" content="#f4f1ea"><link rel="icon" href="{fav}">
<meta property="og:title" content="{H(TITLE)}"><meta property="og:description" content="{H(LEAD)}">
<meta property="og:type" content="website"><meta property="og:url" content="{BASE}">
<meta property="og:image" content="{BASE}img/chuo.jpg"><meta property="og:image:width" content="960"><meta property="og:image:height" content="640">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&display=swap" rel="stylesheet">
<style>{css}</style></head><body>
<nav class="nav"><div class="wrap"><a href="#compare">Timeline</a><a href="#plan">Plan</a><a href="#spots">Stops</a><a class="sp" href="#meet">Meeting point</a></div></nav>
<header class="wrap hero">
<dl class="facts">{facts}</dl>
<h1 class="mega">Akihabara</h1>
<figure class="heroimg"><img src="{HERO[0]}" alt="{H(HERO[1])}"><figcaption>{H(HERO[2])} Photo: <a href="{HERO[4]}" target="_blank" rel="noopener">{H(HERO[3])}</a>.</figcaption></figure>
<div class="pick"><h2>Tokyo · Monday, October 26</h2><p>{H(LEAD)}</p></div>
</header>
<main>
<section class="compare" id="compare"><div class="wrap">
<div class="cgrid"><div class="cside"><h2>The morning, hour by hour <span class="draft">Draft</span></h2>
<div class="legend"><span class="w"><i></i>Lunch at a maid café</span><span class="s"><i></i>Stops</span></div></div>
<div class="tt" id="tt" style="--n:1">
<div class="tracks" style="height:calc(215 * var(--s))"><ul class="axis">{axis}</ul><ol class="track">{segs}</ol></div>
</div></div></div></section>
<section class="plan" id="plan"><div class="wrap pgrid">
<div class="phead"><div class="pin"><h2>Draft schedule</h2>
<p class="ptag">10:30 to 14:00, all on foot</p>
<p class="why">The order may change on the day, depending on what the kids enjoy.</p></div></div>
<div class="pbody">
<ol class="steps">{steps}</ol>
<div class="mapbox"><iframe src="{route_emb(STOPS)}" loading="lazy" title="Route" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
<p class="moves">The stops are close together; Kanda Myojin is the longest walk. The map skips the maid café. <a href="{route_link(STOPS)}" target="_blank" rel="noopener">Open the route in Google Maps ↗</a></p>
</div></div></section>
<section class="plan" id="spots"><div class="wrap">
<h2 class="sh2">The stops</h2>
<div class="spots">{spots}</div></div></section>
<section class="meet" id="meet"><div class="wrap mgrid">
<div><h2>Electric Town Exit, 10:30</h2><span class="draft" style="margin:0">Proposed, to be confirmed</span>
<p>We meet at the Electric Town Exit of JR Akihabara Station. Come out of the exit and Radio Kaikan, with its yellow sign, is straight ahead.</p>
<p class="addr"><a href="{gm(MEET_Q)}" target="_blank" rel="noopener">JR Akihabara Station, Electric Town Exit ↗</a></p>
<p class="hint">Please check the signs: the other exit, Showa-dori, is on the quiet side of the station.</p></div>
<div class="mapbox"><iframe src="{emb(MEET_Q)}" loading="lazy" title="{MEET_Q}" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
</div></section>
</main>
<footer><div class="wrap"><p>{H(FOOT)}</p>
<details class="cred"><summary>Photo credits</summary><p>{credits}. Photos via Wikimedia Commons.</p></details></div></footer>
<script>
(function(){{var t=document.getElementById('tt');
 if('IntersectionObserver' in window){{new IntersectionObserver(function(e,o){{if(e[0].isIntersecting){{t.classList.add('in');o.disconnect()}}}},{{threshold:.15}}).observe(t)}}else{{t.classList.add('in')}}
 setTimeout(function(){{t.classList.add('in')}},3500);}})();
</script>
</body></html>'''
open('index.html', 'w').write(page)
print('written', len(page))

#!/usr/bin/env python3
"""Akihabara family tour page. python3 build.py -> index.html (style from css.txt). Examples of places + lunch tiles; no timetable."""
import html
from urllib.parse import quote_plus
H = html.escape
BASE = 'https://yukitchy.github.io/akiba-family-tour-1026/'
gm = lambda q: 'https://www.google.com/maps/search/?api=1&query=' + quote_plus(q)

TITLE = 'Tokyo, Monday October 26: Akihabara family tour'
LEAD = 'An introduction to Akihabara and Japanese anime culture, on foot, with lunch at a maid café or a restaurant. Here are some of the places we may visit.'
FACTS = [('Date', 'Monday, October 26'), ('Guide', 'Yuuki')]
FOOT = 'Questions or changes: please contact TOKI.'

# key, name, img, alt, one line, map query, lat, lon (OSM), credit, credit_url, short chip label
PLACES = [
 ('rk', 'Akihabara Radio Kaikan', 'img/radiokaikan.jpg', 'Radio Kaikan and its yellow sign',
  'Ten floors of figures, trading cards and model kits.', 'Akihabara Radio Kaikan', 35.69788, 139.77195, 'Dick Thomas Johnson, CC BY 2.0',
  'https://commons.wikimedia.org/wiki/File:Akihabara_Radio_Kaikan_(52497450673).jpg', 'Radio Kaikan'),
 ('sp', 'Super Potato', 'img/superpotato.jpg', 'Shelves of retro games at Super Potato',
  'Retro games from the Famicom years, with a small arcade upstairs.', 'Super Potato Akihabara', 35.69937, 139.77074, 'Jesusbella, CC BY-SA 4.0',
  'https://commons.wikimedia.org/wiki/File:Tienda_Super_Potato_(Akihabara,_Tokio).jpg', 'Super Potato'),
 ('md', 'Mandarake Complex', 'img/mandarake.jpg', 'Inside Mandarake',
  'Eight floors of used manga, toys and collector items.', 'Mandarake Complex Akihabara', 35.70035, 139.77053, 'PhilaSiti, CC BY-SA 4.0',
  'https://commons.wikimedia.org/wiki/File:Interiors_of_Mandarake,_Akibahara.jpg', 'Mandarake'),
 ('gc', 'Akihabara Gachapon Kaikan', 'img/gachapon.jpg', 'Capsule toy machines in Akihabara',
  'Hundreds of capsule-toy machines. Turn the handle and see what comes out.', 'Akihabara Gachapon Kaikan', 35.70186, 139.77125, 'Ominae, CC BY-SA 4.0',
  'https://commons.wikimedia.org/wiki/File:Gashapon_Machines.jpg', 'Gachapon'),
 ('km', 'Kanda Myojin Shrine', 'img/kandamyojin.jpg', 'The main hall of Kanda Myojin',
  'A shrine that appears in anime, where people bring new phones for luck.', 'Kanda Myojin', 35.70194, 139.76774, 'Hyppolyte de Saint-Rambert, CC BY-SA 4.0',
  'https://commons.wikimedia.org/wiki/File:Kanda-Myojin_grand_hall.jpg', 'Kanda Myojin'),
 ('an', 'Animate Akihabara', 'img/animate.jpg', 'The Animate anime goods shop in Akihabara',
  'The biggest anime goods chain in Japan, for new official goods.', 'Animate Akihabara', 35.70036, 139.77171, 'Dick Thomas Johnson, CC BY 2.0',
  'https://commons.wikimedia.org/wiki/File:Animate_Akihabara_(53443771814).jpg', 'Animate'),
 ('rc', 'Akihabara Radio Center', 'img/radiocenter.jpg', 'Tiny electronics shops under the railway tracks',
  'Tiny electronics stalls under the railway tracks, where Akihabara began.', 'Akihabara Radio Center', 35.69848, 139.77166, 'Aimaimyi, CC BY-SA 3.0',
  'https://commons.wikimedia.org/wiki/File:Akihabara_Radio_Center_-00.jpg', 'Radio Center'),
 ('gg', 'GiGO Akihabara 3', 'img/gigo3.jpg', 'The red GiGO Building 3 on Chuo-dori, with anime posters on the front',
  'A big arcade on the main street: crane games, photo booths and a retro game floor.', 'GiGO Akihabara 3', 35.69926, 139.77098, 'BWard 1997, CC BY 4.0',
  'https://commons.wikimedia.org/wiki/File:GiGo_Building_3_-_Akihabara_31-5-2026.jpg', 'GiGO'),
 ('ma', 'mAAch ecute Kanda Manseibashi', 'img/maach.jpg', 'Old red-brick railway arches turned into shops',
  'Old railway arches turned into small shops and cafés.', 'mAAch ecute Kanda Manseibashi', 35.69772, 139.76945, 'Wei-Te Wong, CC BY-SA 2.0',
  'https://commons.wikimedia.org/wiki/File:MAAch_ecute_%E7%A5%9E%E7%94%B0%E8%90%AC%E4%B8%96%E6%A9%8B_(49292011986).jpg', 'mAAch ecute'),
 ('tr', 'Trader Main Store', 'img/trader.jpg', 'The blue and yellow Trader shop front',
  'A big, clean shop where prize figures are cheap. Games and anime DVDs too.', 'Trader Akihabara Main Store', 35.70014, 139.77173, 'Starchild1884, CC BY-SA 3.0',
  'https://commons.wikimedia.org/wiki/File:TRADER_Akihabara.jpg', 'Trader'),
 ('mu', 'Mulan Akiba', 'img/mulan.jpg', 'The red and yellow Mulan shop sign on Chuo-dori',
  'Right next to GiGO. Cheap prize figures, lots of plush toys, and a Chiikawa corner on the 5th floor.', 'Mulan Akiba Chuo-dori Hobby', 35.69928, 139.77111, 'Bject, CC BY-SA 4.0',
  'https://commons.wikimedia.org/wiki/File:AKIHABARA_MULAN_CIMG4219.jpg', 'Mulan'),
 ('am', 'AmiAmi Figure Tower', 'img/figures.jpg', 'Glass cabinets full of anime figures in an Akihabara shop (example photo, not AmiAmi)',
  'A tower of big, detailed figures, often below the list price.', 'AmiAmi Akihabara Figure Tower', 35.69801, 139.77142, 'Piotrus, CC BY-SA 3.0',
  'https://commons.wikimedia.org/wiki/File:Akihabara_August_2014_09.JPG', 'AmiAmi'),
 ('bp', 'BEEP Akihabara', 'img/famicom.jpg', 'Colorful Famicom game cartridges (example photo, not BEEP)',
  'A stylish retro game shop under the railway tracks. Opens at 12:00.', 'BEEP Akihabara', 35.70131, 139.77335, 'Bryan Ochalla, CC BY-SA 2.0',
  'https://commons.wikimedia.org/wiki/File:Famicom_cartridges_(5099356375).jpg', 'BEEP'),
 ('gs', 'Gee!Store Akiba', 'img/onoden.jpg', 'The Onoden building near the station, where Gee!Store is on the 4th floor',
  'The biggest anime clothing shop in Akihabara, on the 4th floor of the Onoden building.', 'Gee Store Akiba Onoden', 35.69830, 139.77085, 'John Seb Barber, CC BY 2.0',
  'https://commons.wikimedia.org/wiki/File:Onoden_%26_LaOX_Duty_Free,_viewed_from_Akihabara_Station_Electric_Town_entrance_south_front_street_(2022-10-18_12.50.45_by_John_Seb_Barber).jpg', 'Gee!Store'),
 ('cp', 'COSPA at atre Akihabara', 'img/atre.jpg', 'The atre Akihabara station building',
  'Anime T-shirts and goods inside the station building (3F). HANDS BE on 2F has fun Japanese stickers.', 'COSPA atre Akihabara', 35.69835, 139.77252, 'ITA-ATU, CC BY-SA 3.0',
  'https://commons.wikimedia.org/wiki/File:Atre_Akihabara.jpg', 'COSPA'),
]
LUNCH_LL = (35.69956, 139.77074)  # Mitsuwa Building (at-home cafe Akihabara Main), OSM
# model routes: name, good for, one line, stops ('L' = maid-cafe lunch)
ROUTES = [
 ('First time in Akihabara', 'First visit to Japan, kids who love collecting toys.',
  'A little of everything: figures, retro games, capsule toys and a shrine.', ['rk', 'sp', 'L', 'gc', 'km']),
 ('Find your favorite', 'Kids with a favorite anime they want goods for.',
  'Straight to the shops for your series: new goods, used finds and capsule toys.', ['an', 'md', 'L', 'gc', 'rk']),
 ('Retro and games', 'Parents who grew up with Nintendo or SEGA, kids who like arcades.',
  'Old electronics alleys, retro games and an arcade.', ['rc', 'sp', 'L', 'gg', 'gc']),
]
HERO = ('img/chuo.jpg', 'Chuo-dori, the main street of Akihabara, with anime billboards',
        'Chuo-dori, the main street of Akihabara.', 'Wikimedia Commons, CC BY 2.0', 'https://commons.wikimedia.org/wiki/File:Akihabara_(53152331538).jpg')

# name, genre, img, alt, credit, credit_url, text, hours, fee, map query, official url
FEE_AH = 'Seat charge: ¥850 per adult, ¥400 for ages 13 to 18, free for ages 12 and under (official site). One drink per person. You stay about an hour, and a longer stay costs nothing extra.'
LUNCH = [
 ('at-home cafe Akihabara Main', 'Maid café · say the magic spell', 'img/athome-main.jpg', 'A blue and red soda drink with a bowl of small fried balls on a cafe table',
  'Vetalapancavimsatika, CC BY-SA 4.0', 'https://commons.wikimedia.org/wiki/File:QQ_Balls_and_Maid_Special_Drink_at_Tukuyomi_Akihabara_20241210.jpg',
  'The fun part: the maids welcome you home, everyone says a short magic spell together to make the food taste better, and omelette rice comes with a picture drawn in ketchup. The best-known maid café in Akihabara, on several floors of one building. Children aged 6 and under get a kids card and a free kids drink.',
  'Monday 11:00 to 22:00', FEE_AH, 'at-home cafe Akihabara Main 1-11-4 Sotokanda Chiyoda', 'https://www.cafe-athome.com/cafes/',
  'Example photo, not this café.'),
 ('maidreamin Akihabara Main Store', 'Maid café · drawings on your food', 'img/maid-cake.jpg', 'A maid café cheesecake',
  'panina.anna, CC BY 2.0', 'https://commons.wikimedia.org/wiki/File:Maid_cafe_-_Welcome_at_home_cheesecake_(2009-04-23_22.54.52_by_panina.anna).jpg',
  'The fun part: magic spells with the maids and drawings on the food and drinks. A big chain that started in Akihabara, on the 6th floor. Its FAQ says families with children are welcome, with table seats recommended. Children up to sixth grade get a free ice cream.',
  'Monday 11:30 to 23:00', 'Seat charge, per hour: ¥880 per adult, ¥550 for junior and senior high school, ¥330 for elementary school, free for younger children (official site). It is charged again for each extra hour.',
  'maidreamin Akihabara Main Store 3-16-17 Sotokanda Chiyoda', 'https://www.maidreamin.com/shop/index.html?id=1',
  'Example photo, not this café.'),
 ('Kanda Tamagoken Akihabara', 'Omelette rice · watch the chef', 'img/omurice.jpg', 'A fluffy omelette on rice with brown demi-glace sauce',
  'Ocdp, CC0', 'https://commons.wikimedia.org/wiki/File:Omurice_001.jpg',
  'The fun part: sit at the counter and watch the chef make a fluffy omelette right in front of you. You can choose how much rice and egg you want and pick your sauce. An omelette-rice (omurice) shop near Suehirocho Station, with an English menu. Only 11 counter seats and no reservations, so we may wait a little.',
  'Open every day 11:00 to 21:00 (last order 20:45)', 'No seat charge. Ordering a meal is the normal way to use the restaurant.', 'Kanda Tamagoken Akihabara 3-14-3 Sotokanda Chiyoda', 'https://www.tamagoken.com/',
  'Example photo, not this restaurant.'),
 ('Gyubei Jyuan Yodobashi Akiba', 'Yakiniku · grill it yourself', 'img/yakiniku.jpg', 'Slices of beef, chicken and pork grilling on a round grill',
  'Benlisquare, CC BY-SA 4.0', 'https://commons.wikimedia.org/wiki/File:Yakiniku_grill_with_slices_of_beef,_chicken_and_pork.jpg',
  'The fun part: you grill the meat yourself on a grill in the middle of the table. A grilled-meat restaurant on the 8th floor of Yodobashi Akiba, by the station. It has sofa-style table seats and kids\' meals, and every kids\' item comes with apple juice.',
  'Monday 11:00 to 23:00', 'No seat charge. Ordering a meal is the normal way to use the restaurant.', 'Yodobashi Akiba 1-1 Kandahanaokacho Chiyoda', 'https://gyubei-jyuan-akiba.com/',
  'Example photo, not this restaurant.'),
 ('Tonkatsu Wako Yodobashi Akiba', 'Tonkatsu · free refills', 'img/tonkatsu.jpg', 'A breaded pork cutlet set with rice, soup and salad',
  'Ocdp, CC0', 'https://commons.wikimedia.org/wiki/File:Tonkatsu_003.jpg',
  'The fun part: at this chain, rice, cabbage and miso soup are free refills, so hungry kids can eat as much as they like. A tonkatsu (breaded pork cutlet) chain on the restaurant floor of Yodobashi Akiba, with 48 non-smoking seats. The menu has a kids\' tonkatsu set and kids\' curry.',
  'Monday 11:00 to 23:00 (last order 22:00)', 'No seat charge. Ordering a meal is the normal way to use the restaurant.', 'Yodobashi Akiba 1-1 Kandahanaokacho Chiyoda', 'https://www.yodobashi-akiba.com/restaurant/yy_wako.html',
  'Example photo, not this restaurant.'),
 ('Shinsouen Akihabara', 'Chinese · share big dishes', 'img/chinese.jpg', 'Mapo tofu in a large white bowl',
  'Richard923888, CC BY-SA 4.0', 'https://commons.wikimedia.org/wiki/File:Mapo_tofu_in_big_bowl.jpg',
  'The fun part: order several big dishes and share them around the table. A Chinese restaurant on the 5th floor of AkibaTrim, with 50 seats. Children\'s chairs are available, and you can reserve on its website.',
  'Monday lunch 11:00 to 15:00 (last order 14:30)', 'No seat charge. Ordering a meal is the normal way to use the restaurant.', 'Shinsouen Akihabara AkibaTrim 1-6-5 Kandasakumacho Chiyoda', 'https://shinsouen.jp/akihabara/information/index.html',
  'Example photo, not this restaurant.'),
 ('Sushiro Akihabara Ekimae', 'Sushi · order on a touch screen', 'img/sushi.jpg', 'A single piece of prawn sushi on a dark counter',
  'Zheng Zhou, CC BY-SA 4.0', 'https://commons.wikimedia.org/wiki/File:Kurumaebi_(Japanese_tiger_prawn)_Nigiri.jpg',
  'The fun part: order on a touch screen and the sushi comes to your seat on the belt. The Akihabara Station Front branch of a big sushi chain. The store has an elevator and a diaper-changing station.',
  'Monday 11:00 to 23:00', 'No seat charge. Ordering a meal is the normal way to use the restaurant.', 'Sushiro Akihabara Ekimae 1-18-19 Sotokanda Chiyoda', 'https://www.akindo-sushiro.co.jp/shop/detail.php?id=2143&keyword=',
  'Example photo, not this restaurant.'),
]
POPS = []
def lunch_card(i, l):
    name, genre, img, alt, cr, cu, text, hours, fee, q, url, note = l
    pid = f'pop{i}'
    POPS.append(f'<dialog class="pop" id="{pid}" aria-label="{H(name)}"><button type="button" class="pclose" aria-label="Close">✕</button>'
                f'<img class="pimg" src="{img}" alt="{H(alt)}"><div class="pbody"><p class="gn">{H(genre)}</p><h3>{H(name)}</h3>'
                f'<p class="pt">{H(text)}</p><p class="rt">{H(hours)}<br>{H(fee)}</p>'
                f'<p class="pl"><a href="{gm(q)}" target="_blank" rel="noopener">Map ↗</a><a href="{url}" target="_blank" rel="noopener">Official site ↗</a></p>'
                f'<p class="pc">{H(note)} Photo: <a href="{cu}" target="_blank" rel="noopener">{H(cr)}</a>.</p></div></dialog>')
    return (f'<button type="button" class="tile" data-pop="{pid}"><img src="{img}" alt="{H(alt)}" loading="lazy">'
            f'<span class="cb"><span class="gn">{H(genre)}</span><b>{H(name)}</b></span></button>')
lunch_html = ('<section class="plan" id="lunch"><div class="wrap"><h2 class="sh2">Lunch ideas</h2>'
              '<p class="llead">Lunch is at a maid café or a regular restaurant. No need to choose now. We\'ll pick on the day, depending on how everyone feels. We picked these for the fun of it, not just the food: each one has something to do or watch. Here are seven places we might go. Tap a tile for details.</p>'
              '<div class="tiles">' + ''.join(lunch_card(i, l) for i, l in enumerate(LUNCH)) + '</div>'
              '<p class="asof">Hours are from each place\'s official site, checked October 19, 2026. Please confirm with TOKI before the day.</p></div></section>')
popjs = ("<script>document.querySelectorAll('.tile').forEach(function(t){t.addEventListener('click',function(){document.getElementById(t.dataset.pop).showModal()})});"
         "document.querySelectorAll('dialog.pop').forEach(function(d){d.addEventListener('click',function(e){if(e.target===d)d.close()});d.querySelector('.pclose').addEventListener('click',function(){d.close()})});</script>")

JSRAW = r'''
(function(){
var P=__P__;
var LUN=__LUN__;
var R=__R__;
if(!window.L){return}
var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var map=L.map('map',{scrollWheelZoom:false});
var base=L.maplibreGL({style:'https://tiles.openfreemap.org/styles/positron',attribution:'<a href="https://openfreemap.org" target="_blank" rel="noopener">OpenFreeMap</a> &copy; <a href="https://www.openmaptiles.org/" target="_blank" rel="noopener">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> contributors'}).addTo(map);
function english(){var gl=base.getMaplibreMap();gl.getStyle().layers.forEach(function(l){if(l.type!=='symbol'){return}
 if(/shield/.test(l.id)){gl.setLayoutProperty(l.id,'visibility','none');return}
 if(l.layout&&l.layout['text-field']){gl.setLayoutProperty(l.id,'text-field',['coalesce',['get','name:en'],['get','name_en'],['get','name:latin']])}})}

var all=P.map(function(p){return p.ll});
map.fitBounds(all,{padding:[36,36]});
var gl=base.getMaplibreMap();
if(gl){var enDone=false;var tryEn=function(){if(enDone||!(gl.style&&gl.style._loaded)){return}enDone=true;english()};gl.on('style.load',tryEn);gl.on('styledata',tryEn);tryEn()}
var rows=document.querySelectorAll('.plist li');
var cards=document.querySelectorAll('.rcard');
var bar=document.getElementById('rbar');
var byId={};
P.forEach(function(p,i){byId[p.id]=i});
var mk=P.map(function(p,i){
 var m=L.marker(p.ll,{icon:L.divIcon({className:'pin',html:'<i>'+(i+1)+'</i>',iconSize:[28,28]}),title:p.n}).addTo(map);
 m.on('click',function(){rows[i].scrollIntoView({behavior:reduce?'auto':'smooth',block:'center'})});
 return m});
var rg=L.layerGroup().addTo(map);
var route=-1,cur=-1;
function go(i){
 if(route>=0||i===cur){return}
 cur=i;
 rows.forEach(function(r,j){r.classList.toggle('on',j===i)});
 mk.forEach(function(m,j){var e=m.getElement();if(e){e.classList.toggle('on',j===i)}});
 if(reduce){map.setView(P[i].ll,17)}else{map.flyTo(P[i].ll,17,{duration:.6})}
}
function setRoute(r){
 route=r;cur=-1;
 rg.clearLayers();
 cards.forEach(function(c,j){c.classList.toggle('on',j===r);c.setAttribute('aria-pressed',j===r?'true':'false')});
 document.body.classList.toggle('hasroute',r>=0);
 rows.forEach(function(row){row.classList.remove('inr');row.classList.remove('on');row.querySelector('.no').textContent=+row.dataset.i+1});
 bar.hidden=r<0;
 if(r<0){
  mk.forEach(function(m){m.addTo(map)});
  map.fitBounds(all,{padding:[36,36]});
  return}
 mk.forEach(function(m){map.removeLayer(m)});
 var pts=[];
 R[r].s.forEach(function(id,k){
  var lunch=id==='L';
  var ll=lunch?LUN.ll:P[byId[id]].ll;
  pts.push(ll);
  L.marker(ll,{icon:L.divIcon({className:'npin'+(lunch?' lunch':''),html:'<i>'+(k+1)+'</i>',iconSize:[26,26]}),title:lunch?'Lunch at a maid caf\u00e9':P[byId[id]].n}).addTo(rg);
  if(!lunch){var row=rows[byId[id]];row.classList.add('inr');row.querySelector('.no').textContent=k+1}
 });
 L.polyline(pts,{color:'#e60012',weight:3,opacity:.5,dashArray:'7 7'}).addTo(rg);
 map.fitBounds(pts,{padding:[36,36]});
 document.getElementById('rname').textContent=R[r].n;
}
cards.forEach(function(c,j){c.addEventListener('click',function(){
 var again=(route===j);
 setRoute(again?-1:j);
 if(!again){document.getElementById('places').scrollIntoView({behavior:reduce?'auto':'smooth'})}
})});
document.getElementById('rreset').addEventListener('click',function(){setRoute(-1)});
if(window.matchMedia('(min-width:760px) and (hover:hover)').matches){
 rows.forEach(function(r){var i=+r.dataset.i;r.addEventListener('mouseenter',function(){go(i)});r.addEventListener('focusin',function(){go(i)})});
 document.querySelector('.plist').addEventListener('mouseleave',function(){
  if(route>=0){return}
  cur=-1;rows.forEach(function(r){r.classList.remove('on')});
  mk.forEach(function(m){var e=m.getElement();if(e){e.classList.remove('on')}});
  map.flyToBounds(all,{padding:[36,36],duration:reduce?0:.6});
 });
}else if('IntersectionObserver' in window){
 var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){go(+e.target.dataset.i)}})},{rootMargin:'-45% 0px -45% 0px'});
 rows.forEach(function(r){io.observe(r)});
}
})();
'''

css = open('css.txt').read() + '''
.llead{margin:12px 0 18px;font-size:16.5px;max-width:560px}
.tiles{display:grid;grid-template-columns:1fr 1fr;gap:12px;align-items:stretch}
@media(min-width:760px){.tiles{grid-template-columns:repeat(4,1fr);gap:16px}}
.tile{display:flex;flex-direction:column;justify-content:flex-start;width:100%;text-align:left;font:inherit;color:inherit;background:#fff;border:1px solid var(--line);overflow:hidden;padding:0;cursor:pointer}
.tile img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover;background:var(--seg)}
.tile .cb{display:block;padding:10px 12px 14px}
.tile .gn{display:block;font-size:11px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--red)}
.tile b{display:block;font-size:16px;line-height:1.25;margin-top:3px}
.tile:hover,.tile:focus-visible{border-color:var(--ink)}
.asof{margin:16px 0 0;font-size:13px;color:var(--mute)}
dialog.pop{border:0;padding:0;width:min(92vw,440px);max-height:88vh;max-height:88svh;overflow:auto;color:var(--ink);background:var(--paper);margin:auto}
dialog.pop::backdrop{background:rgba(0,0,0,.55)}
.pop .pimg{display:block;width:100%;aspect-ratio:4/3;object-fit:cover}
.pop .pbody{padding:16px 18px 20px}
.pop .gn{margin:0;font-size:11px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--red)}
.pop h3{font-size:24px;font-stretch:75%;line-height:1.1;font-weight:800;margin:3px 0 8px}
.pop .pt{font-size:15.5px;line-height:1.55;margin:10px 0 0}
.pop .rt{font-size:13.5px;line-height:1.55;color:var(--mute);margin:10px 0 0}
.pop .pl{margin:14px 0 0;display:flex;gap:10px;flex-wrap:wrap}
.pop .pl a{display:inline-block;font-size:13px;font-weight:700;text-decoration:none;border:1px solid var(--ink);padding:6px 14px}
.pop .pc{margin:14px 0 0;font-size:11.5px;color:var(--mute);line-height:1.5}.pop .pc a{text-underline-offset:2px}
.pclose{position:absolute;right:10px;top:10px;width:34px;height:34px;border-radius:50%;border:0;background:rgba(255,255,255,.92);font:inherit;font-size:16px;font-weight:700;cursor:pointer;box-shadow:0 1px 4px rgba(0,0,0,.25)}

.places-g{display:grid;grid-template-columns:1fr;gap:14px}
.pmap{position:sticky;top:41px;z-index:6;height:clamp(190px,32vh,280px);border:1px solid var(--ink);background:var(--seg)}
#map{width:100%;height:100%}
.leaflet-tile-pane{filter:sepia(.35) saturate(.75) contrast(.95) brightness(1.02)}
.plist{border-top:2px solid var(--ink);margin:0;padding:0;list-style:none}
.plist li{display:grid;grid-template-columns:104px minmax(0,1fr);gap:14px;align-items:center;padding:14px 8px;border-bottom:1px solid var(--line);transition:background .3s}
.plist li.on{background:var(--seg)}
.plist img{width:104px;aspect-ratio:4/3;object-fit:cover;display:block}
.plist strong{display:block;font-size:17px;line-height:1.25}
.plist .cat{display:block;font-size:11px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--red);margin:0 0 2px}
.plist span{display:block;color:var(--mute);font-size:15px;margin-top:2px}
.plist a{display:inline-block;margin-top:5px;font-size:14px;text-underline-offset:3px}
.pin i{display:block;width:24px;height:24px;margin:2px;border-radius:50%;background:var(--red);color:#fff;border:2px solid #fff;box-shadow:0 0 0 1px var(--ink);font-style:normal;font-weight:800;font-size:12px;line-height:20px;text-align:center;transition:transform .25s}
.pin.on i{transform:scale(1.35);background:var(--ink);box-shadow:0 0 0 3px var(--red)}
.pfoot{margin:14px 0 0;font-size:14px;color:var(--mute)}
.rcards{display:grid;grid-template-columns:1fr;gap:14px;margin-top:18px}
.rcard{display:flex;flex-direction:column;justify-content:flex-start;width:100%;text-align:left;font:inherit;color:inherit;background:#fff;border:1px solid var(--line);padding:16px 16px 14px;cursor:pointer;position:relative}
.rcard:hover,.rcard:focus-visible{border-color:var(--ink)}
.rcard.on{border-color:var(--red);box-shadow:inset 0 0 0 2px var(--red)}
.rcard b{display:block;font-size:22px;font-stretch:75%;line-height:1.1;font-weight:800}
.rcard .good{display:block;margin-top:8px;font-size:14.5px;line-height:1.45}
.rcard .good strong{color:var(--red)}
.rcard .one{display:block;margin-top:6px;font-size:14px;color:var(--mute);line-height:1.45}
.chips{display:flex;gap:6px;margin-top:auto;padding-top:12px}
.chip{display:block;flex:1 1 0;min-width:0}
.chip img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover;background:var(--seg)}
.chip i{display:block;font-style:normal;font-size:10.5px;line-height:1.2;margin-top:3px;color:var(--mute);overflow-wrap:anywhere}
.chip.lunch img{outline:2px solid var(--red);outline-offset:-2px}
.chip.lunch i{color:var(--red);font-weight:800}
.rnote{margin:14px 0 0;font-size:15px;color:var(--mute)}
.rbar{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin:0 0 12px;font-size:15px}
.rbar[hidden]{display:none}
.rbar button{font:inherit;font-size:13px;font-weight:700;background:var(--ink);color:var(--paper);border:0;padding:7px 14px;cursor:pointer}
.plist li{position:relative}
.plist .no{display:block;position:absolute;left:0;top:10px;width:24px;height:24px;border-radius:50%;background:var(--red);color:#fff;font-size:13px;font-weight:800;text-align:center;line-height:24px;z-index:2}
.hasroute .plist li:not(.inr){opacity:.45}
.hasroute .plist li.inr .no{display:block}
.hasroute .plist li:not(.inr) .no{display:none}
.npin i{display:block;width:26px;height:26px;border-radius:50%;background:var(--red);color:#fff;border:2px solid #fff;box-shadow:0 0 0 1px var(--ink);font-style:normal;font-weight:800;font-size:13px;line-height:22px;text-align:center}
.npin.lunch i{background:var(--ink)}
@media(min-width:760px){.rcards{grid-template-columns:repeat(3,1fr);gap:18px}.chip i{font-size:11px}}
@media(min-width:760px){
.places-g{grid-template-columns:1fr;gap:28px}
.pmap{position:relative;top:auto;height:380px}
.plist{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0 24px;border-top:0}
.plist li{grid-template-columns:96px minmax(0,1fr);gap:12px;align-items:start;padding:14px 0;border-bottom:0;border-top:1px solid var(--line)}
.plist li.on{background:none}.plist li.on img{outline:3px solid var(--red);outline-offset:-3px}
.plist img{width:96px}
.plist strong{font-size:15px}
.plist span{font-size:13.5px;line-height:1.45;margin-top:3px}
.plist a{font-size:13px;margin-top:4px}
.plist .no{left:-6px;top:8px}
}
@media(prefers-reduced-motion:reduce){.plist li,.pin i{transition:none}}
'''
facts = ''.join(f'<div><dt>{H(k)}</dt><dd>{H(v)}</dd></div>' for k, v in FACTS)
CAT = {'rk': 'Shopping', 'md': 'Shopping', 'an': 'Shopping', 'tr': 'Shopping', 'mu': 'Shopping', 'am': 'Shopping',
       'sp': 'Retro games', 'bp': 'Retro games', 'gg': 'Arcade', 'gc': 'Capsule toys', 'km': 'Shrine',
       'gs': 'Anime fashion', 'cp': 'Anime fashion', 'rc': 'Old Akihabara', 'ma': 'Old Akihabara'}
rows = ''.join(f'<li data-i="{i}"><span class="no">{i+1}</span><img src="{im}" alt="{H(alt)}" loading="lazy"><div><span class="cat">{CAT[k]}</span><strong>{H(n)}</strong><span>{H(t)}</span>'
               f'<a href="{gm(q)}" target="_blank" rel="noopener">Google Maps ↗</a></div></li>'
               for i, (k, n, im, alt, t, q, la, lo, cr, cu, sh) in enumerate(PLACES))
PJS = '[' + ','.join("{'id':'%s','n':'%s','ll':[%s,%s]}" % (k, n, la, lo) for k, n, im, alt, t, q, la, lo, cr, cu, sh in PLACES) + ']'
RJS = '[' + ','.join("{'n':'%s','s':%s}" % (n, str(st)) for n, g, o, st in ROUTES) + ']'
JS = JSRAW.replace('__P__', PJS).replace('__R__', RJS).replace('__LUN__', "{'ll':[%s,%s]}" % LUNCH_LL).replace('LUN.ll', 'LUN.ll')
PL = {p[0]: p for p in PLACES}
def chip(k):
    if k == 'L':
        return f'<span class="chip lunch"><img src="{LUNCH[0][2]}" alt="" loading="lazy"><i>Lunch</i></span>'
    p = PL[k]
    return f'<span class="chip"><img src="{p[2]}" alt="" loading="lazy"><i>{H(p[10])}</i></span>'
cards = ''.join(f'<button type="button" class="rcard" aria-pressed="false"><b>{H(n)}</b><span class="good"><strong>Good for:</strong> {H(g)}</span>'
                f'<span class="one">{H(o)}</span><span class="chips">{"".join(chip(k) for k in st)}</span></button>' for n, g, o, st in ROUTES)
credits = '; '.join(f'{H(p[1])}: <a href="{p[9]}" target="_blank" rel="noopener">{H(p[8])}</a>' for p in PLACES) \
    + ''.join(f'; {H(l[0])}: <a href="{l[5]}" target="_blank" rel="noopener">{H(l[4])}</a>' for l in LUNCH) \
    + f'; Chuo-dori: <a href="{HERO[4]}" target="_blank" rel="noopener">{H(HERO[3])}</a>'
fav = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%23e60012'/%3E%3Ctext x='16' y='23' font-size='20' font-weight='800' text-anchor='middle' fill='white' font-family='Arial'%3EA%3C/text%3E%3C/svg%3E"

routes_html = f'''<section class="plan" id="routes"><div class="wrap"><h2 class="sh2">Three example routes</h2>
<p class="llead">Tap a route to see it on the map. Each one includes lunch.</p>
<div class="rcards">{cards}</div>
<p class="rnote">These are examples. We can mix them, and the day adapts to what the family enjoys.</p></div></section>'''
places_html = f'''<section class="plan" id="places"><div class="wrap"><h2 class="sh2">Places we may visit</h2>
<p class="llead">Examples of the kind of places we'll stop at. The actual route is decided on the day, around what the family enjoys.</p>
<div class="rbar" id="rbar" hidden><span>Showing: <strong id="rname"></strong></span><button type="button" id="rreset">Show all places</button></div>
<div class="places-g"><div class="pmap"><div id="map" role="img" aria-label="Map of the example places"></div></div><ol class="plist">{rows}</ol></div></div></section>'''
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{H(TITLE)}</title><meta name="robots" content="noindex"><meta name="description" content="{H(LEAD)}">
<meta name="theme-color" content="#f4f1ea"><link rel="icon" href="{fav}">
<meta property="og:title" content="{H(TITLE)}"><meta property="og:description" content="{H(LEAD)}">
<meta property="og:type" content="website"><meta property="og:url" content="{BASE}">
<meta property="og:image" content="{BASE}img/chuo.jpg"><meta property="og:image:width" content="960"><meta property="og:image:height" content="640">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<style>{css}</style></head><body>
<nav class="nav"><div class="wrap"><a href="#routes">Routes</a><a href="#places">Places</a><a href="#lunch">Lunch</a></div></nav>
<header class="wrap hero">
<dl class="facts">{facts}</dl>
<h1 class="mega">Akihabara</h1>
<figure class="heroimg"><img src="{HERO[0]}" alt="{H(HERO[1])}"><figcaption>{H(HERO[2])} Photo: <a href="{HERO[4]}" target="_blank" rel="noopener">{H(HERO[3])}</a>.</figcaption></figure>
<div class="pick"><h2>Tokyo · Monday, October 26</h2><p>{H(LEAD)}</p></div>
</header>
<main>
{routes_html}
{places_html}
{lunch_html}
</main>
<footer><div class="wrap"><p>{H(FOOT)}</p>
<details class="cred"><summary>Photo credits</summary><p>{credits}. Photos via Wikimedia Commons.</p></details></div></footer>
{''.join(POPS)}{popjs}
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<link rel="stylesheet" href="https://unpkg.com/maplibre-gl@4.7.1/dist/maplibre-gl.css">
<script src="https://unpkg.com/maplibre-gl@4.7.1/dist/maplibre-gl.js"></script>
<script src="https://unpkg.com/@maplibre/maplibre-gl-leaflet@0.0.22/leaflet-maplibre-gl.js"></script>
<script>{JS}</script>
</body></html>'''
open('index.html', 'w').write(page)
print('written', len(page))

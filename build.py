import json,base64,io,urllib.request,html
from PIL import Image
S="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/"
G=[
("steam","Hexcells Infinite","Matthew Brown","解謎",S+"304410/header.jpg","六角格版踩地雷，全靠推理、不用猜。","2,567 則評論・97% 好評","NT$102（原價）","無繁中","https://store.steampowered.com/app/304410/","玩過踩地雷就能上手；幾乎不用讀字。"),
("steam","Cobalt Core","Rocket Rat Games","Roguelike",S+"2179850/header.jpg","太空船閃避＋卡牌戰鬥，角色互動很有梗。","3,449 則評論・96% 好評","NT$164（特價 5 折）","有繁中","https://store.steampowered.com/app/2179850/","特價中可先入；後期重複性稍高。"),
("steam","Roadwarden","Moral Anxiety Studio","敘事",S+"1155970/header.jpg","文字為主的奇幻冒險，選擇都有後果。","3,879 則評論・94% 好評","NT$208（原價）","無繁中","https://store.steampowered.com/app/1155970/","雷點：英文量很大。"),
("steam","ISLANDERS","Coatsink 等","策略",S+"1046030/1bc0f29a0f3e4cdfd7a0d209ca0264228e39ee98/header.jpg","放建築拼分數，一局約 30 分鐘的放鬆策略。","10,228 則評論・95% 好評","NT$118（原價）","無繁中","https://store.steampowered.com/app/1046030/","幾乎不用讀字；深度有限。"),
("steam","Tiny Glade","Pounce Light","模擬",S+"2198150/b3a0326cc6d63ca88973fdee61d09052433abf94/header_alt_assets_0.jpg","隨手拉線長出童話城堡，零壓力。","14,039 則評論・97% 好評","NT$268（原價）","無繁中","https://store.steampowered.com/app/2198150/","沒有目標，要有「純蓋好玩」的心態。"),
("steam","Pentiment","Obsidian Entertainment","敘事",S+"1205520/header.jpg","16 世紀修道院謀殺案，手抄本畫風。","5,280 則評論・94% 好評","NT$538（原價）","無繁中","https://store.steampowered.com/app/1205520/","節奏慢、字多，英文門檻高。"),
("itch","A Short Hike","adamgryu","冒險","https://img.itch.zone/aW1nLzIyNDgzNjgucG5n/original/LlCi9O.png","小島爬山散步，療癒又短。","itch 4.9★・4,399 人評分","US$7.99","繁中未確認","https://adamgryu.itch.io/a-short-hike","週末一下午的小品。"),
("itch","Celeste Classic","Maddy Makes Games","動作","https://img.itch.zone/aW1hZ2UvMzEzMTgvMTMzNjQyLmdpZg==/original/vIUIrE.gif","Celeste 原型，PICO-8 硬核平台跳躍。","itch 4.7★・1,003 人評分","免費","繁中未確認","https://maddymakesgamesinc.itch.io/celesteclassic","用來測你吃不吃高難度操作。"),
("itch","We Become What We Behold","Nicky Case","敘事","https://img.itch.zone/aW1hZ2UvOTIxMTUvNDU0MDMxLnBuZw==/original/qEmwk6.png","幾分鐘看懂媒體如何製造衝突的諷刺小品。","itch 4.8★・8,946 人評分","免費","繁中未確認","https://ncase.itch.io/wbwwb","很短，偏體驗。"),
]
def thumb(u):
  r=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=30).read()
  im=Image.open(io.BytesIO(r)).convert("RGB");im.thumbnail((480,480));b=io.BytesIO();im.save(b,"JPEG",quality=80)
  return "data:image/jpeg;base64,"+base64.b64encode(b.getvalue()).decode()
e=html.escape;cards=""
for i,g in enumerate(G,1):
  p,n,d,t,img,s,rv,pr,zh,l,tip=g
  cards+=f'''<div class="c" data-tags="#{p} #{t}" data-id="{i}"><a href="{l}" target="_blank" rel="noopener"><img src="{thumb(img)}" alt="{e(n)}"></a><div class="b"><h3>{i}. <a href="{l}" target="_blank" rel="noopener">{e(n)}</a></h3><div class="m">{"Steam" if p=="steam" else "itch.io"}・{t}・{e(d)}</div><p>{e(s)}</p><div class="m">{e(rv)}｜{e(pr)}｜{zh}</div><p class="tip">💡 {e(tip)}</p><label><input type="checkbox" class="ni"> 不感興趣</label></div></div>'''
btn=lambda xs:"".join(f'<button data-k="{k}"{" class=on" if k=="" else ""}>{n}</button>' for n,k in xs)
r1=btn([("全部",""),("Steam","#steam"),("itch.io","#itch")]);r2=btn([("全部",""),("解謎","#解謎"),("Roguelike","#Roguelike"),("敘事","#敘事"),("策略","#策略"),("模擬","#模擬"),("動作","#動作"),("冒險","#冒險")])
open("index.html","w").write(f'''<!doctype html><html lang="zh-Hant-TW"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>冷門好遊戲雷達</title><style>
body{{background:#14161a;color:#e6e6e6;font-family:system-ui,"Noto Sans TC",sans-serif;margin:0;padding:20px}}h1{{margin:0}}.sub{{color:#9aa}}input[type=search]{{padding:8px;width:260px;background:#22252b;color:#eee;border:1px solid #444;border-radius:6px}}
.row{{margin:8px 0}}button{{background:#22252b;color:#ccc;border:1px solid #444;border-radius:16px;padding:5px 12px;margin:2px;cursor:pointer}}button.on{{background:#3d6fd8;color:#fff}}
.g{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px;margin-top:12px}}.c{{background:#1e2127;border-radius:10px;overflow:hidden}}.c.x{{opacity:.4}}.c img{{width:100%;aspect-ratio:460/215;object-fit:cover;display:block}}.b{{padding:10px 12px}}h3{{margin:0 0 4px;font-size:1.05em}}h3 a{{color:#fff;text-decoration:none}}.m{{color:#9ab;font-size:.85em}}p{{margin:6px 0;font-size:.92em}}.tip{{color:#cba}}#none{{display:none;color:#999;margin:20px}}#out{{width:100%;max-width:500px;background:#22252b;color:#eee}}</style></head><body>
<h1>冷門好遊戲雷達</h1><div class="sub">共 {len(G)} 款・更新 2026-10-28・Steam 好評率/評論數取自商店頁（可能僅英文評論），itch 為頁面星等；遊玩時數未確認</div>
<div class="row"><input type="search" id="q" placeholder="搜尋名稱、類型、開發商…"> <button id="clr">清除</button> <span id="cnt"></span></div>
<div class="row" id="r1">{r1}</div><div class="row" id="r2">{r2}</div>
<div class="row"><button id="exp">匯出「不感興趣」編號</button> <textarea id="out" rows="2" readonly></textarea></div>
<div class="g" id="g">{cards}</div><div id="none">找不到符合的項目</div>
<script>
const K='radar-ni',st=new Set(JSON.parse(localStorage.getItem(K)||'[]')),cs=[...document.querySelectorAll('.c')];
cs.forEach(c=>{{const b=c.querySelector('.ni');b.checked=st.has(c.dataset.id);c.classList.toggle('x',b.checked);b.onchange=()=>{{b.checked?st.add(c.dataset.id):st.delete(c.dataset.id);localStorage.setItem(K,JSON.stringify([...st]));c.classList.toggle('x',b.checked)}}}});
const f={{r1:'',r2:''}};['r1','r2'].forEach(r=>document.querySelectorAll('#'+r+' button').forEach(b=>b.onclick=()=>{{document.querySelectorAll('#'+r+' button').forEach(x=>x.classList.remove('on'));b.classList.add('on');f[r]=b.dataset.k;go()}}));
function go(){{const q=document.getElementById('q').value.toLowerCase();let n=0;cs.forEach(c=>{{const t=c.dataset.tags,ok=(!f.r1||new RegExp(f.r1).test(t))&&(!f.r2||new RegExp(f.r2).test(t))&&(c.textContent+t).toLowerCase().includes(q);c.style.display=ok?'':'none';n+=ok}});document.getElementById('cnt').textContent='顯示 '+n+' 款';document.getElementById('none').style.display=n?'none':'block'}}
document.getElementById('q').oninput=go;document.getElementById('clr').onclick=()=>{{document.getElementById('q').value='';go()}};
document.getElementById('exp').onclick=()=>{{const o=document.getElementById('out');o.value=[...st].sort((a,b)=>a-b).length?'不感興趣：'+[...st].sort((a,b)=>a-b).join(', '):'（尚未勾選）';o.select();navigator.clipboard&&navigator.clipboard.writeText(o.value).catch(()=>{{}})}};go();
</script></body></html>''')

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
S2=S
G2=[
("steam","PICO PARK","TECOPARK","解謎",S+"1509960/header.jpg","2–8 人合作過關，必須互相疊羅漢才能開門。","9,519 則評論・92% 好評","NT$102（原價）","無繁中","https://store.steampowered.com/app/1509960/","人越多越歡樂；單人無法遊玩。","本地合作・線上合作","主線約 3 小時（HLTB，經第三方轉載）"),
("steam","Unrailed!","Indoor Astronaut","動作",S+"1016920/header.jpg","邊砍樹挖礦邊幫火車鋪軌，手忙腳亂的合作派對。","4,685 則評論・94% 好評","NT$400（原價）","有繁中","https://store.steampowered.com/app/1016920/","有線上配對；吵架風險高。","本地合作・線上合作・本地對戰・線上對戰","主線約 6.5 小時（HLTB，經第三方轉載）"),
("steam","Lovers in a Dangerous Spacetime","Asteroid Base","動作",S+"252110/header.jpg","一起操縱一艘霓虹太空船的砲台、護盾和引擎。","1,881 則評論・93% 好評","NT$398（原價）","有繁中","https://store.steampowered.com/app/252110/","最適合兩人沙發同樂；Steam 只標本地合作。","本地合作","主線約 5.6 小時（HLTB）"),
("steam","Lethal League Blaze","Team Reptile","動作",S+"553310/header.jpg","越打越快的街頭棒球格鬥對戰。","4,050 則評論・97% 好評","NT$318（原價）","有繁中","https://store.steampowered.com/app/553310/","上手容易、精通難；以對戰為主。","本地對戰・線上對戰","未確認"),
("steam","Boomerang Fu","Cranky Watermelon","動作",S+"965680/header.jpg","可愛食物拿迴力鏢互砍，一擊必殺的派對遊戲。","1,830 則評論・97% 好評","NT$308（原價）","有繁中","https://store.steampowered.com/app/965680/","Steam 未標線上，要線上可用 Remote Play（未確認）。","本地合作・本地對戰","未確認"),
("steam","Keep Talking and Nobody Explodes","Steel Crate Games","解謎",S+"341800/header.jpg","一人拆炸彈、其他人看手冊，全靠嘴巴溝通。","8,142 則評論・98% 好評","NT$268（原價）","有繁中","https://store.steampowered.com/app/341800/","同一個房間玩最好；手冊可免費印。","本地合作","主線約 5 小時（HLTB，經第三方轉載）"),
("steam","PlateUp!（速速上菜！）","It's happening","模擬",S+"1599600/ca2449fda2ccb4e2bb81a3f027f76b6fba04b7fb/header_alt_assets_19.jpg","Roguelite 餐廳經營，越開越大越崩潰。","12,660 則評論・96% 好評","NT$328（原價）","有繁中","https://store.steampowered.com/app/1599600/","單人也能玩，但多人才是精華。","本地合作・線上合作","主線約 15 小時（HLTB，經第三方轉載）"),
("steam","Baba Is You","Hempuli Oy","解謎",S+"736260/header.jpg","推動文字方塊改寫規則，「牆是你」也能成立。","12,719 則評論・97% 好評","NT$268（原價）","有繁中","https://store.steampowered.com/app/736260/","後期非常燒腦，卡關正常。","僅單人","主線約 7.5 小時（HLTB，經第三方轉載）"),
("itch","A Tavern for Tea","npckc","敘事","https://img.itch.zone/aW1nLzExNDQ0MzI0LmdpZg==/original/f5EOOa.gif","在奇幻酒館泡茶聽客人心事的小品視覺小說。","itch 4.7★・513 人評分","US$1.49","有繁中","https://npckc.itch.io/a-tavern-for-tea","約一小時，適合睡前。","未確認","約 1 小時（HLTB，經第三方轉載）"),
("itch","Celeste Classic 2: Lani's Trek","Maddy Makes Games","動作","https://img.itch.zone/aW1nLzUwNTA4NDAucG5n/original/5KxkXW.png","Celeste 團隊的 PICO-8 續作，加入抓鉤。","itch 4.7★・595 人評分","未確認","繁中未確認","https://maddymakesgamesinc.itch.io/celeste-classic-2","比第一代溫和一些。","未確認","主線約 0.6 小時（HLTB）"),
]
G3=[
("steam","Ultimate Chicken Horse（超級雞馬）","Clever Endeavour Games","動作",S+"386940/header.jpg","每回合輪流替關卡放陷阱，再一起闖，既坑人又被坑。","14,845 則評論・96% 好評","NT$299（原價）","有繁中","https://store.steampowered.com/app/386940/","規則一局就懂；單人能玩但多人才有趣，支援跨平台。","本地合作・線上合作・本地對戰・線上對戰","未確認"),
("steam","Bopl Battle","Johan Grönvall","動作",S+"1686940/header.jpg","黏液小球自選三種技能互轟，招式組合很多。","17,338 則評論・97% 好評","NT$188（原價）","有繁中","https://store.steampowered.com/app/1686940/","先在練習場試技能組合；線上大廳人數未確認。","本地合作・線上合作・本地對戰・線上對戰","未確認"),
("steam","BattleBlock Theater","The Behemoth","動作",S+"238460/header.jpg","《城堡毀滅者》團隊的雙人合作平台關卡，旁白超吵超好笑。","23,686 則評論・97% 好評","NT$268（原價）","有繁中","https://store.steampowered.com/app/238460/","兩人合作模式最精華；隊友可以把你丟下懸崖。","本地合作・線上合作・本地對戰・線上對戰","未確認"),
("steam","Duck Game","Landon Podbielski","動作",S+"312530/header.jpg","持槍鴨子一擊必殺的快節奏亂鬥，一回合只有幾秒。","11,094 則評論・97% 好評","NT$238（原價）","無繁中","https://store.steampowered.com/app/312530/","純對戰，沒有合作模式；新手會被秒很多次。","本地對戰・線上對戰","未確認"),
("steam","Dome Keeper（穹頂守護者）","Bippinbits","策略",S+"1637320/2a1d143606c3077209136f1bfe088336a094d16e/header_tchinese.jpg","往地底挖礦升級，時間到要趕回去守住穹頂。","11,890 則評論・93% 好評","NT$298（原價）","有繁中","https://store.steampowered.com/app/1637320/","Roguelite，前幾局多半會輸；多人是後來更新加入的。","本地合作・線上合作・本地對戰・線上對戰","未確認"),
("steam","Pikuniku","Sectordub 等","冒險",S+"572890/header.jpg","紅色豆子腿長長的荒謬小冒險，還有獨立的雙人合作關。","4,119 則評論・95% 好評","NT$238（原價）","有繁中","https://store.steampowered.com/app/572890/","主線單人；雙人合作是另外的關卡，Steam 只標本地。","本地合作・本地對戰","未確認"),
("steam","Heave Ho","Le Cartel Studio","動作",S+"905340/header.jpg","只有兩隻手的小人互相抓著盪過深淵，手放開就掉。","1,095 則評論・91% 好評","NT$188（原價）","有繁中","https://store.steampowered.com/app/905340/","Steam 只標本地；要線上可試 Remote Play（未確認）。","本地合作・本地對戰","未確認"),
("steam","Operation: Tango","Clever Plays","解謎",S+"1335790/header_tchinese.jpg","兩人分飾特務與駭客，只能靠語音溝通破關。","2,301 則評論・91% 好評","NT$82（特價 25 折，原價 NT$328）","有繁中","https://store.steampowered.com/app/1335790/","只能兩人線上、必須開語音；隊友是否需另購未確認。","線上合作","未確認"),
("itch","EGGNOGG+","madgarden","動作","https://img.itch.zone/aW1hZ2UvMzM5LzUxNjQ0LnBuZw==/original/loDBsG.png","像素劍客雙人對砍、搶著衝向對方終點。","itch 4.7★・436 人評分","自訂價格","無繁中","https://madgarden.itch.io/eggnogg","一局幾分鐘；需要兩人同台。","本地對戰","單局數分鐘（itch 頁面標示）"),
("itch","Regular Human Basketball","Powerhoof","動作","https://img.itch.zone/aW1hZ2UvMjcxNjgvMTM2NDkwMS5qcGc=/original/k%2BJvtN.jpg","全隊一起開一台巨大機器人打籃球，越搶越亂。","itch 4.8★・139 人評分","US$4.99 起","無繁中","https://powerhoof.itch.io/regular-human-basketball","至少兩人；頁面標本地與伺服器連線多人。","本地合作・線上合作・本地對戰・線上對戰","單局數分鐘（itch 頁面標示）"),
("itch","Micro Mages","Morphcat Games","動作","https://img.itch.zone/aW1hZ2UvNDE1NzQ5LzIwNjY3MTkucG5n/original/y5br8z.png","真正能放進 NES 卡帶的 4 人合作平台跳躍。","itch 4.8★・247 人評分","US$9.99 起","無繁中","https://morphcatgames.itch.io/micromages","僅 Windows；難度偏懷舊硬派。","本地合作","單次約一小時（itch 頁面標示）"),
]
def thumb(u):
  r=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=30).read()
  im=Image.open(io.BytesIO(r)).convert("RGB");im.thumbnail((480,480));b=io.BytesIO();im.save(b,"JPEG",quality=80)
  return "data:image/jpeg;base64,"+base64.b64encode(b.getvalue()).decode()
e=html.escape;cards=""
MP={"A Short Hike":"未確認","Celeste Classic":"未確認","We Become What We Behold":"未確認"}
items=[(i+len(G)+len(G2),g[:11],g[11],g[12],"2026-11-01") for i,g in enumerate(G3,1)]+[(i+len(G),g[:11],g[11],g[12],"2026-10-31") for i,g in enumerate(G2,1)]+[(i,g,MP.get(g[1],"僅單人"),"未確認","2026-10-28") for i,g in enumerate(G,1)]
for i,g,mp,hr,dt in items:
  p,n,d,t,img,s,rv,pr,zh,l,tip=g
  cards+=f'''<div class="c" data-tags="#{p} #{t} #mp-{mp} #{dt}" data-id="{i}"><a href="{l}" target="_blank" rel="noopener"><img src="{thumb(img)}" alt="{e(n)}"></a><div class="b"><span class="dt">{dt} 推薦</span><h3>{i}. <a href="{l}" target="_blank" rel="noopener">{e(n)}</a></h3><div class="m">{"Steam" if p=="steam" else "itch.io"}・{t}・{e(d)}</div><p>{e(s)}</p><div class="m">{e(rv)}｜{e(pr)}｜{zh}</div><div class="m">👥 多人：{mp}</div><div class="m">⏱ {e(hr)}</div><p class="tip">💡 {e(tip)}</p><label><input type="checkbox" class="ni"> 不感興趣</label></div></div>'''
btn=lambda xs:"".join(f'<button data-k="{k}"{" class=on" if k=="" else ""}>{n}</button>' for n,k in xs)
r1=btn([("全部",""),("Steam","#steam"),("itch.io","#itch")]);r2=btn([("全部",""),("解謎","#解謎"),("Roguelike","#Roguelike"),("敘事","#敘事"),("策略","#策略"),("模擬","#模擬"),("動作","#動作"),("冒險","#冒險")]);r3=btn([("全部",""),("僅單人","#mp-僅單人"),("本地合作","#mp-[^ ]*本地合作"),("線上合作","#mp-[^ ]*線上合作"),("對戰","#mp-[^ ]*對戰")])
open("index.html","w").write(f'''<!doctype html><html lang="zh-Hant-TW"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>冷門好遊戲雷達</title><style>
body{{background:#14161a;color:#e6e6e6;font-family:system-ui,"Noto Sans TC",sans-serif;margin:0;padding:20px}}h1{{margin:0}}.sub{{color:#9aa}}input[type=search]{{padding:8px;width:260px;background:#22252b;color:#eee;border:1px solid #444;border-radius:6px}}
.row{{margin:8px 0}}button{{background:#22252b;color:#ccc;border:1px solid #444;border-radius:16px;padding:5px 12px;margin:2px;cursor:pointer}}button.on{{background:#3d6fd8;color:#fff}}
.g{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px;margin-top:12px}}.c{{background:#1e2127;border-radius:10px;overflow:hidden}}.c.x{{opacity:.4}}.c img{{width:100%;aspect-ratio:460/215;object-fit:cover;display:block}}.b{{padding:10px 12px}}h3{{margin:0 0 4px;font-size:1.05em}}h3 a{{color:#fff;text-decoration:none}}.m{{color:#9ab;font-size:.85em}}p{{margin:6px 0;font-size:.92em}}.dt{{float:right;font-size:.75em;background:#3d6fd8;color:#fff;border-radius:8px;padding:1px 6px}}.tip{{color:#cba}}#none{{display:none;color:#999;margin:20px}}#out{{width:100%;max-width:500px;background:#22252b;color:#eee}}</style></head><body>
<h1>冷門好遊戲雷達</h1><div class="sub">共 {len(G)+len(G2)+len(G3)} 款・更新 2026-11-01・Steam 好評率/評論數取自商店頁（可能僅英文評論），itch 為頁面星等；多人資訊 Steam 取自商店分類、itch 頁面未標示者為未確認；遊玩時數來自 HowLongToBeat（部分經第三方轉載），查不到標未確認</div>
<div class="row"><input type="search" id="q" placeholder="搜尋名稱、類型、開發商…"> <button id="clr">清除</button> <span id="cnt"></span></div>
<div class="row" id="r1">{r1}</div><div class="row" id="r2">{r2}</div><div class="row" id="r3">{r3}</div>
<div class="row"><button id="exp">匯出「不感興趣」編號</button> <textarea id="out" rows="2" readonly></textarea></div>
<div class="g" id="g">{cards}</div><div id="none">找不到符合的項目</div>
<script>
const K='radar-ni',st=new Set(JSON.parse(localStorage.getItem(K)||'[]')),cs=[...document.querySelectorAll('.c')];
cs.forEach(c=>{{const b=c.querySelector('.ni');b.checked=st.has(c.dataset.id);c.classList.toggle('x',b.checked);b.onchange=()=>{{b.checked?st.add(c.dataset.id):st.delete(c.dataset.id);localStorage.setItem(K,JSON.stringify([...st]));c.classList.toggle('x',b.checked)}}}});
const f={{r1:'',r2:'',r3:''}};['r1','r2','r3'].forEach(r=>document.querySelectorAll('#'+r+' button').forEach(b=>b.onclick=()=>{{document.querySelectorAll('#'+r+' button').forEach(x=>x.classList.remove('on'));b.classList.add('on');f[r]=b.dataset.k;go()}}));
function go(){{const q=document.getElementById('q').value.toLowerCase();let n=0;cs.forEach(c=>{{const t=c.dataset.tags,ok=(!f.r1||new RegExp(f.r1).test(t))&&(!f.r2||new RegExp(f.r2).test(t))&&(!f.r3||new RegExp(f.r3).test(t))&&(c.textContent+t).toLowerCase().includes(q);c.style.display=ok?'':'none';n+=ok}});document.getElementById('cnt').textContent='顯示 '+n+' 款';document.getElementById('none').style.display=n?'none':'block'}}
document.getElementById('q').oninput=go;document.getElementById('clr').onclick=()=>{{document.getElementById('q').value='';go()}};
document.getElementById('exp').onclick=()=>{{const o=document.getElementById('out');o.value=[...st].sort((a,b)=>a-b).length?'不感興趣：'+[...st].sort((a,b)=>a-b).join(', '):'（尚未勾選）';o.select();navigator.clipboard&&navigator.clipboard.writeText(o.value).catch(()=>{{}})}};go();
</script></body></html>''')

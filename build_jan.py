# Builds jan.html — the January (stage-1) producer home — from index.html.
# Scope after the 2–3 Nov calls: Today's brief (action items from Salesforce + Outlook) · Today's meetings ·
# Prep my next meeting · Company brief · Capture Agent · Deal Review · BDR Agent. No goal panel, no pipeline
# screen, no sources slide. Built on what Ask Artemis already does (Today/Ask, Outlook, Salesforce quick actions, Dictate).
import re
BRAND = 'PA'
ASSISTANT = 'Ask Atlas'
h = open('index.html', encoding='utf-8').read()

def cut(s, start, end):
    a = s.index(start); b = s.index(end, a)
    return s[:a] + s[b:]

def rep(s, a, b):
    assert a in s, 'missing: ' + a[:90]
    return s.replace(a, b, 1)

h = rep(h, '<title>Producer Assistant</title>', '<title>Producer Home — January</title>')

# ---------- extra CSS ----------
h = rep(h, '</style>\n</head>', '''
/* January additions */
.jan-goal{display:flex;align-items:center;gap:14px;flex-wrap:wrap;padding:10px 16px;border:1px dashed var(--line);border-radius:12px;font-size:12.5px;color:var(--muted)}
.jan-goal .l{font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--faint);font-weight:600}
.jan-goal b{color:var(--fg);font-weight:600}
.jan-goal .num{font-size:15px;color:var(--fg)}
.jan-goal .later{margin-left:auto;font-size:11.5px;color:var(--faint)}
.mtg{list-style:none;margin:0;padding:0}
.mtg li{display:grid;grid-template-columns:76px 1fr auto auto;gap:12px;align-items:center;padding:10px 16px;border-top:1px solid var(--line);font-size:13.5px}
.mtg li:first-child{border-top:0}
.mtg .t{font-family:var(--mono);font-size:12.5px;color:var(--muted)}
.mtg .n b{font-weight:600}
.mtg .n small{display:block;color:var(--muted);font-size:11.5px}
.mtg .tg{font-size:11px;padding:2px 8px;border-radius:9px;background:var(--info-bg);color:var(--info);white-space:nowrap}
.mtg .tg.cl{background:var(--ok-bg);color:var(--ok)}
.mtg .go{font-size:12.5px;font-weight:600;color:var(--navy);text-decoration:none;white-space:nowrap}
.voice{display:inline-flex;align-items:center;gap:6px;font-size:11.5px;color:var(--muted);background:var(--panel-2);border-radius:10px;padding:3px 9px}
.voice svg{width:12px;height:12px;color:var(--navy)}
@media (max-width:760px){.mtg li{grid-template-columns:60px 1fr;row-gap:4px}.mtg .tg,.mtg .go{grid-column:2}}
</style>
</head>''')

# ---------- Home: goal panel → compact strip ----------
a = h.index('<!-- Goal panel'); b = h.index('<!-- Hero prompt -->')
strip = '''<!-- Goal: what Salesforce can say today; goal & pace come with the production feed (stage 2) -->
        <section class="jan-goal" aria-label="New business">
          <span class="l">New business · 2026</span>
          <span><b class="num">$1.08M</b> closed won YTD <span class="num">· 7</span> open deals <span class="num">· $2.4M</span> pipeline</span>
          <span class="src">Salesforce opportunities, as you</span>
          <span class="later">Goal, pace and “what closes the gap” arrive with the production data feed → stage 2</span>
        </section>

        '''
h = h[:a] + strip + h[b:]

# ---------- Hero: voice first ----------
h = rep(h, '<div class="date">Monday, October 26 · 2 meetings today · 4 items need you</div>',
        '<div class="date">Monday, 5 January · 3 meetings today · 4 items need you</div>')
h = rep(h, '<div class="hint">Try: “Prep me for the 2:00 with Meridian” · “Which of my renewals in Q1 have no opportunity yet?” · “Find an SME for cold-storage trucking”</div>',
        '<div class="hint"><span class="voice"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 10a7 7 0 0014 0M12 17v4M8 21h8"/></svg>Speak or type</span> &nbsp;Try: “Prep me for the 2:00 with Meridian” · “Just met Jordan at Northwind — they want revised numbers by the 14th” · “What did I promise this week?”</div>')

# ---------- Chips: five ----------
h = rep(h, '<button class="chip" data-prompt="Which of my leads haven\'t been touched? Draft first touches.">',
        '<button class="chip" data-prompt="Give me a company brief on: "><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 016.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15A2.5 2.5 0 016.5 2z"/></svg>Company brief</button>\n          <button class="chip" data-prompt="Capture my meeting notes: "><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 10a7 7 0 0014 0M12 17v4M8 21h8"/></svg>Capture Agent</button>\n          <button class="chip" data-prompt="Run my deal review: what did I promise this week and what is due?"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/></svg>Deal Review</button>\n          <button class="chip" data-prompt="Which of my leads haven\'t been touched? Draft first touches.">')
# remove the original Company brief / Deal Review / Capture / Pipeline / Update chips that follow BDR
h = cut(h, '<button class="chip" data-prompt="Give me a company brief on: "><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 016.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15A2.5 2.5 0 016.5 2z"/></svg>Company brief</button>\n          <button class="chip" data-prompt="Run my deal review',
        '</section>')
# the cut above removed from the 2nd "Company brief" chip (the original) to </section>; now the chips section ends after BDR. Verify counts later.

# ---------- Prepared-for-you + pipeline tiles → portal-style counters + today's meetings ----------
a = h.index('<!-- Prepared for you'); b = h.index('<!-- Brief + attention -->')
tiles = '''<!-- Counters: what the portal agent already shows today, now with our flags behind them -->
        <section class="tiles" aria-label="Today">
          <div class="tile"><div class="l">Meetings today<span class="src">Outlook</span></div><div class="v num">3</div><div class="d"><b>1</b> prospect, <b>2</b> clients · prep ready for all</div></div>
          <div class="tile"><div class="l">Emails to answer<span class="src">Outlook</span></div><div class="v num">7</div><div class="d"><b>2</b> from clients with an open deal · drafts ready</div></div>
          <div class="tile"><div class="l">Closing this month<span class="src">Salesforce</span></div><div class="v num">1 <small>$310K</small></div><div class="d">Brightline Foods · quote held till 5 PM</div></div>
          <div class="tile"><div class="l">Gone cold<span class="src">Salesforce</span></div><div class="v num">2 <small>$226K</small></div><div class="d"><b class="risk">Sable &amp; Finch</b> 21 days · Orion 18 days</div></div>
        </section>

        <!-- Today's meetings: the calendar is the context for Prep -->
        <section class="panel" aria-label="Today's meetings">
          <div class="ph"><h2>Today’s meetings</h2><span class="sub">From Outlook · matched to Salesforce</span><span class="right"><a class="src-link" href="#prep">Prep my next meeting →</a></span></div>
          <ul class="mtg">
            <li><span class="t">10:30 AM</span><span class="n"><b>Harbor Point Health</b><small>Cyber renewal review · Dr. Amir Patel, Mia Chen</small></span><span class="tg cl">client</span><a class="go" href="#company-brief" data-prompt="Open the company brief for Harbor Point Health">Prepare me →</a></li>
            <li><span class="t">2:00 PM</span><span class="n"><b>Meridian Logistics</b><small>First in-person · at their yard · Karen Harris (SME) joins 2:30</small></span><span class="tg">prospect</span><a class="go" href="#prep">Prepare me →</a></li>
            <li><span class="t">4:30 PM</span><span class="n"><b>Northwind Dental Partners</b><small>EB renewal · revised numbers · Jordan Lee</small></span><span class="tg cl">client</span><a class="go" href="#" onclick="return false">Prepare me →</a></li>
          </ul>
        </section>

        '''
h = h[:a] + tiles + h[b:]

# ---------- Today's brief: action items only, one source each, one write-back; Needs attention removed ----------
a = h.index('<!-- Brief + attention -->'); b = h.index('<!-- Connected sources -->')
CB = '<button class="cb" aria-label="Mark done"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M5 12l5 5L20 7"/></svg></button>'
CBD = '<button class="cb" aria-label="Mark not done"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M5 12l5 5L20 7"/></svg></button>'
def item(kind, label, txt, meta, via, act, act_href=None, done=None):
    cls = 'item done' if done else 'item'
    cb = CBD if done else CB
    a_ = '<a class="act" href="%s">%s</a>' % (act_href, act) if act_href else '<button class="act">%s</button>' % act
    extra = ' data-done="%s"' % done if done else ''
    return ('              <li class="%s" data-kind="%s"%s>\n                %s\n'
            '                <div><div class="txt"><span class="kind %s">%s</span>%s</div>\n'
            '                  <div class="meta"><span>%s</span><span class="via">%s</span></div></div>\n'
            '                %s\n              </li>\n') % (cls, kind, extra, cb, kind, label, txt, meta, via, a_)
brief = ('<!-- Today\'s brief: what needs an action today. Meetings live in their own list; prep is one click there. -->\n'
         '        <section class="cols" style="grid-template-columns:1fr">\n'
         '          <div class="panel">\n'
         '            <div class="ph"><h2>Today’s brief</h2><span class="sub">What needs you, in order · one source per item, one write-back</span><span class="right" id="briefCount"></span></div>\n'
         '            <ul class="brief" id="brief">\n'
    + item('review', 'Follow-up due', 'Send Northwind Dental the revised numbers before the 4:30 call — Jordan asked for them on Friday.', 'Salesforce · Task · due today', 'Deal Review · check = Task completed', 'Draft the email')
    + item('reply', 'Reply', 'Tom Reyes (Cascade Freight) will send the loss runs once you confirm the meeting — the thread has been waiting since Friday.', 'Outlook · thread matched to the Cascade Freight opportunity', 'draft ready', 'Open draft in Outlook')
    + item('call', 'Call back', 'Tallgrass Manufacturing referral from Karen Harris. They asked for a call this week.', 'Salesforce · Lead · untouched 6 days', 'BDR Agent', 'Draft intro', '#bdr')
    + item('overdue', 'Overdue', 'Sable &amp; Finch: revised professional liability proposal was due Oct 17. The deal has had no activity for 21 days.', 'Salesforce · Task · overdue 19 days', 'Deal Review · move or mark lost', 'Decide')
    + item('done', 'Capture', 'Friday’s Harbor Point meeting logged: 3 follow-up Tasks and 1 Event written to Salesforce.', 'Done 8:52 AM', 'dictated in the car', 'Open', None, '8:52 AM')
    + item('done', 'Follow-up', 'Recap and the two open items sent to Harbor Point Health.', 'Done 8:47 AM', 'email drafted by Capture, sent from Outlook', 'Open', None, '8:47 AM')
    + '            </ul>\n          </div>\n        </section>\n\n        ')
h = h[:a] + brief + h[b:]
h = rep(h, '.kind.renewal{color:var(--ok)}', '.kind.renewal{color:var(--ok)} .kind.reply{color:var(--navy)} .kind.overdue{color:var(--crit)}')

# ---------- Connected ----------
h = rep(h, '<span class="s">Salesforce</span><span class="s">Outlook</span><span class="s">Broker AI workflows</span><span class="s">Agency management</span><span class="s">SharePoint</span><span class="s">Reports</span><span class="s">SME directory</span><a href="#sources" class="src-link">Where each block gets its data →</a>',
        '<span class="s">Broker portal agent</span><span class="s">Salesforce (as you)</span><span class="s">Outlook · Teams</span><span class="s">Existing prospect briefs</span><span class="s">SME directory</span><span class="src-link" style="cursor:default">January: five agents on the existing portal agent · goal panel, renewals / at-risk, pipeline and sales-leader lens in stage 2</span>')

# ---------- Header / sidebar ----------
h = rep(h, '<span class="title">Producer Home</span><span class="role">Employee Benefits · P&amp;C</span>',
        '<span class="title">Producer Home</span><span class="role">January version</span>')

# ---------- Company brief: Artemis-aware notes ----------
h = rep(h, '<div class="pg"><span class="pl"></span><span class="ortype">or type a name…</span></div>\n          </div>',
        '<div class="pg"><span class="pl"></span><span class="ortype">or type a name…</span></div>\n          </div>\n          <p class="muted" style="font-size:12px;margin:10px 0 0">Names are matched on Account, Lead and Opportunity; if two records match (“Dreisbach Enterprises” and “Dreisbach Enterprises Inc”), you pick one before anything is read.</p>')
h = rep(h, '<div class="side-h ext"><span>2</span>What is out there<small>External · from the brief and the web</small></div>',
        '<div class="side-h ext"><span>2</span>What is out there<small>External · the existing prospect brief (Salesforce) or the portal’s prospect-intelligence agent</small></div>')
h = rep(h, '<p class="scope"><b>Wave 1:</b> internal from Salesforce (policies only where the object is populated); external from existing briefs, web search labelled "not screened". A new full research brief only if the Salesforce-side job stays.</p>',
        '<p class="scope"><b>January:</b> internal from Salesforce as you (policies only where the object is populated); external = the brief that already exists — the prospect briefing on the Account or the output of the portal’s prospect-intelligence agent — surfaced here, not regenerated. A fresh research run is stage 2.</p>')

# ---------- other scope notes ----------
h = rep(h, '<p class="scope"><b>Wave 1:</b> runs on existing Tasks and Opportunities',
        '<p class="scope"><b>January:</b> runs on existing Tasks and Opportunities')
h = rep(h, '<p class="scope"><b>Wave 1:</b> dictation and speech-to-text come from the Microsoft stack (Teams / Azure AI Speech).',
        '<p class="scope"><b>January:</b> dictation uses the portal’s Dictate (Microsoft speech-to-text).')
h = rep(h, '<p class="scope"><b>Wave 1:</b> list + drafts only. Lead scoring, routing and reply tracking are increment 2.</p>',
        '<p class="scope"><b>January:</b> list + drafts only; the draft opens in Outlook the way the portal already opens replies. Lead scoring, routing and reply tracking are stage 2.</p>')

# ---------- drop Pipeline view and sources slide ----------
h = cut(h, '<section class="thread uc" id="v-pipeline"', '<!-- Deal Review -->')
h = cut(h, '<section class="slide" id="sourcesView"', '<div class="toast"')
h = rep(h, '<div class="toast"', '    </div>\n  </div>\n</div>\n\n<div class="toast"')

# ---------- Sidebar: portal-agent structure (Today | Ask, New question, search, Today's work, Chats, quick links) ----------
SIDE_CSS = '''
/* portal-style sidebar */
.seg{margin:6px 12px 10px;display:grid;grid-template-columns:1fr 1fr;background:var(--panel-2);border-radius:9px;padding:3px}
.seg a{text-align:center;padding:7px 0;border-radius:7px;font-size:13px;font-weight:600;color:var(--muted);text-decoration:none}
.seg a.on{background:var(--navy);color:#fff}
.newq{margin:0 12px 8px;display:flex;align-items:center;gap:8px;padding:8px 10px;font-size:13.5px;font-weight:600;color:var(--fg);text-decoration:none;border-radius:8px}
.newq:hover{background:var(--panel-2)}
.newq svg{width:15px;height:15px}
.ssearch{margin:0 12px 10px;display:flex;align-items:center;gap:8px;padding:7px 10px;border:1px solid var(--line);border-radius:8px;color:var(--faint);font-size:12.5px;background:var(--bg)}
.work a{display:flex;justify-content:space-between;gap:8px;color:var(--fg);font-size:12.5px;padding:5px 10px;border-radius:6px;text-decoration:none}
.work a:hover{background:var(--panel-2)}
.work a .st{color:var(--ok);font-size:11.5px;font-weight:600}
.work a .st.run{color:var(--warn)}
.side .sect.sub{margin-top:8px;color:var(--faint);font-weight:500;letter-spacing:.06em;text-transform:none;font-size:11.5px}
.quick{padding:6px 10px 0;border-top:1px solid var(--line);margin-top:6px}
.quick a{display:flex;align-items:center;gap:10px;padding:7px 10px;border-radius:7px;color:var(--fg);text-decoration:none;font-size:13px}
.quick a:hover{background:var(--panel-2)}
.quick a svg{width:15px;height:15px;color:var(--muted)}
.quick a small{margin-left:auto;color:var(--faint);font-size:11px;white-space:nowrap}
.sidefoot{padding:10px 14px;border-top:1px solid var(--line);display:flex;align-items:center;gap:10px}
.sidefoot .av{width:30px;height:30px;border-radius:50%;background:var(--navy);color:#fff;font-size:11px;font-weight:700;display:grid;place-items:center}
.sidefoot b{display:block;font-size:13px;font-weight:600}
.sidefoot small{color:var(--muted);font-size:11.5px}
'''
h = rep(h, '</style>\n</head>', SIDE_CSS + '</style>\n</head>')

a = h.index('<aside class="side"'); b = h.index('</aside>') + len('</aside>')
side = '''<aside class="side" aria-label="Workspace navigation">
    <div class="brand"><span class="mark">__BRAND__</span><span class="name">Producer Assistant</span><span class="dot" title="Connected"></span></div>
    <div class="seg" role="tablist"><a href="#home" class="on" id="segToday">Today</a><a href="#ask" id="segAsk">Ask</a></div>
    <a class="newq" href="#ask"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 5v14M5 12h14"/></svg>New question</a>
    <div class="ssearch"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>Search chat history</div>

    <div class="sect">Today’s work</div>
    <nav class="nav work">
      <a href="#prep">Prep · Meridian Logistics 2:00<span class="st">Ready</span></a>
      <a href="#company-brief" data-prompt="Open the company brief for Harbor Point Health">Company brief · Harbor Point<span class="st">Ready</span></a>
      <a href="#bdr">First-touch draft · Tallgrass<span class="st">Ready</span></a>
      <a href="#deal-review">Deal review · this week<span class="st run">Running</span></a>
    </nav>

    <div class="sect">Chats</div>
    <div class="sect sub">Starred</div>
    <nav class="nav recents">
      <a href="#company-brief" data-prompt="Open the company brief for Harbor Point Health">What is happening with Harbor Point Health</a>
    </nav>
    <div class="sect sub">Today</div>
    <nav class="nav recents">
      <a href="#capture">Capture: call with Jordan at Northwind</a>
      <a href="#prep">Prepare me for my next meeting</a>
      <a href="#deal-review">What did I promise this week?</a>
    </nav>
    <div class="sect sub">Previous 7 days</div>
    <nav class="nav recents">
      <a href="#r3">Who covers trucking physical damage?</a>
      <a href="#r4">Draft BOR letter for Cobalt Ridge</a>
    </nav>

    <div class="spacer"></div>
    <div class="quick">
      <a href="#capture"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 10a7 7 0 0014 0M12 17v4M8 21h8"/></svg>Salesforce quick actions<small>→ Capture Agent</small></a>
      <a href="#home"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h10"/></svg>Briefing prompts<small>5 agents</small></a>
    </div>
    <div class="ver"><div class="t">Wireframes</div><a href="index.html">North Star<small>full vision</small></a><a href="jan.html" class="on">January<small>stage 1</small></a><a href="leader.html">Sales Leader<small>second lens</small></a></div><!--/ver-->
    <div class="sidefoot"><span class="av">DW</span><div><b>Dana Whitfield</b><small>Producer · Employee Benefits · signed in through the broker portal</small></div></div>
  </aside>'''
h = h[:a] + side.replace('__BRAND__', BRAND) + h[b:]

# nav handling: Today -> home; Ask -> home + focus prompt; chat links -> their views; segment state follows the view
h = rep(h, """  $$('.nav a').forEach(function(a){a.addEventListener('click',function(e){
    var h=a.getAttribute('href'); if(h==='#home'){e.preventDefault();showHome()} else if(h==='#r1'){e.preventDefault();showView('prep')}
  })});""",
"""  function setSeg(ask){ $('#segToday').classList.toggle('on',!ask); $('#segAsk').classList.toggle('on',!!ask); }
  $$('.nav a, .quick a, .seg a, .newq').forEach(function(a){a.addEventListener('click',function(e){
    var h=a.getAttribute('href'), p=a.getAttribute('data-prompt');
    if(h==='#home'){e.preventDefault();showHome();setSeg(false);return}
    if(h==='#ask'){e.preventDefault();showHome();setSeg(true);input.focus();input.scrollIntoView({behavior:'smooth',block:'center'});return}
    var v=h.slice(1); if(VIEWS[v]){e.preventDefault();showView(v,p||'');setSeg(true);return}
    e.preventDefault(); toast('Wireframe: this chat is not filled in');
  })});""")
# the old showView toggled .nav a.active by href; keep it harmless
h = rep(h, "    $$('.nav a').forEach(function(a){a.classList.toggle('active',name==='prep'&&a.getAttribute('href')==='#r1')});\n", "")
h = rep(h, "    $$('.nav a').forEach(function(a){a.classList.toggle('active',a.getAttribute('href')==='#home')});\n", "")


# ---------- JS ----------
h = rep(h, """  var VIEWS={prep:['#prepView','Prep: Meridian Logistics'],sources:['#sourcesView','Where the data comes from'],
    pipeline:['#v-pipeline','Pipeline'],'deal-review':['#v-deal-review','Deal Review'],capture:['#v-capture','Capture Agent'],
    'company-brief':['#v-company-brief','Company brief'],bdr:['#v-bdr','BDR Agent']};""",
        """  var VIEWS={prep:['#prepView','Prep: Meridian Logistics'],
    'deal-review':['#v-deal-review','Deal Review'],capture:['#v-capture','Capture Agent'],
    'company-brief':['#v-company-brief','Company brief'],bdr:['#v-bdr','BDR Agent']};""")
h = rep(h, "var ROUTES=[[/prep|meridian|next meeting/i,'prep'],[/pipeline/i,'pipeline'],[/deal review|promise/i,'deal-review'],[/capture/i,'capture'],[/company brief|client summary|harbor point/i,'company-brief'],[/lead|bdr/i,'bdr']];",
        "var ROUTES=[[/prep|meridian|next meeting/i,'prep'],[/pipeline|goal|pace/i,'later'],[/deal review|promise/i,'deal-review'],[/capture|just met/i,'capture'],[/company brief|client summary|harbor point/i,'company-brief'],[/lead|bdr/i,'bdr']];")
h = rep(h, "    var v=c.getAttribute('data-view')||route(p);\n    if(v){e.preventDefault();showView(v,p);return}",
        "    var v=c.getAttribute('data-view')||route(p);\n    if(v==='later'){e.preventDefault();toast('Pipeline sweep and goal panel: stage 2 (after 4 January)');return}\n    if(v){e.preventDefault();showView(v,p);setSeg(true);return}")
h = rep(h, "var r=route(v);if(r){showView(r,v)}else{toast('Wireframe: the assistant would answer here')}",
        "var r=route(v);if(r==='later'){toast('Pipeline sweep and goal panel: stage 2 (after 4 January)')}else if(r){showView(r,v)}else{toast('Wireframe: the assistant would answer here')}")
h = rep(h, "if(current&&current!=='sources'){", "if(current){")
h = rep(h, "  $('#months').innerHTML=months.map(function(m){", "  if($('#months')) $('#months').innerHTML=months.map(function(m){")
h = rep(h, "var dateEl=$('.hero .date');dateEl.textContent='Monday, October 26 · 2 meetings today · '",
        "var dateEl=$('.hero .date');dateEl.textContent='Monday, 5 January · 3 meetings today · '")

# the Pipeline flow key is referenced only from the removed screen; harmless.
# ---------- Portal skin: colours, type, header, briefing header, pills, prompt box ----------
LOGO = ('<svg class="alogo" viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="20" fill="#14307e"/>'
        '<ellipse cx="20" cy="20" rx="13" ry="6" fill="none" stroke="#fff" stroke-width="1.6" transform="rotate(-28 20 20)"/>'
        '<ellipse cx="20" cy="20" rx="13" ry="6" fill="none" stroke="#9fb4e8" stroke-width="1.2" transform="rotate(34 20 20)"/>'
        '<circle cx="20" cy="20" r="4.2" fill="#fff"/><circle cx="30" cy="12" r="1.8" fill="#f5c518"/></svg>')

SKIN_CSS = '''
/* ===== portal skin ===== */
@import url("https://fonts.googleapis.com/css2?family=Lora:wght@500;600;700&family=Nunito+Sans:wght@400;600;700&display=swap");
:root{--bg:#f3f6fb;--panel:#ffffff;--panel-2:#eaf0f9;--line:#dbe3f0;--fg:#0f1f4d;--muted:#4e5d80;--faint:#8592b3;
  --navy:#14307e;--navy-ink:#fff;--gold:#f5c518;--gold-ink:#2a2000;--info:#1f4fd1;--info-bg:#e4ebfb;--ok:#1d7a52;--ok-bg:#e1f3ea;--warn:#a8640f;--warn-bg:#fdf1dc;--crit:#b23a2b;--crit-bg:#fbe6e2;
  --sans:"Nunito Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--serif:"Lora",Georgia,"Times New Roman",serif;--shadow:0 1px 2px rgba(15,31,77,.05),0 8px 24px -16px rgba(15,31,77,.18)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#0d1430;--panel:#141c3d;--panel-2:#1c254c;--line:#2a3560;--fg:#eef1fb;--muted:#aab4d6;--faint:#7280a8;--navy:#3b5bd6}}
:root[data-theme="dark"]{--bg:#0d1430;--panel:#141c3d;--panel-2:#1c254c;--line:#2a3560;--fg:#eef1fb;--muted:#aab4d6;--faint:#7280a8;--navy:#3b5bd6}
body{font-size:14.5px}
h1,h2,.serif,.tile .v,.goal .big .v,.msg-ai .lead b,.brief-card h2,.kpis .v{font-family:var(--serif)}
.hero h1{font-size:34px;font-weight:700;letter-spacing:0}
.ph h2{font-size:19px;font-weight:600}
.tile .v{font-size:34px;font-weight:600;color:var(--navy)}
.tile .v.cold{color:#b24a1b}
.tile{border-radius:14px;padding:18px 20px}
.tile .l{font-size:14px;color:var(--fg);order:2;margin-top:2px}
.tile .l .src{display:none}
.tile .d{order:3}
.tile .v{order:1}
.panel,.prompt,.brief-card{border-radius:16px}
.content{gap:18px;max-width:1180px}
/* sidebar */
.brand{padding:18px 16px 12px;gap:10px}
.brand .mark{display:none}
.alogo{width:34px;height:34px;flex:none}
.brand .name{font-size:17px;font-weight:700}
.brand .dot{display:none}
.brand .collapse{margin-left:auto;width:18px;height:18px;color:var(--muted)}
.seg{margin:4px 12px 10px;background:#e8eefb;border-radius:10px;padding:0;gap:0}
.seg a{padding:10px 0;font-size:14px;border-radius:10px}
.seg a.on{background:var(--navy)}
.newq{font-size:15px}
.ssearch{border-radius:10px;padding:9px 12px}
.side .sect{font-size:13px;letter-spacing:0;text-transform:none;color:var(--fg);font-weight:700}
.side .sect.sub{color:var(--faint);font-weight:500;font-size:12px}
.nav.recents a{font-size:13.5px;color:var(--fg)}
.work a{font-size:13.5px}
.quick a{font-size:14px}
.sidefoot .av{background:#e8eefb;color:var(--navy)}
/* top bar */
.top{padding:12px 28px}
.top .title{font-size:17px;font-weight:700}
.top .search{display:none}
.top .user{display:none}
.icon-btn .pip{top:2px;right:2px;width:16px;height:16px;border-radius:8px;background:var(--navy);color:#fff;font:700 9px/12px var(--sans);text-align:center;border-width:2px}
.srcbtn{display:inline-flex;align-items:center;gap:8px;padding:8px 14px;border:1px solid var(--line);border-radius:10px;font-size:14px;font-weight:600;color:var(--fg);background:var(--panel)}
.srcbtn svg{width:15px;height:15px}
/* briefing header */
.bhead{display:flex;align-items:flex-end;gap:16px;flex-wrap:wrap;padding-bottom:14px;border-bottom:3px solid var(--gold)}
.bhead .eyebrow{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--navy);font-weight:700}
.bhead h1{margin-top:6px}
.bhead .sub{color:var(--muted);font-size:14px;margin-top:4px}
.bhead .actions{margin-left:auto;display:flex;gap:10px;align-items:center}
.abtn{padding:10px 16px;border-radius:10px;border:1px solid var(--line);background:var(--panel);font-size:14px;font-weight:600;color:var(--fg)}
.abtn.soft{background:#dfe7f8;color:var(--navy);border-color:#dfe7f8}
/* pills */
.chips{justify-content:flex-start;width:100%;gap:10px;margin:0}
.chip{padding:10px 18px;border-radius:999px;font-size:14px;font-weight:600;border:1px solid var(--line);background:var(--panel);color:var(--fg)}
.chip.on{background:var(--navy);color:#fff;border-color:var(--navy)}
.chip .n{background:var(--gold);color:var(--gold-ink);font-size:12px;font-weight:700;padding:1px 7px;border-radius:9px}
.chip svg{display:none}
/* meetings / brief cards */
.mtg li{padding:14px 20px;font-size:15px}
.mtg .t{font-family:var(--sans);font-weight:600;color:var(--fg);font-size:14px}
.mtg .tg{background:#dfe7f8;color:var(--navy);font-weight:600;padding:3px 10px}
.mtg .tg.cl{background:#dfe7f8;color:var(--navy)}
.mtg .go,.mtg .join{color:var(--info);font-weight:700;font-size:14px}
.ph .right .src-link{font-weight:700}
.pillmini{font-size:12.5px;font-weight:600;padding:4px 10px;border-radius:999px;background:#dfe7f8;color:var(--navy)}
.pillmini.ghost{background:transparent;color:#9aaad8}
.brief .kind{font-family:var(--sans)}
.brief .txt{font-size:15px}
.brief .act{color:var(--info);font-weight:700}
/* goal strip */
.jan-goal{border-style:solid;background:var(--panel)}
/* prompt box at the bottom */
.askbox{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:14px 16px 12px;box-shadow:var(--shadow)}
.askbox .prompt{width:100%;border:0;box-shadow:none;padding:0 0 10px;border-radius:0}
.askbox .prompt input{font-size:16px}
.askbox .foot{display:flex;align-items:center;gap:8px}
.askbox .foot .pillmini{background:#e8eefb}
.askbox .foot .send2{margin-left:auto;padding:9px 20px;border-radius:10px;background:#dfe7f8;color:var(--navy);font-weight:700;font-size:14px}
.askbox .foot .send2.live{background:var(--navy);color:#fff}
.asknote{text-align:center;color:var(--muted);font-size:13px;margin-top:-6px}
.hint{display:none}
.hero{display:contents}
.dock .prompt{border-radius:14px}
'''
h = rep(h, '</style>\n</head>', SKIN_CSS + '</style>\n</head>')

# ---- sidebar brand
h = rep(h, '<div class="brand"><span class="mark">' + BRAND + '</span><span class="name">Producer Assistant</span><span class="dot" title="Connected"></span></div>',
        '<div class="brand">' + LOGO + '<span class="name">' + ASSISTANT + '</span><svg class="collapse" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M9 4v16"/></svg></div>')

# ---- top bar
a = h.index('<header class="top">'); b = h.index('</header>') + len('</header>')
h = h[:a] + ('<header class="top">\n'
    '      <span class="title">' + ASSISTANT + '</span>\n'
    '      <span class="gap"></span>\n'
    '      <button class="icon-btn" aria-label="Notifications"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8a6 6 0 00-12 0c0 7-3 9-3 9h18s-3-2-3-9M13.7 21a2 2 0 01-3.4 0"/></svg><span class="pip">1</span></button>\n'
    '      <button class="icon-btn" id="themeBtn" aria-label="Toggle theme"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.8A9 9 0 1111.2 3a7 7 0 009.8 9.8z"/></svg></button>\n'
    '      <button class="srcbtn" type="button"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M15 4v16"/></svg>Sources</button>\n'
    '    </header>') + h[b:]
# make the gap flexible
h = rep(h, '.top .title{font-size:17px;font-weight:700}', '.top .title{font-size:17px;font-weight:700} .top .gap{flex:1}')

# ---- briefing header replaces hero h1/date; prompt moves to the bottom
a = h.index('<!-- Hero prompt -->'); b = h.index('<!-- Capability chips -->')
hero_block = h[a:b]
form_a = hero_block.index('<form class="prompt"'); form_b = hero_block.index('</form>') + len('</form>')
form_html = hero_block[form_a:form_b]
bhead = ('<!-- Briefing header -->\n'
    '        <section class="bhead" aria-label="Daily briefing">\n'
    '          <div><div class="eyebrow">Daily briefing · Monday, January 5</div><h1>Good morning, Dana</h1><div class="sub date">Briefing ready · 3 meetings today · 4 items need you</div></div>\n'
    '          <div class="actions"><button class="abtn" type="button">Notify me when it’s done</button><button class="abtn soft" type="button">↻ Refresh</button><button class="abtn" type="button">Close</button></div>\n'
    '        </section>\n'
    '        <section class="hero">\n' + form_html.replace('<form class="prompt" id="promptForm">', '<form class="prompt" id="promptForm" hidden>') + '\n        </section>\n\n        ')
h = h[:a] + bhead + h[b:]
# the JS updates '.hero .date' — now the .sub.date in the header
h = rep(h, "var dateEl=$('.hero .date');dateEl.textContent='Monday, 5 January · 3 meetings today · '+open.length+(open.length===1?' item needs':' items need')+' you';",
        "var dateEl=$('.bhead .date');dateEl.textContent='Briefing ready · 3 meetings today · '+open.length+(open.length===1?' item needs':' items need')+' you';")

# ---- chips become pills, with a "Today" pill in front and a count on Prep
h = rep(h, '<section class="chips" aria-label="Things you can ask" style="margin:-6px auto 0">',
        '<section class="chips" aria-label="Things you can ask">\n          <button class="chip on" data-view="home">Today</button>')
h = rep(h, '</svg>Prep my next meeting</button>', '</svg>Prep my next meeting<span class="n">3</span></button>')
h = rep(h, "    var v=c.getAttribute('data-view')||route(p);\n    if(v==='later')", "    var v=c.getAttribute('data-view')||route(p);\n    if(v==='home'){e.preventDefault();showHome();setSeg(false);return}\n    if(v==='later')")

# ---- tiles: wording and the orange "gone cold"
h = rep(h, '<div class="tile"><div class="l">Gone cold<span class="src">Salesforce</span></div><div class="v num">2 <small>$226K</small></div>',
        '<div class="tile"><div class="l">Deals gone cold<span class="src">Salesforce</span></div><div class="v num cold">2 <small>$226K</small></div>')
h = rep(h, '<div class="l">Closing this month<span class="src">Salesforce</span></div>', '<div class="l">Deals closing this month<span class="src">Salesforce</span></div>')

# ---- meetings card header pills + Join links
h = rep(h, '<div class="ph"><h2>Today’s meetings</h2><span class="sub">From Outlook · matched to Salesforce</span><span class="right"><a class="src-link" href="#prep">Prep my next meeting →</a></span></div>',
        '<div class="ph"><h2>Today’s meetings</h2><span class="sub">From Outlook · matched to Salesforce</span><span class="right"><span class="pillmini">Graph</span> <span class="pillmini ghost">Update</span></span></div>')
h = h.replace('<a class="go" href="#company-brief" data-prompt="Open the company brief for Harbor Point Health">Prepare me →</a>',
              '<span><a class="join" href="#" onclick="return false">Join</a>&nbsp;&nbsp;<a class="go" href="#company-brief" data-prompt="Open the company brief for Harbor Point Health">Prepare me</a></span>')
h = h.replace('<a class="go" href="#prep">Prepare me →</a>', '<span><a class="join" href="#" onclick="return false">Join</a>&nbsp;&nbsp;<a class="go" href="#prep">Prepare me</a></span>')
h = h.replace('<a class="go" href="#" onclick="return false">Prepare me →</a>', '<span><a class="join" href="#" onclick="return false">Join</a>&nbsp;&nbsp;<a class="go" href="#" onclick="return false">Prepare me</a></span>')
h = rep(h, '.mtg li{display:grid;grid-template-columns:76px 1fr auto auto;', '.mtg li{display:grid;grid-template-columns:90px 1fr auto auto;')

# ---- brief card header pills
h = rep(h, '<div class="ph"><h2>Today’s brief</h2><span class="sub">What needs you, in order · one source per item, one write-back</span><span class="right" id="briefCount"></span></div>',
        '<div class="ph"><h2>Today’s brief</h2><span class="sub">What needs you, in order</span><span class="right"><span class="pillmini">Salesforce</span> <span class="pillmini">Outlook</span> <span class="pillmini ghost" id="briefCount"></span></span></div>')

# ---- Ask box at the bottom (before Connected)
askbox = ('<!-- Ask -->\n'
    '        <section class="askbox" aria-label="Ask">\n'
    '          <form class="prompt" id="askForm">\n'
    '            <input id="askInput" type="text" placeholder="Ask about an account, meeting, or renewal — or dictate what just happened" autocomplete="off">\n'
    '            <button type="button" class="mic" aria-label="Dictate" title="Dictate"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 10a7 7 0 0014 0M12 17v4M8 21h8"/></svg></button>\n'
    '          </form>\n'
    '          <div class="foot"><span class="pillmini">Salesforce</span><span class="pillmini">Outlook</span><span class="pillmini">Briefs</span><button type="submit" form="askForm" class="send2">Send</button></div>\n'
    '        </section>\n'
    '        <p class="asknote">Check sources before sharing with a client.</p>\n\n        ')
h = rep(h, '<!-- Connected sources -->', askbox + '<!-- Connected sources -->')
# wire the ask form to the same router as the hidden hero form
h = rep(h, "  $('#promptForm').addEventListener('submit',function(e){e.preventDefault();var v=input.value.trim();",
        "  $('#askForm').addEventListener('submit',function(e){e.preventDefault();var v=$('#askInput').value.trim();if(!v)return;var r=route(v);if(r==='later'){toast('Pipeline sweep and goal panel: stage 2 (after 4 January)')}else if(r){showView(r,v)}else{toast('Wireframe: the assistant would answer here')}});\n"
        "  $('#promptForm').addEventListener('submit',function(e){e.preventDefault();var v=input.value.trim();")
# "Ask" in the sidebar focuses the bottom box
h = rep(h, "if(h==='#ask'){e.preventDefault();showHome();setSeg(true);input.focus();input.scrollIntoView({behavior:'smooth',block:'center'});return}",
        "if(h==='#ask'){e.preventDefault();showHome();setSeg(true);var ai=$('#askInput');ai.focus();ai.scrollIntoView({behavior:'smooth',block:'center'});return}")
# chips: when a chip fills the (hidden) prompt instead of routing, put the text in the ask box
h = rep(h, "    input.value=p;input.focus(); toast('Wireframe: only Team pipeline review and Prep my 1:1 are filled in');", "    input.value=p;input.focus();") if "only Team pipeline review" in h else h
h = rep(h, "    input.value=p;input.focus();\n  })});", "    var ai=$('#askInput'); ai.value=p; ai.focus();\n  })});")


h = h.replace("$('.top .title').textContent='Producer Home';", "$('.top .title').textContent='Daily briefing';")
# move the goal strip below the pills
_a = h.index('<!-- Goal: what Salesforce'); _b = h.index('<!-- Briefing header'); _strip = h[_a:_b]; h = h[:_a] + h[_b:]
_c = h.index('<!-- Counters:'); h = h[:_c] + _strip + h[_c:]

for bad in ('id="v-pipeline"', 'id="sourcesView"', 'data-tab="stalled"', 'data-tab="risk"', 'Needs attention</h2>', 'Update Salesforce</button>'):
    assert bad not in h, bad
assert h.count('class="chip" data-prompt') >= 5
open('jan.html', 'w', encoding='utf-8').write(h)
print('jan.html', len(h))

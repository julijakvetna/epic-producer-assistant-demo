# Builds jan.html — the January (stage-1) producer home — from index.html.
# Scope after the 2–3 Nov calls: Today's brief (action items from Salesforce + Outlook) · Today's meetings ·
# Prep my next meeting · Company brief · Capture Agent · Deal Review · BDR Agent. No goal panel, no pipeline
# screen, no sources slide. Built on what Ask Artemis already does (Today/Ask, Outlook, Salesforce quick actions, Dictate).
import re
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

# ---------- Prepared-for-you + pipeline tiles → Artemis-style counters + today's meetings ----------
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
    + item('decide', 'Decide', 'Approve the Beazley cyber quote for Brightline Foods. The $2.1M limit is held until 5:00 PM today.', 'Salesforce · Opportunity · Proposal · closes Jan 9', 'Deal Review', 'Open deal review', '#deal-review')
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
h = rep(h, '<div class="foot">Signed in as Dana Whitfield · Salesforce permissions apply</div>',
        '<div class="foot">Signed in through the broker portal · every read and write runs as Dana in Salesforce</div>')

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
        "    var v=c.getAttribute('data-view')||route(p);\n    if(v==='later'){e.preventDefault();toast('Pipeline sweep and goal panel: stage 2 (after 4 January)');return}\n    if(v){e.preventDefault();showView(v,p);return}")
h = rep(h, "var r=route(v);if(r){showView(r,v)}else{toast('Wireframe: the assistant would answer here')}",
        "var r=route(v);if(r==='later'){toast('Pipeline sweep and goal panel: stage 2 (after 4 January)')}else if(r){showView(r,v)}else{toast('Wireframe: the assistant would answer here')}")
h = rep(h, "if(current&&current!=='sources'){", "if(current){")
h = rep(h, "  $('#months').innerHTML=months.map(function(m){", "  if($('#months')) $('#months').innerHTML=months.map(function(m){")
h = rep(h, "var dateEl=$('.hero .date');dateEl.textContent='Monday, October 26 · 2 meetings today · '",
        "var dateEl=$('.hero .date');dateEl.textContent='Monday, 5 January · 3 meetings today · '")

# the Pipeline flow key is referenced only from the removed screen; harmless.
for bad in ('id="v-pipeline"', 'id="sourcesView"', 'data-tab="stalled"', 'data-tab="risk"', 'Needs attention</h2>', 'Update Salesforce</button>'):
    assert bad not in h, bad
assert h.count('class="chip" data-prompt') >= 5
open('jan.html', 'w', encoding='utf-8').write(h)
print('jan.html', len(h))

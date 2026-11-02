# Builds jan.html — the skinny January (stage-1) home — from index.html by removing what is not in the 6-week scope.
import re
h = open('index.html', encoding='utf-8').read()

def cut(s, start, end, keep_end=True):
    a = s.index(start); b = s.index(end, a)
    return s[:a] + (s[b:] if keep_end else s[:a] + s[b + len(end):])

def rep(s, a, b, count=1):
    assert a in s, a[:80]
    return s.replace(a, b, count)

h = rep(h, '<title>Producer Assistant</title>', '<title>Producer Home — January</title>')

# ---- Home: goal panel → "coming" strip
a = h.index('<!-- Goal panel'); b = h.index('<!-- Hero prompt -->')
strip = '''<!-- Goal strip: not in the January scope -->
        <section class="sources" aria-label="Goal panel coming" style="justify-content:flex-start">
          <span class="l">Your goal &amp; pace</span>
          <span style="color:var(--muted);font-size:12.5px">Booked vs goal, pace and “what closes the gap” arrive with the production data feed (stage 2). Everything below works on 4 January.</span>
        </section>

        '''
h = h[:a] + strip + h[b:]

# ---- chips: keep four
h = cut(h, '<button class="chip" data-prompt="Which of my leads haven\'t been touched?', '<button class="chip" data-prompt="Run my deal review')
h = cut(h, '<button class="chip" data-prompt="Update Salesforce: ">', '</section>')
h = rep(h, '<div class="hint">Try: “Prep me for the 2:00 with Meridian” · “Which of my renewals in Q1 have no opportunity yet?” · “Find an SME for cold-storage trucking”</div>',
        '<div class="hint">Try: “Prep me for the 2:00 with Meridian” · “What did I promise this week?” · “Capture: just met Jordan at Northwind, they want revised numbers by Nov 4”</div>')

# ---- remove Prepared-for-you and pipeline tiles
h = cut(h, '<!-- Prepared for you', '<!-- Brief + attention -->')

# ---- Today's brief: drop the BDR item, retag the brief item
h = cut(h, '<li class="item" data-kind="call">', '<li class="item" data-kind="renewal">')
h = rep(h, 'Prospect brief for Meridian Logistics is ready. Two coverage gaps flagged: cargo contingent and motor truck cargo sublimit.',
        'Prep for Meridian Logistics is ready: CRM context, the existing prospect brief and last week’s emails.')
h = rep(h, '<span class="via">Prospect Briefing · Coverage Gap Analyzer</span>', '<span class="via">Prep my next meeting</span>')
h = rep(h, '<span class="via">Pipeline Agent</span>', '<span class="via">Pipeline sweep</span>')

# ---- Needs attention: drop At risk, make Overdue default
h = rep(h, '<button class="tab active" role="tab" data-tab="risk">At risk<span class="n">3</span></button>\n', '')
h = rep(h, '<button class="tab" role="tab" data-tab="tasks">Overdue tasks', '<button class="tab active" role="tab" data-tab="tasks">Overdue tasks')
h = cut(h, '<ul class="alist" data-pane="risk">', '<ul class="alist" data-pane="renew" hidden>')
h = rep(h, '<ul class="alist" data-pane="tasks" hidden>', '<ul class="alist" data-pane="tasks">')
h = rep(h, '<div class="ph"><h2>Needs attention</h2><span class="sub">Across your book</span></div>',
        '<div class="ph"><h2>Needs attention</h2><span class="sub">From the sweep</span></div>')

# ---- Connected sources
h = rep(h, '<span class="s">Salesforce</span><span class="s">Outlook</span><span class="s">Broker AI workflows</span><span class="s">Agency management</span><span class="s">SharePoint</span><span class="s">Reports</span><span class="s">SME directory</span><a href="#sources" class="src-link">Where each block gets its data →</a>',
        '<span class="s">Salesforce</span><span class="s">Outlook · Teams</span><span class="s">Broker portal agent</span><span class="s">Existing prospect briefs</span><span class="s">SME directory</span><span class="src-link" style="cursor:default">January scope: four agents, reads and writes as you</span>')

# ---- drop Company brief, BDR and sources views
h = cut(h, '<section class="thread uc" id="v-company-brief"', '<div class="toast"')
h = rep(h, '<div class="toast"', '    </div>\n  </div>\n</div>\n\n<div class="toast"')

# ---- header
h = rep(h, '<span class="title">Producer Home</span><span class="role">Employee Benefits · P&amp;C</span>',
        '<span class="title">Producer Home</span><span class="role">January version</span>')
h = rep(h, "$('.top .title').textContent='Producer Home';", "$('.top .title').textContent='Producer Home';")

# ---- JS: views and routes
h = rep(h, """  var VIEWS={prep:['#prepView','Prep: Meridian Logistics'],sources:['#sourcesView','Where the data comes from'],
    pipeline:['#v-pipeline','Pipeline'],'deal-review':['#v-deal-review','Deal Review'],capture:['#v-capture','Capture Agent'],
    'company-brief':['#v-company-brief','Company brief'],bdr:['#v-bdr','BDR Agent']};""",
        """  var VIEWS={prep:['#prepView','Prep: Meridian Logistics'],
    pipeline:['#v-pipeline','Pipeline'],'deal-review':['#v-deal-review','Deal Review'],capture:['#v-capture','Capture Agent']};""")
h = rep(h, "    if(name==='company-brief'){var hp=!!(text&&/harbor/i.test(text)); $('#cbResult').hidden=!hp; $$('.pick').forEach(function(x){x.classList.toggle('on',hp&&x.getAttribute('data-co')==='hp')})}\n", '')
h = rep(h, "var ROUTES=[[/prep|meridian|next meeting/i,'prep'],[/pipeline/i,'pipeline'],[/deal review|promise/i,'deal-review'],[/capture/i,'capture'],[/company brief|client summary|harbor point/i,'company-brief'],[/lead|bdr/i,'bdr']];",
        "var ROUTES=[[/prep|meridian|next meeting/i,'prep'],[/pipeline/i,'pipeline'],[/deal review|promise/i,'deal-review'],[/capture|just met/i,'capture'],[/company brief|client summary|lead|bdr/i,'later']];")
h = rep(h, "    var v=c.getAttribute('data-view')||route(p);\n    if(v){e.preventDefault();showView(v,p);return}",
        "    var v=c.getAttribute('data-view')||route(p);\n    if(v==='later'){e.preventDefault();toast('Company brief and BDR Agent: stage 2 (after 4 January)');return}\n    if(v){e.preventDefault();showView(v,p);return}")
h = rep(h, "var r=route(v);if(r){showView(r,v)}else{toast('Wireframe: the assistant would answer here')}",
        "var r=route(v);if(r==='later'){toast('Company brief and BDR Agent: stage 2 (after 4 January)')}else if(r){showView(r,v)}else{toast('Wireframe: the assistant would answer here')}")
h = rep(h, "if(current&&current!=='sources'){", "if(current){")
h = rep(h, "  $$('.pick[data-co]').forEach(function(p){p.addEventListener('click',function(){\n    if(p.getAttribute('data-co')!=='hp'){toast('Wireframe: only Harbor Point Health is filled in');return}\n    $$('.pick').forEach(function(x){x.classList.toggle('on',x===p)});\n    $('#cbResult').hidden=false; $('#cbResult').scrollIntoView({behavior:'smooth',block:'start'});\n  })});\n", '')
# months chart no longer exists
h = rep(h, "  $('#months').innerHTML=months.map(function(m){", "  if($('#months')) $('#months').innerHTML=months.map(function(m){")
h = rep(h, "var dateEl=$('.hero .date');dateEl.textContent='Monday, October 26 · 2 meetings today · '+open.length+(open.length===1?' item needs':' items need')+' you';",
        "var dateEl=$('.hero .date');dateEl.textContent='Monday, 5 January · 2 meetings today · '+open.length+(open.length===1?' item needs':' items need')+' you';")
h = rep(h, '<div class="date">Monday, October 26 · 2 meetings today · 4 items need you</div>', '<div class="date">Monday, 5 January · 2 meetings today · 3 items need you</div>')

# sidebar: foot line
h = rep(h, '<div class="foot">Signed in as Dana Whitfield · Salesforce permissions apply</div>',
        '<div class="foot">Signed in as Dana Whitfield via the broker portal · Salesforce permissions apply</div>')

# scope notes in threads → January wording
h = rep(h, '<p class="scope"><b>Wave 1:</b> Opportunity, Task/Event, stage history. Writes limited to close date, next step, amount and Task, each confirmed.</p>',
        '<p class="scope"><b>January:</b> Opportunity, Task/Event, stage history. Writes limited to close date, next step, amount and Task, each confirmed. Scheduled morning run if Artemis supports schedules, otherwise on open.</p>')

assert 'v-company-brief' not in h and 'sourcesView' not in h and 'v-bdr' not in h
open('jan.html', 'w', encoding='utf-8').write(h)
print('jan.html', len(h))

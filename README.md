# Producer Assistant — wireframe

Clickable mid-fidelity wireframe of the home screen for an insurance producer's AI workbench: one assistant in front of the CRM, the agency management system, email and the brokerage's existing AI workflows. A concept demo; all names, clients and figures are fictional.

**Live demo:** https://julijakvetna.github.io/epic-producer-assistant-demo/
**Meeting prep (direct link):** https://julijakvetna.github.io/epic-producer-assistant-demo/#prep

**Data sources (slide view):** https://julijakvetna.github.io/epic-producer-assistant-demo/#sources · PNG for decks: `docs/data-sources-slide.png` (append `?export` to the URL for a chrome-free capture)

**Run locally:** clone and open `index.html` in a browser. No build step, no dependencies beyond Google Fonts.

## What the screen shows

| Block | Purpose |
|---|---|
| **Goal panel** | New business booked vs annual goal with a pace marker for today, booked by month (Nov–Dec expected from pipeline), and "what closes the gap" — the live deals that would reach the number. |
| **Prompt** | One assistant for everything. Dictation lives in the mic icon; notes, next steps and tasks are captured to the CRM from there. |
| **Chips** | The agents, one tap away: Prep my next meeting · BDR Agent · Company brief · Deal Review · Capture Agent · Pipeline · Update Salesforce. Each fills the prompt. |
| **Prepared for you** | Outputs that exist right now, keyed to the calendar: a prospect brief for today's meeting, a client summary for Thursday, leads scored overnight. |
| **Pipeline tiles** | Suspects / Prospects / Opportunities / Clients from the CRM and agency management system. |
| **Today's brief** | What needs the producer, in order. Checking an item strikes it, stamps the time, and moves it under "Handled today". Open items always stay on top. |
| **Needs attention** | At risk · Renewals 90d · Overdue tasks · Stalled deals, each with one suggested action. |
| **Connected** | The sources behind the screen — makes the harness visible without a diagram. Links to the data-sources slide view. |
| **Where the data comes from** (`#sources`) | Slide-style view: the home screen schematized with numbered callouts, and for each block the systems it reads from and writes to, color-coded by source. |

Left sidebar follows a general-purpose agent harness (New chat, My Briefs, AI Workflows, Memory, Dashboards, Scheduled, Proposals) with producer labels.

## Interactions that work

- Check / uncheck items in Today's brief (re-orders the list)
- Tabs in Needs attention
- "Prep my next meeting" (chip, prepared card, or typing it) opens the meeting-prep screen; Home or New chat returns
- Every write to Salesforce runs as a chat exchange: the producer's message, then one card per record with required-field and access checks and its own Confirm / Skip; refused writes say why and offer "Ask Sales Ops"
- "Salesforce ↗" links open the record in a new tab; Capture notes can be edited in place and exported
- Every agent chip opens its own screen: Pipeline (stage board + reversible fixes), Deal Review (promises + one question at a time), Capture Agent (dictated note → what gets written), Company brief (one-click picker → internal + external brief), BDR Agent (untouched leads + first-touch draft). Direct links: `#pipeline`, `#deal-review`, `#capture`, `#company-brief`, `#bdr`
- Chips and Prepared-for-you cards fill the prompt
- Hover on monthly bars
- Light / dark theme toggle (moon icon)

Everything else is static.

## January version (`jan.html`)

The stage-1 home: what can be live on day one on an existing portal agent that already has a Today/Ask view, Outlook, Salesforce quick actions and dictation. Same shell and code as `index.html`; the stage-2 blocks are removed instead of promised.

| Block | Stage 1 |
|---|---|
| **New business strip** | Closed-won YTD, open deals and pipeline from Salesforce opportunities; goal, pace and "what closes the gap" marked as stage 2 (production feed). |
| **Prompt** | Speak or type — dictation is the headline. |
| **Chips (5)** | Prep my next meeting · Company brief · Capture Agent · Deal Review · BDR Agent. No Pipeline, no Update Salesforce. |
| **Counters** | Meetings today, emails to answer, closing this month, gone cold. |
| **Today's meetings** | From Outlook, matched to Salesforce, "Prepare me" on each (client → Company brief, prospect → Prep). |
| **Today's brief** | Decide · Review · Call back · Renewal, check-off writes the Task. |
| **Needs attention** | At risk · Renewals 90d · Overdue tasks. No Stalled deals (no pipeline sweep in stage 1). |

**Live:** https://julijakvetna.github.io/epic-producer-assistant-demo/jan.html · direct links: `jan.html#prep`, `#company-brief`, `#capture`, `#deal-review`, `#bdr`

`jan.html` is generated from `index.html` by `build_jan.py`.

## Sales Leader home (`leader.html`)

Same harness, second lens. A regional sales leader (fictional, 12 producers) sees the same agents, data and guardrails through a predefined view for his role: everything he sees is what his CRM role hierarchy already shows him; writes are Tasks on producers' deals, chat messages and his own 1:1 notes, each confirmed.

**Live:** https://julijakvetna.github.io/epic-producer-assistant-demo/leader.html · direct links: `leader.html#team-review`, `leader.html#one-on-one`

| Block | Purpose |
|---|---|
| **Team against goal** | Team booked vs goal with pace marker and Q4 commit; booked by producer (who is behind pace); "what closes the gap" — the deals, with owners, that reach the number. |
| **Chips** | Team pipeline review · Forecast · Who needs help · Prep my 1:1 · Deal Review · Stalled deals · Update Salesforce. |
| **Prepared for you** | Overnight team review, tomorrow's forecast draft, Thursday's 1:1 prep. |
| **Team tiles** | Producers (behind pace), open pipeline and coverage, Q4 commit vs needed, stalled deals. |
| **Today's brief** | Decide · Escalate · Coach · Review · Renewal — what needs the leader, in order. |
| **Needs attention** | Behind pace · Slipping deals · Single-threaded · CRM hygiene. |

Scenarios that work end to end:

- **Team pipeline review** (`#team-review`) — Monday morning run: KPIs, by-producer table with flags and week-over-week change, what slipped since last Monday, and "send the Monday nudges" → one Task per producer, confirmed one by one (with a duplicate-Task check).
- **Prep my 1:1** (`#one-on-one`) — the producer's number and activity, what she committed at the last 1:1 and its status (from the agent's Memory), suggested questions derived from her flags, her deals in three columns, and "write the 1:1 outcome" from dictation → Tasks for her and for the leader, a restricted field routed to Sales Ops, and the 1:1 note saved to Memory.

The producer flags are computed once by the pipeline sweep and shown twice — on the producer's home as "fix the reversible ones", on the leader's home rolled up by producer. Nothing the leader sees is a surprise to the producer.

## Design principle

The agents are named once, as chips under the prompt, so producers learn what the assistant can do. Everywhere else their output appears as brief items, prepared briefs and attention flags rather than as separate tools. The producer talks to one assistant, and the CRM is updated as a by-product of selling.

## Structure

```
index.html                   producer home — single self-contained page (HTML + CSS + JS)
jan.html                     stage-1 home — generated from index.html by build_jan.py
leader.html                  sales leader home — same shell, second lens
docs/data-sources-slide.png  16:9 export of the data-sources view
README.md
```

## Versions

- **v0.11** (2026-11-03) — stage-1 home rebuilt: 5 chips, counters, today's meetings, no pipeline
- **v0.10** (2026-11-02) — stage-1 home: `jan.html`

- **v0.9** (2026-11-02) — Sales Leader lens: `leader.html` with team home, Team pipeline review and Prep my 1:1

- **v0.8** (2026-10-28) — confirm-per-record write flow in the chat, validation and access checks, Salesforce links, Capture edit/export; sources slide: Power BI, data warehouse (Azure DW → Databricks), no Data Cloud
- **v0.7** (2026-10-28) — one screen per agent chip, in their wave-1 form
- **v0.6** (2026-10-27) — Briefing and Client summary merged into one "Company brief" chip (internal CRM summary + external research)
- **v0.5** (2026-10-27) — chips renamed to the agents: Prep my next meeting · BDR Agent · Briefing · Deal Review · Client summary · Capture Agent · Pipeline · Update Salesforce
- **v0.4** (2026-10-26) — "Where the data comes from" slide view with per-block source callouts; PNG export
- **v0.3** (2026-10-26) — "Prep my meeting" screen: assistant thread with a full prospect brief, back to home
- **v0.2** (2026-10-26) — goal panel added; agent cards replaced by chips + "Prepared for you"
- **v0.1** (2026-10-26) — first clickable home screen

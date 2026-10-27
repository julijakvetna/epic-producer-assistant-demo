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
- Chips and Prepared-for-you cards fill the prompt
- Hover on monthly bars
- Light / dark theme toggle (moon icon)

Everything else is static.

## Design principle

The agents are named once, as chips under the prompt, so producers learn what the assistant can do. Everywhere else their output appears as brief items, prepared briefs and attention flags rather than as separate tools. The producer talks to one assistant, and the CRM is updated as a by-product of selling.

## Structure

```
index.html                   single self-contained page (HTML + CSS + JS)
docs/data-sources-slide.png  16:9 export of the data-sources view
README.md
```

## Versions

- **v0.6** (2026-10-27) — Briefing and Client summary merged into one "Company brief" chip (internal CRM summary + external research)
- **v0.5** (2026-10-27) — chips renamed to the agents: Prep my next meeting · BDR Agent · Briefing · Deal Review · Client summary · Capture Agent · Pipeline · Update Salesforce
- **v0.4** (2026-10-26) — "Where the data comes from" slide view with per-block source callouts; PNG export
- **v0.3** (2026-10-26) — "Prep my meeting" screen: assistant thread with a full prospect brief, back to home
- **v0.2** (2026-10-26) — goal panel added; agent cards replaced by chips + "Prepared for you"
- **v0.1** (2026-10-26) — first clickable home screen

# 13. Taking the sting out of common frustrations

*Decided by Hendrik, 12 Oct 2026, accepting all proposals in the project research note
product/frustrations.md (what frustrates people most, with German survey data, and how we answer
it). Restructured the same day: each feature now lives in the topic it changes, listed below.
This file keeps the reasons and the principles.*

## Why this topic exists

The research ranked what frustrates people most on other apps. In Germany (forsa for KKH, 2025)
the top cause is **ghosting or getting no reply** (54%); Bitkom (2025) found that for 54% of
online daters a contact **rarely becomes a real meeting**, and 19% have used **AI-written chat
texts**. Earlier decisions already dealt with overwhelm, harassment, too much choice and
paywalls. The four gaps were: chats that never become a date, people going silent
mid-conversation, old or embellished photos and profiles, and AI-written chats.

## Decided: principles

1. **Help the person, never nag them for the app's sake.** Every nudge is shown inside the app,
   only to the person it concerns, never as a push notification, and can be switched off.
   Nothing is ever shown to the other person as pressure.
2. **Make the kind exit as easy as vanishing.** People ghost to avoid an awkward sentence; the
   ghosted want closure. So ending well is one tap.
3. **Give the chat a destination.** Meeting is the obvious next step, offered, not forced.
4. **Honesty through structure, not surveillance.** Chats are end-to-end encrypted; we cannot and
   will not read or classify them. Profile and message design make specific, personal content the
   easy path.
5. **Computed on the phone.** Timers, labels and nudges use timestamps the two phones already
   have. The server learns nothing new.

## Decided: the features, and where each one lives

| Item | Feature | Spec |
|---|---|---|
| **A. From chat to meeting** | | |
| A1 | "Suggest meeting" message in the chat | [04](04-conversations.md) |
| A2 | "How soon do you like to meet?" profile field | [02](02-profile-data-model.md) |
| A3 | Private nudge after a week of writing | [04](04-conversations.md) |
| A4 | "Did you meet? Did you feel safe?" check-in, for safety only | [05](05-safety.md) |
| **B. Going silent** | | |
| B1 | Ending kindly is the default (three fixed lines or free text) | [04](04-conversations.md) |
| B2 | Quiet conversations archive themselves after 30 days | [04](04-conversations.md) |
| B3 | "Waiting for your reply", visible only to you | [04](04-conversations.md) |
| B4 | Reply or end before writing to someone new (more than 8 waiting) | [04](04-conversations.md) |
| B5 | Community agreement sentence: end with a tap, don't disappear | [02](02-profile-data-model.md) |
| **C. Current, specific photos and profiles** | | |
| C1 | Photo age bands | [02](02-profile-data-model.md) |
| C2 | Verification badge with a date, renewed yearly | [05](05-safety.md) |
| C3 | "Taken in the app" photos | [02](02-profile-data-model.md) |
| C4 | Narrative prompts instead of a blank "About me" | [02](02-profile-data-model.md) |
| C5 | Soft report sub-reason "Photos don't look like the person" | [05](05-safety.md) |
| **AI. AI-written chats** | | |
| AI1 | The app never offers AI writing help | [04](04-conversations.md) |
| AI2 | The other person's profile is the writing aid, with one fixed tip | [04](04-conversations.md) |
| AI3 | Meeting sooner is the real answer (section A) | |
| AI4 | Community agreement sentence: write your own messages | [02](02-profile-data-model.md) |
| **E. Small additions** | | |
| E1 | "Take a break" screen on top of pause; no streaks or daily picks | [03](03-visibility.md) |
| E2 | No rejection counters; "expired", never "no reply" | [04](04-conversations.md) |
| E3 | Full profile opens on the texts (tried with phase 3 testers) | [03](03-visibility.md) |

## Not built

- No-chat dating and paid dates (Breeze style). They punish people who need time to feel safe.
  The chat stays; it just has somewhere to go.
- Read receipts, "last active" in chats, ghosting scores or reputations, and any notification
  that someone is waiting.
- AI detectors, "I write my own messages" badges, typing heuristics.

## Background

Project research: frustrations (product/frustrations.md), with the evidence and sources.

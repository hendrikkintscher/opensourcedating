# App spec

*Started 11 Oct 2026, restructured 12 Oct 2026. Goes through every key feature and rule of the
app, one topic at a time, before prototype code is written, so the decisions that would cause a
lot of rework later are settled first. Each topic has one file; a decision is written in exactly
one of them. The one-line index of all decisions is [docs/decisions.md](../decisions.md).*

Phases: numbers like "phase 5" refer to the seven project phases in
[docs/phases.md](../phases.md). "Before real users" always means the gate before phase 5.
"Stage 1" and "stage 2" mean the server setup (one server, then a network), see
[12](12-stage-2-network.md).

## How a topic file is laid out

Every file starts with a status line (who decided what, when, with decision numbers), then:
**Decided** sections, **Recommended, not yet decided**, **Still open**, and **Background** (which
project research notes hold the reasoning). Research notes live in the project folder, not in
this repo; where they and a spec differ, the spec wins.

## Topics, costliest to change first

"Cost" means how much code and data would have to be rewritten or migrated if we changed our
mind after the prototype is built.

| # | Topic | Cost to change later | Status |
|---|---|---|---|
| [01](01-accounts-and-identity.md) | Accounts and identity: account IDs, sign-in, devices, recovery, email | Very high: every table, chat key and block points at an account ID | decided |
| [02](02-profile-data-model.md) | Profile data model: gender labels, search groups, "looking for", profile texts, first publishing | Very high: drives the two-way filter, Art. 9 encryption and the community test | decided, except relationship dimensions |
| [03](03-visibility.md) | Who sees what, and when: six steps, per-field visibility, pause | High | decided |
| [04](04-conversations.md) | Opening messages, inbox, conversations, meeting suggestions, ending | High: shapes the relay protocol and libsignal sessions | decided |
| [05](05-safety.md) | Safety: block, report, moderation, verification, ban evasion | High: safety data lives in its own service to be shareable in stage 2 | decided, backup moderator to be named |
| [06](06-location.md) | Location tiles and travel-time bands | Medium | decided |
| [07](07-photos.md) | Photos: upload pipeline, moderation, resolutions | Medium | **open** |
| [08](08-age-check.md) | Age check (18+) | Medium: sits behind one interface so the method can change | decided, stronger check deferred to phase 5 |
| [09](09-deletion-and-retention.md) | Deletion, retention, export, inactive accounts, IP logging | Medium: designed into every store, backups included | decided, lawyer confirms ban-record period |
| [10](10-search.md) | Search and browsing: filters, sort, tags, limits, no swiping | Low to medium | decided |
| [11](11-test-bots.md) | Test bots and test data separation | Low, but needed from day one | decided |
| [12](12-stage-2-network.md) | Stage 2: one server program on sealed and plain levels | Low now, if 01, 02 and 05 are built ready for it | decided, details open |
| [13](13-frustrations.md) | Common frustrations: the reasons and principles; the features live in 02 to 05 | Low to medium | decided |
| [14](14-app-framework.md) | App framework: React Native with Expo, native libsignal module | High once built | decided |

## Principles across all topics

- **Search, never swiping.** No card stacks, no endless feed, no daily picks, no streaks
  ([10](10-search.md)).
- **No hidden ranking and no paid visibility.** Sort order is always the user's choice.
- **No "who viewed me", no "online now", no exact distance** ([03](03-visibility.md)).
- **No AI writing help** of any kind ([04](04-conversations.md)).
- **Details only become more precise when that person acts** ([03](03-visibility.md)).
- **The server learns as little as possible:** chats are end-to-end encrypted, location is only
  as precise as the person chose, nudges and timers run on the phone.
- **Built for stage 2 from the start:** account IDs, the safety service, profile storage and
  search sit behind their own interfaces ([12](12-stage-2-network.md)).

## Still open

One line each; the details are in the linked topic.

- Relationship dimensions: which dimensions, answers and layout (**not decided**, draft in the
  project research) ([02](02-profile-data-model.md)). Wording of the narrative prompts.
- Photos: the whole pipeline, number of photos, preview resolution ([07](07-photos.md)).
- Kratos passkeys in native apps: a one-day spike before building login; optional recovery PIN
  ([01](01-accounts-and-identity.md)).
- Which EU email provider ([01](01-accounts-and-identity.md)).
- Who the backup moderator is; escalation contacts per case ([05](05-safety.md)).
- The stronger age check, before real users ([08](08-age-check.md)).
- Search request rate limits ([10](10-search.md)).
- Stage 2: who holds profile content keys, sealed-server hosting, the protocol between servers,
  deletion across servers, the operator agreement ([12](12-stage-2-network.md)).
- **For the lawyer:** ban-record period and legal basis, the open-report hold, JMStV age level,
  AI Act readings for age estimation and photo verification, operator roles in stage 2,
  libsignal on iOS. The full list of questions for the lawyer and DPO is in the project research
  (legal-and-org/legal.md).

## Wording

The app, its docs and announcements never use the word "match". We say writing, answering,
conversation.

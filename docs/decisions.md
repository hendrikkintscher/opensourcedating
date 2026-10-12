# Decision log

*One line per decision, with the date and the file that holds it. This is an index: the
decision itself, with its details and reasons, lives only in the linked file. When something is
decided, add a line here and write the decision in its spec topic. Started 12 Oct 2026.*

Status words used across the docs: **decided** (Hendrik decided), **recommended** (research
suggests it, not yet confirmed), **open** (needs a decision), **deferred** (to be decided at a
named phase gate).

## Project and licence

| Decision | Decided | Where |
|---|---|---|
| Free software under AGPL-3.0-or-later, no contributor licence agreement | 11 Oct 2026 | [CONTRIBUTING.md](../CONTRIBUTING.md) |
| Public repository from the start, no patents (the reasoning is in the project research archive, patents-and-foss) | 11 Oct 2026 | this log |
| Build our own app rather than fork Alovoa (reasoning: project research archive, alovoa-dossier) | 11 Oct 2026 | this log |
| Test location is Berlin; stage 1 is one central server run by a Berlin legal entity | 11 Oct 2026 | [phases.md](phases.md), [spec 12](spec/12-stage-2-network.md) |
| Seven project phases, from planning to beyond Berlin, with gates | 12 Oct 2026 | [phases.md](phases.md) |
| **D13** Found the e.V. now, with seven founders, before any public announcement or grant press | 12 Oct 2026 | [GOVERNANCE.md](../GOVERNANCE.md) |
| **D15** Section 7 additional permission for app store distribution; the lawyer is asked once about libsignal on iOS | 12 Oct 2026 | [LICENSE-EXCEPTION](../LICENSE-EXCEPTION) |
| Every commit carries a DCO sign-off, enforced by a CI check | 12 Oct 2026 | [CONTRIBUTING.md](../CONTRIBUTING.md) |
| The word "match" is never used in the app, docs or announcements | 11 Oct 2026 | [spec README](spec/README.md) |

## App spec

| Decision | Decided | Where |
|---|---|---|
| Sign-in with Ory Kratos: passkeys first, email codes as the fallback, no passwords or phone number | 11 Oct 2026 | [01](spec/01-accounts-and-identity.md) |
| One phone per account in the pilot, no chat backup, lost phone means old chats are gone | 11 Oct 2026 | [01](spec/01-accounts-and-identity.md) |
| **D1** Account ID is a random opaque 128-bit ID, no server name, bound to the device key by a certificate | 12 Oct 2026 | [01](spec/01-accounts-and-identity.md) |
| **D3** Keep Kratos, add a device key, 24-hour recovery waiting period with a cancel notice | 12 Oct 2026 | [01](spec/01-accounts-and-identity.md) |
| **D14** EU-based transactional email provider with a DPA, minimal email content | 12 Oct 2026 | [01](spec/01-accounts-and-identity.md) |
| Two-way filtering: you only see people who are also looking for someone like you | 11 Oct 2026 | [02](spec/02-profile-data-model.md) |
| **D5** Exact age in previews, date of birth never shown | 12 Oct 2026 | [02](spec/02-profile-data-model.md) |
| **D7** Self-chosen search groups, orientation as a hidden display-only label, "looking for" as a list, no trans filter in the fake-data phases | 12 Oct 2026 | [02](spec/02-profile-data-model.md) |
| Gender labels (any number) and exactly one search group; openness and relationship status as own fields | 12 Oct 2026 | [02](spec/02-profile-data-model.md) |
| Deliberate first publishing: a profile is hidden until published; the publish step holds the privacy choices and the Art. 9 consent | 12 Oct 2026 | [02](spec/02-profile-data-model.md) |
| Six visibility steps replace like/like-back; fit checklist; "only people I write to" mode; pause; no secret "both interested" signal | 12 Oct 2026 | [03](spec/03-visibility.md) |
| One opening message per person, a reply starts the conversation, weekly allowance, 30-day expiry | 11 Oct 2026 | [04](spec/04-conversations.md) |
| Chat end to end encrypted with libsignal; the relay stores ciphertext only until delivery | 11 Oct 2026 | [04](spec/04-conversations.md) |
| Opening messages end to end encrypted; "no links" enforced on the recipient's phone; either person can end a conversation | 11 Oct 2026 | [04](spec/04-conversations.md) |
| **D17** Inbox cap of 15, allowance back after 30 days unanswered, 5 opening messages a week (2 for new or unverified accounts) | 12 Oct 2026 | [04](spec/04-conversations.md) |
| Hide, silent two-way block, report always blocks; separate safety service; message franking; ban evasion without face data | 11 Oct 2026 | [05](spec/05-safety.md) |
| **D9** Photo verification: optional on-device liveness and face comparison, only a signed yes or no leaves the phone | 12 Oct 2026 | [05](spec/05-safety.md) |
| **D16** Seven report reasons, response targets, Hendrik plus one named backup moderate | 12 Oct 2026 | [05](spec/05-safety.md) |
| No GPS: home tile on a ~500 m Berlin grid, travel-time bands, only the chosen precision stored, tile changes rate-limited | 11 Oct 2026 | [06](spec/06-location.md) |
| **D6** Precision levels 500 m, about 1.5 km (default) and district; finer location only phone to phone | 12 Oct 2026 | [06](spec/06-location.md) |
| Photos: pipeline and moderation not decided yet | open | [07](spec/07-photos.md) |
| Self-declared date of birth in the fake-data phases, stronger check before real users, only the result stored | 11 Oct 2026 | [08](spec/08-age-check.md) |
| **D10** Which stronger age check: deferred to the gate before phase 5 | 12 Oct 2026 (deferred) | [08](spec/08-age-check.md) |
| **D11** No IP logging in the fake-data phases; keyed, daily-rotated IP hashes kept 7 days before real users | 12 Oct 2026 | [09](spec/09-deletion-and-retention.md) |
| **D12** Deletion and retention package: instant deletion, open-report hold, 30-day backups, crypto-shredded photos, 2-year ban records, export, inactive accounts | 12 Oct 2026 | [09](spec/09-deletion-and-retention.md) |
| Discovery by filtered search like classic OkCupid, never swiping; 20 results per page; daily profile-view caps | 11 Oct 2026 | [10](spec/10-search.md) |
| **D4** Interest tags instead of keyword search; opt-in, reciprocal searchable profile texts; saved searches on the phone | 12 Oct 2026 | [10](spec/10-search.md) |
| **D8** Age two-way with a 5-year margin, travel time one-way, range symbols on tiles | 12 Oct 2026 | [10](spec/10-search.md) |
| Test bots: bot flag on all bot data, visible badge, generated photos, bots run from Hendrik's laptops through the public API | 11 Oct 2026 | [11](spec/11-test-bots.md) |
| **D2** Stage 2 is one server program on sealed and plain levels; sealed level only by vetted operators; shards and home servers dropped | 12 Oct 2026 | [12](spec/12-stage-2-network.md) |
| Common frustrations: meeting suggestions, kind endings, current photos, no AI writing help | 12 Oct 2026 | [13](spec/13-frustrations.md) |
| App framework: React Native with Expo, chat crypto in a native libsignal module | 11 Oct 2026 | [14](spec/14-app-framework.md) |

## Still open

Relationship dimensions (which replace "intensity") are an approved draft and **not decided**.
Everything else that is open is listed in the [spec README](spec/README.md#still-open).

The D numbers come from the design review of 12 Oct 2026, kept as a dated record in the project
research archive.

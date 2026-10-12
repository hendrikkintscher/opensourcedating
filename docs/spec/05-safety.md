# 5. Safety and moderation

*Decided by Hendrik, 11 Oct 2026. Photo verification added 12 Oct 2026 (design review decision
D9); report reasons, response times and staffing added 12 Oct 2026 (D16); dated badge, stale-photo
report and meeting check-in added 12 Oct 2026 (topic 13).*

## Decided: hide, block, report

- **Hide** removes a person from your results (undoable). **Block** is silent, both ways and
  enforced by the server. **Report** always also blocks.
- Reported users are told nothing when a report is filed; they are told, with reasons and a way
  to appeal, only when action is taken (DSA Art. 17 statement of reasons).

## Decided: the safety service

- **A separate safety service from day one.** Bans, reports, moderation decisions, verification
  status and ban-evasion records live in their own service with its own database and API, apart
  from profiles. In stage 2, vetted servers can share a ban list through that API without a
  rewrite.
- **Verifiable reports (message franking) are part of the message format from the first
  version.** Each chat message, opening messages included, carries a cryptographic commitment
  that the relay stamps on delivery. When someone reports a conversation, their phone forwards the
  messages, and moderation can check they are genuine without the server ever reading chats.

## Decided: fixed safety tips, no scanning of chats (12 Oct)

- **Every new conversation shows one fixed safety tip** to both people, for example: "Never send
  money to someone you haven't met. Stay in the app until you feel sure." It is the same text for
  everyone and does not depend on what anyone writes.
- **No scanning of chat text, not even on the phone.** No scam keyword warnings, no hint when
  someone shares a messenger handle or payment link early, and no "are you sure?" check before
  sending a message. Scams and harassment are handled by the allowance, rate limits, reports with
  franked evidence and moderation. This keeps principle 4 of [13](13-frustrations.md).

## Decided: photo verification (12 Oct, D9)

The "photo verified" search filter uses **on-device liveness and face comparison**:

- **Optional.** The face comparison needs its own explicit Art. 9 consent, separate from the
  profile consent. Saying no costs only the "photo verified" badge.
- **Nothing biometric leaves the phone.** The check runs on the phone; no selfie or face template
  is uploaded. The selfie and template are deleted after the check. The server gets only a
  signed yes or no plus the model version.
- **App attestation on the result** (Play Integrity / App Attest), because the server can't see
  the check and a modified app could fake a yes. Profile photo changes trigger a new check, and
  users can report a wrong badge. The app says plainly what the badge does and doesn't prove.
- **Before real users (gate to phase 5):** the DPO and the lawyer confirm the consent design and the AI Act
  reading (1:1 verification is outside the high-risk biometric identification category, but
  Art. 50 transparency and the DPIA still apply).
- The on-device model is open source, with a known false acceptance rate across skin tones and
  genders, and is tested before launch.
- **Dated and renewed yearly (topic 13):** the badge shows the month of the check ("verified
  Mar 2026") and lapses after twelve months until the check runs again.

## Decided: who gets in, phases 3 to 5 (12 Oct)

*Background: dangerous-people.md in the project research. Decided after looking at how open
projects (Mastodon, Lobste.rs, Tildes, Matrix, Bluesky) handle dangerous people: by admission
through people and open, transparent moderation, not by identity vendors.*

- **Invite tree.** In phases 3 to 5 every account is created from an invitation by an existing
  member. The safety service records who invited whom. Moderators can see the tree; users
  cannot, and it is never public (on a dating app that would out people).
- **Inviter accountability.** When an invited person is banned, the inviter's invite rights are
  paused for a period; repeated bans among someone's invitees end their invite rights. A
  suspension alone does not touch the inviter.
- **Inviter protection (decided 12 Oct).** A paused inviter is told only "paused for N days
  because an invitation led to a ban", never which invitee. The app tells every invitee that
  inviters have no power over their account, so a threat of "I got you in, I can get you out"
  is known to be empty.
- **Moderator approval.** A new sign-up is approved by a moderator before the profile becomes
  findable, with a short "who invited you and why do you want to join" field, as Mastodon's
  approval mode does.
- **No ID, no eID, no face data** is needed for admission in these phases. The optional
  "photo verified" badge (D9) stays as it is.
- **Later, optional:** a "verified real person" badge through public infrastructure only (the
  German eID or the EU digital identity wallet), never through a commercial ID-scan vendor,
  together with a "only verified people can write to me" setting. Not designed yet.
- **Limit.** The tree does not stop a first offence by a well-liked person, and it stops
  working once sign-up opens to all of Berlin (phase 6). Admission for phase 6 is decided
  before that phase, when the EU wallet may be available.

**Not doing, and why:** background checks and sex-offender registries (US practice, no such
registry in Germany, and no legal basis for a dating app to process criminal-record data under
GDPR Art. 10, lawyer to confirm); asking users for a Führungszeugnis (same legal problem, easy
to fake, excludes people, misses the great majority of offenders who were never convicted, and
gives false comfort); sharing bans with other companies (accusation data, defamation risk).

## Decided: ban evasion, kept clear of biometric data

To stop banned people from coming back, the safety service keeps, for a fixed period:

- a hashed email address (and a hashed phone number, if one was ever given);
- perceptual hashes of the banned account's **photo files** (for example PDQ), which recognise
  the same or a slightly edited picture uploaded again;
- device attestation signals, as a risk signal only.

It does **not** keep face templates or any face recognition data. Tying bans to a person's face
would mean keeping biometric data (GDPR Art. 9) of banned users without their consent, which
the legal research flags as the riskiest item in the safety design. File hashes are not designed
to identify a person and are not face recognition. Ban records are kept for 2 years, pending the
lawyer (see [09](09-deletion-and-retention.md)).

## Decided: reports and moderation (12 Oct, D16)

**Report reasons.** The report screen offers seven reasons:

1. Under 18
2. Fake profile or scam
3. Unwanted sexual content
4. Harassment or threats
5. Something happened when we met
6. Hate
7. Other

Reason 2 has a milder sub-choice, **"Photos don't look like the person"** (topic 13): moderation
asks for a re-verification or new photos; no ban for this alone.

**"Did you meet?" check-in (topic 13).** After an accepted meeting time has passed (see
[04](04-conversations.md)), each person's app asks privately: *Did you meet? Did you feel safe?*
"I felt unsafe" opens the report flow with reason 5. Answers never reach the other person and
feed no ranking (there is none). For the pilot only, and with its own consent, an aggregate count
(met / not met) tells us whether the design works.

**Suspend at once on a meeting report (decided 12 Oct).** One credible report with reason 5
("Something happened when we met") suspends the reported account immediately, before a
moderator has looked: the profile is hidden and no messages go in or out. A moderator confirms
the ban or lifts the suspension within 24 hours. The person is told nothing while suspended
(see above) and gets the reasons and an appeal only if the ban is confirmed. A false report
therefore costs at most a day of silence; a day in which a reported attacker could reach
another person is the greater harm. A suspension does not touch the inviter.

*Against misuse (decided 12 Oct):* the immediate effect needs an **accepted meeting
suggestion** between the reporter and the reported person (the "Did you meet?" check-in links
it automatically). A reason-5 report without one goes to the queue like any other reason, with
the 24-hour target. So nobody can silence a person they never arranged to meet, and a meeting
arranged off the app is reported the normal way.

**False reports have a cost (decided 12 Oct).** Reports are never anonymous to moderators; the
reported person never learns who reported them. The report form says that a report is a
statement we act on. A report found baseless after review is noted on the reporter's record and
weighs less next time. A report found malicious (an invented account of events) or a pattern of
baseless reports breaks the rules in the same way harassment does: a warning, then a ban. The
rules say this openly. A lifted suspension leaves no trace on the reported person's record.

**Independent reports (decided 12 Oct).** Several reports against one person weigh more only
when they are independent: from accounts in different invite subtrees, each with its own
conversation with the reported person, and not filed within the same short window. Otherwise
the moderator tool shows a cluster warning instead of "several reports".

**Earlier contacts are told after a confirmed ban for harm at a meeting (decided 12 Oct).**
When a ban after a reason-5 report is confirmed, everyone who had an accepted meeting with that
person in the last months gets one neutral notice: "Someone you met through the app was removed
for breaking our safety rules. If something happened, you can tell us or find support here",
with the report flow and the support contacts. No name of the reporter, no details of the
report. The lawyer approves the wording and the look-back period before phase 5, since the
notice points at a person on the strength of one confirmed report. If an appeal succeeds after
the notice went out, the same people get one neutral line that the earlier notice no longer
applies, and the ban record is deleted (decided 12 Oct).

**Meeting tools (decided 12 Oct).** An accepted meeting suggestion offers *Share my date* and
a *check-in timer* to a friend; both run entirely on the phone and are described in
[04](04-conversations.md#decided-the-conversation). Before a first meeting the app shows the
fixed safety tips (public place, tell a friend, own transport).

**Response targets:**

- CSAM and threats to life: immediately.
- Under 18: within a few hours.
- Everything else: within 24 hours.

**Four eyes, recusal and the other side (decided 12 Oct).** A confirmed ban and the notice
to earlier contacts need both moderators. A moderator who personally knows either person steps
aside, and the log says so (with two moderators, the other one then decides alone). An appeal
goes to the moderator who did not decide. Before confirming a ban after a meeting report, the
moderator may ask the reported person for their own franked copy of the conversation, without
saying who reported them; the suspension stays in force meanwhile. The appeal always allows the
reported person to submit their copy. Every decision is logged; the public moderation report
shows counts only, never people.

**Who moderates during the pilot:** Hendrik plus one named backup (not named yet). Both have
the escalation contacts at hand: the police, and jugendschutz.net or the BKA as the lawyer
advises.

## Recommended, not yet decided

- A report attaches the reported messages from the reporter's phone (with franking, above).
- A moderator web tool with a queue, evidence view, warn / suspend / ban and the statement of
  reasons (DSA Art. 17).

## Still open

- Admission for phase 6, once sign-up opens to everyone.
- Who the backup moderator is.
- Which escalation contacts apply to which case; wording and look-back period of the notice to
  earlier contacts; GDPR Art. 10 reading of background checks (lawyer).
- Retention: ban records are kept 2 years pending the lawyer, see
  [09](09-deletion-and-retention.md); the legal basis for keeping them after consent is
  withdrawn still needs the lawyer.

## Background

Project research: safety and moderation (security/safety-and-moderation.md), dangerous people
(security/dangerous-people.md), security baseline, legal (legal-and-org/legal.md, the answers
to the safety questions).

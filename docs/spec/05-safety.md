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

**Response targets:**

- CSAM and threats to life: immediately.
- Under 18: within a few hours.
- Everything else: within 24 hours.

**Who moderates during the pilot:** Hendrik plus one named backup (not named yet). Both have
the escalation contacts at hand: the police, and jugendschutz.net or the BKA as the lawyer
advises.

## Recommended, not yet decided

- A report attaches the reported messages from the reporter's phone (with franking, above).
- A moderator web tool with a queue, evidence view, warn / suspend / ban and the statement of
  reasons (DSA Art. 17).

## Still open

- Who the backup moderator is.
- Which escalation contacts apply to which case (lawyer).
- Retention: ban records are kept 2 years pending the lawyer, see
  [09](09-deletion-and-retention.md); the legal basis for keeping them after consent is
  withdrawn still needs the lawyer.

## Background

Project research: safety and moderation (security/safety-and-moderation.md), security
baseline, legal (legal-and-org/legal.md, the answers to the safety questions).

# 5. Safety and moderation

*Decided by Hendrik, 11 Oct 2026. Background: safety-and-moderation.md, data-security.md §8 and
§12.3, legal-gdpr-berlin.md §8 in the project research. Photo verification added 12 Oct 2026
(design review decision D9); report reasons, response times and staffing added 12 Oct 2026
(D16).*

## Already decided earlier

- **Hide** removes a person from your results (undoable). **Block** is silent, both ways and
  enforced by the server. **Report** always also blocks.
- Reported users are told nothing when a report is filed; they are told, with reasons and a way
  to appeal, only when action is taken (DSA Art. 17 statement of reasons).

## Decided now

- **A separate safety service from day one.** Bans, reports, moderation decisions, verification
  status and ban-evasion records live in their own service with its own database and API, apart
  from profiles. In stage 2, vetted servers can share a ban list through that API without a
  rewrite.
- **Verifiable reports (message franking) are part of the message format from the first
  version.** Each chat message, opening messages included, carries a cryptographic commitment
  that the relay stamps on delivery. When someone reports a conversation, their phone forwards the
  messages, and moderation can check they are genuine without the server ever reading chats.

## Photo verification (decided 12 Oct)

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
- **Dated and renewed yearly (topic 13):** the badge shows the month of the check and lapses
  after twelve months until the check runs again.

## Ban evasion, kept clear of biometric data

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

## Reports and moderation (decided 12 Oct, D16)

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

**"Did you meet?" check-in (topic 13).** After an accepted meeting time has passed, each
person's app asks privately whether they met and felt safe. "I felt unsafe" opens the report flow
with reason 5. Answers never reach the other person and feed no ranking; an aggregate count for
the pilot needs its own consent.

**Response targets:**

- CSAM and threats to life: immediately.
- Under 18: within a few hours.
- Everything else: within 24 hours.

**Who moderates during the pilot:** Hendrik plus one named backup (not named yet). Both have
the escalation contacts at hand: the police, and jugendschutz.net or the BKA as the lawyer
advises.

## Still open

- Who the backup moderator is.
- Which escalation contacts apply to which case (lawyer).
- Retention: ban records are kept 2 years pending the lawyer, see
  [09](09-deletion-and-retention.md); the legal basis for keeping them after consent is
  withdrawn still needs the lawyer.

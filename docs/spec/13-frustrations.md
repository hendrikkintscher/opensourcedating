# 13. Taking the sting out of common frustrations

*Decided by Hendrik, 12 Oct 2026, accepting all proposals in the project research notes
"user-frustrations" (what frustrates people most, with German survey data) and
"frustrations-solutions" (how we address it). This topic collects the decisions in one place;
the ones that change another topic are repeated there with a pointer back here.*

## Why this topic exists

The research ranked what frustrates people most on other apps. In Germany (forsa for KKH, 2025)
the top cause is **ghosting or getting no reply** (54%); Bitkom (2025) found that for 54% of
online daters a contact **rarely becomes a real meeting**, and 19% have used **AI-written chat
texts**. Our existing decisions already deal with overwhelm, harassment, too much choice and
paywalls. The four gaps were: chats that never become a date, people going silent
mid-conversation, old or embellished photos and profiles, and AI-written chats.

## Principles

1. **Help the person, never nag them for the app's sake.** Every nudge below is shown inside the
   app, only to the person it concerns, never as a push notification, and can be switched off.
   Nothing is ever shown to the other person as pressure.
2. **Make the kind exit as easy as vanishing.** People ghost to avoid an awkward sentence; the
   ghosted want closure. So ending well is one tap.
3. **Give the chat a destination.** Meeting is the obvious next step, offered, not forced.
4. **Honesty through structure, not surveillance.** Chats are end-to-end encrypted; we cannot and
   will not read or classify them. Profile and message design make specific, personal content the
   easy path.
5. **Computed on the phone.** Timers, labels and nudges use timestamps the two phones already
   have. The server learns nothing new.

## A. From chat to meeting

- **A1. "Suggest meeting" in the chat.** A button next to the text field opens a short form:
  what (coffee, walk, drink, other), where (free text, with a hint to pick a public place), when
  (a day and a rough time). It is sent as a special end-to-end encrypted message. The other person
  answers *yes*, *suggest another time* (the same form, pre-filled) or *not yet*. An accepted
  suggestion is pinned at the top of the chat. See [04](04-conversations.md).
- **A2. "How soon do you like to meet?" on the profile.** Four values: *after a few messages*,
  *after a week or two of writing*, *after a call first*, *no rush*. Optional, one-way (your own
  filter only), shown on the full profile and in the fit checklist. See
  [02](02-profile-data-model.md).
- **A3. A private nudge after a week.** When both sides have written on several days across more
  than a week and no meeting has been suggested, the chat shows one line, only to you: "You two
  have been writing for a week. Suggest meeting?" No notification, never shown to the other
  person, off in settings. The threshold is a setting tuned in the pilot.
- **A4. "Did you meet?" check-in, for safety only.** After an accepted meeting time has passed,
  each person's app asks privately: *Did you meet? Did you feel safe?* "I felt unsafe" opens the
  report flow with reason 5 ("Something happened when we met"). Answers never go to the other
  person and never feed any ranking (there is none). For the pilot only, and with its own
  consent, an aggregate count (met / not met) tells us whether the design works. See
  [05](05-safety.md).
- **Later, not in the prototype:** a short in-app voice or video call before meeting (after phase
  4 at the earliest); a community-maintained list of first-meeting places in Berlin offered in
  the "where" field (a few lines in the repo, nice to have).
- **Not built:** no-chat dating and paid dates (Breeze style). They punish people who need time
  to feel safe. The chat stays; it just has somewhere to go.

## B. Going silent

- **B1. Ending kindly is the default.** "End conversation" offers three fixed kind lines (for
  example "Thanks for chatting, I don't feel it's a fit. All the best." / "I've started seeing
  someone, so I'll stop here. Take care." / "I'm taking a break from dating. Be well.") and a
  free-text option. Sending one is the default; "end without a message" is a second tap. The other
  person sees the line and the closed chat, nothing else. Makes the optional message from topic 4
  the default.
- **B2. Quiet conversations archive themselves.** If neither side has written for 30 days, both
  apps move the chat to an archive with one neutral line: "This conversation went quiet." No
  blame, no notification. Either person can reopen it by writing, unless the other ended it.
- **B3. "Waiting for your reply" is visible only to you.** The chat list shows, privately, which
  conversations are waiting on you and for how long, and can sort by it. The other person never
  sees this; there are no reminders.
- **B4. Reply or end before writing to someone new.** When more than 8 conversations are waiting
  on your reply, the app asks you to answer or end some before sending a new opening message. A
  setting, on by default, number tuned in the pilot. Consistent with the allowance: limits sit on
  the sender's side, never pressure on the recipient.
- **B5. One sentence in the community agreement at first publish:** "If you lose interest, end
  the conversation with a tap. Don't just disappear."
- **Not built:** read receipts, "last active" in chats, ghosting scores or reputations, and any
  notification that someone is waiting.

## C. Photos and profiles that are current and specific

- **C1. Photo age bands.** On upload the phone reads the capture date, asks the person to confirm
  or correct it, and strips all metadata before upload. The profile shows one line per photo or
  for the set: "from the last year" / "from 1 to 2 years ago" / "older than 2 years". Self-declared,
  like everything on the profile; the point is the norm, not proof. The server stores the band,
  never the date.
- **C2. Verification with a date, renewed yearly.** The "photo verified" badge shows the month
  ("verified Mar 2026") and lapses after twelve months until the on-device check runs again.
- **C3. "Taken in the app" photos.** The in-app camera can take a photo straight into the profile;
  it gets a "taken in the app, Oct 2026" mark. Optional.
- **C4. Narrative prompts instead of a blank "About me".** The three profile texts become prompts
  that invite specifics (for example "a Saturday I'd gladly repeat", "something I've changed my
  mind about", "write to me if …"). Prompt wording is a later detail. See
  [02](02-profile-data-model.md).
- **C5. A soft report sub-reason, "Photos don't look like the person"** under reason 2.
  Moderation asks for a re-verification or new photos; no ban for this alone. See
  [05](05-safety.md).

## D. AI-written chats

- **D1. The app never offers AI writing help.** No AI openers, no reply suggestions, no
  profile-text generator. A principle of the project, alongside "no swiping".
- **D2. The other person's profile is the writing aid.** While you write an opening message,
  their prompts, tags and the fit checklist stay visible beside the text field, with one fixed
  tip: "Mention something from their profile. Short and specific beats long and polished."
- **D3. Meeting sooner is the real answer** (section A).
- **D4. One honest sentence in the community agreement:** "We can't read your chats and we won't
  try. Please write your own messages; the people here want to meet you, not your assistant."
- **Not built:** AI detectors, "I write my own messages" badges, typing heuristics.

## E. Small additions

- **A "take a break" screen** on top of the decided pause: no guilt, no "you'll miss out". No
  streaks, no "X new people", no daily picks anywhere in the app.
- **No rejection counters.** The app never shows counts of sent, unanswered or expired messages
  beyond what the allowance needs ("3 of 5 left this week"); an expired opening message is shown
  as "expired", never as "no reply".
- **Full profile opens on the texts**, with the fit checklist; photos one swipe up. Tried with
  the phase 3 testers; the preview stays as decided in topic 3.

## Accepted leaks and costs

- A meeting suggestion is a message type the relay can distinguish only by size, not content; it
  is encrypted like any other message.
- A3 and B2 rely on both phones agreeing on timestamps; a clock set wrong on one phone only
  affects what that phone shows.
- Photo age bands and "taken in the app" marks are claims, not proof; a modified app could fake
  them. They set a norm, the verification badge (with app attestation) carries the proof.

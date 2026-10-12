# 4. Opening messages and conversations

*Decided by Hendrik, 11 Oct 2026. Inbox cap and allowance numbers added 12 Oct 2026 (design
review decision D17); ending kindly, inbox sorting and filters added 12 Oct 2026 (topic 3);
meeting suggestions and going silent added 12 Oct 2026 (topic 13, see
[13](13-frustrations.md) for the reasons).*

## Decided: the opening message

- **Anyone can send one text-only opening message to anyone whose profile they can see.** The
  recipient starts the conversation by answering; until then the sender can't send more to that
  person.
- **Weekly allowance** of opening messages (numbers below). It encourages people to choose
  carefully and stops mass messaging. An opening message that gets an answer doesn't count
  against the allowance a second time.
- **Unanswered opening messages disappear after 30 days.** No read receipts on them. Not
  answering is a normal, silent "no".
- **Opening messages are end-to-end encrypted like the rest of the chat.** The sender's phone
  encrypts to the recipient's published prekeys. The server never reads them; it only checks and
  counts them against the sender's weekly allowance and enforces "one per person".
- **"Text only, no links" is enforced on the recipient's phone**, which does not render links or
  attachments in an opening message. The sender's app also prevents them, but a modified app
  could not get around the recipient's side.
- **Spam is handled by the allowance, rate limits and reports.** Every opening message can be
  reported or blocked directly; reporting forwards it from the recipient's phone to moderation
  and always blocks.
- **The other person's profile is the writing aid.** While you write an opening message, their
  prompts, tags and the fit checklist stay visible beside the text field, with one fixed tip:
  "Mention something from their profile. Short and specific beats long and polished."
- **The app never offers AI writing help:** no AI openers, no reply suggestions, no
  profile-text generator.

## Decided: inbox cap and allowance (12 Oct, D17)

- **Inbox cap:** at most 15 unanswered opening messages wait in someone's inbox. The recipient
  can change the number in settings. When the inbox is full, a sender gets a notice that it is
  full, with no number, and keeps the allowance for that message.
- **Allowance returned on expiry:** when an opening message expires unanswered after the full 30
  days, the sender gets that allowance back. Silence the sender can't control is not punished.
- **Weekly allowance:** 5 opening messages per week; 2 per week for accounts under two weeks old
  or without verification. The numbers are starting values and get tuned with pilot data.
- **No rejection counters.** The app never shows counts of sent, unanswered or expired messages
  beyond what the allowance needs ("3 of 5 left this week"); an expired opening message is shown
  as "expired", never as "no reply".
- **Accepted leak:** the "full" notice tells a sender that the recipient gets many messages (yes
  or no only, never a count).

## Decided: the recipient's inbox (12 Oct)

- **Sorting is the recipient's choice:** newest, oldest, shortest travel time, or best fit. No
  hidden ordering.
- **Inbox filters:** the recipient can hide opening messages from, for example, unverified
  accounts. Filtering happens on the recipient's phone, since opening messages are end-to-end
  encrypted. Hidden messages still expire normally after 30 days.
- **No pressure:** no read receipts, no "someone is waiting" notices, no reminders to answer.

## Decided: the conversation

- **Chat is end-to-end encrypted with libsignal**; the relay holds ciphertext only until
  delivery.
- **"Suggest meeting" in the chat.** A button next to the text field opens a short form: what
  (coffee, walk, drink, other), where (free text, with a hint to pick a public place), when (a
  day and a rough time). It is sent as a special end-to-end encrypted message. The other person
  answers *yes*, *suggest another time* (the same form, pre-filled) or *not yet*. An accepted
  suggestion is pinned at the top of the chat.
- **A private nudge after a week.** When both sides have written on several days across more
  than a week and no meeting has been suggested, the chat shows one line, only to you: "You two
  have been writing for a week. Suggest meeting?" No notification, never shown to the other
  person, off in settings. The threshold is a setting tuned in the pilot.
- **"Waiting for your reply" is visible only to you.** The chat list shows, privately, which
  conversations are waiting on you and for how long, and can sort by it. No reminders.
- **Quiet conversations archive themselves.** If neither side has written for 30 days, both apps
  move the chat to an archive with one neutral line: "This conversation went quiet." No blame, no
  notification. Either person can reopen it by writing, unless the other ended it.
- **Reply or end before writing to someone new.** When more than 8 conversations are waiting on
  your reply, the app asks you to answer or end some before sending a new opening message. A
  setting, on by default, number tuned in the pilot. Limits sit on the sender's side, never
  pressure on the recipient.

## Decided: ending a conversation

- **Either person can end a conversation at any time.** The server then refuses all further
  messages between the two, and neither can send a new opening message to the other. Unlike a
  block, both can still appear in each other's search.
- **Ending kindly is the default.** "End conversation" offers three fixed kind lines (for
  example "Thanks for chatting, I don't feel it's a fit. All the best." / "I've started seeing
  someone, so I'll stop here. Take care." / "I'm taking a break from dating. Be well.") and a
  free-text option. Sending one is the default; "end without a message" is a second tap. The
  other person sees the line and the closed chat, nothing else.

## Not built

Read receipts, "last active" in chats, ghosting scores or reputations, any notification that
someone is waiting, AI detectors or "I write my own messages" badges.

## Accepted leaks and costs

- A meeting suggestion is a message type the relay can distinguish only by size, not content.
- The nudge and the quiet-chat archive rely on both phones agreeing on timestamps; a clock set
  wrong on one phone only affects what that phone shows.

## Rejected alternative

A server that can read opening messages to filter spam centrally. Rejected because the first
message of every contact would sit readable on the server.

## Recommended, not yet decided

- Photos in chat off for the prototype.
- Push notifications never carry content (empty "new message" payloads).

## Still open

- **Future idea:** the weekly allowance could later be set relative to the number of available
  profiles (for example, the profiles that fit the sender's search) instead of a fixed number.
- **Later, not in the prototype:** a short in-app voice or video call before meeting (after
  phase 4 at the earliest); a community-maintained list of first-meeting places in Berlin for the
  "where" field.

## Background

Project research: visibility (product/visibility.md), frustrations (product/frustrations.md),
security baseline (chat relay).

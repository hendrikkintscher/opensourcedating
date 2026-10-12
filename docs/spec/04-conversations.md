# 4. Opening messages and conversations

*Decided by Hendrik, 11 Oct 2026. Builds on [profile-discovery.md](../design/profile-discovery.md)
(section 4, Messaging). Inbox cap and allowance numbers added 12 Oct 2026 (design review
decision D17).*

## Already decided earlier

- Anyone can send one text-only opening message to anyone whose profile they can see. The
  recipient starts the conversation by answering; until then the sender can't send more.
- Weekly allowance of opening messages (starting at 5, lower for new accounts).
- Unanswered opening messages disappear after 30 days; no read receipts on them.
- Chat is end-to-end encrypted with libsignal; the relay holds ciphertext only until delivery.

## Decided now

- **Opening messages are end-to-end encrypted like the rest of the chat.** The sender's phone
  encrypts to the recipient's published prekeys. The server never reads them; it only checks and
  counts them against the sender's weekly allowance and enforces "one per person".
- **"Text only, no links" is enforced on the recipient's phone**, which does not render links or
  attachments in an opening message. The sender's app also prevents them, but a modified app
  could not get around the recipient's side.
- **Spam is handled by the allowance, rate limits and reports.** Reporting an opening message
  forwards it from the recipient's phone to moderation (and always blocks).
- **Either person can end a conversation at any time.** The server then refuses all further
  messages between the two, and neither can send a new opening message to the other. Unlike a
  block, both can still appear in each other's search.
- **Ending kindly (decided 12 Oct):** when ending, the person can send one optional fixed
  message, for example "Thanks for chatting, I don't think we're right for each other. All the
  best." Ending is as easy as disappearing, but clearer for the other person.

## Inbox cap and allowance (decided 12 Oct, D17)

- **Inbox cap:** at most 15 unanswered opening messages wait in someone's inbox. The recipient
  can change the number in settings. When the inbox is full, a sender gets a notice that it is
  full, with no number, and keeps the allowance for that message.
- **Allowance returned on expiry:** when an opening message expires unanswered after the full 30
  days, the sender gets that allowance back. Silence the sender can't control is not punished.
- **Weekly allowance:** 5 opening messages per week; 2 per week for accounts under two weeks old
  or without verification. The numbers are starting values and get tuned with pilot data.
- **Accepted leak:** the "full" notice tells a sender that the recipient gets many messages (yes
  or no only, never a count).
- **Future idea, not decided:** the weekly allowance could later be set relative to the number
  of available profiles (for example, the profiles that fit the sender's search) instead of a
  fixed number.

## Recipient's inbox (decided 12 Oct)

- **Sorting is the recipient's choice:** newest, oldest, shortest travel time, or best fit. No
  hidden ordering.
- **Inbox filters:** the recipient can hide opening messages from, for example, unverified
  accounts. Filtering happens on the recipient's phone, since opening messages are end-to-end
  encrypted. Hidden messages still expire normally after 30 days.
- **No pressure:** no read receipts, no "someone is waiting" notices, no reminders to answer.

## Rejected alternative

A server that can read opening messages to filter spam centrally. Rejected because the first
message of every contact would sit readable on the server.

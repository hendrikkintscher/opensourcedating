# 4. Opening messages and conversations

*Decided by Hendrik, 11 Oct 2026. Builds on [profile-discovery.md](../design/profile-discovery.md)
(section 4, Messaging).*

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

## Rejected alternative

A server that can read opening messages to filter spam centrally. Rejected because the first
message of every contact would sit readable on the server.

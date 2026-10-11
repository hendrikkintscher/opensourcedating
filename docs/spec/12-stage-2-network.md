# 12. Stage 2: a network of servers

*Decided by Hendrik, 11 Oct 2026. Stage 1 (the Berlin pilot) stays one server.*

## Decided

- **A vetted network.** Only servers whose operators sign a shared safety policy can join, and
  they share one ban list through the safety service (see [05](05-safety.md)). Rejected: an open
  network like Mastodon (a banned person moves to the least strict server; profiles reach servers
  nobody checked) and pure phone-to-phone (bans can't be enforced, IP addresses are exposed,
  messages only arrive while both phones are on).
- **No single server holds a full profile.** Profile information is encrypted, split into pieces
  and stored redundantly across several servers, so that a defined share of servers can fail or
  go offline without the profile being lost. One server's breach or operator alone can't read a
  whole profile.
- **Servers are primarily for brokering contact, not for storage:** helping people find each
  other, passing on opening messages and encrypted chat, enforcing blocks and bans.
- Account IDs already include the home server (see [01](01-accounts-and-identity.md)).

## To be worked out

- **What exactly search needs, and where it can be read.** Filtering (gender and "looking for",
  age, travel time, relationship type, keywords) needs some data in readable form somewhere. If
  no server holds a full profile, we have to decide which search fields exist, in what form
  (coarse, hashed, encrypted), and on which servers. This decides what our servers actually do.
  Ties in with the "who sees what, and when" topic and the photo and profile storage topic.
- **Who holds the keys** to the profile pieces (the owner's phone, the servers together, or
  both), and how a person viewing a profile gets to see it.
- **Splitting method:** encryption plus redundancy coding (any k of n pieces rebuild the data)
  or secret sharing (fewer than k pieces reveal nothing). The values of k and n.
- How deletion reaches every piece, and the joint-controller agreement between operators.

## What stage 1 must do so this isn't a rewrite

- Profile storage sits behind its own interface in the server code, so the single-server store
  can later be replaced by distributed storage without touching search, chat or safety.
- Search reads only the fields it needs through a separate interface, never the full profile.

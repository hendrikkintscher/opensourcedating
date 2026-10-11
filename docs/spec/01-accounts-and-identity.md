# 1. Accounts and identity

*Decided by Hendrik, 11 Oct 2026.*

## Decisions

- **Sign-in:** Ory Kratos with passkeys plus email one-time codes. No passwords, no phone number
  required. (Decided earlier, see data-security.md §12.2 in the project research.)
- **Account ID:** a random, opaque ID combined with the home server's domain, for example
  `k7f3q…@berlin.example`, from day one. Every table, chat key, block and report refers to this
  ID. The email address is only a login detail and is never used as a key or shown to anyone.
  This keeps the data model ready for stage 2 (a network of servers) without a migration.
- **One phone per account during the pilot.** Signal-protocol multi-device support is extra work
  and can be added later without changing the account ID.
- **No chat backup in the pilot.** Chats exist only on the phone.
- **Lost or new phone:** the account comes back by signing in with an email code. Old chats are
  gone. The app creates new chat keys, and the people the user was writing with see a notice
  that the security code changed. An encrypted chat backup is possible later.

## Follows from this

- Sessions are listed in settings, with "log out everywhere".
- Re-authentication before deleting the account, exporting data or changing the email address.
- Signing in on a second phone ends the first phone's session and chat keys.

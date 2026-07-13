---
title: "Access - Independent MFA for infrastructure applications"
url: "https://developers.cloudflare.com/changelog/post/2026-07-01-ssh-mfa-piv-keys/"
date: "2026-07-01"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Access for Infrastructure now supports independent multi-factor authentication (MFA) for SSH connections using YubiKey PIV keys. This adds a hardware-backed second factor to SSH access, ensuring that a compromised device session alone is not sufficient to reach your servers. With per-application and per-policy configuration, you can enforce PIV key authentication for sensitive usernames (for example, root ) while applying different requirements for other usernames.

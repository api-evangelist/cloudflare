---
title: "Email security - Post-quantum key exchange for MX deployments"
url: "https://developers.cloudflare.com/changelog/post/2026-08-17-post-quantum-key-exchange-mx/"
date: "2026-08-17"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare Email Security now supports post-quantum hybrid key exchange with X25519MLKEM768 on the SMTP connections we make to receive and deliver mail. Deploying Email Security in front of a provider that supports post-quantum hybrid key agreement (like Google Workspace) will create a TLS 1.3 connection using post-quantum key agreement. Inbound MX connections and outbound delivery connections now negotiate the X25519MLKEM768 hybrid key agreement when the peer supports it, protecting SMTP traffic against harvest-now, decrypt-later ↗ attacks.

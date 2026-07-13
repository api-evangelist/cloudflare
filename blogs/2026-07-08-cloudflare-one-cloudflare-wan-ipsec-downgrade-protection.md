---
title: "Cloudflare One, Cloudflare WAN - IPsec downgrade protection (beta)"
url: "https://developers.cloudflare.com/changelog/post/2026-07-08-ipsec-downgrade-protection/"
date: "2026-07-08"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare IPsec now supports the IKE_SA_INIT_FULL_TRANSCRIPT_AUTH IKEv2 extension to protect against downgrade attacks on IPsec tunnels. IKEv2's original authentication design has each endpoint sign only its own outbound messages, not the full handshake transcript. A quantum-capable on-path attacker can exploit this to bypass post-quantum key exchange by downgrading the connection to classical cryptography.

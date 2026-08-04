---
title: "SSL/TLS - Faster and more secure TLS handshakes to your origins, automatically"
url: "https://developers.cloudflare.com/changelog/post/2026-07-21-automatic-origin-key-exchange/"
date: "2026-07-21"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare now takes the guesswork out of TLS 1.3 key agreement with your origins. Automatic key exchange predicts the preferred algorithm and sends its key share in the first ClientHello , helping avoid a HelloRetryRequest and one extra network round trip. Automatic key exchange is on for all existing zones and on by default for new zones.

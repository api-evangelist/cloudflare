---
title: "Radar - TLS bug detection in the Cloudflare Radar post-quantum checker"
url: "https://developers.cloudflare.com/changelog/post/2026-05-29-radar-pq-tls-bug-detection/"
date: "2026-05-29"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
The Radar post-quantum TLS support checker now also reports TLS bugs detected during the handshake test. When a scanned host exhibits compatibility issues, the results include details on the specific bugs detected, along with guidance on how to investigate and remediate each issue. The bugs section only appears for hosts where issues are found.

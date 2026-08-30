---
title: "Access - Access service token secrets use a scannable format"
url: "https://developers.cloudflare.com/changelog/post/2026-08-26-service-token-secret-format/"
date: "2026-08-26"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare Access service token Client Secrets created on or after August 26, 2026, use the format cfast_[40 alphanumeric characters][8-character checksum] . The prefix and checksum make these credentials easier for secret scanning tools to identify with fewer false positives. Existing service token secrets continue to work and do not require rotation.

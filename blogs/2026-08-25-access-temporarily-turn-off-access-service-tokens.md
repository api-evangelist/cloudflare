---
title: "Access - Temporarily turn off Access service tokens"
url: "https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-status-controls/"
date: "2026-08-25"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare Access administrators can now temporarily turn off service tokens without deleting them. A disabled token cannot authenticate, but its configuration remains available so administrators can turn it on again later. Turning off a token also stops any previous secret in an active rotation grace period.

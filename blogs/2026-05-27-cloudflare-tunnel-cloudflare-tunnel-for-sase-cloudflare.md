---
title: "Cloudflare Tunnel, Cloudflare Tunnel for SASE - Cloudflare Tunnel now runs connectivity pre-checks at startup"
url: "https://developers.cloudflare.com/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/"
date: "2026-05-27"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Starting with cloudflared version 2026.5.2 , Cloudflare Tunnel automates the entire connectivity pre-checks workflow directly inside the binary. Previously, customers had to install dig and netcat and run those commands by hand to verify their environment. Now cloudflared does it natively at startup — and surfaces actionable remediation when something is blocked.

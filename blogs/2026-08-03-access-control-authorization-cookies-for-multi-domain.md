---
title: "Access - Control authorization cookies for multi-domain Access applications"
url: "https://developers.cloudflare.com/changelog/post/2026-08-03-eager-redirect-cookie-setting/"
date: "2026-08-03"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare Access administrators can now control whether a self-hosted application preemptively sets authorization cookies across its public hostnames. Previously, Access automatically used eager redirects for applications with five or fewer hostnames. Applications with more than five hostnames received cookies as users visited each hostname.

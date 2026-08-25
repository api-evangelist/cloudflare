---
title: "WAF - Leaked credentials detection now scans Authorization headers"
url: "https://developers.cloudflare.com/changelog/post/2026-08-20-leaked-credentials-authorization-header/"
date: "2026-08-20"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Leaked credentials detection now scans the Authorization request header for Basic Authentication credentials. Previously, the detection only inspected request bodies, query strings, and headers for well-known web applications or custom detection locations, which meant credentials sent through HTTP Basic Authentication were not covered by default. This new default scan location decodes the Authorization: Basic header and compares the extracted username and password against Cloudflare's database of leaked credentials, the same way as other default scan locations.

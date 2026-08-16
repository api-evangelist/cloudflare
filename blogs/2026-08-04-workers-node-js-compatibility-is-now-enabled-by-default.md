---
title: "Workers - Node.js compatibility is now enabled by default"
url: "https://developers.cloudflare.com/changelog/post/2026-08-04-nodejs-compat-default/"
date: "2026-08-04"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Workers now enable the nodejs_compat and nodejs_compat_v2 compatibility flags by default for compatibility dates of 2026-08-04 or later. These flags are not used for these compatibility dates because the compatibility date enables the same behavior. This means all Node.js built-in APIs supported by the Workers runtime are available by default, including node:crypto , node:buffer , node:stream , node:net , node:dns , node:fs , node:http , and more.

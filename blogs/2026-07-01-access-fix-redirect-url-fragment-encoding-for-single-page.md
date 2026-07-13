---
title: "Access - Fix redirect URL fragment encoding for single-page applications"
url: "https://developers.cloudflare.com/changelog/post/2026-07-01-spa-redirect-fragment-fix/"
date: "2026-07-01"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Access now correctly preserves URL fragment characters ( / , ? , = , & , ; ) when redirecting users back to an application after login. Previously, these characters were encoded with encodeURIComponent , which mangled fragment-based routes used by single-page applications (SPAs).

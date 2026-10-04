---
title: "Rules - Compare dynamic values in Rules expressions"
url: "https://developers.cloudflare.com/changelog/post/2026-10-01-dynamic-comparison-values/"
date: "2026-10-01"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare Rules expressions now support dynamic values on both sides of equality and ordering comparisons. You can compare request fields or function results with one another. For example, compare the current request path with its original value: http.request.uri.path ne raw.http.request.uri.path For supported operators and examples, refer to Compare dynamic values .

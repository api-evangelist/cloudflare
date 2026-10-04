---
title: "Rules - concat() now supports up to 32 arguments"
url: "https://developers.cloudflare.com/changelog/post/2026-09-22-concat-argument-limit/"
date: "2026-09-22"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
The concat() function in Cloudflare Rules now accepts up to 32 arguments, increased from 16. This allows you to build richer dynamic values directly in Rules expressions and simplify configurations that combine request data. A common use case is adding a request header that sends context to your origin.

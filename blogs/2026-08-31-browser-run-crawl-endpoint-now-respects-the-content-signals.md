---
title: "Browser Run - Crawl endpoint now respects the Content Signals `use` directive"
url: "https://developers.cloudflare.com/changelog/post/2026-08-31-crawl-content-use/"
date: "2026-08-31"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
The /crawl endpoint now respects the use directive of the Content Signals ↗ standard, letting site owners express the maximum level at which their content may be used. You can declare your intended level with the new contentUse parameter. Allowed values, from least to most permissive, are reference and full , and the default is full .

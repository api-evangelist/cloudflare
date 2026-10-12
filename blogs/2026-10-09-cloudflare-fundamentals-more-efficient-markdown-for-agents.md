---
title: "Cloudflare Fundamentals - More efficient Markdown for Agents conversion"
url: "https://developers.cloudflare.com/changelog/post/2026-10-09-markdown-for-agents-in-process-conversion/"
date: "2026-10-09"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Markdown for Agents now converts HTML with an in-process streaming engine at the edge. It processes content as it arrives instead of buffering the HTML response and sending it to a separate conversion service. This reduces conversion overhead and memory use.

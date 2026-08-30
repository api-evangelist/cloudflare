---
title: "AI Search - Store larger custom metadata values in AI Search"
url: "https://developers.cloudflare.com/changelog/post/2026-08-25-larger-custom-metadata-values/"
date: "2026-08-25"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
AI Search supports larger custom metadata values within a shared 10 KiB metadata envelope for each vector. The envelope includes AI Search system metadata and JSON overhead, so it is not a per-field limit. The first 64 UTF-8 bytes of each indexed string remain filterable.

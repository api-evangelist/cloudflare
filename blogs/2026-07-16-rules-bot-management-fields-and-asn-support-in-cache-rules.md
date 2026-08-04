---
title: "Rules - Bot management fields and ASN support in Cache Rules"
url: "https://developers.cloudflare.com/changelog/post/2026-07-16-cache-rules-bot-fields-asn/"
date: "2026-07-16"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Bot management fields and ASN support in Cache Rules Cache Rules now supports bot management fields and the ip.src.asnum field in expression filters. You can now build cache policies that differentiate between automated and human traffic, or segment caching behavior by autonomous system number (ASN). This allows you to apply different caching strategies for verified bots, high-risk traffic, or specific network operators without affecting legitimate user requests.

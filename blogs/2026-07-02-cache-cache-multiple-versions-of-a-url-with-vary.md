---
title: "Cache - Cache multiple versions of a URL with Vary"
url: "https://developers.cloudflare.com/changelog/post/2026-07-02-vary-for-cache-rules/"
date: "2026-07-02"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Your origin can serve different responses for the same URL — different languages based on Accept-Language , or different formats based on Accept — by returning a Vary response header. Cloudflare's cache now honors that header directly in Cache Rules , so the same URL can hold multiple cached versions and each request is matched to the right one. Content that previously had to bypass cache to stay correct can now be cached, following standard HTTP caching behavior .

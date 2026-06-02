---
title: "Cache - BYPASS status now returned for uncacheable responses"
url: "https://developers.cloudflare.com/changelog/post/2026-05-26-bypass-status-for-uncacheable-responses/"
date: "2026-05-26"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare now returns a BYPASS cache status whenever a response is not cacheable, instead of the previous mix of BYPASS and MISS that depended on why Cloudflare chose not to cache the response. There are multiple reasons Cloudflare may refuse to cache a response — for example, the response exceeds the maximum cacheable file size for your plan, the origin sends Cache-Control: no-cache , private , or max-age=0 , the response includes a Set-Cookie header, or the request includes an Authorization header. Previously, only some of these conditions returned BYPASS .

---
title: "Rules - Handle missing values with coalesce()"
url: "https://developers.cloudflare.com/changelog/post/2026-10-01-coalesce-function/"
date: "2026-10-01"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
The coalesce() function returns the first argument that is not nil. Use it to provide a fallback in rule expressions: http.request.uri.path eq coalesce(http.request.uri.args["expected_path"][0], "/") For details, refer to the coalesce() function reference .

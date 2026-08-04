---
title: "Gateway - New header control options for Gateway HTTP policies"
url: "https://developers.cloudflare.com/changelog/post/2026-07-17-http-request-header-manipulation/"
date: "2026-07-17"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare Gateway now supports advanced header control on Allow policies . Administrators can add, overwrite, or delete headers on matching requests using static values or dynamic variables. Header operations Gateway HTTP policies using the Allow action support three operations in rule_settings : Operation API field Behavior Add add_headers Appends a value to the header.

---
title: "Cloudflare Fundamentals - Improved SCIM 2.0 group synchronization"
url: "https://developers.cloudflare.com/changelog/post/2026-08-21-scim-put-group-synchronization/"
date: "2026-08-21"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Dashboard SCIM now supports replacing groups using HTTP PUT , as defined by RFC 7644 section 3.5.1 ↗ . This allows identity providers to synchronize a group's full state, including its display name, external ID, and members, in a single request. What's New Group replacement via PUT : Full-state group synchronization improves compatibility with identity providers that use replacement semantics and helps keep Cloudflare groups aligned with their source identity provider.

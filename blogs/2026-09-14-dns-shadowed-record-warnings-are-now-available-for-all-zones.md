---
title: "DNS - Shadowed record warnings are now available for all zones"
url: "https://developers.cloudflare.com/changelog/post/2026-09-14-shadowed-record-warnings/"
date: "2026-09-14"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare now displays warnings for shadowed records in all zones. A record is shadowed when a subdomain delegation gives authority for its name, or a name below it, to another set of nameservers. The record remains present, but your zone is not authoritative for it thus Cloudflare will not respond with it to matching DNS queries.

---
title: "DNS - Account-level DNS records quota"
url: "https://developers.cloudflare.com/changelog/post/2026-06-10-account-level-record-quota/"
date: "2026-06-10"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare now enforces DNS records quotas at the account level for Enterprise accounts. Instead of a per-zone limit, these accounts have a quota on the total number of records across all of their zones, letting you distribute records across your zones however you like — regardless of each zone's plan. Public and internal zones are counted separately, each with a default quota of 1,000,000 records.

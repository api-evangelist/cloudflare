---
title: "Logs - Account-scoped firewall events dataset in Logpush"
url: "https://developers.cloudflare.com/changelog/post/2026-06-30-account-level-firewall-events/"
date: "2026-06-30"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare Logpush now supports firewall events as an account-scoped dataset . Configure a single Logpush job at the account level to receive firewall events for every zone in the account, instead of creating and maintaining a separate job per zone. The dataset includes a new ZoneName field so you can identify which zone each event came from when consuming logs in your downstream pipeline.

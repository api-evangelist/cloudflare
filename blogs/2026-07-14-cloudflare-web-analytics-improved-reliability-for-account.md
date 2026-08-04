---
title: "Cloudflare Web Analytics - Improved reliability for account-wide Web Analytics dashboards"
url: "https://developers.cloudflare.com/changelog/post/2026-06-10-improved-reliability-for-web-analytics-dash/"
date: "2026-07-14"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare Web Analytics (Real User Monitoring) has rolled out performance optimizations to significantly improve the stability and loading speed of account-wide dashboards. For larger accounts (with >100 Web Analytics sites), loading the aggregate account-wide view would often fail, running into timeouts or unexpected interface errors due to the massive scale of parallel query processing. This update optimizes how high-volume multi-site data is queried to reduce errors and provide a snappier dashboard experience.

---
title: "Load Balancing - Load balancing analytics now filters by pool name"
url: "https://developers.cloudflare.com/changelog/post/2026-08-17-pool-name-analytics-filter/"
date: "2026-08-17"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Load balancing analytics now filters traffic data by pool name instead of pool ID, aligning the query behavior with the pool names displayed in the filter dropdown. Previously, the analytics pool filter queried by internal pool ID while displaying pool names in the UI dropdown. This mismatch caused filtering issues when pools shared similar names or when you expected results based on the visible pool name.

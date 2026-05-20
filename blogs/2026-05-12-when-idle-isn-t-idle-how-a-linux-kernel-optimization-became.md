---
title: "When \"idle\" isn't idle: how a Linux kernel optimization became a QUIC bug"
url: "https://blog.cloudflare.com/quic-death-spiral-fix/"
date: "Tue, 12 May 2026 13:00:00 GMT"
author: "Antonio Vicente"
feed_url: "https://blog.cloudflare.com/rss/"
---
We investigated a bug where CUBIC's congestion window became pinned at its minimum floor, causing a performance to plummet. The fix involved correctly measuring idle periods to distinguish RTT wait times from actual application idleness.

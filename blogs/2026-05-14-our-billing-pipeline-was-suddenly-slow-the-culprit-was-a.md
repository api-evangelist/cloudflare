---
title: "Our billing pipeline was suddenly slow. The culprit was a hidden bottleneck in ClickHouse"
url: "https://blog.cloudflare.com/clickhouse-query-plan-contention/"
date: "Thu, 14 May 2026 13:00:00 GMT"
author: "Christian Endres"
feed_url: "https://blog.cloudflare.com/rss/"
---
When a partitioning change to our petabyte-scale ClickHouse cluster caused critical billing jobs to stall, standard metrics showed no obvious errors. This post explores how we identified severe lock contention in ClickHouse's query planner and built upstream patches to fix it.

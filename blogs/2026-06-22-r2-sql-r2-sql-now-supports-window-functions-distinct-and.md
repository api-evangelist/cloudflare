---
title: "R2 SQL - R2 SQL now supports window functions, DISTINCT, and set operations"
url: "https://developers.cloudflare.com/changelog/post/2026-06-21-window-functions-distinct-set-operations/"
date: "2026-06-22"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
R2 SQL now supports window functions, SELECT DISTINCT , set operations, and additional aggregates, making it easier to write analytical queries without preprocessing your data elsewhere. R2 SQL is Cloudflare's serverless, distributed SQL engine for querying Apache Iceberg tables stored in R2 Data Catalog . New capabilities Window functions — ROW_NUMBER , RANK , DENSE_RANK , PERCENT_RANK , CUME_DIST , NTILE , LAG , LEAD , FIRST_VALUE , LAST_VALUE , NTH_VALUE , and aggregates with an OVER (...) clause, including PARTITION BY and explicit frames QUALIFY — filter rows based on a window function re

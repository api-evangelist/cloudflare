---
title: "Vectorize - Reduced end-to-end latency for vector changes"
url: "https://developers.cloudflare.com/changelog/post/2026-06-30-improved-wal-throughput/"
date: "2026-07-01"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
We have greatly improved the throughput of the Vectorize write-ahead log (WAL) . As a result, we have significantly reduced the end-to-end latency for a vector change to become queryable: median latency has dropped from 2 minutes to under 30 seconds, and p99 latency from 5 minutes to under 2 minutes. This means inserts, upserts, and deletes are reflected in query results faster, improving the freshness of semantic search, recommendation, and retrieval-augmented generation (RAG) workloads.

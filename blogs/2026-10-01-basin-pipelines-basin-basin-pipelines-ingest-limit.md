---
title: "Basin Pipelines, Basin - Basin Pipelines ingest limit increased to 1 GB/s"
url: "https://developers.cloudflare.com/changelog/post/2026-10-01-stream-ingest-limit-increase/"
date: "2026-10-01"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Each Basin Pipelines stream can now ingest up to 1 GB/s, increased from 5 MB/s. The higher per-stream limit gives high-volume application events, telemetry, and logs more room to grow without splitting ingestion across streams solely to stay within the previous limit. For the full list of stream, sink, and pipeline limits, refer to Basin Pipelines limits .

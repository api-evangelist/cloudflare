---
title: "R2 Data Catalog, R2 - R2 Data Catalog compaction now optimizes manifest files"
url: "https://developers.cloudflare.com/changelog/post/2026-07-13-r2-data-catalog-manifest-optimization/"
date: "2026-07-13"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
R2 Data Catalog , a managed Apache Iceberg catalog built into R2, now automatically optimizes manifest files as part of compaction . Manifest files track the data files that make up an Iceberg table. As a table accumulates many small or fragmented manifests, query engines must read more metadata during query planning, which slows down queries even before any data is scanned.

---
title: "R2 - R2 Data Catalog now supports read-only API tokens"
url: "https://developers.cloudflare.com/changelog/post/2026-07-09-r2-data-catalog-read-only-tokens/"
date: "2026-07-13"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
R2 Data Catalog now accepts read-only API tokens, so query engines and clients that only read data no longer need a read-write token. Previously, every catalog operation required an Admin Read & Write token, which meant read-only clients were granted more access than they needed. You can now authenticate your Iceberg engine based on your workload: Read-only operations (such as listing namespaces, loading tables, and querying data) work with an Admin Read only token (R2 Data Catalog read and R2 storage read).

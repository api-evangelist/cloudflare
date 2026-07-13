---
title: "R2 - R2 Data Catalog warns before you delete data manually"
url: "https://developers.cloudflare.com/changelog/post/2026-07-06-r2-data-catalog-delete-warnings/"
date: "2026-07-07"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
R2 Data Catalog is a managed Apache Iceberg catalog built directly into your R2 bucket. Iceberg tracks your data through a tree of metadata files, so every insert, update, and delete must go through a catalog transaction. Manually adding, modifying, or deleting objects outside the catalog can leave pointers referencing files that no longer exist, corrupting the table into an inconsistent state that is difficult to recover from.

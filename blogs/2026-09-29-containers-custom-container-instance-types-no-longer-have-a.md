---
title: "Containers - Custom Container instance types no longer have a disk to memory ratio limit"
url: "https://developers.cloudflare.com/changelog/post/2026-09-29-remove-disk-to-memory-ratio/"
date: "2026-09-29"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Containers custom instance types no longer limit disk based on memory. Previously, a custom instance type could have a maximum of 2 GB of disk for each 1 GiB of memory. You can now allocate up to the 20 GB disk maximum to any custom instance type.

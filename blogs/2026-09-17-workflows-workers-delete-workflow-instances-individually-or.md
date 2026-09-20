---
title: "Workflows, Workers - Delete Workflow instances individually or in batches"
url: "https://developers.cloudflare.com/changelog/post/2026-09-17-instance-delete/"
date: "2026-09-17"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
You can now delete one or up to 100 Workflow instances and their stored state via the Workflows API or Wrangler 4.125.0 and later. Deleting an instance frees its stored state and stops its current execution. Storage billing is based on the average daily peak.

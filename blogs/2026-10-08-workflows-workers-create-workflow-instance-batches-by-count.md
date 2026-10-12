---
title: "Workflows, Workers - Create Workflow instance batches by count or list"
url: "https://developers.cloudflare.com/changelog/post/2026-10-08-create-batch-object-form/"
date: "2026-10-08"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
createBatch() now accepts an options object that creates up to 100 Workflow instances in one call. The result lists the created instances and explains why any others were not created. To use this form in local development and get its types from wrangler types , use Wrangler 4.148.0 or later.

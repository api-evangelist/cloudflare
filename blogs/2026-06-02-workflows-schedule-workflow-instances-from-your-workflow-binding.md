---
title: "Workflows, Workers - Schedule Workflow instances directly from your Workflow binding"
url: "https://developers.cloudflare.com/changelog/post/2026-06-02-cron-workflows/"
date: "2026-06-02"
author: ""
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare Workflows now supports attaching cron schedules directly to workflow bindings in wrangler.jsonc, allowing automatic creation of Workflow instances on a recurring interval without requiring a separate Worker. This simplifies building scheduled jobs like backups and report generation while retaining Workflows' built-in retries and durable execution guarantees.

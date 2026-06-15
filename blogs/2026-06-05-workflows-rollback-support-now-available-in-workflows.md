---
title: "Workflows - Rollback support now available in Workflows"
url: "https://developers.cloudflare.com/changelog/post/2026-06-05-saga-rollbacks/"
date: "2026-06-05"
author: ""
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare Workflows now supports saga-style rollbacks, enabling developers to attach compensating logic to each step that executes in reverse order if failures occur. The feature includes independent retry and timeout configuration for rollback handlers, plus new analytics events to help debug rollback execution in production environments.

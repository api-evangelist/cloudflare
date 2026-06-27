---
title: "Workflows - Workflows rollback handlers now include step context"
url: "https://developers.cloudflare.com/changelog/post/2026-06-16-rollback-options/"
date: "2026-06-23"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Workflows makes it easier to build reliable multi-step applications that can recover when downstream systems fail. Rollback handlers now receive the original step context via a ctx object for the step being rolled back. This includes ctx.step.name , ctx.step.count , ctx.attempt , and the step config with defaults applied.

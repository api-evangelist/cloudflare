---
title: "Workers - Workers tracing now supports custom spans"
url: "https://developers.cloudflare.com/changelog/post/2026-06-16-custom-spans/"
date: "2026-06-16"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Custom trace spans can now be created using tracing.enterSpan() and appear alongside platform instrumentation. Spans nest automatically based on async context, with setAttribute() for metadata attachment and isTraced properties.

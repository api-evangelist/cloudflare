---
title: "Workers - Workers tracing — write custom spans with new startActiveSpan() and span.end() runtime APIs"
url: "https://developers.cloudflare.com/changelog/post/2026-07-28-start-active-span/"
date: "2026-07-28"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
The Workers runtime now provides built-in tracing.startActiveSpan() and span.end() APIs, allowing you to write custom spans for operations that last beyond a single callback — for example, instrumenting a stream pipeline where the span should stay open until the stream is fully consumed. This augments the existing API for writing custom spans , tracing.enterSpan() , which automatically ends a span when its callback is returned. With startActiveSpan() , the span remains open after the callback returns, and you call span.end() when the work is complete: src/index.js js import { tracing } from "c

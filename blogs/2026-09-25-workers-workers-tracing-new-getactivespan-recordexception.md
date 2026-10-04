---
title: "Workers - Workers tracing — new getActiveSpan(), recordException(), startSpan(), and setAttributes() APIs"
url: "https://developers.cloudflare.com/changelog/post/2026-09-25-custom-span-apis/"
date: "2026-09-25"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Custom spans in Workers now support more of the OpenTelemetry span API, so you can instrument more of your code and record errors directly on your spans. tracing.startSpan(name) creates a span without making it the active span, and returns it. Other spans do not nest under it.

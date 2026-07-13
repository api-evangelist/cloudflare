---
title: "Workers, Durable Objects - Track memory usage for Workers and Durable Objects in the dashboard"
url: "https://developers.cloudflare.com/changelog/post/2026-06-30-memory-usage-metrics/"
date: "2026-06-30"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
You can now monitor how much memory your Workers and Durable Objects consume across invocations with the new Memory Usage chart in the Workers Metrics tab, broken down by P50, P90, P99, and P999 percentiles. Memory usage measures the V8 isolate memory at the time of each invocation, subject to the 128 MB per-isolate limit — a single isolate can handle many concurrent requests and shares memory across them. Use the Memory Usage chart to: Track memory trends — Spot gradual increases that may indicate a memory leak before they cause Exceeded Memory errors.

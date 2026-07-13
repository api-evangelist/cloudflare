---
title: "Durable Objects, Workers - Test Durable Object eviction with new cloudflare:test helpers"
url: "https://developers.cloudflare.com/changelog/post/2026-06-25-durable-object-eviction-test-helpers/"
date: "2026-06-25"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
The @cloudflare/vitest-pool-workers package now includes evictDurableObject and evictAllDurableObjects test helpers, exported from cloudflare:test . These helpers let you test how a Durable Object behaves across evictions, simulating the production lifecycle where an idle Durable Object can be evicted from memory. For more context, refer to Lifecycle of a Durable Object .

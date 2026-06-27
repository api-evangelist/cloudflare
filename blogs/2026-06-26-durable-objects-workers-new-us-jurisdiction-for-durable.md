---
title: "Durable Objects, Workers - New `us` jurisdiction for Durable Objects"
url: "https://developers.cloudflare.com/changelog/post/2026-06-26-durable-objects-us-jurisdiction/"
date: "2026-06-26"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Durable Objects now supports a us jurisdiction , letting you create Durable Objects that only run and store data within the United States. Use the us jurisdiction when you need to keep a Durable Object's compute and storage inside the United States to meet data residency requirements. Create a namespace restricted to the us jurisdiction the same way as any other jurisdiction: // Worker export default { async fetch ( request , env ) { const usSubnamespace = env .

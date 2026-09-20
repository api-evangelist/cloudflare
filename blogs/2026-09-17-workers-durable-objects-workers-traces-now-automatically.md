---
title: "Workers, Durable Objects - Workers traces now automatically include JavaScript RPC session spans"
url: "https://developers.cloudflare.com/changelog/post/2026-09-17-javascript-rpc-session-spans/"
date: "2026-09-17"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Workers traces can now follow JavaScript RPC calls across Worker boundaries and into Durable Objects. Previously, a trace stopped at the caller's RPC boundary. The dashboard now shows the caller-side session and method calls alongside the callee invocation, nested calls, and callbacks into another Worker.

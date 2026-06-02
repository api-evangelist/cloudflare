---
title: "Browser Run - Use Browser Run Quick Actions directly from Workers"
url: "https://developers.cloudflare.com/changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/"
date: "2026-05-28"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
You can now call Browser Run Quick Actions directly from a Cloudflare Worker using the quickAction() method on the browser binding. This simplifies how Workers interact with Browser Run by removing the need for API tokens or external HTTP requests. Your Worker communicates with Browser Run directly over Cloudflare's network, resulting in simpler code and lower latency.

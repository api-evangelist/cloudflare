---
title: "Workers - Test every pull request in an isolated environment with Worker Previews"
url: "https://developers.cloudflare.com/changelog/post/2026-09-22-worker-previews/"
date: "2026-09-22"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
You can now test every change you make in an isolated, production-like environment with Worker Previews ↗︎ . Each Preview runs under the same Worker with its own code, configuration, URL, and observability, isolated from production and every other Preview. Configure each Preview Define the variables, bindings, and settings that new Previews start with in the previews block of your Wrangler configuration file .

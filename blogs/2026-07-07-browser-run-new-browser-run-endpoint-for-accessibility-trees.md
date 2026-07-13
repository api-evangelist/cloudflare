---
title: "Browser Run - New Browser Run endpoint for accessibility trees"
url: "https://developers.cloudflare.com/changelog/post/2026-07-07-browser-run-accessibility-tree-endpoint/"
date: "2026-07-07"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Browser Run now supports a standalone /accessibilityTree endpoint, giving agent and automation workflows direct access to the browser's accessibility tree for a rendered webpage. An accessibility tree is the browser's structured view of a rendered page: roles, names, states, values, and hierarchy. It is useful for accessibility tooling, but also for AI agents and automation workflows that need page structure without the noise of raw HTML or the cost of screenshots.

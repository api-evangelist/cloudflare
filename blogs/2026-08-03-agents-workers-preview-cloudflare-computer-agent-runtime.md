---
title: "Agents, Workers - Preview: @cloudflare/computer agent runtime"
url: "https://developers.cloudflare.com/changelog/post/2026-08-03-cloudflare-computer/"
date: "2026-08-03"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
We're releasing an early preview of @cloudflare/computer ↗ , an open-source agent runtime that gives every agent its own computer. The runtime dynamically orchestrates between fast, efficient isolates and full Linux containers, so the agent always runs on the right compute primitive for the task at hand. @cloudflare/computer provides a virtual filesystem backed by SQLite, which you can populate from cloud storage, source control, or any files you choose.

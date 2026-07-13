---
title: "Workers - Simpler runtime types with @cloudflare/workers-types v5"
url: "https://developers.cloudflare.com/changelog/post/2026-07-03-workers-types-v5/"
date: "2026-07-03"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
We have released version 5 of @cloudflare/workers-types . This release simplifies the package to expose only the latest runtime types. We still recommend that you generate types for your Worker using wrangler types , but if you want to use the package directly, you can install it with your package manager of choice: npm i -D @cloudflare/workers-types@latest yarn add -D @cloudflare/workers-types@latest pnpm add -D @cloudflare/workers-types@latest bun add -d @cloudflare/workers-types@latest The package now exposes two entrypoints: @cloudflare/workers-types reflects the latest compatibility date,

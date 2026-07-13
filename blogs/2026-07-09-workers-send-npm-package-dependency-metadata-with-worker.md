---
title: "Workers - Send npm package dependency metadata with Worker uploads"
url: "https://developers.cloudflare.com/changelog/post/2026-07-07-wrangler-deploy-upload-dependencies-metadata/"
date: "2026-07-09"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Wrangler now collects npm package dependency information from your project's package.json during wrangler deploy and wrangler versions upload , and includes it in the upload metadata sent to the Cloudflare API. This data, each dependency's name, declared version range, and exact installed version, enables dependency analytics and future supply chain security features such as vulnerability alerting. To opt out, set dependencies_instrumentation.enabled to false in your Wrangler configuration file: wrangler.jsonc { " dependencies_instrumentation " : { " enabled " : false } } wrangler.toml [ depen

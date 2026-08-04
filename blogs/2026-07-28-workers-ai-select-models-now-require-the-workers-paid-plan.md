---
title: "Workers AI - Select models now require the Workers Paid plan"
url: "https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/"
date: "2026-07-28"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
We are limiting Workers Free plan access to a few resource-intensive models so we can prioritize capacity for the broader Workers AI user base. This helps everyone get a more reliable inference experience, with fewer 429 and 3040 (Out of Capacity) errors. The following models now require the Workers Paid plan : @cf/moonshotai/kimi-k2.6 @cf/moonshotai/kimi-k2.7-code @cf/zai-org/glm-5.2 On the Workers Free plan, requests to these models now return a 403 HTTP error ( internal error 5035 ) prompting you to upgrade.

---
title: "Flagship - Flagship API reference now available"
url: "https://developers.cloudflare.com/changelog/post/2026-06-10-api-reference/"
date: "2026-06-10"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
The Flagship API reference is now available. You can use the Cloudflare API to create and update apps, and to create, update, delete, and list feature flags without using the dashboard. For example, create a new boolean flag with the API: curl https://api.cloudflare.com/client/v4/accounts/ $ACCOUNT_ID /flagship/apps/ $APP_ID /flags \ -H "Content-Type: application/json" \ -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN " \ -d '{ "key": "new-checkout", "enabled": true, "default_variation": "off", "variations": { "off": false, "on": true }, "rules": [] }' To create an API token, go to Account API

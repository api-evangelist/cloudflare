---
title: "Flagship - Manage Flagship from the command line with Wrangler"
url: "https://developers.cloudflare.com/changelog/post/2026-07-16-wrangler-commands/"
date: "2026-07-16"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Wrangler now includes wrangler flagship , a command suite for managing Flagship apps and feature flags from your terminal. Create an app and, if you use it from a Worker, add it to your wrangler.json or wrangler.jsonc file as a binding: wrangler flagship apps create "My Worker App" \ --binding FLAGS \ --update-config Then create flags for the behavior you want to control. Flags can be booleans, strings, numbers, or JSON values: wrangler flagship flags create new-checkout wrangler flagship flags create checkout-flow \ --variation control=old-checkout \ --variation treatment=new-checkout \ --def

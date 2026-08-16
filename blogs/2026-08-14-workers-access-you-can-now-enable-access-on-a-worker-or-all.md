---
title: "Workers, Access - You can now enable Access on a Worker or all Workers at once"
url: "https://developers.cloudflare.com/changelog/post/2026-08-14-workers-access/"
date: "2026-08-14"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
You now have two new ways to protect your Workers with Cloudflare Access . Protect an application across all its domains at once Until now, if a Worker was reachable on a route, a Custom Domain, and a workers.dev URL, you had to manually add each one to an Access application and keep the list in sync whenever routes or domains changed. Now, Access attaches the policy to the Worker itself, so every associated domain and preview URL stays protected even when its routes or domains change.

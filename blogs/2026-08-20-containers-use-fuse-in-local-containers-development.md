---
title: "Containers - Use FUSE in local Containers development"
url: "https://developers.cloudflare.com/changelog/post/2026-08-20-fuse-local-development/"
date: "2026-08-20"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Miniflare now automatically grants local Containers the Docker privileges required for Filesystem in Userspace (FUSE). This applies to wrangler dev , the Cloudflare Vite plugin, and direct Miniflare use. Miniflare grants these privileges when the local Docker daemon runs inside a virtual machine (VM).

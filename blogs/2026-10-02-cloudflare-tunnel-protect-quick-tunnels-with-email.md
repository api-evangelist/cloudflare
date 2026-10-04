---
title: "Cloudflare Tunnel - Protect Quick Tunnels with email authentication"
url: "https://developers.cloudflare.com/changelog/post/2026-10-02-protected-quick-tunnels/"
date: "2026-10-02"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
You can now restrict who can access a Quick Tunnel . Use the new --allowed-mail flag in cloudflared to require visitors to authenticate with a one-time PIN sent to their email before they reach your local service. cloudflared tunnel --url http://localhost:8080 --allowed-mail alice@example.com Previously, anyone with a trycloudflare.com URL could access the service behind it.

---
title: "Agents - Share sandbox previews through Cloudflare Tunnel"
url: "https://developers.cloudflare.com/changelog/post/2026-05-29-sandbox-named-tunnels/"
date: "2026-05-29"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Sandboxes can expose a service running inside the container on a public preview URL through the sandbox.tunnels namespace. The SDK uses cloudflared inside the sandbox so you can share a running service without configuring exposePort() or a custom domain. By default, sandbox.tunnels.get(port) creates a quick tunnel on a zero-config *.trycloudflare.com URL — no Cloudflare account, DNS record, or custom domain required.

---
title: "Cloudflare Mesh, Cloudflare One - Hostname routing for Cloudflare Mesh"
url: "https://developers.cloudflare.com/changelog/post/2026-07-02-mesh-hostname-routing/"
date: "2026-07-02"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
You can now add hostname routes to a Cloudflare Mesh node, in addition to CIDR routes. Client device Requests wiki.internal.local DNS query ↓ Cloudflare Gateway Returns a token IP, then rewrites the destination to the real private IP. 100.80.0.0/16 Hostname route ↓ Mesh node Forwards traffic to the host on the local network ↓ Private host wiki.internal.local · 10.0.0.50 Instead of managing IP ranges, you can attract traffic for a hostname to a Mesh node: Private hostname (for example, wiki.internal.local ) — reach an internal application by name, which is useful when it has an unknown or ephem

---
title: "Cloudflare Mesh, Cloudflare Tunnel, Cloudflare One, Gateway, Workers VPC - Identify Mesh, Workers VPC, and Cloudflare Tunnel replicas in network logs"
url: "https://developers.cloudflare.com/changelog/post/2026-09-29-mesh-workers-vpc-network-logs/"
date: "2026-09-29"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
You can now tell a person on a laptop apart from a Mesh node or an AI agent running on Workers, without matching on connector email addresses or Mesh IP ranges — and see exactly which Cloudflare Tunnel and cloudflared replica received each session. Gateway network logs and Zero Trust Network Session Logs now identify two new kinds of traffic: Mesh — Traffic sent from or delivered to a Cloudflare Mesh node. Previously, Mesh nodes were logged the same way as devices running the Cloudflare One Client , because Mesh nodes run the client in headless mode.

---
title: "Gateway, Cloudflare Mesh, Workers VPC - Filter Workers' public Internet traffic using Gateway policies"
url: "https://developers.cloudflare.com/changelog/post/2026-06-05-gateway-egress/"
date: "2026-06-05"
author: ""
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Workers using the cf1:network VPC binding now route their public Internet traffic through Cloudflare Gateway, where existing Zero Trust policies for DNS, HTTP, and network filtering apply automatically. This enables visibility into Worker egress through Gateway logs and enforcement of policies like DNS category filtering and destination blocking already in place for the organization.

---
title: "Gateway, Cloudflare One - Traffic Destination selector in Gateway policies"
url: "https://developers.cloudflare.com/changelog/post/2026-09-23-traffic-destination-selector/"
date: "2026-09-23"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Gateway HTTP and Network policies now include a Traffic Destination selector that identifies how traffic exits Cloudflare. This allows administrators to write policies that target specific off-ramp methods - for example, applying different rules to traffic destined for the public Internet compared to traffic routed through Cloudflare Tunnel or Cloudflare WAN. Available traffic destination values UI name API value Description Internet internet Traffic to the public Internet Cloudflare WAN cloudflare_wan Traffic through a Cloudflare WAN connection Cloudflare Tunnel cloudflare_tunnel Traffic to a

---
title: "Radar - AS-level connectivity and upstream providers on Cloudflare Radar"
url: "https://developers.cloudflare.com/changelog/post/2026-08-07-radar-as-connectivity-upstreams/"
date: "2026-08-07"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Radar expands its Routing section ↗ with two widgets on AS pages, such as AS13335 ↗ , that describe how a network reaches the rest of the Internet: the paths it takes toward the Tier-1 ↗ networks, and the mix of direct upstreams carrying its routes. Both are derived from RouteViews ↗ RIB snapshots, unioned across selected collectors. AS-level connectivity The AS-level connectivity graph aggregates the BGP paths an AS uses to reach the Tier-1 networks, unioned across all the prefixes it announces, as observed by selected RouteViews collectors.

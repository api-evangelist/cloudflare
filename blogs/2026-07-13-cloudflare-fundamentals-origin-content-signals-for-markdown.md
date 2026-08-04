---
title: "Cloudflare Fundamentals - Origin Content Signals for Markdown for Agents"
url: "https://developers.cloudflare.com/changelog/post/2026-07-13-markdown-for-agents-header-preservation/"
date: "2026-07-13"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Markdown for Agents now preserves security- and cache-relevant response headers from your origin when converting HTML to Markdown: Markdown for Agents preserves security headers such as Strict-Transport-Security (HSTS), Content-Security-Policy (CSP), X-Frame-Options , Set-Cookie , and CORS headers (for example, Access-Control-Allow-Origin ) on the converted response. Caching headers ( Cache-Control , Expires , Age ) continue to pass through. Your origin's Content Signals policy is now authoritative.

---
title: "Agents - New web_search tool in the Agents SDK, powered by the Cloudflare Web Search API"
url: "https://developers.cloudflare.com/changelog/post/2026-10-12-web-search/"
date: "2026-10-12"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
The Cloudflare Agents SDK now provides a web_search tool that searches the public web through the Cloudflare Web Search API , powered by ceramic.ai, Exa, and Linkup . When you give the web_search tool to your agent, the model provides a query and max results, and receives back a short numbered list of titles, URLs, and trimmed descriptions. When you also provide the web_fetch tool to your agent, the model is told to use it to read the pages that the web_search tool returns.

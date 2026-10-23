---
title: "Agents - New persistent browser tool in the Agents SDK, with tabs and logins that last between turns"
url: "https://developers.cloudflare.com/changelog/post/2026-10-13-persistent-browser/"
date: "2026-10-13"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
The Cloudflare Agents SDK now provides a browserTool that gives your agent a Browser Run browser it can return to on later turns. Your agent can open a website, inspect a page, and come back to it with its tabs, cookies, and login session intact while the browser session remains alive. When you give browserTool to your agent, the model writes code that drives the browser through the Chrome DevTools Protocol (CDP) .

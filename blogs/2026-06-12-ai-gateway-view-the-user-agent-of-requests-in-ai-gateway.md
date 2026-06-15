---
title: "AI Gateway - View the user agent of requests in AI Gateway logs"
url: "https://developers.cloudflare.com/changelog/post/2026-06-12-user-agent-logging/"
date: "2026-06-12"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
AI Gateway logs now capture the user agent of the client that made each request, making it easier to identify which SDK, library, or application sent the traffic flowing through your gateway. For example, you can tell apart requests coming from openai-python versus a custom application or a Cloudflare Worker. The user agent appears alongside the other details in each log entry, and you can filter logs by user agent (equals, does not equal, or contains) in the dashboard.

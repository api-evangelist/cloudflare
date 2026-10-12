---
title: "AI Gateway - Standardize provider credential error responses in AI Gateway"
url: "https://developers.cloudflare.com/changelog/post/2026-10-05-provider-credential-errors/"
date: "2026-10-06"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
AI Gateway's REST API now returns consistent responses when an AI provider rejects credentials. The change applies to POST /ai/run ↗︎ . Scenario Previous AI Gateway response New AI Gateway response ElevenLabs Provider-specific UserCredentialsError with HTTP 403 HTTP 401 with error code 2009 Google Vertex HTTP 500 for rejected credentials, with upstream retries HTTP 401 with error code 2009 ; the request fails without retrying the provider All other providers HTTP 402 or another provider-specific status for rejected credentials HTTP 401 with error code 2009 When using Unified Billing , the prov

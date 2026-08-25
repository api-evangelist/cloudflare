---
title: "Cloudflare Fundamentals - Enriched 403 responses for the Cloudflare API"
url: "https://developers.cloudflare.com/changelog/post/2026-08-20-contextual-403s/"
date: "2026-08-21"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare API 403 Forbidden responses now include a documentation_url field that links directly to the API documentation for the endpoint that was denied. This gives developers, administrators, and agents an immediate path to the relevant docs with role information instead of guessing at which role or permission they are missing for that endpoint. What's New Enriched 403 error responses : When a Cloudflare API request is denied, the error response now includes a documentation_url field that points to the documentation for that specific endpoint.

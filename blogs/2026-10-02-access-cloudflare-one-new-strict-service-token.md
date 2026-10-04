---
title: "Access, Cloudflare One - New strict service token authentication setting for Access"
url: "https://developers.cloudflare.com/changelog/post/2026-10-02-strict-service-token-authentication/"
date: "2026-10-02"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
The strict service token authentication setting applies consistent behavior to requests made with service tokens. When the setting is on for a Zero Trust organization, Access handles requests with service token headers as follows: If authentication or authorization fails, Access always returns 401 or 403 instead of redirecting the client to the login page with 302 . Only Service Auth policies can authorize the request.

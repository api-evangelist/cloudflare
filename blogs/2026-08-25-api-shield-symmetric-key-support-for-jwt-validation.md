---
title: "API Shield - Symmetric key support for JWT validation"
url: "https://developers.cloudflare.com/changelog/post/2026-08-25-symmetric-jwt-validation/"
date: "2026-08-25"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
API Shield JSON Web Token validation now supports symmetric keys that use the HS256 , HS384 , and HS512 algorithms. You can configure HMAC verification keys in the Cloudflare dashboard or with the Cloudflare API. Cloudflare never stores symmetric credentials in plaintext.

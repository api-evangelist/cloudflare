---
title: "Cloudflare Images - Images binding is now billed per unique transformation"
url: "https://developers.cloudflare.com/changelog/post/2026-07-01-binding-unique-transformations/"
date: "2026-07-01"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
The Images binding is now billed per unique transformation, matching the model already used for URL-based transformations. Repeat requests for the same combination of source image and parameters within the same calendar month are counted only once. Previously, every call to the binding counted as a separate transformation regardless of whether the image or parameters were unique.

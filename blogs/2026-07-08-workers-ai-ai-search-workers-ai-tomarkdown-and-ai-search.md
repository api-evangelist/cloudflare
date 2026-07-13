---
title: "Workers AI, AI Search - Workers AI toMarkdown and AI Search now supports GIF and BMP image conversion"
url: "https://developers.cloudflare.com/changelog/post/2026-07-08-gif-bmp-image-support/"
date: "2026-07-08"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Workers AI Markdown conversion ( toMarkdown ) now supports .gif and .bmp image files, in addition to the JPEG, PNG, WebP, and SVG formats already supported. GIF and BMP files run through the same image pipeline as other formats. Each image is resized if needed (and for animated GIFs, only the first frame is used), then passed to an object-detection model to identify what it contains.

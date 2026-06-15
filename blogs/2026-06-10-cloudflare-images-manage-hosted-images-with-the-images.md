---
title: "Cloudflare Images - Manage hosted images with the Images binding"
url: "https://developers.cloudflare.com/changelog/post/2026-06-10-hosted-images-binding/"
date: "2026-06-10"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Use the Images binding to upload, list, retrieve, update, and delete images stored in Images directly from your Worker without managing API tokens or making HTTP requests. The env.IMAGES.hosted namespace supports the following storage and management operations: .upload(image, options) — Upload a new image to your account. .list(options) — List images with pagination.

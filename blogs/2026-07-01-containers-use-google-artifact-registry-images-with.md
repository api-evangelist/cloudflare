---
title: "Containers - Use Google Artifact Registry images with Containers"
url: "https://developers.cloudflare.com/changelog/post/2026-07-01-google-artifact-registry-images/"
date: "2026-07-01"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Containers now support Google Artifact Registry images. After you configure credentials, you can use a fully qualified Google Artifact Registry image reference in your Wrangler configuration instead of first pushing the image to Cloudflare Registry. Provide the service account email with --gar-email and pipe the service account JSON key through stdin : cat | npx wrangler containers registries configure -docker.pkg.dev --gar-email= --secret-name= wrangler.jsonc { " $schema " : "./node_modules/wrangler/config-schema.json" , " containers " : [ { " image " : " -docker.pkg.dev/ / / : " } ] } wrangl

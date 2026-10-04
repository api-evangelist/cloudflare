---
title: "Containers - New scheduling policy for Containers to configure image and instance from Durable Objects"
url: "https://developers.cloudflare.com/changelog/post/2026-09-30-durable-object-scheduling-policy/"
date: "2026-09-30"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Containers now support the durable_object scheduling policy in public beta. This policy lets a Durable Object select the image and instance size for a Container at runtime instead of using one centrally managed configuration for the application. To use custom images, configure the policy and one or more named images in Wrangler: { "containers" : [ { "class_name" : "AgentComputer" , "scheduling_policy" : "durable_object" , "images" : { "base" : { "dockerfile" : "./container/Dockerfile" , }, }, }, ], } [[ containers ]] class_name = "AgentComputer" scheduling_policy = "durable_object" [ container

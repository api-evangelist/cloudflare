---
title: "WAF - Updated unsafe topic detection for AI Security for Apps"
url: "https://developers.cloudflare.com/changelog/post/2026-10-07-ai-security-for-apps-unsafe-topic-detection/"
date: "2026-10-07"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
AI Security for Apps now supports an updated set of categories for detecting unsafe topics in incoming prompts. The values available in cf.llm.prompt.unsafe_topic_categories have changed. Existing WAF custom rules remain valid, but rules that reference a removed or renamed category will no longer match that category.

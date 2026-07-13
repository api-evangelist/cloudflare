---
title: "AI Search - Manage AI Search sync jobs with Wrangler CLI"
url: "https://developers.cloudflare.com/changelog/post/2026-07-02-manage-sync-jobs/"
date: "2026-07-02"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
When you connect a data source to your AI Search instance, AI Search runs sync jobs to keep your index up to date with your content. You can now manage those jobs directly from Wrangler . For example, you can trigger a sync job from your CI/CD or automated pipelines with the jobs create command so your index refreshes when you push a change: wrangler ai-search jobs create my-instance This creates an asynchronous sync job that checks for changes in your data source, and sends new, modified, or deleted files to be indexed.

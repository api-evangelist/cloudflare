---
title: "Durable Objects, Workers - Declare Durable Object class lifecycle with `exports`"
url: "https://developers.cloudflare.com/changelog/post/2026-06-30-declarative-do-class-exports/"
date: "2026-07-04"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
A new declarative exports field in your Wrangler configuration file replaces the imperative migrations array for managing Durable Object class lifecycle. Instead of writing an ordered list of migration steps with unique tags, you declare each Durable Object class your Worker exports and Cloudflare compares that against what's already deployed to determine what Durable Object state needs to be created, renamed, or deleted. With legacy migrations, renaming ChatRoom to Room requires retaining both tagged steps: { " migrations " : [ { " tag " : "v1" , " new_sqlite_classes " : [ "ChatRoom" ] }, { "

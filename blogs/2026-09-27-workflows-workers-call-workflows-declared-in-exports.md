---
title: "Workflows, Workers - Call Workflows declared in `exports` through `ctx.exports`"
url: "https://developers.cloudflare.com/changelog/post/2026-09-27-workflow-ctx-exports/"
date: "2026-09-27"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
A Worker can now call the Workflows it declares in the exports field of its Wrangler configuration through ctx.exports . You no longer need a workflows binding to call a Workflow from the Worker that defines it. Each Workflow is keyed by class name, and has the same API as a Workflow binding: src/index.js js export default { async fetch ( request , env , ctx ) { const instance = await ctx.exports.MyWorkflow.

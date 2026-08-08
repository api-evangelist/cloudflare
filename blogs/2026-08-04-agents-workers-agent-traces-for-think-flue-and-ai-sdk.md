---
title: "Agents, Workers - Agent traces for Think, Flue, and AI SDK instrumented by Agents SDK"
url: "https://developers.cloudflare.com/changelog/post/2026-08-04-agent-tracing/"
date: "2026-08-04"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Agent tracing is now available for applications built with the Agents SDK. Traces show each agent turn alongside model calls, tool runs, approvals, token usage, and Workers runtime operations. Turn on Workers tracing in your Wrangler configuration: { "$schema" : "./node_modules/wrangler/config-schema.json" , "observability" : { "traces" : { "enabled" : true } } } [ observability .

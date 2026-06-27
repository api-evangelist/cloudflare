---
title: "Agents, Workers - Agents SDK adds background sub-agents and a unified turn entry point"
url: "https://developers.cloudflare.com/changelog/post/2026-06-26-agents-sdk-v0170/"
date: "2026-06-26"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
The latest release of the Agents SDK makes it easier to run long work in the background, drive turns through one entry point, and keep chat agents working through deploys, evictions, and reconnects. This release adds first-class detached (background) sub-agent runs with live progress and durable milestones, a single runTurn turn-admission entry point, and a large round of recovery and reliability fixes that continue converging @cloudflare/think and @cloudflare/ai-chat onto one model. Background sub-agents with progress and milestones runAgentTool can now dispatch a sub-agent without blocking t

---
title: "Workflows, Workers - Stream Workflow instance events in your Worker or via the API with .subscribe()"
url: "https://developers.cloudflare.com/changelog/post/2026-09-15-instance-event-subscriptions/"
date: "2026-09-15"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
You can now stream Workflow instance events via WorkflowInstance.subscribe() and the GET /subscribe API endpoint. Workers and HTTP clients can react to workflow and step events, including attempts, sleeps, waits, and rollbacks, without polling for instance status. A subscription first streams the entire event history of the Workflow instance.

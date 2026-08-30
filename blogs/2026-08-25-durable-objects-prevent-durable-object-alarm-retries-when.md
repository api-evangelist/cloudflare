---
title: "Durable Objects - Prevent Durable Object alarm retries when using `ctx.abort()`"
url: "https://developers.cloudflare.com/changelog/post/2026-08-25-durable-object-alarm-abort-no-retry/"
date: "2026-08-25"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
By default, an alarm interrupted by ctx.abort() retries after the Durable Object resets. Pass { retryAlarm: false } when the alarm should stop instead: src/index.js js import { DurableObject } from "cloudflare:workers" ; export class CleanupTask extends DurableObject { async alarm () { await this .ctx.storage. deleteAll (); this .ctx.

---
title: "Email Service, Queues - Subscribe to Email Sending events with Queues"
url: "https://developers.cloudflare.com/changelog/post/2026-07-15-event-subscriptions/"
date: "2026-07-15"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
You can now subscribe to Email Sending events through Queues event subscriptions and receive outbound transactional email lifecycle events on a queue. Each subscription is scoped to one sending domain — either the zone apex, such as example.com , or a verified sending subdomain, such as send.example.com . Six event types are published: message.delivered , message.deferred , message.bounced , message.failed , message.rejected , and message.complained .

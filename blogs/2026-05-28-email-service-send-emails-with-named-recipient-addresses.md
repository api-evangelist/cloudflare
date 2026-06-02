---
title: "Email Service - Send emails with named recipient addresses"
url: "https://developers.cloudflare.com/changelog/post/2026-05-28-named-email-recipients/"
date: "2026-05-28"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
You can now send emails with display names on recipient addresses in addition to the existing from support. Pass an object with email and an optional name field for to , cc , bcc , replyTo , or from : JavaScript export default { async fetch ( request , env ) { const response = await env . EMAIL .

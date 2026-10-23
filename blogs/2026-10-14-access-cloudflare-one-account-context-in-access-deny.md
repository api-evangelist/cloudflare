---
title: "Access, Cloudflare One - Account context in Access deny redirects"
url: "https://developers.cloudflare.com/changelog/post/2026-10-14-deny-redirect-account-id/"
date: "2026-10-14"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
App-aware Cloudflare Access deny redirects include an account_id query parameter when account context is available. Custom block pages can use it to identify the account that owns the application represented by kid . For example, a custom redirect can include: https://denied.example.com/?kid= &account_id= &original_url=app.example.com%2Fadmin The account ID helps block-page integrations look up applications through account-scoped APIs.

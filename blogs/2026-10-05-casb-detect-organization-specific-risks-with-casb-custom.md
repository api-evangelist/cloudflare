---
title: "CASB - Detect organization-specific risks with CASB custom finding types"
url: "https://developers.cloudflare.com/changelog/post/2026-10-05-casb-custom-findings/"
date: "2026-10-05"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare CASB now supports custom finding types , giving security teams full control over the security conditions CASB detects across their SaaS and cloud integrations. In addition to CASB's library of standard finding types, you can now write your own detection logic using Rego ↗︎ , the open-source policy language from Open Policy Agent (OPA). Use custom finding types to match your organization's own thresholds and exceptions, such as flagging admin accounts without two-factor authentication, and get higher-confidence findings to act on.

---
title: "WAF - WAF Release - 2026-08-26 - Emergency"
url: "https://developers.cloudflare.com/changelog/post/2026-08-26-emergency-waf-release/"
date: "2026-08-26"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
This emergency release updates an existing Next.js remote code execution rule to identify CVE-2026-75604 and adds a new rule for remote code execution in the Next.js Image Optimizer via crafted AVIF images. Key Findings CVE-2026-75604 affects Windows-hosted Next.js applications using both the Pages Router and App Router without Cache Components and can lead to unauthenticated remote code execution. GHSA-2xp9-vwfh-vxw4 affects the Next.js Image Optimizer and can lead to unauthenticated remote code execution when it optimizes an attacker-controlled AVIF image.

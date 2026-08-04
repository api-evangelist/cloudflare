---
title: "WAF - WAF Release - 2026-07-17 - Emergency"
url: "https://developers.cloudflare.com/changelog/post/2026-07-17-emergency-waf-release/"
date: "2026-07-17"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
This emergency release adds a new managed rule to block active exploitation of a critical remote code execution (RCE) and SQL injection (SQLi) vulnerability found in popular web frameworks. Key Findings Generic Frameworks - Unauthenticated RCE: Attackers can execute arbitrary system commands with web server privileges by sending malicious input containing invalid path sequences during request processing. Generic Frameworks - SQLi: Attackers can execute unauthorized database queries due to a failure to sanitize input values within request parameters.

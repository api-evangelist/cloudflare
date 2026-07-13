---
title: "Data Loss Prevention - Source code detection improvements"
url: "https://developers.cloudflare.com/changelog/post/2026-07-10-source-code-detection-improvements/"
date: "2026-07-10"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Data Loss Prevention (DLP) source code detection now focuses on identifying whole source code file uploads and downloads. Previously, source code detection performed partial scans resulting in a higher rate of false positives. Since only whole source code files are evaluated, code embedded in other content — such as chat messages, documentation, or code samples — is no longer flagged as source code, removing a common source of false positives.

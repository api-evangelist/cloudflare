---
title: "Gateway - Detect and control software package downloads with package registry security"
url: "https://developers.cloudflare.com/changelog/post/2026-08-13-package-protection/"
date: "2026-08-13"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare Gateway can now detect software package downloads and give you policy control over supply chain traffic. When a developer or CI/CD pipeline downloads a package through Gateway, the proxy identifies the registry protocol from the request URL and extracts the package ecosystem, name, version, and namespace. You can then write HTTP policies using pkg.* selectors to allow or block package downloads.

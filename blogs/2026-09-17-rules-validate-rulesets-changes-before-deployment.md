---
title: "Rules - Validate Rulesets changes before deployment"
url: "https://developers.cloudflare.com/changelog/post/2026-09-17-rulesets-dry-run-validation/"
date: "2026-09-17"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare Rules now validates ruleset changes before deployment, helping you catch invalid expressions, action parameters, permission issues, unavailable features, and quota limits without publishing the configuration. The Cloudflare dashboard performs this validation automatically when you create or update rules from Security > Security rules or Rules > Overview . Supported Rulesets API mutation endpoints now also accept the dry_run=true query parameter.

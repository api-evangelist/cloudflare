---
title: "WAF, Rules - Failed detections field available in Rules"
url: "https://developers.cloudflare.com/changelog/post/2026-10-09-failed-detections/"
date: "2026-10-09"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
You can now use cf.appsec.request.failed_detections to control how your rules handle requests when a security detection reports a failure. The field is an Array of detection IDs that reports failures from content scanning, WAF attack score, attack signature detection, leaked credentials detection, and AI prompt detections for personally identifiable information (PII), prompt injection, custom topics, and unsafe topics. The field does not alter the existing behavior of detections.

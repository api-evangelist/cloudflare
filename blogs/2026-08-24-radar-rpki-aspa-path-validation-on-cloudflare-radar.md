---
title: "Radar - RPKI ASPA path validation on Cloudflare Radar"
url: "https://developers.cloudflare.com/changelog/post/2026-08-24-radar-aspa-validation/"
date: "2026-08-24"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Radar adds an ASPA validation tool ↗ to its Routing section ↗ . Enter a BGP AS_PATH and the tool checks it against the Autonomous System Provider Authorization (ASPA) ↗ records currently published in the RPKI, returning a verdict of Valid , Invalid , or Unknown . An Invalid verdict means no chain of provider authorizations covers the whole path, which is the signature of a route leak.

---
title: "Cloudflare One, Access - Infrastructure applications support a configurable session duration"
url: "https://developers.cloudflare.com/changelog/post/2026-10-14-infrastructure-ssh-session-duration/"
date: "2026-10-14"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Infrastructure applications now have a configurable session duration with a default value of 24 hours. You can set the session duration when creating or editing an infrastructure application in the dashboard or via the API. When the session duration elapses, any active SSH connections through that application will be closed, and users will need to reconnect.

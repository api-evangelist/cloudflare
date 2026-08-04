---
title: "Stream - Rotate Stream broadcast keys for live inputs"
url: "https://developers.cloudflare.com/changelog/post/2026-07-30-rotate-stream-broadcast-keys/"
date: "2026-07-31"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
You can now rotate the broadcast credentials for a Stream live input without changing the live input identifier. Use key rotation when live input credentials may have been shared with the wrong audience, exposed in client code or a screenshare, or need to be refreshed as part of your security process. Rotating keys revokes the old credentials, disconnects broadcasts using stale credentials, and returns refreshed credentials in the API response.

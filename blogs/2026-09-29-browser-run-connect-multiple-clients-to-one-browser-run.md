---
title: "Browser Run - Connect multiple clients to one Browser Run session"
url: "https://developers.cloudflare.com/changelog/post/2026-09-29-concurrent-session-connections/"
date: "2026-09-29"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Browser Run sessions now accept multiple concurrent connections. Before, a session accepted only one connection at a time, and other Workers had to wait until that connection closed. Now multiple Workers can connect to the same browser at the same time.

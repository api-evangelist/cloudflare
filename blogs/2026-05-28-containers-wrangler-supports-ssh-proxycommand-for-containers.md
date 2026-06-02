---
title: "Containers - Wrangler supports SSH ProxyCommand for Containers"
url: "https://developers.cloudflare.com/changelog/post/2026-05-28-ssh-proxy-command/"
date: "2026-05-28"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Wrangler supports using wrangler containers ssh as an OpenSSH ProxyCommand for Containers . This lets your local SSH client connect to a running Container through Wrangler. ssh -o ProxyCommand="wrangler containers ssh %h" cloudchamber@ When standard input and output are piped, Wrangler forwards data to the SSH server in the Container.

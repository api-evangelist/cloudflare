---
title: "Access - Browser-based login for plaintext HTTP private applications"
url: "https://developers.cloudflare.com/changelog/post/2026-07-20-http-private-apps-l7-auth/"
date: "2026-07-20"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare Access now uses the standard browser-based login flow for private applications served over plaintext HTTP on port 80 . Previously, plaintext HTTP private apps fell back to the same session flow used for SSH, RDP, and other non-HTTP protocols: users got an Authentication required pop-up from the Cloudflare One Client, then had to select the notification to open a browser and log in. Now, users hitting an HTTP private app see the Access login page directly in the browser and receive a standard Access application token on success.

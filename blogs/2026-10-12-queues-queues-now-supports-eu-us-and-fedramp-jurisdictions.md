---
title: "Queues - Queues now supports EU, US, and FedRAMP jurisdictions"
url: "https://developers.cloudflare.com/changelog/post/2026-09-18-queues-jurisdictions/"
date: "2026-10-12"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
You can now create Cloudflare Queues with jurisdictional restrictions, ensuring that messages published to a queue are stored and processed only within a specific jurisdiction. This helps you comply with data residency requirements such as the GDPR ↗︎ or FedRAMP ↗︎ . To create a jurisdiction-restricted queue with the Cloudflare CLI ( cf ), use the --jurisdiction flag: cf queues create --queue-name my-eu-queue --jurisdiction eu You can also pass a jurisdiction parameter when calling the Create Queue endpoint: curl https://api.cloudflare.com/client/v4/accounts/ $ACCOUNT_ID /queues \ --request PO

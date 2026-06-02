---
title: "Realtime - Record specific participant audio tracks in RealtimeKit"
url: "https://developers.cloudflare.com/changelog/post/2026-05-28-realtimekit-track-recording/"
date: "2026-05-28"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
You can now record specific participant audio tracks in RealtimeKit with track recording . Track recording creates separate WebM files for each participant instead of a single composite recording, which is useful for post-processing, transcription, and regulated or content-sensitive workflows. To record specific participants, pass user_ids when starting a track recording: curl --request POST \ --url https://api.cloudflare.com/client/v4/accounts/ /realtime/kit/ /recordings/track \ --header 'Authorization: Bearer ' \ --header 'Content-Type: application/json' \ --data '{ "meeting_id": "97440c6a-1

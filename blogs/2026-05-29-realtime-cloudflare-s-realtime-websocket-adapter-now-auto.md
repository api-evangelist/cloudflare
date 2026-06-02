---
title: "Realtime - Cloudflare's Realtime WebSocket adapter now auto-reconnects and buffers WebRTC media"
url: "https://developers.cloudflare.com/changelog/post/2026-05-29-websocket-adapter-auto-reconnect/"
date: "2026-05-29"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare Realtime SFU is a WebRTC Selective Forwarding Unit that runs on Cloudflare's global network , so you can route live audio, video, and data between WebRTC clients around the world without managing SFU infrastructure or regions. When you use the WebSocket adapter to stream WebRTC media to a WebSocket endpoint, the adapter now auto-reconnects and buffers audio and video after brief endpoint disconnects or restarts. Streaming WebRTC media to WebSocket endpoints Many teams also use Realtime SFU as the media layer for backend applications, such as transcription, recording, note-taking, an

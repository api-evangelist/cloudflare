---
title: "Agents - New web_fetch tool in the Agents SDK for reading webpages and documents, with automatic markdown conversion"
url: "https://developers.cloudflare.com/changelog/post/2026-10-11-web-fetch/"
date: "2026-10-12"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
The Cloudflare Agents SDK now provides a web_fetch tool that reads webpages, PDFs, and supported Office documents, using Workers AI Markdown Conversion to turn them into text the model can read. The tool requests Markdown directly from sites that support Markdown for Agents and formats JSON for the model. When you give the web_fetch tool to your agent, the model provides a URL and receives back the page content, along with the final URL, HTTP status, and content type.

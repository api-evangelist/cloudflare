---
title: "AI Search - AI Search keyword search supports Japanese, Chinese, and Korean queries"
url: "https://developers.cloudflare.com/changelog/post/2026-10-16-cjk-keyword-search/"
date: "2026-10-16"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
AI Search keyword search with the trigram tokenizer now matches Japanese, Chinese, and Korean queries, including full natural-language questions such as 経費精算の締め日はいつですか？ . Previously, a query without spaces was treated as a single exact phrase and usually returned no keyword results. The porter tokenizer does not work well for these languages.

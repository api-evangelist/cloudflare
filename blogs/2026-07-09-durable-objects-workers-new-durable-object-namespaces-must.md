---
title: "Durable Objects, Workers - New Durable Object namespaces must use the SQLite storage backend"
url: "https://developers.cloudflare.com/changelog/post/2026-07-09-restrict-new-kv-backed-namespaces/"
date: "2026-07-09"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
If your account does not already have a key-value (KV) backed Durable Object namespace, you can no longer create new ones. New Durable Object namespaces must use the SQLite storage backend , which has been recommended for all new Durable Objects since it became generally available in 2024. Create a new class with a new_sqlite_classes migration: wrangler.jsonc { " $schema " : "./node_modules/wrangler/config-schema.json" , " migrations " : [ { " tag " : "v1" , " new_sqlite_classes " : [ "MyDurableObject" ] } ] } wrangler.toml [[ migrations ]] tag = "v1" new_sqlite_classes = [ "MyDurableObject" ]

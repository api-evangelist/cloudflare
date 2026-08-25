---
title: "R2 - New `us` jurisdiction for R2"
url: "https://developers.cloudflare.com/changelog/post/2026-08-17-r2-us-jurisdiction/"
date: "2026-08-17"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
R2 now supports a us jurisdiction , which guarantees that bucket data is stored and processed within the United States. Use this jurisdiction when you need explicit US data residency guarantees. Use the jurisdiction-specific S3 endpoint to create and access buckets in the us jurisdiction: https:// .us.r2.cloudflarestorage.com To access a bucket in the us jurisdiction from Workers, set jurisdiction in your R2 binding: { "r2_buckets" : [ { "binding" : "MY_BUCKET" , "bucket_name" : " " , "jurisdiction" : "us" } ] } [[ r2_buckets ]] binding = "MY_BUCKET" bucket_name = " " jurisdiction = "us" Once 

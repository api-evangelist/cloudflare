---
title: "R2 - Sippy now supports Azure Blob Storage and S3-compatible storage providers"
url: "https://developers.cloudflare.com/changelog/post/2026-07-24-r2-sippy-azure-s3-compatible-support/"
date: "2026-07-24"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Sippy can now incrementally migrate data from Azure Blob Storage and any S3-compatible object storage provider to Cloudflare R2 , in addition to Amazon S3 and Google Cloud Storage. Sippy copies objects to R2 as your application requests them, so you can start serving data from R2 without first moving your entire dataset or paying migration-specific egress fees. Enable Sippy Run the following command and follow the prompts to select and configure your source storage provider: npx wrangler r2 bucket sippy enable BUCKET_NAM E > For Azure Blob Storage, provide your storage account name, container 

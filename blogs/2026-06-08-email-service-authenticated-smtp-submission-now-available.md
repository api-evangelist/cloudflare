---
title: "Email Service - Authenticated SMTP submission now available in beta"
url: "https://developers.cloudflare.com/changelog/post/2026-06-08-smtp-submission/"
date: "2026-06-08"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
You can now send emails through Cloudflare Email Service using authenticated SMTP submission on smtp.mx.cloudflare.net:465 . SMTP joins the REST API and the Workers binding as a third way to send transactional email — useful for existing applications that already speak SMTP and language-native SMTP libraries (Nodemailer, smtplib , PHPMailer, JavaMail). Setting Value Host smtp.mx.cloudflare.net Port 465 (implicit TLS) AUTH PLAIN or LOGIN Username api_token Password A Cloudflare API token (account-owned or user-owned) with Email Sending: Edit Submissions enter the same delivery pipeline as the R

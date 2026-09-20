---
title: "Access - Require fresh authentication for SAML identity providers"
url: "https://developers.cloudflare.com/changelog/post/2026-09-14-saml-force-authentication/"
date: "2026-09-14"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare Access can now request fresh authentication from a SAML identity provider for every login. Turn on Require reauthentication in the Cloudflare dashboard, or set force_authn to true through the API. Access will then set ForceAuthn to true in signed and unsigned SAML authentication requests.

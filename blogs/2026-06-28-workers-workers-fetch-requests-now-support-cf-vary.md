---
title: "Workers - Workers fetch requests now support cf.vary"
url: "https://developers.cloudflare.com/changelog/post/2026-06-28-cf-vary-request-option/"
date: "2026-06-28"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Workers fetch() requests now support the cf.vary request option. Use cf.vary to control how Cloudflare caches origin responses with a Vary header for a single subrequest. JavaScript export default { async fetch ( request ) { return fetch ( request , { cf : { vary : { default : { action : "bypass" }, headers : { accept : { action : "normalize" , media_types : [ "text/html" , "application/json" ] , }, "accept-language" : { action : "normalize" , languages : [ "en" , "fr" , "de" ] , }, }, }, }, } ) ; }, }; TypeScript export default { async fetch ( request ) : Promise Response > { return fetch ( r

---
title: "R2 SQL - R2 SQL now supports UNION, INTERSECT, EXCEPT, and SELECT DISTINCT"
url: "https://developers.cloudflare.com/changelog/post/2026-06-05-union-intersect-except-select-distinct/"
date: "2026-06-08"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
R2 SQL now supports set operations ( UNION , INTERSECT , EXCEPT ) and SELECT DISTINCT , expanding the range of analytical queries you can run directly on Apache Iceberg tables in R2 Data Catalog . Set operations Combine the results of multiple SELECT statements: UNION — returns all rows from both queries, removing duplicates UNION ALL — returns all rows from both queries, including duplicates INTERSECT — returns only rows that appear in both queries EXCEPT — returns rows from the first query that do not appear in the second -- Find zones that had either firewall blocks OR high-risk requests SE

---
title: "Workers - Run integration tests against your Worker's production build"
url: "https://developers.cloudflare.com/changelog/post/2026-07-21-integration-test-harness/"
date: "2026-07-27"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Wrangler now provides createTestHarness() , an API for running integration tests against Workers built with Wrangler or the Cloudflare Vite plugin from any Node.js test runner. The test harness starts a local Worker server with helpers for dispatching requests, resetting storage, and inspecting runtime logs . This is useful for tests that need to: Route requests across multiple Workers Mock outbound fetch() requests with Node.js request mocking libraries such as MSW ↗ Run Playwright tests against a Worker For example, this test starts two Workers and mocks an upstream API: tests/vitest.test.js

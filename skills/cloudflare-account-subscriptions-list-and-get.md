---
name: cloudflare-account-subscriptions-list-and-get
description: List all subscriptions for an account and retrieve details of a specific subscription.
api: openapi/cloudflare-openapi.json
operations:
- account-subscriptions-list-subscriptions
- account-subscriptions-get-subscription
generated: '2026-10-03'
method: generated
generator: extract-docs-artifacts.py skills (local)
source: openapi/cloudflare-openapi.json ; every operationId checked against the contract
---

# cloudflare-account-subscriptions-list-and-get

List all subscriptions for an account and retrieve details of a specific subscription.

## Steps

1. 1. Call `account-subscriptions-list-subscriptions` with the path parameter `account_id` and include the required authentication header (e.g., `X-Auth-Key`).
2. 2. Call `account-subscriptions-get-subscription` with the path parameters `account_id` and `subscription_identifier` and include the required authentication header.

## Rules

- Authentication: Provide an API key in the `X-Auth-Key` header (or use any of the documented auth schemes).

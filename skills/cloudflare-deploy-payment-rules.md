---
name: cloudflare-deploy-payment-rules
description: Deploy a payment ruleset to a zone after confirming its eligibility.
api: openapi/cloudflare-openapi.json
operations:
- monetization-check-zone-eligibility
- monetization-list-rules
- monetization-deploy-ruleset
generated: '2026-10-03'
method: generated
generator: extract-docs-artifacts.py skills (local)
source: openapi/cloudflare-openapi.json ; every operationId checked against the contract
---

# cloudflare-deploy-payment-rules

Deploy a payment ruleset to a zone after confirming its eligibility.

## Steps

1. 1. Call `monetization-check-zone-eligibility` with header `X-Auth-Key` (apiKey) and path parameter `zone_id`.
2. 2. Call `monetization-list-rules` with header `X-Auth-Key` (apiKey) and path parameter `zone_id` to view existing rules.
3. 3. Call `monetization-deploy-ruleset` with header `X-Auth-Key` (apiKey), path parameter `zone_id`, and request body containing the ruleset definition.

## Rules

- Authentication: Provide an API key in the `X-Auth-Key` header (apiKeyAuth).
- Idempotency: The `monetization-deploy-ruleset` operation is idempotent; repeated calls with the same ruleset produce the same result.
- Errors: The API returns standard Cloudflare error responses (e.g., 400 for bad request, 403 for unauthorized, 404 for not found).

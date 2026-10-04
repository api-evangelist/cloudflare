---
name: cloudflare-onramps-create-and-apply
description: Create a new On‑ramp and immediately apply it to the account.
api: openapi/cloudflare-openapi.json
operations:
- onramps-create
- onramps-apply
generated: '2026-10-03'
method: generated
generator: extract-docs-artifacts.py skills (local)
source: openapi/cloudflare-openapi.json ; every operationId checked against the contract
---

# cloudflare-onramps-create-and-apply

Create a new On‑ramp and immediately apply it to the account.

## Steps

1. 1. Call `onramps-create` with the required request body fields for the new On‑ramp and include the `X-Auth-Key` and `X-Auth-Email` headers for authentication.
2. 2. Call `onramps-apply` using the `onramp_id` returned from the create step, supplying the same authentication headers.

## Rules

- Authentication: include both `X-Auth-Key` (apiKey) and `X-Auth-Email` (api_email) headers in every request.
- Idempotency: the `onramps-create` operation is not idempotent; avoid duplicate calls unless you intend to create multiple On‑ramps.

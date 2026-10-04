---
name: cloudflare-pay-unpaid-invoice
description: Pay an unpaid invoice for an account using the Cloudflare Billing API, detailing required parameters and authentication methods.
api: openapi/cloudflare-openapi.json
operations:
- account-billing-get-unpaid-invoices
- account-billing-pay-invoice
generated: '2026-10-03'
method: generated
generator: extract-docs-artifacts.py skills (local)
source: openapi/cloudflare-openapi.json ; every operationId checked against the contract
---

# cloudflare-pay-unpaid-invoice

Pay an unpaid invoice for an account.

## Steps

1. 1. Retrieve the list of unpaid invoices using `account-billing-get-unpaid-invoices` (requires `account_id` path parameter).
2. 2. Select the desired invoice ID from the response.
3. 3. Pay the selected invoice using `account-billing-pay-invoice` (requires `account_id` path parameter and `invoice_id` in the request body).

## Rules

- Authentication: include either `X-Auth-Key` (apiKeyAuth) and `X-Auth-Email` (api_email) headers, or a bearer token via `Authorization: Bearer <token>`.
- Idempotency: not specified for these endpoints; repeat calls may create duplicate payments.

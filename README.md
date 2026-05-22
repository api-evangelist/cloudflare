# Cloudflare (cloudflare)

Cloudflare is a global network designed to make everything you connect to the Internet secure, private, fast, and reliable.

**URL:** [Visit APIs.json URL](https://raw.githubusercontent.com/api-search/infrastructure/main/_apis/cloudflare/apis.md)

## Scope

- **Type:** Contract
- **Position:** Consuming
- **Access:** 3rd-Party

## Tags

AI Gateway, API Gateway, Artificial Intelligence, CDN, Cloud, Containers, DDoS Protection, DNS, Edge, Edge Computing, Object Storage, Platform, Real-Time Communication, Security, Serverless, Web Performance

## Timestamps

- **Created:** 2024-04-14
- **Modified:** 2026-05-22

## Pipeline Inventory

| Artifact | Count |
|---|---|
| APIs documented | 54 |
| OpenAPI specs (`openapi/`) | 24 |
| AsyncAPI specs (`asyncapi/`) | 2 |
| Naftiko capabilities (`capabilities/`) | 71 |
| JSON Schemas (`json-schema/`) | 76 |
| JSON Structures (`json-structure/`) | 70 |
| JSON-LD contexts (`json-ld/`) | 17 |
| Example payloads (`examples/`) | 70 |
| Spectral rules (`rules/`) | 1 (`cloudflare-spectral-rules.yml`) |
| Plans / Pricing (`plans/`) | 1 |
| Rate Limits (`rate-limits/`) | 1 |
| FinOps (`finops/`) | 1 |
| Vocabulary (`vocabulary/`) | 1 |
| Mirrored blog posts (`blogs/`) | 27 |

## APIs

This repository profiles 54 Cloudflare API surfaces. Highlights:

### Account & Identity
- **Cloudflare API** — Master API at `api.cloudflare.com/client/v4` (`openapi/cloudflare-openapi-original.yml`)
- **Accounts API** — Account-level management (`openapi/cloudflare-accounts--openapi-original.yml`)
- **Memberships API** — Cross-account user memberships
- **User API** — Per-user details and tokens
- **Organizations API** — Multi-account org management

### Edge Compute & Runtimes
- **Workers API** — JavaScript / Wasm / Rust / Python serverless runtime (`openapi/cloudflare-workers-openapi.yml`)
- **Workers for Platforms API** — Multi-tenant dispatch namespaces
- **Workers VPC API** — Private connectivity into AWS / Azure / GCP / on-prem and Cloudflare WAN (added 2026-05)
- **Workflows API** — Durable multi-step execution (with Dynamic Workflows)
- **Durable Objects API** — Stateful coordination + per-instance SQLite (`openapi/cloudflare-durable-objects-openapi.yml`)
- **Containers API** — Serverless container runtime co-located with Workers (SSH-by-default via Wrangler)
- **Agents API** — Stateful AI agents on Durable Objects (npm `agents`, v0.13.2 May 2026)

### AI / ML
- **Workers AI API** — 78+ open-source models (Llama 3.1, Mistral, Qwen3, Kimi K2.6, Flux 2, Whisper, Aura 2, LLaVA, BGE) with OpenAI-compatible endpoints (`openapi/cloudflare-workers-ai-openapi.yml`)
- **AI Gateway API** — Unified REST endpoint across 23+ providers (OpenAI, Anthropic, Google, Mistral, Cohere, Groq, DeepSeek, Cerebras, xAI, Perplexity, Replicate, HuggingFace, Bedrock, Azure OpenAI, ElevenLabs, Deepgram, Workers AI), with caching, fallback, rate limiting, guardrails, evaluations (`openapi/cloudflare-ai-gateway-openapi.yml`)
- **AI Search API** — Managed RAG pipelines on R2
- **Vectorize API** — Distributed vector database (`openapi/cloudflare-vectorize-openapi.yml`)
- **Claude Managed Agents on Cloudflare** — Anthropic-managed agents on Cloudflare's Agents SDK substrate (announced 2026-05-19)

### Storage & Data
- **R2 API** — S3-compatible object storage, zero egress fees (`openapi/cloudflare-r2-openapi.yml`)
- **R2 SQL API** — Iceberg-backed analytic SQL with JOIN / subquery support (May 2026)
- **D1 API** — Serverless SQLite, global read replication, 30-day Time Travel (`openapi/cloudflare-d1-openapi.yml`)
- **KV API** — Low-latency key-value store (`openapi/cloudflare-kv-openapi.yml`)
- **Queues API** — Guaranteed-delivery message queues (`openapi/cloudflare-queues-openapi.yml`)
- **Hyperdrive API** — Connection pooling and query caching for external DBs (`openapi/cloudflare-hyperdrive-openapi.yml`)
- **Pipelines API** — HTTP/Worker ingest → Iceberg or Parquet in R2
- **Artifacts API** — Versioned Git-compatible file storage (closed beta 2026-05)
- **Secrets Store API** — Account-wide encrypted secrets reused across products

### Media
- **Stream API** — VOD + live ingest (RTMPS, SRT, TUS) (`openapi/cloudflare-stream-openapi.yml`)
- **Realtime API** — RealtimeKit + Selective Forwarding Unit + TURN for WebRTC
- **Images API** — Upload, store, transform on the edge (`openapi/cloudflare-images-openapi.yml`)
- **Browser Rendering / Browser Run API** — Headless Chrome on Containers with `/screenshot`, `/pdf`, `/markdown`, `/scrape`, `/crawl`, `/links` Quick Actions plus full Puppeteer / Playwright / CDP / Stagehand support

### Networking & Performance
- **DNS API** — Records, DNSSEC, batch, scanning, analytics (`openapi/cloudflare-dns-openapi.yml`)
- **Zones API** — DNS zone lifecycle (`openapi/cloudflare-zones--openapi-original.yml`)
- **1.1.1.1 DNS Resolver API** — DoH / DoT public resolver
- **Cache API** — CDN cache control, purging, cache reserve, tiered caching
- **Argo Smart Routing API** — Real-time network-aware routing
- **Load Balancing API** — Multi-pool failover and steering
- **Spectrum API** — Layer-4 protection
- **Magic Transit API** — BGP-anycast L3 protection
- **Email Routing API** — Catch-all + custom-address routing (free, all plans)

### Security & Zero Trust
- **DDoS Protection API** — Application + network rulesets
- **WAF API** — Cloudflare-managed and custom rulesets
- **API Shield API** — Schema validation, mTLS, sequence analytics, discovery (Enterprise)
- **Turnstile API** — CAPTCHA replacement (`openapi/cloudflare-turnstile-openapi.yml`)
- **Page Shield API** — Client-side script monitoring
- **Certificates API** — Universal, Advanced, Custom, Keyless SSL (`openapi/cloudflare-certificates--openapi-original.yml`)
- **IP Addresses API** — Cloudflare-issued anycast IP management (`openapi/cloudflare-ips--openapi-original.yml`)
- **Zero Trust / Cloudflare One API** — Access, Tunnel, Gateway, CASB, Browser Isolation, DLP, DEX, Email Security

### Observability
- **Logpush API** — Logs → S3 / R2 / GCS / SIEMs (`openapi/cloudflare-logpush-openapi.yml`)
- **GraphQL Analytics API** — Account / zone / Workers / R2 analytics
- **Web Analytics API** — Privacy-first RUM
- **Radar API** — Internet traffic, attacks, BGP, DNS, AI Insights, Quality, Outages (CC BY-NC 4.0) (`openapi/cloudflare-radar--openapi-original.yml`)

### Developer Platform
- **Pages API** — JAMstack hosting (`openapi/cloudflare-pages-openapi.yml`)
- **Registrar API** — Domain registration at cost
- **Zaraz API** — Server-side third-party tag management
- **Waiting Room API** — Origin offload queue

## Common Properties

- Portal — https://developers.cloudflare.com/
- Pricing — https://www.cloudflare.com/plans/ (Free, Pro $25, Business $200, Enterprise from ~$5k/zone/mo)
- Workers Pricing — https://developers.cloudflare.com/workers/platform/pricing/ (Free 100k req/day; Paid $5/mo + $0.30/M req + $0.02/M CPU ms)
- Authentication — https://developers.cloudflare.com/fundamentals/api/get-started/create-token/
- Rate Limits — https://developers.cloudflare.com/fundamentals/api/reference/limits/ (1,200 req/5min global)
- Changelog — https://developers.cloudflare.com/changelog/ (RSS: https://developers.cloudflare.com/changelog/rss/index.xml)
- Status — https://www.cloudflarestatus.com/
- Blog — https://blog.cloudflare.com/ (RSS: https://blog.cloudflare.com/rss/)
- Console — https://dash.cloudflare.com/
- Support — https://support.cloudflare.com/, https://community.cloudflare.com/, https://discord.com/invite/cloudflaredev
- GitHub Org — https://github.com/cloudflare (563 public repos)
- OpenAPI Source — https://github.com/cloudflare/api-schemas (BSD-3, single bundled `openapi.yaml` + `common.yaml`; 29k+ commits)
- Privacy / Terms — https://www.cloudflare.com/privacypolicy/ · https://www.cloudflare.com/terms/

## SDKs, CLIs, and Tooling

| Type | Name | Source |
|---|---|---|
| SDK | TypeScript (Stainless-generated) | https://github.com/cloudflare/cloudflare-typescript (v6.3.0, May 2026) |
| SDK | Go (Stainless-generated) | https://github.com/cloudflare/cloudflare-go (v7.3.0, May 2026) |
| SDK | Python | https://github.com/cloudflare/cloudflare-python |
| SDK | Agents SDK | https://github.com/cloudflare/agents (npm `agents` v0.13.2) |
| CLI | Wrangler | https://developers.cloudflare.com/workers/wrangler/ |
| IaC | Terraform provider | https://developers.cloudflare.com/terraform/ |
| IaC | Pulumi provider | https://developers.cloudflare.com/pulumi/ |
| Runtime | workerd | https://github.com/cloudflare/workerd |
| Runtime | workers-rs | https://github.com/cloudflare/workers-rs |
| Tunnel | cloudflared | https://github.com/cloudflare/cloudflared |
| Network | quiche (QUIC/HTTP3) | https://github.com/cloudflare/quiche |
| Network | Pingora reverse proxy | https://github.com/cloudflare/pingora |

## MCP Servers (Remote)

Cloudflare ships 14+ remote MCP servers at `*.mcp.cloudflare.com` for AI agents:

| Server | URL |
|---|---|
| Observability | https://observability.mcp.cloudflare.com/mcp |
| Workers Bindings | https://bindings.mcp.cloudflare.com/mcp |
| Workers Builds | https://builds.mcp.cloudflare.com/mcp |
| Radar | https://radar.mcp.cloudflare.com/mcp |
| DNS Analytics | https://dns-analytics.mcp.cloudflare.com/mcp |
| AI Gateway | https://ai-gateway.mcp.cloudflare.com/mcp |
| Browser Rendering | https://browser.mcp.cloudflare.com/mcp |
| Logpush | https://logpush.mcp.cloudflare.com/mcp |
| GraphQL | https://graphql.mcp.cloudflare.com/mcp |
| CASB | https://casb.mcp.cloudflare.com/mcp |
| Container Sandbox | https://containers.mcp.cloudflare.com/mcp |
| Audit Logs | https://auditlogs.mcp.cloudflare.com/mcp |
| Digital Experience Monitoring | https://dex.mcp.cloudflare.com/mcp |

Source monorepo: https://github.com/cloudflare/mcp-server-cloudflare (3.8k stars).

## Key 2026 Movements (verbatim from changelog)

- **May 21** — AI Gateway: *"Call any AI model through AI Gateway's new REST API"*
- **May 19** — *"Announcing Claude Managed Agents on Cloudflare"*
- **May 19** — CASB: *"Claude Compliance API integration support"*
- **May 15** — R2 SQL: *"Support for JOINs, subqueries, multi-table queries"*
- **May 13** — *"Browser Run: now running on Cloudflare Containers, it's faster and more scalable"*
- **May 12** — Containers: *"SSH enabled by default via Wrangler"*
- **May 01** — *"Introducing Dynamic Workflows — durable execution that follows runtime logic"*
- **Apr 30** — *"Agents can now create Cloudflare accounts, buy domains, and deploy"*
- **Apr 30** — Cloudflare IPsec: *"Post-quantum encryption is generally available"*

## Notable Absences / Caveats

- No single canonical OpenAPI per product — all specs live as one bundled `openapi.yaml` in `cloudflare/api-schemas`; the per-product specs in `openapi/` here were split for usability.
- No public AsyncAPI for most webhook surfaces — only Notifications and Stream webhooks are formally specified.
- Radar data licensed CC BY-NC 4.0 (commercial use restricted).
- Several newer products (Agents, Containers, Workflows, Pipelines, Workers VPC, Artifacts) are SDK / Wrangler-first with no top-level REST surface exposed in `api.cloudflare.com/client/v4`.

## Maintainers

- **Kin Lane** — kin@apievangelist.com — http://apievangelist.com
- **Cloudflare** — api@cloudflare.com — https://www.cloudflare.com

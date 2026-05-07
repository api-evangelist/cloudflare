#!/usr/bin/env python3
"""Build the Cloudflare API tube-style map.

~45 of Cloudflare's APIs grouped onto 8 product lines.
"""

import sys
from pathlib import Path

sys.path.insert(0, "/Users/kinlane/GitHub/all/.claude/skills")
from _subway_engine import build_subway  # noqa: E402

ABBREV = {
    "Workers for Platforms":  "Workers Platforms",
    "Browser Rendering":      "Browser Render",
    "1.1.1.1 DNS Resolver":   "1.1.1.1 Resolver",
    "Multi-Region Access Points":"Multi-Region APs",
    "GraphQL Analytics":      "GraphQL Analytics",
    "DDoS Protection":        "DDoS",
    "Argo Smart Routing":     "Argo Routing",
    "Email Routing":          "Email Routing",
    "Workers AI":             "Workers AI",
    "AI Gateway":             "AI Gateway",
    "AI Search":              "AI Search",
    "Page Shield":            "Page Shield",
    "API Shield":             "API Shield",
    "Magic Transit":          "Magic Transit",
    "Web Analytics":          "Web Analytics",
    "Secrets Store":          "Secrets Store",
    "Durable Objects":        "Durable Objects",
}

LINES = [
    {
        "name": "DNS & Network",
        "color": "#F38020",  # Cloudflare orange
        "stations": [
            ("DNS",          (260, 195)),
            ("Zones",        (380, 175)),
            ("IP Addresses", (510, 165)),
            ("Registrar",    (640, 165)),
            ("1.1.1.1 DNS Resolver",(800, 175)),
            ("Cache",        (970, 200)),
        ],
    },
    {
        "name": "Edge Compute",
        "color": "#7B3FE4",
        "stations": [
            ("Workers",       (260, 290)),
            ("Pages",         (390, 270)),
            ("Containers",    (510, 265)),
            ("Workflows",     (630, 270)),
            ("Browser Rendering",(770, 280)),
            ("Realtime",      (920, 295)),
            ("Agents",        (1030, 320)),
        ],
    },
    {
        "name": "Storage & Data",
        "color": "#0E9D6E",
        "stations": [
            ("R2",          (270, 380)),
            ("R2 SQL",      (390, 405)),
            ("D1",          (500, 405)),
            ("KV",          (610, 405)),
            ("Queues",      (720, 405)),
            ("Vectorize",   (840, 405)),
            ("Hyperdrive",  (960, 380)),
            ("Pipelines",   (1030, 415)),
        ],
    },
    {
        "name": "AI",
        "color": "#C5318B",
        # Closed triangle of three AI services.
        "closed": True,
        "stations": [
            ("Workers AI", (820, 480)),
            ("AI Gateway", (905, 540)),
            ("AI Search",  (735, 540)),
        ],
    },
    {
        "name": "Media",
        "color": "#1E5BD0",
        "stations": [
            ("Stream", (300, 510)),
            ("Images", (550, 510)),
        ],
    },
    {
        "name": "Security",
        "color": "#E0245E",
        "stations": [
            ("WAF",            (260, 615)),
            ("API Shield",     (380, 595)),
            ("Page Shield",    (500, 595)),
            ("Turnstile",      (620, 595)),
            ("Zero Trust",     (740, 595)),
            ("DDoS Protection",(880, 595)),
            ("Argo Smart Routing",(1030, 615)),
        ],
    },
    {
        "name": "Observability",
        "color": "#5A6275",
        "stations": [
            ("Radar",            (270, 720)),
            ("Logpush",          (410, 700)),
            ("GraphQL Analytics",(580, 700)),
            ("Web Analytics",    (760, 700)),
            ("Zaraz",            (920, 720)),
        ],
    },
    {
        "name": "Account & Identity",
        "color": "#B89719",
        "stations": [
            ("Accounts",      (270, 805)),
            ("User",          (430, 785)),
            ("Memberships",   (590, 785)),
            ("Certificates",  (760, 785)),
            ("Secrets Store", (920, 805)),
        ],
    },
]

URL_OVERRIDES = {
    "DNS":                "https://apis.apis.io/apis/cloudflare/cloudflare-dns-api/",
    "Zones":              "https://apis.apis.io/apis/cloudflare/cloudflare-zones-api/",
    "IP Addresses":       "https://apis.apis.io/apis/cloudflare/cloudflare-ip-addresses-api/",
    "Registrar":          "https://apis.apis.io/apis/cloudflare/cloudflare-registrar-api/",
    "1.1.1.1 DNS Resolver":"https://apis.apis.io/apis/cloudflare/cloudflare-1111-dns-resolver-api/",
    "Cache":              "https://apis.apis.io/apis/cloudflare/cloudflare-cache-api/",
    "Workers":            "https://apis.apis.io/apis/cloudflare/cloudflare-workers-api/",
    "Pages":              "https://apis.apis.io/apis/cloudflare/cloudflare-pages-api/",
    "Containers":         "https://apis.apis.io/apis/cloudflare/cloudflare-containers-api/",
    "Workflows":          "https://apis.apis.io/apis/cloudflare/cloudflare-workflows-api/",
    "Browser Rendering":  "https://apis.apis.io/apis/cloudflare/cloudflare-browser-rendering-api/",
    "Realtime":           "https://apis.apis.io/apis/cloudflare/cloudflare-realtime-api/",
    "Agents":             "https://apis.apis.io/apis/cloudflare/cloudflare-agents-api/",
    "R2":                 "https://apis.apis.io/apis/cloudflare/cloudflare-r2-api/",
    "R2 SQL":             "https://apis.apis.io/apis/cloudflare/cloudflare-r2-sql-api/",
    "D1":                 "https://apis.apis.io/apis/cloudflare/cloudflare-d1-api/",
    "KV":                 "https://apis.apis.io/apis/cloudflare/cloudflare-kv-api/",
    "Queues":             "https://apis.apis.io/apis/cloudflare/cloudflare-queues-api/",
    "Vectorize":          "https://apis.apis.io/apis/cloudflare/cloudflare-vectorize-api/",
    "Hyperdrive":         "https://apis.apis.io/apis/cloudflare/cloudflare-hyperdrive-api/",
    "Pipelines":          "https://apis.apis.io/apis/cloudflare/cloudflare-pipelines-api/",
    "Workers AI":         "https://apis.apis.io/apis/cloudflare/cloudflare-workers-ai-api/",
    "AI Gateway":         "https://apis.apis.io/apis/cloudflare/cloudflare-ai-gateway-api/",
    "AI Search":          "https://apis.apis.io/apis/cloudflare/cloudflare-ai-search-api/",
    "Stream":             "https://apis.apis.io/apis/cloudflare/cloudflare-stream-api/",
    "Images":             "https://apis.apis.io/apis/cloudflare/cloudflare-images-api/",
    "WAF":                "https://apis.apis.io/apis/cloudflare/cloudflare-waf-api/",
    "API Shield":         "https://apis.apis.io/apis/cloudflare/cloudflare-api-shield-api/",
    "Page Shield":        "https://apis.apis.io/apis/cloudflare/cloudflare-page-shield-api/",
    "Turnstile":          "https://apis.apis.io/apis/cloudflare/cloudflare-turnstile-api/",
    "Zero Trust":         "https://apis.apis.io/apis/cloudflare/cloudflare-zero-trust-api/",
    "DDoS Protection":    "https://apis.apis.io/apis/cloudflare/cloudflare-ddos-protection-api/",
    "Argo Smart Routing": "https://apis.apis.io/apis/cloudflare/cloudflare-argo-smart-routing-api/",
    "Radar":              "https://apis.apis.io/apis/cloudflare/cloudflare-radar-api/",
    "Logpush":            "https://apis.apis.io/apis/cloudflare/cloudflare-logpush-api/",
    "GraphQL Analytics":  "https://apis.apis.io/apis/cloudflare/cloudflare-graphql-analytics-api/",
    "Web Analytics":      "https://apis.apis.io/apis/cloudflare/cloudflare-web-analytics-api/",
    "Zaraz":              "https://apis.apis.io/apis/cloudflare/cloudflare-zaraz-api/",
    "Accounts":           "https://apis.apis.io/apis/cloudflare/cloudflare-accounts-api/",
    "User":               "https://apis.apis.io/apis/cloudflare/cloudflare-user-api/",
    "Memberships":        "https://apis.apis.io/apis/cloudflare/cloudflare-memberships-api/",
    "Certificates":       "https://apis.apis.io/apis/cloudflare/cloudflare-certificates-api/",
    "Secrets Store":      "https://apis.apis.io/apis/cloudflare/cloudflare-secrets-store-api/",
}


def main():
    seen = set()
    n_unique = 0
    for ln in LINES:
        for (st, _) in ln["stations"]:
            if st not in seen:
                n_unique += 1
                seen.add(st)
    build_subway(
        title="The Cloudflare API · Underground Map",
        subtitle=f"{n_unique} APIs · {len(LINES)} functional lines · click any station for the apis.io page",
        lines=LINES,
        abbrev=ABBREV,
        source_label="Source: cloudflare/openapi/*.yml · github.com/api-evangelist/cloudflare",
        out_dir=Path(__file__).resolve().parent,
        out_basename="cloudflare-subway-map",
        provider_id="cloudflare",
        station_url_overrides=URL_OVERRIDES,
    )


if __name__ == "__main__":
    main()

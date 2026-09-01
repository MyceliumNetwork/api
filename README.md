# Mycelium Network API

Open corporate carbon emissions data. Search companies by name or identifier and retrieve their greenhouse gas disclosure history, broken down by scope (1, 2 and 3), with every figure tagged as **reported by the company** or **estimated by Mycelium**.

- **Base URL:** `https://api.mycelium.global`
- **Interactive reference docs:** https://api.mycelium.global/docs/v1
- **OpenAPI 3 spec:** https://api.mycelium.global/openapi/v1.json (mirrored in this repo at [`openapi/v1.json`](openapi/v1.json))
- **Website:** https://mycelium.global
- **MCP server for AI assistants:** https://github.com/MyceliumNetwork/mcp-server

## Authentication

Every request needs an API key in the `X-Api-Key` header. Keys are issued per user and subject to daily rate limits. Request one via https://mycelium.global.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| GET | `/v1/entities/search` | Search entities by name, LEI, ISIN, BIC, registration number or country code |
| GET | `/v1/entities/{id}` | Full entity profile: identifiers, addresses, classifications, alternative names |
| GET | `/v1/entities/{id}/disclosures` | The entity's emissions disclosures, optionally filtered by reporting year |
| GET | `/v1/disclosures/{id}` | One disclosure in full: emissions broken down by scope and category |
| GET | `/v1/disclosures/count` | Count of disclosures on the platform |

All emissions values are in **kgCO2e**.

## Quickstart

Search for a company:

```bash
curl -H "X-Api-Key: $MYCELIUM_API_KEY" \
  "https://api.mycelium.global/v1/entities/search?name=unilever"
```

Then use a `publicId` from the results to pull the profile and its disclosures:

```bash
curl -H "X-Api-Key: $MYCELIUM_API_KEY" \
  "https://api.mycelium.global/v1/entities/{publicId}/disclosures"
```

Python and JavaScript versions of the same flow are in [`examples/`](examples/).

## Typical workflow

1. **Search** - `GET /v1/entities/search` with a name, identifier or country code.
2. **Entity detail** - `GET /v1/entities/{id}` using the `publicId` from the search results.
3. **Disclosures** - `GET /v1/entities/{id}/disclosures`, optionally filtered by year.
4. **Disclosure detail** - `GET /v1/disclosures/{id}` for the per-scope breakdown.

## Provenance

Every emissions line carries its basis: disclosed in a company's own reporting, or estimated by Mycelium's models. Preserve that distinction when you present figures; never show an estimate as a company's own disclosure.

## For AI assistants (MCP)

A hosted [Model Context Protocol](https://modelcontextprotocol.io) server exposes the same database to Claude, ChatGPT, Cursor and other MCP clients, no API key required: see [MyceliumNetwork/mcp-server](https://github.com/MyceliumNetwork/mcp-server).

## Spec mirror

[`openapi/v1.json`](openapi/v1.json) is refreshed automatically from the live spec by a scheduled GitHub Action, so this repo always matches production.

## License

The example code and documentation in this repository are MIT licensed (see [LICENSE](LICENSE)). Use of the API itself is governed by the terms at https://mycelium.global.

"""Search for a company and print its disclosure history.

Usage: MYCELIUM_API_KEY=... python quickstart.py "unilever"
"""

import os
import sys

import requests

BASE = "https://api.mycelium.global/v1"
HEADERS = {"X-Api-Key": os.environ["MYCELIUM_API_KEY"]}


def main(name: str) -> None:
    search = requests.get(
        f"{BASE}/entities/search", params={"name": name}, headers=HEADERS, timeout=30
    ).json()
    if not search["results"]:
        print(f"No entities matched {name!r}")
        return

    entity = search["results"][0]
    public_id = entity["publicId"]
    print(f"{entity['legalName']} (publicId {public_id}, Mycelium Score {entity['myceliumScore']})")

    disclosures = requests.get(
        f"{BASE}/entities/{public_id}/disclosures", headers=HEADERS, timeout=30
    ).json()
    for disclosure in disclosures["results"]:
        total = disclosure["total"]["value"] if disclosure.get("total") else None
        print(f"  {disclosure['year']}: total {total} kgCO2e (disclosure {disclosure['publicId']})")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "unilever")

// Search for a company and print its disclosure history.
// Usage: MYCELIUM_API_KEY=... node quickstart.js "unilever"

const BASE = "https://api.mycelium.global/v1";
const headers = { "X-Api-Key": process.env.MYCELIUM_API_KEY };

async function main(name) {
  const search = await fetch(
    `${BASE}/entities/search?name=${encodeURIComponent(name)}`,
    { headers },
  ).then((r) => r.json());

  if (!search.results.length) {
    console.log(`No entities matched "${name}"`);
    return;
  }

  const entity = search.results[0];
  console.log(
    `${entity.legalName} (publicId ${entity.publicId}, Mycelium Score ${entity.myceliumScore})`,
  );

  const disclosures = await fetch(
    `${BASE}/entities/${entity.publicId}/disclosures`,
    { headers },
  ).then((r) => r.json());

  for (const disclosure of disclosures.results) {
    const total = disclosure.total ? disclosure.total.value : null;
    console.log(
      `  ${disclosure.year}: total ${total} kgCO2e (disclosure ${disclosure.publicId})`,
    );
  }
}

main(process.argv[2] ?? "unilever");

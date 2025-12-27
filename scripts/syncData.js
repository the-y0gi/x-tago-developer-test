const fs = require("fs");
const path = require("path");

const source = path.join(
  __dirname,
  "../backend/data/processed/cleaned_products.json"
);

const destinationDir = path.join(
  __dirname,
  "../frontend/src/data"
);

const destinationFile = path.join(
  destinationDir,
  "cleaned_products.json"
);

if (!fs.existsSync(source)) {
  console.error("Source file not found:", source);
  process.exit(1);
}

if (!fs.existsSync(destinationDir)) {
  fs.mkdirSync(destinationDir, { recursive: true });
}

fs.copyFileSync(source, destinationFile);
console.log("Data synced from backend → frontend");

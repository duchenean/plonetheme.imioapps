// Copy the self-hosted font files from the Fontsource packages into
// theme/fonts. The theme must not load fonts from a third party service.
// Keep the weights in step with scss/_fonts.scss.

import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const themeDir = join(here, "..");
const out = join(themeDir, "fonts");

const FACES = {
  quicksand: [300, 400, 500, 600, 700],
  nunito: [400, 600, 700],
};

mkdirSync(out, { recursive: true });

let n = 0;
for (const [family, weights] of Object.entries(FACES)) {
  for (const weight of weights) {
    const name = `${family}-latin-${weight}-normal.woff2`;
    const src = join(themeDir, "node_modules", "@fontsource", family, "files", name);
    copyFileSync(src, join(out, name));
    n += 1;
  }
}
console.log(`copied ${n} font files into theme/fonts`);

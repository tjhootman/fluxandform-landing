// @ts-check
import { defineConfig } from 'astro/config';

// Static output for GitHub Pages on the custom domain fluxandform.io.
// Default `build.format: 'directory'` -> clean URLs (/privacy, /inkling).
// No integrations, no client JS, no external services (see BRIEF §3, §9).
export default defineConfig({
  site: 'https://fluxandform.io',
  trailingSlash: 'ignore',
});

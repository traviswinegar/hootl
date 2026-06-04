// astro.config.mjs
//
// Static site for hootl.org. `npm run build` produces a fully static
// `dist/` directory uploadable to any static host (Namecheap shared
// hosting, Netlify, Vercel, GitHub Pages).

import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

export default defineConfig({
  site: 'https://hootl.org',
  output: 'static',
  trailingSlash: 'ignore',
  build: {
    format: 'directory',
    assets: '_assets',
  },
  integrations: [mdx()],
  markdown: {
    shikiConfig: {
      theme: 'github-dark',
      wrap: false,
    },
  },
});

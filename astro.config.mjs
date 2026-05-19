// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://cgiar-climate-data-hub.github.io',
  base: '/use-cases',
  trailingSlash: 'always',
  vite: {
    plugins: [tailwindcss()],
  },
});

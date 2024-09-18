import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { VitePWA } from 'vite-plugin-pwa'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(), VitePWA({
    manifest:{
      "name": "Club Socios App",
      "short_name": "Club",
      "icons": [
      {
          "src": "/img/icons/logo.png",
          "sizes": "any",
          "type": "image/png"
      }
      ],
      "start_url": "/",
      "display": "standalone",
      "background_color": "#ffffff",
      "lang": "en",
      "scope": "/"
  }
  })],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})

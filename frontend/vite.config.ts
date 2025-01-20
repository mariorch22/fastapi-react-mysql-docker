import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vite.dev/config/
export default defineConfig({
  resolve: { alias: { '@': '/src' } },
  plugins: [react()],
  server: {
    host: true,
    strictPort: true,
    port: 5173,
    watch: {
      usePolling: true,
      interval: 100
    },
    hmr: {
      host: 'localhost',
      port: 5173,
      protocol: 'ws'
    }
  }
})
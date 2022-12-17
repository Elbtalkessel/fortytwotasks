import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
const { resolve } = require("path");

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  root: resolve("./src"),
  base: "/static/",
  server: {
    host: "0.0.0.0",
    port: 3001,
    open: false,
    watch: {
      usePolling: true,
      disableGlobbing: false,
    }
  },
  resolve: {
    extensions: [".js", ".vue", ".css", ".png"],
    alias: {
      "@": resolve(__dirname, "./src"),
    },
  },
  build: {
    outDir: resolve("./static"),
    assetsDir: "",
    manifest: true,
    emptyOutDir: true,
    target: "es2015",
    rollupOptions: {
      input: {
        main: resolve("./src/main.js"),
      },
      output: {
        chunkFileNames: undefined,
      }
    },
  }
});

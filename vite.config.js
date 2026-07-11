import { defineConfig } from 'vite';
import { resolve } from 'path';
import glob from 'fast-glob';

const htmlEntries = glob.sync('**/*.html', { 
  ignore: [
    '**/node_modules/**', 
    '**/dist/**', 
    '**/public/**', 
    'index.html'
  ] 
});

export default defineConfig({
  base: '/web-tools/',
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        // Escanear dinámicamente todos los archivos .html en subcarpetas, ignorando carpetas especiales
        ...Object.fromEntries(
          htmlEntries.map(file => [
            // Generar clave limpia a partir de la ruta del archivo
            file.replace(/\.html$/, '').replace(/\//g, '-'),
            resolve(__dirname, file)
          ])
        )
      }
    }
  }
});

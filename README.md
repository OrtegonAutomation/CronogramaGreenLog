# Cronograma Interactivo GREENLOG-CENIT 2026

Plataforma de gestión de proyectos para el control ambiental de CENIT. Incluye dashboard para clientes y panel administrativo para registro de avances.

## 🚀 Acceso
- **Dashboard Cliente:** `index.html` (URL Base)
- **Panel Administrativo:** `/admin/` (URL Base/admin/)


## 🛠️ Herramientas
- **`cronograma_cenit.py`**: Motor Python para sincronizar datos y generar:
  - Excel con Gantt Visual dinámico.
  - Imagen Gantt ejecutiva.
  - Sincronización de base de datos para la web.

## 🔄 Flujo de Trabajo
1. Realizar cambios en el panel `/admin/`.
2. Descargar el archivo `cronograma_data.json` generado.
3. Reemplazar el archivo en la carpeta local.
4. Ejecutar `python cronograma_cenit.py sync`.
5. Subir los cambios a GitHub para actualizar la página pública.

## 🏗️ Tecnología
- **Frontend:** Vanilla HTML5, CSS3 (Outfit Font), JavaScript (ES6).
- **Backend (Local):** Python (Pandas, OpenPyXL, Matplotlib).
- **Despliegue:** GitHub Pages.

# Cronograma Interactivo GREENLOG-CENIT 2026

Plataforma de gestión de proyectos para el control ambiental de CENIT. Esta solución integra un Dashboard interactivo para clientes y un Panel Administrativo en tiempo real, utilizando infraestuctura en la nube.

## 🚀 Acceso
- **Dashboard Cliente:** `index.html` (Desplegado en GitHub Pages)
- **Panel Administrativo:** `/admin/` (Acceso protegido por clave)

## 🏗️ Tecnología y Arquitectura
- **Base de Datos:** [Supabase](https://supabase.com/) (PostgreSQL Cloud) para almacenamiento en tiempo real.
- **Frontend:** Vanilla HTML5, CSS3 (Outfit Font), JavaScript (ES6).
- **Librerías Clave:**
  - **Supabase JS:** Conexión y actualización de datos en la nube.
  - **ExcelJS:** Generación dinámica de reportes sobre demanda.
- **Automatización:** Scripts en Python (`scripts/`) para tareas complementarias como extracción de datos de PDF y migración inicial.

## 📁 Estructura del Proyecto
- `admin/`: Panel de control para actualizar estados y porcentajes de avance.
- `assets/img/`: Recursos visuales y diagramas ejecutivos.
- `docs/`: Documentación del proyecto y archivos de referencia.
- `scripts/`: Utilidades en Python para gestión avanzada (migración, extracción).
- `index.html`: Dashboard principal del proyecto.

## 🔄 Flujo de Trabajo (Cloud)
1. El Administrador accede a `/admin/` y registra avances o cambia la fecha de inicio del proyecto hoy.
2. Los cambios se sincronizan **automáticamente** con la base de datos de Supabase.
3. El Dashboard refleja los cambios al instante para el cliente final.
4. Cualquier usuario puede generar un reporte detallado en Excel pulsando el botón de descarga, el cual se construye en tiempo real con los datos más recientes de la nube.

## 🔐 Seguridad
El área administrativa cuenta con una capa de protección simple para prevenir accesos no autorizados en entornos estáticos como GitHub Pages.

---
© 2026 Greenlog | Proyectos de Ingeniería y Control Ambiental.

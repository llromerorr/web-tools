# Reglas y Estructura del Proyecto: Web Tools

Este archivo proporciona contexto directo para asistentes de IA, permitiendo arrancar y trabajar de manera rápida y eficiente sin consumir tokens escaneando todo el proyecto en cada sesión.

## Estructura del Proyecto
* [Crear tablas de acordes.html](file:///c:/Users/Luis%20Romero/GitHub/web-tools/Adoradores/Crear%20tablas%20de%20acordes.html): Aplicación principal e interactiva de edición y transposición de tablas de acordes musicales.

## Reglas de Desarrollo del Proyecto
1. **Desarrollo en Local:** Todos los cambios deben realizarse únicamente de manera local. NO hacer commits o pushes a GitHub sin la autorización explícita del usuario.
2. **Tipografías de la Interfaz:**
   * **Interfaz y Textos Generales:** Utiliza la fuente `Segoe UI` (y equivalentes de sistema) para dar un estilo limpio tipo Microsoft Office.
   * **Acordes en Cuadrícula y Vistas Previas:** Utiliza exclusivamente fuentes monoespaciadas como `Consolas` y `Cascadia Code` (las fuentes de VSCode) para que las notas queden perfectamente alineadas y estructuradas.
3. **Gestión de Celdas Vacías (VACÍO):**
   * El estado interno de una celda sin acordes se guarda como `"VACÍO"`.
   * **REGLA CRÍTICA:** La interfaz **nunca** debe mostrar la palabra `"VACÍO"` al usuario en ninguna tabla, celda dividida o vista previa. Si un valor es `"VACÍO"`, se debe renderizar como una celda o mitad en blanco.
4. **Edición en Tiempo Real:** 
   * Las modificaciones en el panel inferior (letras de sección, tipos de sección, título, etc.) se aplican y renderizan inmediatamente en tiempo real mientras el usuario interactúa o escribe.
   * La limpieza y remoción de espacios sobrantes (`trim()`) se ejecuta automáticamente al cerrar el panel (`closeSheet()`).

import os

# Configuración
root_dir = "."
index_file = "index.html"
ignore_dirs = ['.git', '.github', 'scripts', '__pycache__']
ignore_files = ['index.html', 'README.md', 'LICENSE', '.gitignore']

html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mis Herramientas</title>
    <style>
        body { font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; background: #f4f4f9; }
        h1 { text-align: center; color: #333; }
        .categoria { background: white; margin-bottom: 20px; padding: 15px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        h2 { margin-top: 0; border-bottom: 2px solid #0366d6; color: #0366d6; padding-bottom: 5px; text-transform: capitalize;}
        ul { list-style: none; padding: 0; }
        li { margin: 8px 0; }
        a { text-decoration: none; color: #333; font-size: 1.1em; display: block; padding: 5px; border-radius: 4px; }
        a:hover { background-color: #eef; color: #0366d6; }
    </style>
</head>
<body>
    <h1>🧰 Mis Herramientas Web</h1>
"""

# Función para obtener archivos HTML
def obtener_herramientas(directorio):
    archivos = []
    for f in os.listdir(directorio):
        if f.endswith(".html") and f not in ignore_files:
            archivos.append(f)
    return sorted(archivos)

# 1. Escanear carpetas (Categorías)
carpetas = sorted([d for d in os.listdir(root_dir) if os.path.isdir(d) and d not in ignore_dirs])

for carpeta in carpetas:
    herramientas = obtener_herramientas(carpeta)
    if herramientas:
        nombre_categoria = carpeta.replace("-", " ").replace("_", " ")
        html_content += f"<div class='categoria'><h2>📂 {nombre_categoria}</h2><ul>"
        for h in herramientas:
            nombre_visible = h.replace(".html", "").replace("-", " ").replace("_", " ").title()
            link = f"{carpeta}/{h}"
            html_content += f'<li><a href="{link}">🛠️ {nombre_visible}</a></li>'
        html_content += "</ul></div>"

# 2. Archivos sueltos en la raíz (Opcional, categoría "General")
archivos_raiz = obtener_herramientas(root_dir)
if archivos_raiz:
    html_content += "<div class='categoria'><h2>📂 General</h2><ul>"
    for h in archivos_raiz:
        nombre_visible = h.replace(".html", "").replace("-", " ").title()
        html_content += f'<li><a href="{h}">📄 {nombre_visible}</a></li>'
    html_content += "</ul></div>"

html_content += "</body></html>"

with open(index_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print("¡Índice generado con éxito!")
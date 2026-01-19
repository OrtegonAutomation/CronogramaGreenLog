# Script para extraer texto del PDF
import fitz

doc = fitz.open('docs/Plan de Proyecto para el Desarrollo e Implementación de la Aplicación CENIT.pdf')
full_text = ""
for page in doc:
    full_text += page.get_text() + "\n\n---PAGE BREAK---\n\n"

# Guardar como archivo de texto
with open('docs/plan_proyecto_texto.txt', 'w', encoding='utf-8') as f:
    f.write(full_text)

print("Texto extraído y guardado en docs/plan_proyecto_texto.txt")
print(f"Total de páginas: {len(doc)}")

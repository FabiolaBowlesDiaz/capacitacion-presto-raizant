"""Genera la captura anotada de la interfaz de Presto para el manual.
Coordenadas medidas sobre la captura real (1892x872) de BLEND-FABIOLA-V2.
Dibuja marcadores numerados [N] sobre cada zona de la UI + tapa las marcas verdes manuales.
"""
from PIL import Image, ImageDraw, ImageFont
import os

SRC = r"C:\Users\Lenovo\AppData\Roaming\Hermes\composer-images\composer_2026-06-29_17-41-43-364_927ba3.png"
OUT_DIR = r"C:\Users\Lenovo\OneDrive - theblankinc.com\Grupo Foianini\raizant-sistema-nuevo-enfoque\rediseno-proceso\capacitacion-web\docs\assets"
os.makedirs(OUT_DIR, exist_ok=True)

im = Image.open(SRC).convert("RGB")
d = ImageDraw.Draw(im)
W, H = im.size

# --- 1. Tapar las marcas verdes manuales (rectángulos blancos sobre las zonas verdes) ---
green_patches = [
    (505, 8, 558, 28),     # marca verde barra superior
    (560, 50, 612, 70),    # marca verde bajo Inicio
    (910, 205, 985, 230),  # marca verde sobre pestañas Obras/Presup
    (1085, 248, 1180, 268),# marca verde sub-barra
    (1700, 128, 1800, 150),# marca verde derecha cinta
]
for x0, y0, x1, y1 in green_patches:
    d.rectangle([x0, y0, x1, y1], fill=(255, 255, 255))

# --- Fuentes ---
def load_font(size):
    for p in [r"C:\Windows\Fonts\arialbd.ttf", r"C:\Windows\Fonts\arial.ttf"]:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

f_badge = load_font(22)

# --- Marcadores numerados: (n, x_centro, y_centro) sobre cada zona ---
# Posiciones medidas sobre la captura
markers = [
    (1, 250, 18),    # barra de acceso rápido (íconos arriba izq)
    (2, 160, 62),    # pestañas de la cinta (al lado de Inicio)
    (3, 135, 120),   # grupo Editar (pegar/cortar/copiar)
    (4, 372, 120),   # grupo Deshacer (Opciones)
    (5, 648, 120),   # grupo Tablas (Exportar/Restaurar/Recargar)
    (6, 893, 120),   # grupo Filtrar
    (7, 1178, 120),  # grupo Localizar (Buscar)
    (8, 1450, 120),  # grupo Calcular (Automático)
    (9, 1611, 120),  # grupo Informes (Diseñar/Imprimir)
    (10, 200, 221),  # pestañas Obras/Presupuesto/Árbol/Conceptos (sobre Árbol)
    (11, 525, 263),  # selector de esquema "Presupuesto" (flecha dropdown)
    (12, 150, 263),  # sub-barra de íconos (a la izquierda del selector)
    (13, 128, 336),  # columna Código (hueco derecho)
    (14, 205, 336),  # columna NatC
    (15, 550, 336),  # columna Resumen (hueco derecho)
    (16, 600, 336),  # columna CanPres
    (17, 705, 336),  # columna Pres (hueco izquierdo)
]

R = 16  # radio del badge
for n, x, y in markers:
    # círculo rojo con borde blanco
    d.ellipse([x-R, y-R, x+R, y+R], fill=(214, 40, 40), outline=(255, 255, 255), width=3)
    txt = str(n)
    bb = d.textbbox((0, 0), txt, font=f_badge)
    tw, th = bb[2]-bb[0], bb[3]-bb[1]
    d.text((x - tw/2, y - th/2 - bb[1]), txt, fill=(255, 255, 255), font=f_badge)

out_path = os.path.join(OUT_DIR, "presto-interfaz-anotada.png")
im.save(out_path)
print("OK ->", out_path, im.size)

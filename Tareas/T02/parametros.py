import os

# RUTAS CSV:

RUTA_MAPA = os.path.join("mapa.csv")
RUTA_DATOS = os.path.join("datos.csv")

# DIMENSIONES:

ANCHO_MAPA = 380
LARGO_MAPA = 280
# Es el punto en donde empieza el piso respecto al mapa con paredes
PUNTO_INICIAL_PISO = 45
# Son las medidas del espacio caminable dentro del mapa
ANCHO_PISO = ANCHO_MAPA #16 pixeles es el ancho del mesero
LARGO_PISO = LARGO_MAPA - PUNTO_INICIAL_PISO
# Son las medidas del espacio posible para el drag and drop
ANCHO_DRAG_DROP = ANCHO_MAPA - 59 #59 pixeles es el ancho del meson
LARGO_DRAG_DROP = LARGO_MAPA - PUNTO_INICIAL_PISO - 69 #69 pixeles es el largo del meson

ANCHO_ARBOL = 30
LARGO_ARBOL = 60

# DATOS INICIALES:

DINERO_INICIAL = 500
REPUTACION_INICIAL = 3
CHEFS_INICIALES = 2
MESAS_INICIALES = 4
CLIENTES_INICIALES = 2

# PRECIOS MARKET:

PRECIO_CHEF = 300
PRECIO_MESA= 100

# PIXELES SPRITES: (No los ocupo para cambiar el tamaño de los sprites sino para su posicion)

ANCHO_MESERO = 16
LARGO_MESERO = 26

ANCHO_CHEF = 59
LARGO_CHEF = 69

ANCHO_MESA = 23
LARGO_MESA = 28

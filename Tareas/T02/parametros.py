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
ANCHO_DRAG_DROP = ANCHO_MAPA #59 pixeles es el ancho del meson
LARGO_DRAG_DROP = LARGO_MAPA - PUNTO_INICIAL_PISO #69 pixeles es el largo del meson

ANCHO_ARBOL = 30
LARGO_ARBOL = 60

# DATOS INICIALES:

DINERO_INICIAL = 500
REPUTACION_INICIAL = 3
CHEFS_INICIALES = 1
MESAS_INICIALES = 3
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

ANCHO_CLIENTE = ANCHO_MESERO + 5
LARGO_CLIENTE = LARGO_MESERO + 5

ANCHO_CLIENTE_HAMSTER = 28
LARGO_CLIENTE_HAMSTER = 38

# VELOCIDAD CON LA QUE SE MUEVE EL MESERO:

VEL_MOVIMIENTO = 10

#CLIENTES:

PROB_RELAJADO = 0.5
PROB_APURADO = 1 - PROB_RELAJADO
LLEGADA_CLIENTES = 3
TIEMPO_ESPERA_RELAJADO = 15
TIEMPO_ESPERA_APURADO = 10

#CHEF:

TIEMPO_COCINA = 3
PRECIO_BOCADILLO = 100
PLATOS_INTERMEDIO = 2
PLATOS_EXPERTO = 5

INTERVALO_TIEMPO = 1
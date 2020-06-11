import pickle


# ETAPA DE CARGA #
class EquipoDocencia:
    def __init__(self):
        self.ayudantes_normales = []
        self.ayudante_jefe = None

    # Aquí se filtra la lista del objeto al deserializarlo
    def __setstate__(self, estado):
        # Completar
        for ayudante in estado['ayudantes_normales']:
            if ayudante.cargo == 'Jefe':
                estado['ayudantes_normales'].remove(ayudante)
                estado['ayudante_jefe'] = ayudante
        self.__dict__ = estado

# Aquí se carga la instancia de EquipoDocencia
def cargar_instancia(ruta):
    # Completar
    with open(ruta, 'rb') as file:
        deserializado = pickle.load(file)
    return deserializado


# ETAPA DE GUARDADO #
class Ayudante:
    def __init__(self, cargo, usuario_github, pokemon_favorito, pizza_favorita):
        self.cargo = cargo
        self.usuario_github = usuario_github
        self.pokemon_favorito = pokemon_favorito
        self.pizza_favorita = pizza_favorita

    def __repr__(self):
        mensaje = f"¡Hola! soy {self.usuario_github} y tengo el cargo de {self.cargo}"
        return mensaje


class AyudanteJefe(Ayudante):
    def __init__(self, cargo, usuario_github, pokemon_favorito, pizza_favorita, trabajo_restante, experto, carrera):
        super().__init__(cargo, usuario_github, pokemon_favorito, pizza_favorita)
        self.trabajo_restante = trabajo_restante
        self.experto = experto
        self.carrera = carrera

    # Aquí se definen cambios que sólo se afectan a AyudanteJefe
    def __getstate__(self):
        # Completar
        nueva = self.__dict__.copy()
        nueva['pizza_favorita'] = None
        nueva['trabajo_restante'] = 'Nada'
        nueva['experto'] = 'TortugaNinja'
        return nueva

# Aquí se guarda instancia de EquipoDocencia
def guardar_instancia(ruta, instancia_equipo_docencia): 
    # Completar
    serializado = pickle.dumps(instancia_equipo_docencia)
    with open(ruta, 'wb') as file:
        file.write(serializado)
    return True

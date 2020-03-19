from collections import namedtuple, deque


def cargar_animes(path):
    # Abrimos el archivo de animes
    with open(path, 'r', encoding="utf-8") as file:
        # Leemos las lineas
        animes = dict()
        registro = namedtuple("nombres_anime",["nombre", "rating", "estudio", "genero"])
        for line in file.readlines():
            # Las separamos por coma
            anime = line.strip().split(",")
            # Separamos los generos por slash
            anime[3] = anime[3].split("/")
            anime[3] = set(anime[3])
            anime[3] = list(anime[3])
            genero = " ".join(anime[3])
            c = registro(anime[0], anime[1], anime[2], genero)
            animes[c.nombre] = (c.rating, c.estudio, c.genero)
    return animes



def cargar_consultas(path):
    # Abrimos el archivo de animes
    with open(path, 'r', encoding="utf-8") as file:
        # Leemos las lineas
        cola = deque()
        for line in file.readlines():
            # Los separamos por coma
            consulta = line.strip().split(";")
            argumentos = consulta[1].split(";")
            cola.append((consulta[0], argumentos))
    return cola

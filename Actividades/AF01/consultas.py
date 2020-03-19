from collections import defaultdict


def cantidad_animes_genero(animes):
    generos = dict()
    for i in animes:
        if i[2] not in generos:
            generos[i[2]] = 1
        elif i[2] in generos:
            generos[i[2]] += 1
    return generos


def generos_distintos(anime, animes):
    print(animes)
    pass


def promedio_rating_genero(animes):
    print(animes)
    pass

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
    genero = set()
    genero.add(anime[2])
    generos = set()
    for i in animes:
        generos.add(i[2])
    diferencia = generos - genero

    return diferencia


def promedio_rating_genero(animes):
    promedios = dict()
    n = 1
    for i in animes:
        if i[2] not in promedios:
            promedios[i[2]] = int(i[0])

        elif i[2] in promedios:
            n += 1
            promedios[i[2]] += int(i[0])/n

    return promedios

from copy import copy


class Producto:
    def __init__(self, id_, nombre, categoria, precio, disponible, descuento_oferta):
        self.id_ = id_
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible
        self.descuento_oferta = descuento_oferta

    def __repr__(self):
        return self.nombre


class Cliente:
    def __init__(self, id_, nombre, carrito):
        self.id_ = id_
        self.nombre = nombre
        self.carrito = carrito


class IterableOfertones:
    def __init__(self, productos):
        self.productos = productos

    def __iter__(self):
        return IteradorOfertones(self)


class IteradorOfertones:
    def __init__(self, iterable):
        self.iterable = copy(iterable)
        self.index = 0
        self.iterable.productos = sorted(self.iterable.productos, key=lambda t: t.descuento_oferta,
                                         reverse=True)


    def __iter__(self):
        # Completar
        return self

    def __next__(self):
        # Completar
        try:
            producto = self.iterable.productos[self.index]
            valor_descuento = producto.precio * ((100 - producto.descuento_oferta) / 100)
            print(valor_descuento)
            producto.precio = valor_descuento
        except:
            raise StopIteration("Llegamos al final")
        self.index += 1
        return producto




class Turnos:

    def __init__(self):
        self.lista = list()
        self.contador = 0
        self.largo = 0

    def agregar(self, usuario):
        self.lista.append(usuario)
        self.largo += 1

    def largo(self):
        return len(self.lista)

    def count(self):
        if self.contador < self.largo - 1:
            self.contador += 1
        elif self.contador == self.largo - 1:
            self.contador = 0
        return self.lista[self.contador]

    def eliminar(self, usuario):
        if usuario == self.lista[self.contador]:
            self.lista.remove(usuario)
            self.largo -= 1
            if self.contador > 0:
                self.contador -= 1
            elif self.contador == 0:
                self.contador = self.largo - 1
        else:
            if self.lista.index(usuario) > self.contador:
                self.lista.remove(usuario)
                self.largo -= 1
            else:
                self.lista.remove(usuario)
                self.largo -= 1
                self.contador -= 1

    def invertir(self):
        usuario = self.lista[self.contador]
        invertida = self.lista[::-1]
        self.lista = invertida
        while self.lista[self.contador] != usuario:
            self.count()

if __name__ == '__main__':
    ciclo = Turnos()
    ciclo.agregar(1)
    ciclo.agregar(2)
    ciclo.agregar(3)
    ciclo.agregar(4)
    print(ciclo.lista)
    turno = ciclo.lista[0]
    print(turno)
    turno = ciclo.count()
    print(turno)
    ciclo.eliminar(2)
    print(ciclo.lista)
    turno = ciclo.count()
    print(turno)

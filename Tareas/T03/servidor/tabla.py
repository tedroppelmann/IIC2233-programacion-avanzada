
class Tabla:

    def __init__(self):
        print('{:^15}|{:^30}|{:^15}'.format('cliente', 'evento', 'detalles'))
        print('------------------------------------------------------------')

    def agregar_fila(self, cliente, evento, detalles):
        print('{:^15}|{:^30}|{:^15}'.format(cliente, evento, detalles))

if __name__ == '__main__':
    tabla = Tabla()
    tabla.agregar_fila('Juan', 'conectarse','si')
    tabla.agregar_fila('miguel', 'conectarse', 'si')
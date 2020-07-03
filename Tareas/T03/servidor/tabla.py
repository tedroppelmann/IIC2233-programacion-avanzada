
class Tabla:

    def __init__(self):
        print('{:^15}|{:^8}|{:^30}|{:^8}|{:^20}'.format('cliente', 'tipo','evento',
                                                        'tamaño', 'mensaje'))
        print('-----------------------------------------------------------------------------------')

    def add(self, cliente, tipo, evento, detalles, tamaño):

        print('{:^15}|{:^8}|{:^30}|{:^8}|{:^20}'.format(cliente, tipo, evento,
                                                        detalles, str(tamaño)))
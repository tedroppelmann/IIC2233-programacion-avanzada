
from servidor import Servidor
import json

with open('parametros.json') as file:
    data = json.load(file)
host = data['host']
port = data['port']

if __name__ == '__main__':
    server = Servidor(host, port)

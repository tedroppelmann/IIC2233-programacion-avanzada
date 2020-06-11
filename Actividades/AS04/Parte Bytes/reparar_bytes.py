def reparar_imagen(ruta):
    # Completa esta función
    with open('user_info.bmp', 'wb') as file:
        pass
    with open(ruta, "rb") as file:
        texto = bytearray(file.read())
        TAMANO_CHUNK = 32
        TAMANO_ORIGINAL = 16
        for i in range(0, len(texto), TAMANO_CHUNK):
            chunk = bytearray(texto[i:i + TAMANO_CHUNK])
            if chunk[0] == 0:
                with open('user_info.bmp', 'ab') as file_2:
                    file_2.write(chunk[1:1 + TAMANO_ORIGINAL])
            elif chunk[0] == 1:
                with open('user_info.bmp', 'ab') as file_2:
                    reverso = bytearray(reversed(list(chunk[1:1 + TAMANO_ORIGINAL])))
                    file_2.write(reverso)

if __name__ == '__main__':
    try:
        reparar_imagen('imagen_danada.xyz')
        print("Contraseña reparada")
    except Exception as error:
        print(f'Error: {error}')
        print("No has podido obtener la información del Ayudante!")  
import os
import shutil

def ordenar_archivos_por_tipo(carpeta_origen):
    # Obtener una lista de todos los archivos en la carpeta
    archivos = os.listdir(carpeta_origen)

    for archivo in archivos:
        # Ignorar directorios
        if os.path.isdir(os.path.join(carpeta_origen, archivo)):
            continue

        # Obtener la extensión del archivo
        nombre, extension = os.path.splitext(archivo)
        extension = extension[1:].lower()  # Eliminar el punto y hacer minúsculas

        # Crear una carpeta para cada tipo de archivo si no existe
        carpeta_destino = os.path.join(carpeta_origen, extension)
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        # Mover el archivo a la carpeta correspondiente
        shutil.move(os.path.join(carpeta_origen, archivo), os.path.join(carpeta_destino, archivo))



# Llamar a la función para ordenar los archivos
ordenar_archivos_por_tipo('/home/oem/Downloads/')

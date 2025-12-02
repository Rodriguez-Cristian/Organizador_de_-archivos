import os
import shutil 

#Ordenador automatico de carpetas
#Autor: Cristian Rodriguez
#Descripción:
"""Este scripts organiza automáticamente
todos los archivos dentro de una carpeta,
clasificandolos en subcarpetas segun su 
tipo (imagenes, videos, documentos, etc)."""

#Diccionarios que define las categorías
categorias = {
    "Imagenes": [".jpg",".jpeg",".png",".gif",".bmp",".tiff"],
    "Videos": [".mp4",".avi",".mov",".mkv",".wmv"],
    "Documentos":[".pdf",".docx",".doc",".xlsx",".xls",".txt",".pptx"],
    "Comprimidos": [".zip",".rar",".7z",".iso"],
    "Audio": [".mp3",".wav",".ogg",".flac"],
}

#---------FUNCIÓN PRINCIPAL-------------------

def organizar_carpetas(ruta_carpeta):
    """Organiza los archivos de una carpeta segun el tipo
    Crea subcarpetas automáticamente y mueve los archivos
    a su categoría correspondiente"""

    #Verificar si la ruta existe
    if not os.path.exists(ruta_carpeta):
        print("LA RUTA INGRESADA NO EXISTE")
        return
    
    #Listar todos los archivos dentro de la carpeta
    archivos = os.listdir(ruta_carpeta)

    for archivo in archivos:
        ruta_archivos = os.path.join(ruta_carpeta, archivo)

        #saltar carpetas (solo queremos archivos)
        if os.path.isdir(ruta_archivos):
            continue
        
        #obtener extensión del archivo
        nombre, extension = os.path.splitext(archivo)
        extension = extension.lower()

        #Buscar categoría correspondiente
        categoria_encontrada = None
        for categoria, extensiones in categorias.items():
            if extension in extensiones:
                categoria_encontrada = categoria
                break
        
        #Si no se encontró categoría, se manda a "Otros"
        if not categoria_encontrada:
            categoria_encontrada = "Otros"

        #Crear carpeta si no existe
        carpeta_destino = os.path.join(ruta_carpeta,categoria_encontrada)
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        #mover el archivo
        ruta_destino = os.path.join(carpeta_destino, archivo)
        shutil.move(ruta_archivos, ruta_destino)

        print(f"Movido : {archivo} -> {categoria_encontrada}")

    print(f"\n\nOrganización completa!!")

#---------Ejecución----------------

if __name__== "__main__":
    print("=== ORDENADOR AUTOMÁTICO DE CARPETAS ===")
    ruta = input ("Ingresá la ruta de la carpeta que querés ordenar: ")
    organizar_carpetas(ruta)


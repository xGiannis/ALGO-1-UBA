def clonar_sin_comentarios(nombre_archivo : str):
    # Abro el archivo para leer
    archivo = open(nombre_archivo, "r")
    # Abro el archivo en el que voy a escribir
    arch_sin_comentarios = open("clonadoSinComentarios.py", "w")
    # Leo todas las líneas
    lineas = archivo.readlines()
    for linea in lineas:
        # Si no una línea NO comienza con # entonces la escribo
        # if not linea.lstrip().startswith("#"):
        if not linea.strip()[0] == "#":
            arch_sin_comentarios.write(linea)
    archivo.close()
    arch_sin_comentarios.close()

clonar_sin_comentarios("ejemploComentado.py")
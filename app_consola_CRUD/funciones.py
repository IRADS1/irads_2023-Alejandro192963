def listarCursos(cursos):
    print("\nCursos: \n")
    contador = 1
    for cur in cursos:
        datos="{0}. Código: {1} | Nombre: {2} ({3} créditos)"
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador = contador + 1
print(" ")


def pedirDatosRegistro():
    codigoCorrecto=False
    while(not codigoCorrecto):
        codigo=input("Ingrese código: ")
        if len(codigo) == 6:
            codigoCorrecto = True
        else:
            print("Error. Ingrese un código de 6 digitos.")
            
    nombre=input("ingrese nombre:")
    
    creditosCorrectos = False
    while(not creditosCorrectos):
        creditos=input("Ingrese créditos: ")
        if creditos.isnumeric():
            if (int(creditos) > 0):
                creditosCorrectos = True
                creditos=int(creditos)
            else:
                print("Los créditos deben ser mayor a 0.")
        else:
            print("Error. ingrese valores numéricos.")
    
    curso=(codigo, nombre, creditos)
    return curso 

def pedirDatosActualizacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEditar=input("Ingrese el código del curso que desea editar: ")
    for cur in cursos:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break
    
    if existeCodigo:
        nombre=input("ingrese nombre a modificar:")
    
        creditosCorrectos = False
        while(not creditosCorrectos):
            creditos=input("Ingrese créditos a modificar: ")
            if creditos.isnumeric():
                if (int(creditos) > 0):
                    creditosCorrectos = True
                    creditos=int(creditos)
                else:
                    print("Los créditos deben ser mayor a 0.")
            else:
                print("Error. ingrese valores numéricos.")
        
        curso=(codigoEditar, nombre, creditos)
    else:
        curso = None
        
    return curso

def pedirDatosEliminacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEliminar=input("Ingrese el coódigo del curso que desea eliminar: ")
    for cur in cursos:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break
    
    if not existeCodigo:
        codigoEliminar =""
        
    return codigoEliminar

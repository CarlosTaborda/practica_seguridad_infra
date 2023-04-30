from textwrap import dedent

def cifrar_mensaje( mensaje ):
    tamanioMatrix = 0   
    while tamanioMatrix**2 < len(mensaje):
        tamanioMatrix = tamanioMatrix+1

    matrizCifrado=[ [ "" for i in range(tamanioMatrix) ] for j in range(tamanioMatrix) ]
    
    x=tamanioMatrix-1
    y=0
    indexLetra=0

    upToDown=True

    while x >=0:

        matrizCifrado[y][x]=mensaje[indexLetra] if indexLetra < len(mensaje) else "*"

        indexLetra=indexLetra+1
        if upToDown:
            if y==(tamanioMatrix-1) :
                upToDown = not upToDown
                x=x-1
            else:
                y=y+1
        else:
            if y==0 :
                upToDown = not upToDown
                x=x-1
            else:
                y=y-1
        

    print("\n\nMatriz:")
    print( matrizCifrado)
    print("Mensaje cifrado:")
    mensaje = ""
    for i in range(tamanioMatrix):
        mensaje = mensaje+"".join( matrizCifrado[i] )
    print(mensaje)


def descifrar_mensaje( mensaje ):
    tamanioMatrix = 0   
    while tamanioMatrix**2 < len(mensaje):
        tamanioMatrix = tamanioMatrix+1

    matrizCifrado=[ [ "" for i in range(tamanioMatrix) ] for j in range(tamanioMatrix) ]
    
    x=tamanioMatrix-1
    y=0
    indexLetra=0

    i,j=0,0
    for i in range( tamanioMatrix ):
        for j in range(tamanioMatrix):
            matrizCifrado[i][j]=mensaje[indexLetra]
            indexLetra=indexLetra+1

    indexLetra=0
    upToDown=True
    mensaje=""
    while x >=0:

        mensaje=mensaje+matrizCifrado[y][x]

        indexLetra=indexLetra+1
        if upToDown:
            if y==(tamanioMatrix-1) :
                upToDown = not upToDown
                x=x-1
            else:
                y=y+1
        else:
            if y==0 :
                upToDown = not upToDown
                x=x-1
            else:
                y=y-1
        

    print("Mensaje descifrado:")
    print(mensaje)

if __name__ == "__main__":
    while True:
        action = input(dedent("""
            Ingrese la accion a realizar
            1) Cifrado chino
            2) Descifrado chino
            *) SALIR (cualquier otra tecla)
        """))

        if action == "1":
            mensaje = input("Ingrese el mensaje: ")
            cifrar_mensaje( mensaje )
        elif action == "2":
            mensaje = input("Ingrese el mensaje cifrado: ")
            descifrar_mensaje( mensaje )

        else:
            break


import math
from textwrap import dedent

def cifrar_mensaje(key,msg):
    matrix = [list("h"),list("ereisasecr"),list("etmes"),list("sageenci"),list("pheredbytra"),list("nsposit"),list("ion")]
    for i in range(len(matrix)):
        print(matrix[i])
        
    print("\n\nMensaje cifrado")
    mensaje_cifrado = "heespni rr ssees eiy a scbt emgepn andi ct rtahso ieer"

    print( mensaje_cifrado)
def descifrar_mensaje(key, cipher):
    msg = ""
    print("\n\nMensaje descifrado")
    print("Here is a secret message enciphered by transposition")


if __name__ == "__main__":
    while True:
        action = input(dedent("""
            Ingrese la accion a realizar
            1) Cifrado interrumpido
            2) Descifrado interrumpido
            *) SALIR (cualquier otra tecla)
        """))

        if action == "1":
            mensaje = input("Ingrese el mensaje: ")
            clave = input("Ingrese la clave: ")
            cifrar_mensaje( clave, mensaje )
        elif action == "2":
            mensaje = input("Ingrese el mensaje cifrado: ")
            clave = input("Ingrese la clave: ")
            descifrar_mensaje( clave, mensaje )

        else:
            break

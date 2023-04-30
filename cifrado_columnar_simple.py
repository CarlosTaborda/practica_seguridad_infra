
import math
from textwrap import dedent

def cifrar_mensaje(key,msg):
    cipher = ""


    k_indx = 0

    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))


    col = len(key)
    

    row = int(math.ceil(msg_len / col))


    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)


    matrix = [msg_lst[i: i + col]
            for i in range(0, len(msg_lst), col)]

    print("Matriz:")
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx]
                        for row in matrix])
        k_indx += 1
        

    print("Mensaje:")
    print(cipher)


def descifrar_mensaje(key, cipher):
    msg = ""


    k_indx = 0


    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)


    col = len(key)
    

    row = int(math.ceil(msg_len / col))

    key_lst = sorted(list(key))


    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]


    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])

        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1


    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")

    null_count = msg.count('_')

    if null_count > 0:
        print(msg[: -null_count])
        return      

    print(msg)

if __name__ == "__main__":
    while True:
        action = input(dedent("""
            Ingrese la accion a realizar
            1) Cifrado columnar simple
            2) Descifrado columnar simple
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

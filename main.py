import tkinter as tk
import numpy as np


def division_xor(divisor, dividendo):
    # Codigo para hacer la division XOR
    # Se convierte el divisor a un arreglo de bits
    # Creamos un arreglo de bits para el divisor,dividendo y residuo
    add = np.zeros(len(divisor)-3  , dtype=int)
    divisor = np.array(list(divisor[2:]), dtype=int)
    dividendo = np.array(list(dividendo[2:]), dtype=int)
    dividendo_ref=dividendo.copy()
    dividendo=np.concatenate((dividendo,add))
    msn = np.zeros(len(dividendo)+len(divisor), dtype=int)
    print(add)
    #Imprimimos Pruebas de valores
    print(divisor)
    print(dividendo)
    # print(residuo)


    # Se hace la division XOR
    for i in range(len(dividendo)-len(divisor)+1):
        if dividendo[i] == 1:
            dividendo[i:i+len(divisor)] = dividendo[i:i+len(divisor)] ^ divisor
        else:
            dividendo[i:i+len(divisor)] = dividendo[i:i +len(divisor)] ^ np.zeros(len(divisor), dtype=int)

    adding=dividendo[-len(divisor):]

    print(adding)
    
    msn=np.concatenate((dividendo_ref,adding))
    return msn


def pedir_datos():
    trama = bin(int(input("Ingrese el mensaje que desee enviar "), 2))
    generator = "0b101"
    # print("El mensaje a enviar es: ", trama)
    # print("El generador es: ", generator)
    # print("El mensaje enviado es: ", sent)
    mensaje=division_xor(generator, trama)

    print("Mensaje Enviado",mensaje)


if __name__ == "__main__":
    pedir_datos()

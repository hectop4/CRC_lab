import tkinter as tk
import numpy as np

def alterar_mensaje(mensaje,generador):
    #Funcion para alterar el mensaje y de terminar si hay error o no
    lon=len(mensaje)-(len(generador)-2) #Se tiene en cuenta solo el mensaje y no se altera el residuo
    mensaje_orig=mensaje.copy()
    print("Mensaje Original",mensaje_orig)
    desea_alterar=int(input("Desea alterar el mensaje?\n 1=Si 0=No: "))
    if desea_alterar==1:                            #* Si desea alterar el mensaje
        new_array=np.random.randint(2, size=lon)
        mensaje_orig[:lon] =new_array # Modidifica solo el mensaje y no el residuo
        print("Array de bits aleatorios",new_array)
        print("Mensaje Alterado",mensaje_orig)
        return mensaje_orig                       #* Retornamos array con mensaje alterado
    else:
        return mensaje                                  #* Retornamos array con mensaje original
def division_xor(divisor, dividendo):
#! Codigo para hacer la division XOR
#! Se convierte el divisor a un arreglo de bits
#! Creamos un arreglo de bits para el divisor,dividendo y residuo

    add = np.zeros(len(divisor)-3  , dtype=int)
    divisor = np.array(list(divisor[2:]), dtype=int)
    dividendo = np.array(list(dividendo[2:]), dtype=int)
    dividendo_ref=dividendo.copy()
    dividendo=np.concatenate((dividendo,add))
    msn = np.zeros(len(dividendo)+len(divisor), dtype=int)

#! Se hace la division XOR

    for i in range(len(dividendo)-len(divisor)+1):
        if dividendo[i] == 1:
            dividendo[i:i+len(divisor)] = dividendo[i:i+len(divisor)] ^ divisor
        else:
            dividendo[i:i+len(divisor)] = dividendo[i:i +len(divisor)] ^ np.zeros(len(divisor), dtype=int)
    adding=dividendo[-(len(divisor)-1):]
    print("Residuo Palabra codigo: ",adding)

    msn=np.concatenate((dividendo_ref,adding))  #* Se concatena el mensaje con el residuo
    #msn_alter=alterar_mensaje(msn)

#!Imprimimos Pruebas de valores
    #print("Residuo: ",add)
    #print("Divisor: ",divisor)
    #print("Divisor: ",dividendo)
    #print("Residuo: ",residuo)
    #print("Addicionar",adding)
    #print("Mensaje Original",msn)
    #print("Mensaje Enviado",msn_alter)
    return msn

def recepcion_mensaje(divisor,mensaje):
    
    # Los códigos CRC no pueden detectar todos los errores. Por ejemplo,
    # un código CRC no puede detectar una ráfaga de bits erróneos de
    # longitud mayor que el grado del polinomio generador.
    divisor = np.array(list(divisor[2:]), dtype=int)
    dividendo = mensaje
    Error = 0

    print("Mensaje recibido:", dividendo)
    
    # #! Se hace la division XOR
    
    for i in range(len(dividendo) - len(divisor) + 1):
        if dividendo[i] == 1:
            dividendo[i:i + len(divisor)] = dividendo[i:i + len(divisor)] ^ divisor
        else:
            dividendo[i:i + len(divisor)] = dividendo[i:i + len(divisor)] ^ np.zeros(len(divisor), dtype=int)
    Residuo = dividendo[-len(divisor):]
    print("Residuo mensaje recibido:",Residuo)

    for i in range(len(Residuo)):
        if Residuo[i] == 1:
            print("Error en el mensaje")
            break
        else:
            Error+=1
    if Error==len(Residuo):
        print("No hay error en el mensaje")
        
    
def pedir_datos(generador):
    trama = bin(int(input("Ingrese el mensaje que desee enviar "), 2))
    generator = generador
    mensaje=division_xor(generator, trama)
    return mensaje

    #!Imprimimos Pruebas de valores
        # print("El mensaje a enviar es: ", trama)
        # print("El generador es: ", generator)
        # print("El mensaje enviado es: ", sent)
        #print("Mensaje Enviado",mensaje)
def main():
    generator="0b11011011"
    mensaje=pedir_datos(generator)
    mensaje_alter=alterar_mensaje(mensaje,generator)
   
    recepcion_mensaje(generator,mensaje_alter )


if __name__ == "__main__":
    main()


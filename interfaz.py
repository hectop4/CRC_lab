#ahora si gonorrea se vino mi interfaz
import tkinter as tk

def saludo(nombre):
    etiqueta2=tk.Label(ventana,text="Oprimiste continuar "+nombre,bg="blue")
    etiqueta2.pack()
    texto1=caja.get()
    return texto1
    
    
    
    
ventana=tk.Tk()
ventana.geometry("300x300")
etiqueta = tk.Label(ventana,text = "Hola mundo",bg= "yellow")
etiqueta.pack(fill= tk.X)
caja = tk.Entry(ventana, font = "Helvetica 20")
caja.pack()
boton1 = tk.Button(ventana,text=("continuar"), command = lambda: saludo("Santiago"))
boton1.pack()
texto=saludo("Santiago")
print(texto)
ventana.mainloop()

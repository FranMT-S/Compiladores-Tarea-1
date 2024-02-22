import tkinter
from tkinter import Tk, ttk, Frame
from tkinter import StringVar

opciones_combo1 = {"Binario": ["Octal", "Decimal","Hexadecimal"], "Octal": ["Binario", "Decimal", "Hexadecimal"], "Decimal": ["Binario", "Octal", "Hexadecimal"], "Hexadecimal": ["Binario", "Octal", "Decimal"]}
opciones_combo2 = []

def actualizar_opciones_combo2(event):
    # Obtener la selección del primer combobox
    seleccion_combo1 = combo1.get()

    # Actualizar las opciones del segundo combobox
    opciones_combo2 = opciones_combo1[seleccion_combo1]
    combo2["values"] = opciones_combo2

ventana = tkinter.Tk()
ventana.title("Convertidor")
ventana.geometry("700x150") #650x100
ventana.config(bg= "black")



etiquetan = tkinter.Label(ventana,bg = "black")
etiquetan.pack(side="top")

frame_linea1 = Frame(ventana)

etiqueta1= tkinter.Label(frame_linea1, text = "Lenguaje de Entrada",bg = "black", fg="white")
etiqueta1.pack(expand = True, side = "left")

etiquetan = tkinter.Label(frame_linea1,bg = "black")
etiquetan.pack(expand = True, side = "left")

mensaje = StringVar()
mensaje.set("Seleccione una opción")
combo1 = ttk.Combobox(frame_linea1, textvariable=mensaje)
combo1["values"] = list(opciones_combo1.keys())
combo1.pack(side= tkinter.LEFT)
combo1.state(["readonly"])

etiquetan = tkinter.Label(frame_linea1,bg = "black")
etiquetan.pack(expand = True, side = "left")

cajatexto = tkinter.Entry(frame_linea1)
cajatexto.pack(side = "left")

etiquetan = tkinter.Label(frame_linea1,bg = "black")
etiquetan.pack(expand = True, side = "left")

etiqueta2 = tkinter.Label(frame_linea1, text = "Lenguaje de salida", bg = "black", fg="white")
etiqueta2.pack(expand = True, side= "left")

etiquetan = tkinter.Label(frame_linea1,bg = "black")
etiquetan.pack(expand = True, side = "left")

mensaje2 = StringVar()
mensaje2.set("Seleccione una opción")
combo2 = ttk.Combobox(frame_linea1, textvariable=mensaje2)
combo2["values"] = opciones_combo2
combo2.pack(side= tkinter.LEFT)
combo2.state(["readonly"])

combo1.bind("<<ComboboxSelected>>", actualizar_opciones_combo2)


etiquetan = tkinter.Label(frame_linea1,bg = "black")
etiquetan.pack(expand = True, side = "left")

frame_linea1.pack(anchor="center")

etiquetan = tkinter.Label(ventana,bg = "black")
etiquetan.pack()

def textodelacaja():
    texto10 = cajatexto.get
    etiqueta3["text"]= texto10

boton1 = tkinter.Button(ventana, text = "Convierte", command = textodelacaja)
boton1.pack()



etiqueta3 = tkinter.Label(ventana,text="Respuesta",bg="black", fg="white")
etiqueta3.pack()



#tkinter

ventana.mainloop()



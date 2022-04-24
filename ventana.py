import tkinter

#Funcion para obtener Cetena, Decena y Unidad, segun el valor ingresado en el label
def otenerDatos():
    numero = int(entrada.get()) #Obtener valor desde la entrada solicitada
    centena = int(numero / 100)
    decena = int(numero % 100 / 10)
    unidad = int(numero % 100 % 10)
    texto = "Cetena =  {}".format(centena),"Decena = {}".format(decena),"Unidad = {}".format(unidad) #Formateo para concatenar datos
    if numero >= 0 and numero <=999:
        etiqueta["text"] = texto
    else:
        etiqueta["text"] = "Valor ingresado no esta entre 0 y 999"

formulario = tkinter.Tk() #Declaracion de la ventana que grafica donde se solicitaran los input, y se mostraran los output
formulario.geometry("500x400") #Tamaño de la ventana

titulo = tkinter.Label(formulario, text = "Ingresa un valor entre 0 y 999", font = 30) #declaracion del titulo con tamaño 30
titulo.pack()

entrada= tkinter.Entry(formulario) #Entrada de dato
entrada.pack()

etiqueta = tkinter.Label(formulario) #Etiqueta que mostrara el resultado de de la funcion
etiqueta.pack()

boton = tkinter.Button(formulario, text="Obtener Datos",command = otenerDatos) #Boton que activa nuestra funcion entregando la etiqueta de entrada
boton.pack()

formulario.mainloop()  #Lleva todos los registros de la ventana


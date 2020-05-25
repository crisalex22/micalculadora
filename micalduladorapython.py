from tkinter import *
from math import *

from calculadoraLib import suma, resta, multiplicacion, division, raiz
def recolectar_data_suma():
    num1_data=int(num1.get())
    num2_data=int(num2.get())
    respuesta_total=suma(num1_data,num2_data)
    respuesta.set(respuesta_total)

def recolectar_data_resta():
    num1_data=int(num1.get())
    num2_data=int(num2.get())
    respuesta_total=resta(num1_data,num2_data)
    respuesta.set(respuesta_total)

def recolectar_data_multiplicaion():
    num1_data=int(num1.get())
    num2_data=int(num2.get())
    respuesta_total=multiplicacion(num1_data,num2_data)
    respuesta.set(respuesta_total)

def recolectar_data_division():
    num1_data=int(num1.get())
    num2_data=int(num2.get())
    if (num2_data>0):
        respuesta_total=division(num1_data,num2_data)
        respuesta.set(round((respuesta_total * 100000.0) / 100000.0, 5))
    else:
        respuesta.set("ERROR")
        
def recolectar_data_raiz():
    num2.set("")
    num1_data=int(num1.get())
    respuesta_total=raiz(num1_data)
    respuesta.set(round((respuesta_total * 100000.0) / 100000.0, 5))

def limpiar():
    respuesta_total=""
    num1.set(respuesta_total)
    num2.set(respuesta_total)
    respuesta.set(respuesta_total)


colorFondo="#0F65EA"
colorletra="white"
colorboton="#00CD63"
ventana=Tk()
ventana.title("MI PRIMERA CALCULADORA EN PYTHON V 1.0 cg")
ventana.geometry("350x250")
ventana.configure(background=colorFondo)
color_boton=("gray77")
ventana.resizable(False,False)
titulo=Label(text="Mi calculadora",font=('arial',20,'bold'),bg=colorFondo, fg=colorletra)
titulo.pack()

numero1=Label(text="Ingrese el primer número:",font=('arial',8,),bg=colorFondo, fg=colorletra)
numero1.place(x=40,y=50)

numero2=Label(text="Ingrese el segundo número:",font=('arial',8,),bg=colorFondo, fg=colorletra)
numero2.place(x=40,y=80)

numero2=Label(text="EL RESULTADO ES:",font=('arial',8,'bold'),bg=colorFondo, fg=colorletra)
numero2.place(x=40,y=110)

num1=StringVar()
num2=StringVar()
respuesta=StringVar()

num1_entry=Entry(textvariable=num1, width="10")
num2_entry=Entry(textvariable=num2, width="10")
respuesta_entry=Entry(textvariable=respuesta, width="10")

num1_entry.place(x=210,y=50)
num2_entry.place(x=210,y=80)
respuesta_entry.place(x=210,y=110)

ancho_boton=12
alto_boton=1
input_text=StringVar()
operador=""
suma_btn=Button(ventana,text="Sumar",bg=color_boton,width=ancho_boton,height=alto_boton,command=recolectar_data_suma).place(x=20,y=160)
resta_btn=Button(ventana,text="Restar",bg=color_boton,width=ancho_boton,height=alto_boton,command=recolectar_data_resta).place(x=120,y=160)
multiplicacion_btn=Button(ventana,text="Multiplicar",bg=color_boton,width=ancho_boton,height=alto_boton,command=recolectar_data_multiplicaion).place(x=220,y=160)
division_btn=Button(ventana,text="Dividir",bg=color_boton,width=ancho_boton,height=alto_boton,command=recolectar_data_division).place(x=20,y=200)
raiz_btn=Button(ventana,text="Raíz Cuadrada",bg=color_boton,width=ancho_boton,height=alto_boton,command=recolectar_data_raiz).place(x=120,y=200)
Limpiar_btn=Button(ventana,text="Limpiar",bg=color_boton,width=ancho_boton,height=alto_boton,command=limpiar).place(x=220,y=200)
ventana.mainloop()

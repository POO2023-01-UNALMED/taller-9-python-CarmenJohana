from tkinter import Tk, Button, Entry, END, StringVar

def AdicionarValor(valor):

    textoActual=pantalla.get()
    pantalla.delete(0, END)
    datosEntrada.set(textoActual+valor)

def Operador(value):
    global numero1
    global operador

    textoActual=''+str(pantalla.get())


    numero1=pantalla.get()
    pantalla.delete(0, END)
    if(numero1!=''):
        operador=value
    elif(value=='-'):
        datosEntrada.set(textoActual+value)
            #numero2='-'


def Calcular():
    numero2=''
    numero2=pantalla.get()

    resultado=pantalla.get()
    try:

        pantalla.delete(0, END)
        if operador=='+':
            resultado=float(numero1)+float(numero2)
            pantalla.insert(0,resultado)
        elif operador=='*':
            resultado=float(numero1)*float(numero2)
            pantalla.insert(0,resultado)
        elif operador=='/':
            resultado=float(numero1)/float(numero2)
            pantalla.insert(0,resultado)
        elif operador=='-':
            resultado=float(numero1)-float(numero2)
            pantalla.insert(0,resultado)
    except NameError:
        datosEntrada.set(resultado)
    except TypeError:
        pantalla.insert(0,"ERROR")
    except Exception:
        if(numero1=='' and numero2!=''):
            pantalla.insert(0,'')
        elif(pantalla.get()=='' and (numero2!='' or numero1!='')):
            pantalla.insert(0,'')
        elif(pantalla.get()!=''):
            pantalla.insert(0,str(resultado))




def Borrar():
    pantalla.delete(0, END)
    numero1=0
    numero2=''

# Configuración ventana principal
root = Tk()
root.title('Calculadora POO')
root.resizable(0,0)
root.geometry("295x305")



# Configuración pantalla de salida
datosEntrada=StringVar()
pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"), textvariable=datosEntrada)
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)
pantalla.bind("<Delete>", Borrar)
# Configuración botones
boton_1 = Button(root, text="1", command=lambda:AdicionarValor('1'), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", command=lambda:AdicionarValor('2'), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", command=lambda:AdicionarValor('3'),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4",command=lambda:AdicionarValor('4'), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5",command=lambda:AdicionarValor('5'), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", command=lambda:AdicionarValor('6'), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", command=lambda:AdicionarValor('7'), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", command=lambda:AdicionarValor('8'), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", command=lambda:AdicionarValor('9'), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", command=lambda: Calcular(), width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", command=lambda: AdicionarValor('.'), width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+",command=lambda: Operador('+'), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-",command=lambda:Operador('-'), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",command=lambda: Operador('*'),width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/",command=lambda: Operador('/'), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=4, column=3, padx=1, pady=1)
boton_borrar= Button(root, text="C", command=lambda: Borrar(), width=40, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_borrar.grid(row=5,column=0, columnspan=4, padx=1,pady=1)



root.mainloop()

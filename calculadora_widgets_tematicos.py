import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

coordenada_x = 500
coordenada_y = 80

def cambiarCoordenadaYUp(*args):
    global coordenada_y
    global coordenada_x

    coordenada_y = coordenada_y - 40
    root.geometry("+" + str(coordenada_x)+ "+" + str(coordenada_y))
        
def cambiarCoordenadaYDown(*args):
    global coordenada_x 
    global coordenada_y

    coordenada_y = coordenada_y + 40
    root.geometry("+" + str(coordenada_x) + "+" + str(coordenada_y))

def cambiarCoordenadaYLeft(*args):
    global coordenada_x
    global coordenada_y

    coordenada_x = coordenada_x - 50
    root.geometry("+" + str(coordenada_x) + "+" + str(coordenada_y))

def cambiarCoordenadaYRight(*args):
    global coordenada_x
    global coordenada_y

    coordenada_x = coordenada_x + 50
    root.geometry("+" + str(coordenada_x) + "+" + str(coordenada_y))


def AgregarValores(valor):
    #validar que después de que hagan la operación de raiz cuadrada y vuelvan a ingresar valores, label1 y label2 vuelvan a quedar en nulo
    i = entrada1.get()[0:1]
    if i == "√":
        entrada1.set("")
        entrada2.set("")


    #valida que el primer valor de entrada1 sea parentesis de apertura, si así, va a enviar a entrada 2 lo que tiene entrada1
    if entrada1.get()[0:1] == "(":
        entrada2.set(entrada1.get())
        entrada1.set("")

    #validar para enviar los valores a entrada1
    if valor == "+" or valor == "-" or valor == "*" or valor == "/":
        if entrada2.get() != "":
            entrada1.set(entrada2.get() + valor)
            entrada2.set("")
        elif valor == "-":
            entrada2.set(valor)
    else:
        entrada2.set(entrada2.get()+valor)

    #validar para cambiar el signo cuando el valor ya este en entrada1
    if entrada1.get() != "":
        if valor == "+" or valor == "-" or valor == "*" or valor == "/":
            inicio = 0
            fin = len(entrada1.get())
            entrada1.set(entrada1.get()[inicio:fin-1])
            entrada1.set(entrada1.get() + valor)


    #validar que no introduzcan valores no válidos
    if entrada2.get() == ".." or entrada2.get() == "((" or entrada2.get() == "))" or entrada2.get() == "()" or entrada2.get() == ")(" or entrada2.get() == ")" or entrada2.get() == "-.":
        entrada2.set("")
    
    if entrada1.get() == "-/" or entrada1.get() == "-*":
        entrada1.set("")


    #validar la cantidad de valores en entrada dos para volver más chica el tamaño de la letra 
    longitud = len(entrada2.get())
    if longitud >= 14 and longitud <= 17:
        estilos_label2.configure('Label2.TLabel', font="arial 29")
        label_entrada2.grid_configure(ipady=18)
    
    if longitud >= 40:
        entrada2.set(entrada2.get()[0: 40])
        
def AgregarValoresTeclado(event):
    #validar que después de que hagan la operación de raiz cuadrada y vuelvan a ingresar valores, label1 y label2 vuelvan a quedar en nulo
    i = entrada1.get()[0:1]
    if i == "√":
        entrada1.set("")
        entrada2.set("")


    tecla = event.char

    #valida que el primer valor de entrada1 sea parentesis de apertura, si así, va a enviar a entrada 2 lo que tiene entrada1
    if entrada1.get()[0:1] == "(":
        entrada2.set(entrada1.get())
        entrada1.set("")

    #validar para enviar los valores a entrada1
    if tecla == "+" or tecla == "-" or tecla == "*" or tecla == "/":
        if entrada2.get() != "":
            entrada1.set(entrada2.get() + tecla)
            entrada2.set("")
        elif tecla == "-":
            entrada2.set(tecla)

    #validar para cambiar el signo cuando el valor ya este en entrada1
    if entrada1.get() != "":
        if tecla == "+" or tecla == "-" or tecla == "*" or tecla == "/":
            inicio = 0
            fin = len(entrada1.get())
            entrada1.set(entrada1.get()[inicio:fin-1])
            entrada1.set(entrada1.get() + tecla)

    if tecla == '0' or tecla == '1' or tecla == '2' or tecla == '3' or tecla == '4' or tecla == '5' or tecla == '6' or tecla == '7' or tecla == '8' or tecla == '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)


    #validar la cantidad de valores en entrada dos para volver más chica el tamaño de la letra 
    longitud = len(entrada2.get())
    if longitud >= 14 and longitud <= 17:
        estilos_label2.configure('Label2.TLabel', font="arial 29")
        label_entrada2.grid_configure(ipady=18)
    

    #validar que la logitud de los valores que hay en label2 no sea mayor a 40
    if longitud >= 40:
        entrada2.set(entrada2.get()[0:40])

    #validar que no introduzcan valores no válidos
    if entrada2.get() == ".." or entrada2.get() == "((" or entrada2.get() == "))" or entrada2.get() == "()" or entrada2.get() == ")(" or entrada2.get() == ")":
        entrada2.set("")

def RealizarOperacion(*args):
    try:
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)
        entrada1.set("")

    except:
        entrada1.set("")
        entrada2.set("")

def BorrarTodo(*args):
    entrada1.set("")
    entrada2.set("")

def Borrar(*args):
    inicio = 0
    fin = len(entrada2.get())
    entrada2.set(entrada2.get()[inicio:fin-1])

def TemaOscuro(*args):
    estilos.configure('mainframe.TFrame', background="#010924")

    estilos_label1.configure('Label1.TLabel', background="#010924", foreground="white")
    estilos_label2.configure('Label2.TLabel', background="#010924", foreground="white")


    estilos_botones_numeros.configure('Botones_numeros.TButton', background="#00044A", foreground="white")
    estilos_botones_numeros.map('Botones_numeros.TButton', background=[('active', '#020A90')])


    estilos_botones_borrar.configure('Botones_borrar.TButton', background="#010924", foreground="white")
    estilos_botones_borrar.map('Botones_borrar.TButton', background=[('active', '#000AB1')])

    estilos_botones_restantes.configure('Botones_restantes.TButton', background="#010924", foreground="white")
    estilos_botones_restantes.map('Botones_restantes.TButton', background=[('active', '#000AB1')])

def TemaClaro(*args):
    estilos.configure('mainframe.TFrame', background="#DBDBDB")

    estilos_label1.configure('Label1.TLabel', background="#DBDBDB", foreground="black")
    estilos_label2.configure('Label2.TLabel', background="#DBDBDB", foreground="black")

    estilos_botones_numeros.configure('Botones_numeros.TButton', background="#FFFFFF", foreground="black")
    estilos_botones_numeros.map('Botones_numeros.TButton', background=[('active', '#B9B9B9')])

    estilos_botones_borrar.configure('Botones_borrar.TButton', background="#CECECE", foreground="black")
    estilos_botones_borrar.map('Botones_borrar.TButton', background=[('active', '#858585')])

    estilos_botones_restantes.configure('Botones_restantes.TButton', background="#CECECE", foreground="black")
    estilos_botones_restantes.map('Botones_restantes.TButton', background=[('active', '#858585')])

def RaizCuadrada(*args):
    try:
        entrada1.set( "√("+entrada2.get()+")")
        entrada2.set(math.sqrt(int(entrada2.get())))
    except:
        entrada2.set("")


#ventana raiz
root = Tk()
root.title("Calculadora")
root.geometry("+500+80")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#marco principal/donde se ponene todos los widgets
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure('mainframe.TFrame', background="#DBDBDB")
mainframe = ttk.Frame(root, style="mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky=(E, W, N, S))

mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)

#estilos para los labes de entrada
estilos_label1 = ttk.Style()
estilos_label1.configure('Label1.TLabel', font="arial 15", anchor=E)

estilos_label2 = ttk.Style()
estilos_label2.configure('Label2.TLabel', font="arial 40", anchor=E)

#label donde se ponen los valores cuando van a sumar/restar/multiplicar/dividir
entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel")
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W, E, N, S))

#label donde se ponen los valores que el usuario ingresa
entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style='Label2.TLabel')
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W, E, N, S))

#estilos para los botones de los núemros
estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure("Botones_numeros.TButton", font="arial 22", width=5, background="#FFFFFF", relief="flat")
estilos_botones_numeros.map('Botones_numeros.TButton', background=[('active', '#B9B9B9')])

#estilos para los botones de borrar
estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure('Botones_borrar.TButton', font="arial 22", width=5, relief="flat", background="#CECECE")
estilos_botones_borrar.map('Botones_borrar.TButton', foreground=[('active', '#FF0000')])
estilos_botones_borrar.map('Botones_borrar.TButton', background=[('active', '#858585')])

#estilos para los demas botones
estilos_botones_restantes = ttk.Style()
estilos_botones_restantes.configure('Botones_restantes.TButton', font="arial 22", width=5, relief="flat", background="#CECECE")
estilos_botones_restantes.map('Botones_restantes.TButton', background=[('active', '#858585')])

#crear los botones
button0 = ttk.Button(mainframe, text="0", style="Botones_numeros.TButton", command=lambda: AgregarValores("0"))
button1 = ttk.Button(mainframe, text="1", style="Botones_numeros.TButton", command=lambda: AgregarValores("1"))
button2 = ttk.Button(mainframe, text="2", style="Botones_numeros.TButton", command=lambda: AgregarValores("2"))
button3 = ttk.Button(mainframe, text="3", style="Botones_numeros.TButton", command=lambda: AgregarValores("3"))
button4 = ttk.Button(mainframe, text="4", style="Botones_numeros.TButton", command=lambda: AgregarValores("4"))
button5 = ttk.Button(mainframe, text="5", style="Botones_numeros.TButton", command=lambda: AgregarValores("5"))
button6 = ttk.Button(mainframe, text="6", style="Botones_numeros.TButton", command=lambda: AgregarValores("6"))
button7 = ttk.Button(mainframe, text="7", style="Botones_numeros.TButton", command=lambda: AgregarValores("7"))
button8 = ttk.Button(mainframe, text="8", style="Botones_numeros.TButton", command=lambda: AgregarValores("8"))
button9 = ttk.Button(mainframe, text="9", style="Botones_numeros.TButton", command=lambda: AgregarValores("9"))

button_borrar          = ttk.Button(mainframe, text=chr(9003), style="Botones_borrar.TButton", command=lambda: Borrar())
button_borrar_todo     = ttk.Button(mainframe, text="C", style="Botones_borrar.TButton", command=lambda: BorrarTodo())
button_parentesis1     = ttk.Button(mainframe, text="(", style="Botones_restantes.TButton", command=lambda: AgregarValores("("))
button_parentesis2     = ttk.Button(mainframe, text=")", style="Botones_restantes.TButton", command=lambda: AgregarValores(")"))
button_punto           = ttk.Button(mainframe, text=".", style="Botones_restantes.TButton", command=lambda:AgregarValores("."))

button_division       = ttk.Button(mainframe, text=chr(247), style="Botones_restantes.TButton",command=lambda:AgregarValores("/"))
button_multiplicacion = ttk.Button(mainframe, text="x", style="Botones_restantes.TButton", command=lambda:AgregarValores("*"))
button_resta          = ttk.Button(mainframe, text="-", style="Botones_restantes.TButton", command=lambda: AgregarValores("-"))
button_suma           = ttk.Button(mainframe, text="+", style="Botones_restantes.TButton", command=lambda: AgregarValores("+"))

button_igual            = ttk.Button(mainframe, text="=", style="Botones_restantes.TButton", command=lambda: RealizarOperacion())
button_raiz_cuadrada    = ttk.Button(mainframe, text="√", style="Botones_restantes.TButton", command=lambda:RaizCuadrada())

#agrefar los botones en pantalla
button_parentesis1.grid(column=0, row=2, sticky=(W, E, N, S))
button_parentesis2.grid(column=1, row=2, sticky=(W, E, N, S))
button_borrar_todo.grid(column=2, row=2, sticky=(W, E, N, S))
button_borrar.grid(column=3, row=2, sticky=(W, E, N, S))

button7.grid(column=0, row=3, sticky=(W, E, N, S))
button8.grid(column=1, row=3, sticky=(W, E, N, S))
button9.grid(column=2, row=3, sticky=(W, E, N, S))
button_division.grid(column=3, row=3, sticky=(W, E, N, S))

button4.grid(column=0, row=4, sticky=(W, E, N, S))
button5.grid(column=1, row=4, sticky=(W, E, N, S))
button6.grid(column=2, row=4, sticky=(W, E, N, S))
button_multiplicacion.grid(column=3, row=4, sticky=(W, E, N, S))

button1.grid(column=0, row=5, sticky=(W, E, N, S))
button2.grid(column=1, row=5, sticky=(W, E, N, S))
button3.grid(column=2, row=5, sticky=(W, E, N, S))
button_suma.grid(column=3, row=5, sticky=(W, E, N, S))

button0.grid(column=0, row=6, columnspan=2, sticky=(W, E, N, S))
button_punto.grid(column=2, row=6, sticky=(W, E, N, S))
button_resta.grid(column=3, row=6, sticky=(W, E, N, S))

button_igual.grid(column=0, row=7, columnspan=3, sticky=(W, E, N, S))
button_raiz_cuadrada.grid(column=3, row=7, sticky=(W, E, N, S))

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

#eventos de teclado
root.bind('<KeyPress-o>', TemaOscuro)
root.bind('<KeyPress-c>', TemaClaro)
root.bind('<Key>', AgregarValoresTeclado)
root.bind('<BackSpace>', Borrar)
root.bind('<Control-BackSpace>', BorrarTodo)
root.bind('<Return>', RealizarOperacion)
root.bind('<Control-r>', RaizCuadrada)
root.bind('<KeyPress-Up>', cambiarCoordenadaYUp)
root.bind('<KeyPress-Down>', cambiarCoordenadaYDown)
root.bind('<KeyPress-Left>', cambiarCoordenadaYLeft)
root.bind('<KeyPress-Right>', cambiarCoordenadaYRight)

root.mainloop()
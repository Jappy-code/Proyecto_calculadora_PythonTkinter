from tkinter import *
from tkinter import messagebox
import math

#Funciones
i = 0
coordenada_x = 550
coordenada_y = 150

def click_boton(valor):
    global  i

    e_texto.insert(i, valor)
    i += 1

    if e_texto.get() == '**':
        e_texto.delete(0, END)
        i=0
    if e_texto.get() == '//':
        e_texto.delete(0, END)
        i=0
    if e_texto.get() == '..':
        e_texto.delete(0, END)
        i=0

#Función para los eventos del teclado
def boton_teclado(event):
    global i
    global coordenada_x
    global coordenada_y
    tecla = event.char

    if tecla == '0' or tecla == '1' or tecla == '2' or tecla == '3' or tecla == '4' or tecla == '5' or tecla == '6' or tecla == '7' or tecla == '8' or tecla == '9' or tecla == '(' or tecla == ')' or tecla == '+' or tecla == '-' or tecla == '*' or tecla == '/' or tecla == '.':
        e_texto.insert(i, tecla)
        i = i +1

        if e_texto.get() == '**':
            e_texto.delete(0, END)
            i=0
        if e_texto.get() == '//':
            e_texto.delete(0, END)
            i=0
        if e_texto.get() == '..':
            e_texto.delete(0, END)
            i=0
    
    if tecla == 'r' or tecla == 'R':
        raiz_cuadrada()

    if tecla == 'o' or tecla == 'O':
        Tema_oscuro()

    if tecla == 'c' or tecla == 'C':
        Tema_claro()
        
    """if tecla == 'b':
        borrar()"""
    
    if tecla == 'B':
        borrar_todo()

    #modificar coordenadas de la ventana por teclado
    if tecla == 'a' or tecla == 'A':
        coordenada_x = coordenada_x - 60
        ventana.geometry("+" + str(coordenada_x) + "+" + str(coordenada_y))

    elif tecla == 'd' or tecla == 'D':
        coordenada_x = coordenada_x + 60
        ventana.geometry("+" + str(coordenada_x) + "+" + str(coordenada_y))
    
    elif tecla == 'w' or tecla == 'W':
        coordenada_y = coordenada_y - 55
        ventana.geometry("+" + str(coordenada_x) + "+" + str(coordenada_y))

    elif tecla == 's' or tecla == 'S':
        coordenada_y = coordenada_y + 55
        ventana.geometry("+" + str(coordenada_x) + "+" + str(coordenada_y))
    
    """elif tecla == "e":
        coordenada_x = coordenada_x + 20
        coordenada_y = coordenada_y - 15
        ventana.geometry("+" + str(coordenada_x) + "+" + str(coordenada_y))"""

def borrar(event = ""):
    global i
    e_texto.delete(i-1, i)
    i = i -1
    if i <= 0:
        i = 0


def borrar_todo():
    global i
    i=0
    e_texto.delete(i, END)

def operaciones(event = ""):#Igualandolo a las comillas, hago que el parámetro sea opcional
    global i
    try:
        ecuacion = e_texto.get()

        #válida que sea diferente de nulo
        if ecuacion != "":
            resultado = eval(ecuacion)
            e_texto.delete(0, END)
            e_texto.insert(0, resultado)

            i = len(e_texto.get())
            
    except:
        e_texto.delete(0, END)
        i=0
        messagebox.showerror("¡Error!", "¡Operación no válida!")

def raiz_cuadrada():
    try:
        global i
        if e_texto.get() == "":
            messagebox.showerror("¡Error!", "No hay valor para sacar la raíz cuadrada")
        else:
            valor = int(e_texto.get())

            raiz_cuadrada = math.sqrt(valor)
            e_texto.delete(0, END)
            e_texto.insert(0, raiz_cuadrada)
            i = len(e_texto.get())
    except:
        messagebox.showerror("¡Error!", "No se puede sacar raíz cuadrada a este valor: " + e_texto.get())
        e_texto.delete(0, END)
        i=0

def Tema_claro():
    ventana.configure(background="ivory3")
    e_texto.configure(bg="ivory3", fg="black")
    button1.configure(bg="white", fg="black")
    button2.configure(bg="white", fg="black")
    button3.configure(bg="white", fg="black")
    button4.configure(bg="white", fg="black")
    button5.configure(bg="white", fg="black")
    button6.configure(bg="white", fg="black")
    button7.configure(bg="white", fg="black")
    button8.configure(bg="white", fg="black")
    button9.configure(bg="white", fg="black")
    button0.configure(bg="white", fg="black")
    button_suma.configure(bg="gray95", fg="black")
    button_resta.configure(bg="gray95", fg="black")
    button_multiplicacion.configure(bg="gray95", fg="black")
    button_division.configure(bg="gray95", fg="black")
    button_punto.configure(bg="gray95", fg="black")
    button_parentesis2.configure(bg="gray95", fg="black")
    button_parentesis1.configure(bg="gray95", fg="black")
    button_borrar.configure(bg="gray95", fg="black")
    button_borrar_todo.configure(bg="gray95", fg="black")
    button_igual.configure(bg="gray95", fg="black")
    button_raiz_cuadrada.configure(bg="gray95", fg="black")

def Tema_oscuro():
    ventana.configure(background="gray26")
    e_texto.configure(bg="gray26", fg="white")
    button1.configure(bg="DeepSkyBlue4", fg="white")
    button2.configure(bg="DeepSkyBlue4", fg="white")
    button3.configure(bg="DeepSkyBlue4", fg="white")
    button4.configure(bg="DeepSkyBlue4", fg="white")
    button5.configure(bg="DeepSkyBlue4", fg="white")
    button6.configure(bg="DeepSkyBlue4", fg="white")
    button7.configure(bg="DeepSkyBlue4", fg="white")
    button8.configure(bg="DeepSkyBlue4", fg="white")
    button9.configure(bg="DeepSkyBlue4", fg="white")
    button0.configure(bg="DeepSkyBlue4", fg="white")
    button_suma.configure(bg="DeepSkyBlue4", fg="white")
    button_resta.configure(bg="DeepSkyBlue4", fg="white")
    button_multiplicacion.configure(bg="DeepSkyBlue4", fg="white")
    button_division.configure(bg="DeepSkyBlue4", fg="white")
    button_punto.configure(bg="DeepSkyBlue4", fg="white")
    button_parentesis2.configure(bg="DeepSkyBlue4", fg="white")
    button_parentesis1.configure(bg="DeepSkyBlue4", fg="white")
    button_borrar.configure(bg="DeepSkyBlue4", fg="white")
    button_borrar_todo.configure(bg="DeepSkyBlue4", fg="white")
    button_igual.configure(bg="DeepSkyBlue4", fg="white")
    button_raiz_cuadrada.configure(bg="DeepSkyBlue4", fg="white")


def confirmar_salida():
    confirmacion = messagebox.askyesno("Salir", "¿Desea salir?")#si selecciona si, el valor que guarda es 1 y si selecciona no, el valor es 0
    if confirmacion:
        ventana.destroy()

def atajos_teclado():
    messagebox.showinfo("Atajos de teclado", "o/O: Activa el modo oscuro\n" + 
                                             "c/C: Activa el modo claro\n" + 
                                             "r/R: Activa la función de raíz cuadrada\n" + 
                                             "a/A: Mueve la ventana a la izquierda\n"+
                                             "d/D: Mueve la ventana a la derecha\n"+
                                             "w/W: Mueve la ventana hacia arriba\n"+
                                             "s/S: Mueve la ventana hacia abajo\n" + 
                                             "↲ / Enter : Activa la función para hacer la operación")

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("+550+150")
ventana.resizable(width=False, height=False)
#ventana.iconbitmap(r"D:\11 Cursos de desarrollo de software\16_mundo python\2_calculadora tkinter\3_calculadora_darwin\img\icon.ico")
ventana.configure(bg="ivory3")

#menú
menu = Menu(ventana)

opcion_menu_temas = Menu(menu, tearoff=0)
opcion_menu_temas.add_command(label='Oscuro', command= lambda:Tema_oscuro())
opcion_menu_temas.add_command(label='Claro', command=lambda: Tema_claro())
menu.add_cascade(label='Temas', menu=opcion_menu_temas)

opcion_instrucciones = Menu(menu, tearoff=0)
opcion_instrucciones.add_command(label='Atajos de teclado', command=atajos_teclado)
menu.add_cascade(label='Instrucciones', menu=opcion_instrucciones)

creditos = Menu(menu, tearoff=0)
creditos.add_command(label="Creditos", command=lambda: messagebox.showinfo('Creador', 'Creado por Darwin'))
menu.add_cascade(label='Más', menu=creditos)

menu.add_command(label='Salir', command=confirmar_salida)
ventana.config(menu=menu)

#widgets de la calculadora
e_texto = Entry(ventana, font="Calibri 25", width=19, bg="ivory3", justify=RIGHT, relief=FLAT)
e_texto.grid(row=0, column=0, columnspan=4, pady=20)


#botones
button1 = Button(ventana, text="1", width=5, font="arial 18", bg="white", command=lambda: click_boton(1), relief=FLAT)
button2 = Button(ventana, text="2", width=5, font="arial 18", bg="white", command=lambda: click_boton(2), relief=FLAT)
button3 = Button(ventana, text="3", width=5, font="arial 18", bg="white", command=lambda: click_boton(3), relief=FLAT)
button4 = Button(ventana, text="4", width=5, font="arial 18", bg="white", command=lambda: click_boton(4), relief=FLAT)
button5 = Button(ventana, text="5", width=5, font="arial 18", bg="white", command=lambda: click_boton(5), relief=FLAT)
button6 = Button(ventana, text="6", width=5, font="arial 18", bg="white", command=lambda: click_boton(6), relief=FLAT)
button7 = Button(ventana, text="7", width=5, font="arial 18", bg="white", command=lambda: click_boton(7), relief=FLAT)
button8 = Button(ventana, text="8", width=5, font="arial 18", bg="white", command=lambda: click_boton(8), relief=FLAT)
button9 = Button(ventana, text="9", width=5, font="arial 18", bg="white", command=lambda: click_boton(9), relief=FLAT)
button0 = Button(ventana, text="0", width=11, font="arial 18", bg="white", command=lambda: click_boton(0), relief=FLAT)

button_borrar = Button(ventana, text=chr(9003), width=5, font="arial 18", bg="gray95", command=lambda: borrar(), relief=FLAT)
button_borrar_todo = Button(ventana, text="C", width=5, font="arial 18", bg="gray95", command=lambda: borrar_todo(), relief=FLAT)
button_parentesis1=Button(ventana, text="(", width=5, font="arial 18", bg="gray95", command=lambda: click_boton("("), relief=FLAT)
button_parentesis2=Button(ventana, text=")", width=5, font="arial 18", bg="gray95", command=lambda: click_boton(")"), relief=FLAT)
button_punto = Button(ventana, text=".", width=5, font="arial 18", bg="gray95", command=lambda: click_boton("."), relief=FLAT)

button_division = Button(ventana, text=chr(247), width=5, font="arial 18", bg="gray95", command=lambda: click_boton("/"), relief=FLAT)
button_multiplicacion = Button(ventana, text="x", width=5, font="arial 18", bg="gray95", command=lambda: click_boton("*"), relief=FLAT)
button_suma = Button(ventana, text="+", width=5, font="arial 18", bg="gray95", command=lambda: click_boton("+"), relief=FLAT)
button_resta =Button(ventana, text="-", width=5, font="arial 18", bg="gray95", command=lambda: click_boton("-"), relief=FLAT)
button_igual =Button(ventana, text="=", width=17, font="arial 18", bg="gray95", command=lambda: operaciones(), relief=FLAT)
button_raiz_cuadrada = Button(ventana, text="√", width=5, font="arial 18", bg="gray95", command=lambda: raiz_cuadrada(), relief=FLAT)


#eventos de teclado
ventana.bind("<Return>", operaciones)
ventana.bind("<Key>", boton_teclado)
ventana.bind("<BackSpace>", borrar)

button0.bind("<Enter>", lambda e: button0.configure(font="arial 16"))
button0.bind("<Leave>", lambda e: button0.configure(font="arial 18"))

button1.bind("<Enter>", lambda e: button1.configure(font="arial 16"))
button1.bind("<Leave>", lambda e: button1.configure(font="arial 18"))

button2.bind("<Enter>", lambda e: button2.configure(font="arial 16"))
button2.bind("<Leave>", lambda e: button2.configure(font="arial 18"))

button3.bind("<Enter>", lambda e: button3.configure(font="arial 16"))
button3.bind("<Leave>", lambda e: button3.configure(font="arial 18"))

button4.bind("<Enter>", lambda e: button4.configure(font="arial 16"))
button4.bind("<Leave>", lambda e: button4.configure(font="arial 18"))

button5.bind("<Enter>", lambda e: button5.configure(font="arial 16"))
button5.bind("<Leave>", lambda e: button5.configure(font="arial 18"))

button6.bind("<Enter>", lambda e: button6.configure(font="arial 16"))
button6.bind("<Leave>", lambda e: button6.configure(font="arial 18"))

button7.bind("<Enter>", lambda e: button7.configure(font="arial 16"))
button7.bind("<Leave>", lambda e: button7.configure(font="arial 18"))

button8.bind("<Enter>", lambda e: button8.configure(font="arial 16"))
button8.bind("<Leave>", lambda e: button8.configure(font="arial 18"))

button9.bind("<Enter>", lambda e: button9.configure(font="arial 16"))
button9.bind("<Leave>", lambda e: button9.configure(font="arial 18"))

button_punto.bind("<Enter>", lambda e: button_punto.configure(font="arial 16"))
button_punto.bind("<Leave>", lambda e: button_punto.configure(font="arial 18"))

button_parentesis1.bind("<Enter>", lambda e: button_parentesis1.configure(font="arial 16"))
button_parentesis1.bind("<Leave>", lambda e: button_parentesis1.configure(font="arial 18"))

button_parentesis2.bind("<Enter>", lambda e: button_parentesis2.configure(font="arial 16"))
button_parentesis2.bind("<Leave>", lambda e: button_parentesis2.configure(font="arial 18"))

button_suma.bind("<Enter>", lambda e: button_suma.configure(font="arial 16"))
button_suma.bind("<Leave>", lambda e: button_suma.configure(font="arial 18"))

button_resta.bind("<Enter>", lambda e: button_resta.configure(font="arial 16"))
button_resta.bind("<Leave>", lambda e: button_resta.configure(font="arial 18"))

button_multiplicacion.bind("<Enter>", lambda e: button_multiplicacion.configure(font="arial 16"))
button_multiplicacion.bind("<Leave>", lambda e: button_multiplicacion.configure(font="arial 18"))

button_division.bind("<Enter>", lambda e: button_division.configure(font="arial 16"))
button_division.bind("<Leave>", lambda e: button_division.configure(font="arial 18"))

button_borrar.bind("<Enter>", lambda e: button_borrar.configure(font="arial 16"))
button_borrar.bind("<Leave>", lambda e: button_borrar.configure(font="arial 18"))

button_borrar_todo.bind("<Enter>", lambda e: button_borrar_todo.configure(font="arial 16"))
button_borrar_todo.bind("<Leave>", lambda e: button_borrar_todo.configure(font="arial 18"))

button_raiz_cuadrada.bind("<Enter>", lambda e: button_raiz_cuadrada.configure(font="arial 16"))
button_raiz_cuadrada.bind("<Leave>", lambda e: button_raiz_cuadrada.configure(font="arial 18"))


#agregar botones en pantalla
button_parentesis1.grid(row=1, column=0, padx=1, pady=5)
button_parentesis2.grid(row=1, column=1, padx=1, pady=5)
button_borrar_todo.grid(row=1, column=2, padx=1, pady=5)
button_borrar.grid(row=1, column=3, padx=1, pady=5)

button7.grid(row=2, column=0, padx=1, pady=1)
button8.grid(row=2, column=1, padx=1, pady=1)
button9.grid(row=2, column=2, padx=1, pady=1)
button_division.grid(row=2, column=3, padx=1, pady=1)

button4.grid(row=3, column=0, padx=1, pady=1)
button5.grid(row=3, column=1, padx=1, pady=1)
button6.grid(row=3, column=2, padx=1, pady=1)
button_multiplicacion.grid(row=3, column=3, padx=1, pady=1)

button1.grid(row=4, column=0, padx=1, pady=1)
button2.grid(row=4, column=1, padx=1, pady=1)
button3.grid(row=4, column=2, padx=1, pady=1)
button_suma.grid(row=4, column=3, padx=1, pady=1)

button0.grid(row=5, column=0, columnspan=2, padx=1, pady=1)
button_punto.grid(row=5, column=2, padx=1, pady=1)
button_resta.grid(row=5, column=3, padx=1, pady=1)

button_igual.grid(row=6, column=0, columnspan=3, padx=1, pady=5)
button_raiz_cuadrada.grid(row=6, column=3)

ventana.mainloop()
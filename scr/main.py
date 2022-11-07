from tkinter import *
from PIL import ImageTk
import PIL.Image
from tkinter import Menu
from menus import *

gui = Tk()

fuente = ("Comic Sans MS", 15, "bold")

gui.geometry("800x315")
gui.title("C.I.P (Menu Principal)")
gui.config(bg="#d4d8e6")
gui.resizable(False, False)

imagen = PIL.Image.open("img/cip.jpg")
imagen = imagen.resize(size=(300, 290))
image = ImageTk.PhotoImage(imagen)
Label(gui, image=image).place(x=250, y=10)

menubar = Menu(gui)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Agregar curso", command=menu_agregar_curso, font=fuente)
filemenu.add_command(label="Cursos disponibles", command=menu_listar_cursos, font=fuente)
menubar.add_cascade(label="Cursos", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Agregar alumno", command=menu_agregar_alumno, font=fuente)
helpmenu.add_command(label="Listar alumnos", command=menu_listar_alumnos, font=fuente)
helpmenu.add_command(label="Tomar lista", command=tomar_lista_menu, font=fuente)
helpmenu.add_command(label="Ver lista", command=ver_lista_menu, font=fuente)
menubar.add_cascade(label="Alumnos", menu=helpmenu)


gui.config(menu=menubar)
gui.mainloop()
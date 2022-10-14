from tkinter import *
from tkinter import ttk
from funciones import *

def test_agregar_curso():
    global cursos
    try:
        añotest = año.get()
        divisiontest = division.get()
        if añotest > 0 and añotest <= 7:
            if divisiontest > 0 and divisiontest <= 6:
                añotest = str(añotest)
                divisiontest = str(divisiontest)
                cursos = agregar_curso(añotest + "°" + divisiontest)
                labelinfo.config(text="Este curso fue agregado satisfactoriamente.")
            else:
                labelinfo.config(text="Ingrese una division desde 1° a 6°.")
        else:
            labelinfo.config(text="Ingrese un año desde 1° a 7°.")
    except NameError:
        pass
        labelinfo.config(text="Ingrese numeros validos.")

def menu_agregar_curso():

    gui_agregar_curso = Toplevel()
    gui_agregar_curso.geometry("400x150")
    gui_agregar_curso.title("C.I.P (Agregar un nuevo curso)")
    gui_agregar_curso.config(bg="#ffffff")

    global año

    año = IntVar()

    labelaño = Label(gui_agregar_curso, text="Año:", background="#ffffff")
    entryaño = Entry(gui_agregar_curso, textvariable=año, width=5)

    labelaño.place(y=10, x=10)
    entryaño.place(y=10, x=50)

    global division

    division = IntVar()

    labeldivision = Label(gui_agregar_curso, text="Division:", background="#ffffff")
    entrydivision = Entry(gui_agregar_curso, textvariable=division, width=5)

    labeldivision.place(y=10, x=100)
    entrydivision.place(y=10, x=150)

    global labelinfo

    labelinfo = Label(gui_agregar_curso, text="", background="#ffffff")

    labelinfo.place(y=50, x=10)

    ingresar = Button(gui_agregar_curso, text="Ingresar curso", command=test_agregar_curso)

    ingresar.place(y=100, x=10)

def menu_listar_cursos():
    gui_listar_cursos = Toplevel()
    gui_listar_cursos.geometry("400x200")
    gui_listar_cursos.title("C.I.P (Lista de cursos)")
    gui_listar_cursos.config(bg="#ffffff")

    labelcursosformateados = Label(gui_listar_cursos, text="", background="#ffffff")

    labelcursosformateados.place(y=10, x=10)

    cursos_formateados = ""

    for x in cursos:
        cursos_formateados = cursos_formateados + " " + x
        print(cursos_formateados)
    
    labelcursosformateados.config(text="Los cursos que existen actualmente son: " + cursos_formateados)

def menu_agregar_alumno():

    gui_agregar_alumno = Toplevel()
    gui_agregar_alumno.geometry("400x150")
    gui_agregar_alumno.title("C.I.P (Agregar un alumno)")
    gui_agregar_alumno.config(bg="#ffffff")

    curso_agregar_alumno = ""

    combocursos = ttk.Combobox(gui_agregar_alumno, values=cursos, textvariable=curso_agregar_alumno)
    combocursos.place(y=10, x=10)

    alumno_agregar_alumno = ""

    labelalumno = Label(gui_agregar_alumno, text="Ingrese el nombre del alumno: ", background="#ffffff")
    entryalumno = Entry(gui_agregar_alumno, textvariable=alumno_agregar_alumno, background="#ffffff")

    labelalumno.place(y=50, x=10)
    entryalumno.place(y=50, x=200)


    ingresar = Button(gui_agregar_alumno, text="Agregar alumno al curso", command=test_agregar_curso)

    ingresar.place(y=100, x=10)

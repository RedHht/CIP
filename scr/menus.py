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
                try:
                    cursos.index(añotest + "°" + divisiontest) 
                    labelinfo.config(text="Este curso ya existe.") 
                except ValueError:
                    cursos = agregar_curso(añotest + "°" + divisiontest)
                    cursos.sort()
                    labelinfo.config(text="Este curso fue agregado satisfactoriamente.")
            else:
                labelinfo.config(text="Ingrese una division desde 1° a 6°.")
        else:
            labelinfo.config(text="Ingrese un año desde 1° a 7°.")
    except:
        pass
        labelinfo.config(text="Ingrese numeros validos.")

def test_agregar_alumno():
    curso = curso_agregar_alumno.get()
    alumno = alumno_agregar_alumno.get()
    if curso == "":
        labelinfoingresaralumno.config(text="No ingresaste ningun curso")
    else:
        if alumno == "":
            labelinfoingresaralumno.config(text="No ingresaste ningun alumno")
        else:
            agregar_alumno(curso, alumno)
            labelinfoingresaralumno.config(text="Alumno agregado correctamente")

def lista_de_alumnos():
    alumnos = lista_alumnos(curso_listar_alumno.get())
    print(alumnos)
    return alumnos

def menu_agregar_curso():

    gui_agregar_curso = Toplevel()
    gui_agregar_curso.geometry("400x115")
    gui_agregar_curso.title("C.I.P (Agregar un nuevo curso)")
    gui_agregar_curso.config(bg="#ffffff")

    global año

    año = IntVar()

    labelaño = Label(gui_agregar_curso, text="Año:", background="#ffffff")
    entryaño = Entry(gui_agregar_curso, textvariable=año, width=5)

    labelaño.grid(row=0, column=0, sticky='w', padx=5, pady=5)
    entryaño.grid(row=0, column=1, sticky='w', padx=5, pady=5)

    global division

    division = IntVar()

    labeldivision = Label(gui_agregar_curso, text="Division:", background="#ffffff")
    entrydivision = Entry(gui_agregar_curso, textvariable=division, width=5)

    labeldivision.grid(row=1, column=0, sticky='w', padx=5, pady=5)
    entrydivision.grid(row=1, column=1, sticky='w', padx=5, pady=5)

    global labelinfo

    labelinfo = Label(gui_agregar_curso, text="", background="#ffffff")

    labelinfo.grid(row=2, column=1, sticky='w', padx=5, pady=5)

    ingresar = Button(gui_agregar_curso, text="Ingresar curso", command=test_agregar_curso)

    ingresar.grid(row=2, column=0, sticky='w', padx=5, pady=5)

def menu_listar_cursos():
    gui_listar_cursos = Toplevel()
    gui_listar_cursos.geometry("400x200")
    gui_listar_cursos.title("C.I.P (Lista de cursos)")
    gui_listar_cursos.config(bg="#ffffff")

    labelcursosformateados = Label(gui_listar_cursos, text="", background="#ffffff", wraplength=390, justify=LEFT)

    labelcursosformateados.place(y=10, x=10)

    cursos_formateados = ""

    for x in cursos:
        if cursos.index(x) == 0:
            cursos_formateados = x
        else: 
            cursos_formateados = cursos_formateados + ", " + x
    
    labelcursosformateados.config(text="Los cursos que existen actualmente son: " + cursos_formateados)

def menu_agregar_alumno():

    gui_agregar_alumno = Toplevel()
    gui_agregar_alumno.geometry("400x150")
    gui_agregar_alumno.title("C.I.P (Agregar un alumno)")
    gui_agregar_alumno.config(bg="#ffffff")

    global curso_agregar_alumno

    curso_agregar_alumno = StringVar()

    combocursos = ttk.Combobox(gui_agregar_alumno, values=cursos, textvariable=curso_agregar_alumno, state="readonly")
    combocursos.grid(row=0, column=0, sticky='w', padx=5, pady=5)

    global alumno_agregar_alumno

    alumno_agregar_alumno = StringVar()

    labelalumno = Label(gui_agregar_alumno, text="Ingrese el nombre del alumno: ", background="#ffffff")
    entryalumno = Entry(gui_agregar_alumno, textvariable=alumno_agregar_alumno, background="#ffffff")

    labelalumno.grid(row=1, column=0, sticky='w', padx=5, pady=5)
    entryalumno.grid(row=1, column=1, sticky='w', padx=5, pady=5)

    global labelinfoingresaralumno

    labelinfoingresaralumno = Label(gui_agregar_alumno, text="", background="#ffffff")

    labelinfoingresaralumno.grid(row=2, column=1, sticky='w', padx=5, pady=5)

    ingresar = Button(gui_agregar_alumno, text="Agregar alumno al curso", command=test_agregar_alumno)

    ingresar.grid(row=2, column=0, sticky='w', padx=5, pady=5)

def menu_listar_alumnos():
    gui_listar_alumno = Toplevel()
    gui_listar_alumno.geometry("400x150")
    gui_listar_alumno.title("C.I.P (Lista de alumnos)")
    gui_listar_alumno.config(bg="#ffffff")

    global curso_listar_alumno

    curso_listar_alumno = StringVar()

    combocursos = ttk.Combobox(gui_listar_alumno, values=cursos, textvariable=curso_listar_alumno, state="readonly")
    combocursos.place(y=10, x=10)

    ingresar = Button(gui_listar_alumno, text="Ver lista de alumnos", command=lista_de_alumnos)

    ingresar.place(y=100, x=10)
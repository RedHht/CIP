from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from funciones import *


def test_agregar_curso():
    global cursos
    try:
        añotest = año.get()
        divisiontest = division.get()
        if 0 < añotest <= 7:
            if 0 < divisiontest <= 6:
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


def test_agregar_profesor():
    curso = curso_agregar_profesor.get()
    profesor = profesor_agregar_profesor.get()
    if curso == "":
        labelinfoingresarprofesor.config(text="No ingresaste ningun curso")
    else:
        if profesor == "":
            labelinfoingresarprofesor.config(text="No ingresaste ningun profesor")
        else:
            agregar_profesor(curso, profesor)
            labelinfoingresarprofesor.config(text="Profesor agregado correctamente")


def ing_valores():
    globals()["pres" + curso_listar_alumno.get()] = []
    for x in checkbox:
        x = x.get()
        globals()["pres" + curso_listar_alumno.get()].append(x)


def lista_de_alumnos():
    if curso_listar_alumno.get() == "":
        messagebox.showerror(title="Error", message="Selecciona un curso")

    else:
        gui_lista_alumno = Toplevel()
        gui_lista_alumno.geometry("400x500")
        gui_lista_alumno.title("C.I.P (Lista de alumnos del curso)")
        gui_lista_alumno.config(bg="#ffffff")

        label_alumnos = Label(gui_lista_alumno, text="Los alumnos de este curso son:", bg="#ffffff")

        label_alumnos.grid(row=0, column=0, sticky='w', padx=5, pady=5)

        if len(globals()["pres" + curso_listar_alumno.get()]) == 0:

            alumnos = lista_alumnos(curso_listar_alumno.get())

            linea = 0

            global checkbox

            checkbox = []

            for x in sorted(alumnos):
                Label(gui_lista_alumno, text=x, background="#ffffff").grid(row=linea, column=1, sticky='w', padx=5,
                                                                           pady=5)
                checkbox.append(IntVar())
                Checkbutton(gui_lista_alumno, background="#ffffff", variable=checkbox[linea]).grid(row=linea, column=2,
                                                                                            sticky='w', padx=5, pady=5)
                linea += 1

            linea += 1
        else:

            alumnos = lista_alumnos(curso_listar_alumno.get())

            linea = 0
            lineaa = 0

            checkbox = []

            for x in sorted(alumnos):
                Label(gui_lista_alumno, text=x, background="#ffffff").grid(row=linea, column=1, sticky='w', padx=5,
                                                                           pady=5)
                linea += 1

            for i in globals()["pres" + curso_listar_alumno.get()]:
                print(globals()["pres" + curso_listar_alumno.get()])
                if i == 1:
                    checkbox.append(IntVar())
                    activo = Checkbutton(gui_lista_alumno, background="#ffffff",
                                         variable=checkbox[lineaa])
                    activo.grid(row=lineaa, column=2, sticky='w', padx=5, pady=5)
                    activo.select()
                elif i == 0:
                    checkbox.append(IntVar())
                    desactivo = Checkbutton(gui_lista_alumno, background="#ffffff", variable=checkbox[lineaa])
                    desactivo.grid(row=lineaa, column=2, sticky='w', padx=5, pady=5)
                    desactivo.deselect()
                lineaa += 1

            linea += 1

        Button(gui_lista_alumno, text="Ingresar valores", command=ing_valores).grid(row=linea, column=0, sticky='w',
                                                                                    padx=5, pady=5)

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
    if len(cursos) == 0:
        messagebox.showerror(message="Actualmente no existe ningun curso", title="Error")
    else:
        gui_listar_cursos = Toplevel()
        gui_listar_cursos.geometry("400x200")
        gui_listar_cursos.title("C.I.P (Lista de cursos)")
        gui_listar_cursos.config(bg="#ffffff")

        labelcursosformateados = Label(gui_listar_cursos, text="", background="#ffffff", wraplength=390, justify=LEFT)

        labelcursosformateados.place(y=10, x=10)

        cursos_formateados = ""

        for x in sorted(cursos):
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

    combocursos = ttk.Combobox(gui_agregar_alumno, values=sorted(cursos), textvariable=curso_agregar_alumno,
                               state="readonly")
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
    gui_listar_alumno.geometry("400x75")
    gui_listar_alumno.title("C.I.P (Lista de alumnos)")
    gui_listar_alumno.config(bg="#ffffff")

    global curso_listar_alumno

    curso_listar_alumno = StringVar()

    combocursos = ttk.Combobox(gui_listar_alumno, values=sorted(cursos), textvariable=curso_listar_alumno,
                               state="readonly")
    combocursos.grid(row=0, column=0, sticky='w', padx=5, pady=5)

    ingresar = Button(gui_listar_alumno, text="Ver lista de alumnos", command=lista_de_alumnos)

    ingresar.grid(row=2, column=0, sticky='w', padx=5, pady=5)


def menu_agregar_profesor():
    gui_agregar_profesor = Toplevel()
    gui_agregar_profesor.geometry("400x150")
    gui_agregar_profesor.title("C.I.P (Agregar un profesor)")
    gui_agregar_profesor.config(bg="#ffffff")

    global curso_agregar_profesor

    curso_agregar_profesor = StringVar()

    combocursos = ttk.Combobox(gui_agregar_profesor, values=cursos, textvariable=curso_agregar_profesor,
                               state="readonly")
    combocursos.grid(row=0, column=0, sticky='w', padx=5, pady=5)

    global profesor_agregar_profesor

    profesor_agregar_profesor = StringVar()

    labelprofesor = Label(gui_agregar_profesor, text="Ingrese el nombre del profesor: ", background="#ffffff")
    entryprofesor = Entry(gui_agregar_profesor, textvariable=profesor_agregar_profesor, background="#ffffff")

    labelprofesor.grid(row=1, column=0, sticky='w', padx=5, pady=5)
    entryprofesor.grid(row=1, column=1, sticky='w', padx=5, pady=5)

    global labelinfoingresarprofesor

    labelinfoingresarprofesor = Label(gui_agregar_profesor, text="", background="#ffffff")

    labelinfoingresarprofesor.grid(row=2, column=1, sticky='w', padx=5, pady=5)

    ingresar = Button(gui_agregar_profesor, text="Agregar profesor al curso", command=test_agregar_profesor)

    ingresar.grid(row=2, column=0, sticky='w', padx=5, pady=5)

# def agregarprof():
#    if(escuela.get() == "s"):
#        print("a seleccionado ausente")
#    else:
#        if(escuela.get() == "a"):
#            print("a seleccionado presente")


# x = Tk()
# x.title("lista de profesores") #Titulo
# x.geometry("520x200") # ancho y altur

# presente=IntVar()
# ausente=IntVar()
# depa=StringVar()
# deps=StringVar()
# escuela= StringVar()
# escuela.set("m")

# Checkbutton(x,text="presente",variable=depa,onvalue="a").place(x=10,y=55)
# Checkbutton(x,text="ausente",variable=deps,onvalue="s").place(x=10,y=55)

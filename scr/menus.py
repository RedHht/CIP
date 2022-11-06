import datetime
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


def ing_valores():
    globals()["pres" + curso_listar_alumno.get()] = []
    for x in checkbox:
        x = x.get()
        globals()["pres" + curso_listar_alumno.get()].append(x)


def tomar_lista_menu():
    menu_tomar_lista = Toplevel()
    menu_tomar_lista.geometry("500x100")
    menu_tomar_lista.title("C.I.P (Menu para tomar lista)")
    menu_tomar_lista.config(bg="#ffffff")

    global curso_tomar_lista

    curso_tomar_lista = StringVar()

    Label(menu_tomar_lista, text="Curso:", background="#ffffff").grid(row=0, column=0, sticky='w', padx=5, pady=5)
    ttk.Combobox(menu_tomar_lista, values=cursos, textvariable=curso_tomar_lista).grid(row=0, column=1, sticky='w', padx=5, pady=5)

    Label(menu_tomar_lista, text="¿Que desea hacer?", background="#ffffff").grid(row=1, column=0, sticky='w', padx=5, pady=5)

    Button(menu_tomar_lista, text="Tomar lista de hoy", command=tomar_lista_hoy).grid(row=2, column=0, sticky='w', padx=5, pady=5)
    Button(menu_tomar_lista, text="Seleccionar fecha", command=tomar_lista_fecha).grid(row=2, column=1, sticky='w', padx=5, pady=5)

    menu_tomar_lista.mainloop()

def tomar_lista_hoy():
    tomar_lista_hoy = Toplevel()
    tomar_lista_hoy.geometry("400x500")
    tomar_lista_hoy.title("C.I.P (Tomar lista de hoy)")
    tomar_lista_hoy.config(bg="#ffffff")

    alumnos = lista_alumnos(curso_tomar_lista.get())
    checkbox = []

    for x in alumnos:
        Label(tomar_lista_hoy, text=x, background="#ffffff").grid(row=alumnos.index(x), column=1, sticky='w', padx=5, pady=5)
        checkbox.append(IntVar())
        Checkbutton(tomar_lista_hoy, variable=checkbox[alumnos.index(x)], background="#ffffff").grid(row=alumnos.index(x), column=2, sticky='w', padx=5, pady=5)

    fecha = datetime.datetime.now().date()

    Label(tomar_lista_hoy, text=f"Fecha: {fecha}", background="#ffffff").grid(row=0, column=0, sticky='w', padx=5, pady=5)

    tomar_lista_hoy.mainloop()


def tomar_lista_fecha():
    tomar_lista_fecha = Toplevel()
    tomar_lista_fecha.geometry("400x500")
    tomar_lista_fecha.title("C.I.P (Tomar lista de hoy)")
    tomar_lista_fecha.config(bg="#ffffff")

    tomar_lista_fecha.mainloop()

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
            Button(gui_lista_alumno, text="Ingresar valores", command=ing_valores).grid(row=linea, column=0,
                                                                                    sticky='w',
                                                                                    padx=5, pady=5)
        else:

            alumnos = lista_alumnos(curso_listar_alumno.get())

            linea = 0
            lineaa = 0
            presentes = 0
            ausentes = 0

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
                    presentes += 1
                elif i == 0:
                    checkbox.append(IntVar())
                    desactivo = Checkbutton(gui_lista_alumno, background="#ffffff", variable=checkbox[lineaa])
                    desactivo.grid(row=lineaa, column=2, sticky='w', padx=5, pady=5)
                    desactivo.deselect()
                    ausentes += 1
                lineaa += 1
            linea += 1

            Label(gui_lista_alumno, text=f"Presentes: {presentes}", background="#ffffff").grid(row=linea, column=1, sticky='w', padx=5, pady=5)
            Label(gui_lista_alumno, text=f"Ausentes: {ausentes}", background="#ffffff").grid(row=linea, column=2, sticky='w', padx=5, pady=5)
            Button(gui_lista_alumno, text="Ingresar valores", command=ing_valores).grid(row=linea, column=0,
                                                                                            sticky='w',
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
        gui_listar_cursos.geometry("325x175")
        gui_listar_cursos.title("C.I.P (Lista de cursos)")
        gui_listar_cursos.config(bg="#ffffff")

        scrollbar = Scrollbar(gui_listar_cursos, orient='vertical')
        scrollbar.grid(row=0, column=2, sticky='ns', padx=5, pady=5)
        labelcursosformateados = Label(gui_listar_cursos, text="Los cursos disponibles son:", background="#ffffff", wraplength=390, justify=LEFT)

        labelcursosformateados.grid(row=0, column=0, sticky='nw', padx=5, pady=5)

        lista = Listbox(gui_listar_cursos)

        lista.grid(row=0, column=1, sticky='nw', padx=5, pady=5)

        cursosordenados = sorted(cursos)

        lista.insert(0, *cursosordenados)

        lista.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=lista.yview)

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



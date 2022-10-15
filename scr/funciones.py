cursos = []

def agregar_curso(curso):
    cursos.append(curso)
    globals()[curso] = []
    return cursos

def agregar_alumno(curso, alumno):
    globals()[curso].append(alumno)
    return globals()[curso]

def lista_alumnos(curso):
    return globals()[curso]

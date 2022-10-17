cursos = []

def agregar_curso(curso):
    cursos.append(curso)
    globals()[curso] = []
    return cursos

def agregar_alumno(curso, alumno):
    globals()[curso].append(alumno)
    return sorted(globals()[curso])

def lista_alumnos(curso):
    return globals()[curso]


agregar_curso("2°4")
agregar_curso("5°3")
agregar_curso("1°4")
agregar_curso("7°3")
agregar_curso("1°2")
agregar_curso("6°4")

agregar_alumno("5°3", "Ianuzzi Thiago")
agregar_alumno("5°3", "Fernandez Luna")
agregar_alumno("5°3", "Paredes Adrian")
agregar_alumno("5°3", "Villanueva karina" )
agregar_alumno("5°3", "Alvarez Carlos")
agregar_alumno("2°4", "Gonzalez Juan")
agregar_alumno("2°4", "Schneider Ian")
agregar_alumno("2°4", "Calo Rodrigo")
agregar_alumno("2°4", "Paredes Melody")
agregar_alumno("2°4", "Gonzales Melanie")
agregar_alumno("1°2", "Blanco Martin")
agregar_alumno("1°2", "Bustamante Mia")
agregar_alumno("1°2", "Casanovas Roberto")
agregar_alumno("1°2", "Bordon Luciano")
agregar_alumno("1°2", "Santacruz Mauricio")
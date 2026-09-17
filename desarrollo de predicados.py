#universo
estudiantes = ["eduardo", "diego", "alexis"]
maestros = ["luis", "carlos"]
tutores = ["oscar"]
proyectos = ["k", "elipsis", "orogedon"]
plumas = ["azul", "rojo", "verde"]
clases = ["algebra", "programacion"]
celulares = ["646-138-5687", "696-139-5687", "646-140-5687", "646-111-2222", "646-111-3333"]
salarios = ["10000", "15000"]



estudianteEnCarrera = {
    "sistemas_computacionales": ["eduardo", "diego", "alexis"]
}

datosMaestro = {
    "luis": {"clase": "algebra", "salario": "10000"},
    "carlos": {"clase": "programacion", "salario": "10000"}
}

datosTutor = {
    "oscar": {"salario": "15000"}
}

celularDePersona = {
    "eduardo": ["646-138-5687"],
    "diego": ["696-139-5687"],
    "alexis": ["646-140-5687"],
    "luis": ["646-111-2222"],
    "carlos": ["646-111-3333"]
}

proyectoDeEstudiante = {
    "eduardo": ["k"],
    "diego": ["elipsis"],
    "alexis": ["orogedon"]
}

plumaDeEstudiante = {
    "eduardo": ["azul"],
    "diego": ["rojo"],
    "alexis": ["verde"]
}

claseDeEstudiante = {
    "algebra": ["eduardo", "alexis"],
    "programacion": ["diego"]
}


#predicados
def maestro(x, y, z):
    if x in datosMaestro:
        ClaseM = datosMaestro[x]["clase"]
        SalarioM= datosMaestro[x]["salario"]
        return y == ClaseM and str(z) == SalarioM
    return False

def tutor(x, y):
    if x in datosTutor:
        SalarioT = datosTutor[x]["salario"]
        return str(y) == SalarioT
    return False

def estudiante(x, y):
    for carrera, alumnos in estudianteEnCarrera.items():
        if x in alumnos and y in carrera:
            return True
    return False

def celular(x, y):
    for persona, numero in celularDePersona.items():
        if x in numero and y in persona:
            return True
    return False

def proyecto(x, y):
    for est, pro in proyectoDeEstudiante.items():
        if x in pro and y in est:
            return True
    return False

def pluma(x, y):
    for est, plu in plumaDeEstudiante.items():
        if x in plu and y in est:
            return True
    return False

def clase(x, y):
    for clase, alumnos in claseDeEstudiante.items():
        if x in clase and y in alumnos:
            return True
    return False

#consultas
print(maestro("luis", "algebra", "10000"))       
print(tutor("oscar", "15000"))                   
print(estudiante("eduardo", "sistemas_computacionales")) 
print(proyecto("k", "eduardo"))
print(celular("646-111-2222", "luis"))                   
print(pluma("azul", "eduardo"))                          
print(clase("algebra", "alexis"))                       

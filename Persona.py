class Persona:
    def __init__(self):
        self.__nombre = None
        self.__apellido = None
        self.__ciudad = None
        self.__edad = None
        self.__correo = None

    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    
    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, valor):
        self.__apellido = valor

    
    @property
    def ciudad(self):
        return self.__ciudad

    @ciudad.setter
    def ciudad(self, valor):
        self.__ciudad = valor

    
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        self.__edad = valor

    
    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        self.__correo = valor


from Persona import Persona

def editar_persona(persona):
    print("--- EDITAR DATOS ---")
    print("Deje vacío para no modificar.")

    nuevo_nombre = input(f"Nombre ({persona.nombre}): ")
    nuevo_apellido = input(f"Apellido ({persona.apellido}): ")
    nueva_ciudad = input(f"Ciudad ({persona.ciudad}): ")
    nueva_edad = input(f"Edad ({persona.edad}): ")
    nuevo_correo = input(f"Correo ({persona.correo}): ")

    if nuevo_nombre != "":
        persona.nombre = nuevo_nombre
    if nuevo_apellido != "":
        persona.apellido = nuevo_apellido
    if nueva_ciudad != "":
        persona.ciudad = nueva_ciudad
    if nueva_edad != "":
        persona.edad = nueva_edad
    if nuevo_correo != "":
        persona.correo = nuevo_correo

    print("Datos actualizados correctamente.")


def eliminar_persona(persona):
    print("¿Está seguro que desea eliminar los datos? (s/n)")
    confirm = input("> ").lower()

    if confirm == "s":
        persona.nombre = None
        persona.apellido = None
        persona.ciudad = None
        persona.edad = None
        persona.correo = None
        print("Datos eliminados exitosamente.")
    else:
        print("Eliminación cancelada.")
class Persona:

    def __init__(self):
        # Constructor: crea los atributos privados y los inicializa en None
        self.__nombre = None
        self.__apellido = None
        self.__ciudad = None
        self.__edad = None
        self.__tipo_documento = None
        self.__documento = None

    @property
    def nombre(self):
        # Getter: permite obtener el valor de __nombre
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        # Setter: permite asignar un valor a __nombre
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
        # No hay validación, se asigna directamente
        self.__edad = valor

    @property
    def tipo_documento(self):
        return self.__tipo_documento

    @tipo_documento.setter
    def tipo_documento(self, valor):
        # Validamos el tipo de documento:
        # Solo se permite CC (cédula) o TI (tarjeta de identidad)
        # Se utiliza upper() para aceptar "cc", "CC", "Cc", etc.
        if valor.upper() in ["CC", "TI"]:
            self.__tipo_documento = valor.upper()
        else:
            # Si no es válido, se lanza un error
            raise ValueError("El tipo de documento debe ser 'CC' o 'TI'.")

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, valor):
        # Validamos que el número de documento sea IMPAR.
        # Se usa valor % 2 != 0 → un número impar da resto diferente a 0
        if valor % 2 != 0:   
            self.__documento = valor
        else:
            # Si es par, se genera un error para obligar al usuario
            # a ingresar un documento válido
            raise ValueError("El número de documento debe ser impar.")
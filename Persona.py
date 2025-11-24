class Persona:
    def __init__(self):
        self.__nombre = None
        self.__apellido = None
        self.__ciudad = None
        self.__edad = None
        self.__tipo_documento = None
        self.__documento = None

    
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
    def tipo_documento(self):
        return self.__tipo_documento

    @tipo_documento.setter
    def tipo_documento(self, valor):
        if valor.upper() in ["CC", "TI"]:
            self.__tipo_documento = valor.upper()
        else:
            raise ValueError("El tipo de documento debe ser 'CC' o 'TI'.")

    
    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, valor):
        if valor % 2 != 0:   
            self.__documento = valor
        else:
            raise ValueError("El número de documento debe ser impar.")
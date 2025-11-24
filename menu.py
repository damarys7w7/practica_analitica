from Persona import Persona
def menu():
    persona = Persona()

    while True:
        print("--- MENÚ ---")
        print("1. Agregar datos")
        print("2. Consultar datos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            persona.nombre = input("Ingrese el nombre: ")
            persona.apellido = input("Ingrese el apellido: ")
            persona.ciudad = input("Ingrese la ciudad: ")
            persona.edad = input("Ingrese la edad: ")

            
            while True:
                try:
                    tipo_doc = input("Ingrese el tipo de documento (CC o TI): ")
                    persona.tipo_documento = tipo_doc
                    break
                except ValueError as e:
                    print(f"{e}. Intente de nuevo.")

            
            while True:
                try:
                    numero_doc = int(input("Ingrese el número del documento (solo impar): "))
                    persona.documento = numero_doc
                    break
                except ValueError as e:
                    print(f"{e}. Intente de nuevo.")

            print("Datos agregados correctamente.")

        elif opcion == "2":
            print("--- DATOS DE LA PERSONA ---")
            print(f"Nombre: {persona.nombre}")
            print(f"Apellido: {persona.apellido}")
            print(f"Ciudad: {persona.ciudad}")
            print(f"Edad: {persona.edad}")
            print(f"Tipo de documento: {persona.tipo_documento}")
            print(f"Número de documento: {persona.documento}")

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, intente nuevamente.")

menu()
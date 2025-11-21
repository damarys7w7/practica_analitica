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
            persona.correo = input("Ingrese el correo: ")
            print("Datos agregados correctamente.")

        elif opcion == "2":
            print("\n--- DATOS DE LA PERSONA ---")
            print(f"Nombre: {persona.nombre}")
            print(f"Apellido: {persona.apellido}")
            print(f"Ciudad: {persona.ciudad}")
            print(f"Edad: {persona.edad}")
            print(f"Correo: {persona.correo}")

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, intente de nuevo.")

menu()
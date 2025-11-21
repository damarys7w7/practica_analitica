from Persona import Persona
from Persona import editar_persona, eliminar_persona 

def menu():
    persona = Persona()

    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Agregar datos")
        print("2. Consultar datos")
        print("3. Editar datos")
        print("4. Eliminar datos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            persona.nombre = input("Ingrese el nombre: ")
            persona.apellido = input("Ingrese el apellido: ")
            persona.ciudad = input("Ingrese la ciudad: ")
            persona.edad = input("Ingrese la edad: ")
            persona.correo = input("Ingrese el correo: ")
            print("Datos agregados correctamente.")

        elif opcion == "2":
            print("--- DATOS DE LA PERSONA ---")
            print(f"Nombre: {persona.nombre}")
            print(f"Apellido: {persona.apellido}")
            print(f"Ciudad: {persona.ciudad}")
            print(f"Edad: {persona.edad}")
            print(f"Correo: {persona.correo}")

        elif opcion == "3":
            editar_persona(persona)

        elif opcion == "4":
            eliminar_persona(persona)

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, intente de nuevo.")

menu()
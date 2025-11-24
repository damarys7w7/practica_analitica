from Persona import Persona  # Importamos la clase Persona desde el archivo Persona.py

def menu():
    persona = Persona()  # Creamos un objeto Persona vacío donde se guardarán los datos

    while True:  # Bucle infinito del menú: se repite hasta que el usuario elija salir
        print("--- MENÚ ---")
        print("1. Agregar datos:")
        print("2. Consultar datos:")
        print("3. Editar datos:")
        print("4. Eliminar datos:")
        print("5. Salir:")

        opcion = input("Seleccione una opción: ")  # El usuario elige una opción del menú

        if opcion == "1":
            # Datos básicos sin validación
            persona.nombre = input("Ingrese el nombre: ")
            persona.apellido = input("Ingrese el apellido: ")
            persona.ciudad = input("Ingrese la ciudad: ")
            persona.edad = input("Ingrese la edad: ")

            # Validación del tipo de documento (solo CC o TI)
            while True:
                try:
                    tipo_doc = input("Ingrese el tipo de documento (CC o TI): ")
                    persona.tipo_documento = tipo_doc  # Setter valida el dato
                    break  # Si es correcto, salimos del while
                except ValueError as e:
                    print(f"{e}. Intente de nuevo.")  # Si es inválido, se repite

            # Validación del número de documento (solo impar)
            while True:
                try:
                    numero_doc = int(input("Ingrese el número del documento (solo impar): "))
                    persona.documento = numero_doc  # Setter valida si es impar
                    break
                except ValueError as e:
                    print(f"{e}. Intente de nuevo.")

            print("Datos agregados correctamente.")

        elif opcion == "2":
            print("--- DATOS DE LA PERSONA ---")
            # Solo mostramos los datos con los getters
            print(f"Nombre: {persona.nombre}")
            print(f"Apellido: {persona.apellido}")
            print(f"Ciudad: {persona.ciudad}")
            print(f"Edad: {persona.edad}")
            print(f"Tipo de documento: {persona.tipo_documento}")
            print(f"Número de documento: {persona.documento}")

        elif opcion == "3":
            print("--- EDITAR DATOS ---")
            print("Dejar vacío si NO quiere cambiar ese dato.")

            # Si el input es vacío: no se modifica
            nuevo_nombre = input("Nuevo nombre: ")
            if nuevo_nombre != "":
                persona.nombre = nuevo_nombre

            nuevo_apellido = input("Nuevo apellido: ")
            if nuevo_apellido != "":
                persona.apellido = nuevo_apellido

            nueva_ciudad = input("Nueva ciudad: ")
            if nueva_ciudad != "":
                persona.ciudad = nueva_ciudad

            nueva_edad = input("Nueva edad: ")
            if nueva_edad != "":
                persona.edad = nueva_edad

            # Validación tipo documento
            while True:
                nuevo_tipo = input("Nuevo tipo documento (CC o TI) o ENTER para no modificar: ")
                if nuevo_tipo == "":
                    break  # ENTER = no editar
                try:
                    persona.tipo_documento = nuevo_tipo
                    break
                except ValueError as e:
                    print(f"{e}. Intente de nuevo.")

            # Validación documento impar
            while True:
                nuevo_doc = input("Nuevo número documento (solo impar) o ENTER para no modificar: ")
                if nuevo_doc == "":
                    break
                try:
                    persona.documento = int(nuevo_doc)
                    break
                except ValueError as e:
                    print(f"{e}. Intente de nuevo.")

            print("Datos editados correctamente.")

        elif opcion == "4":
            confirmacion = input("\n¿Seguro que desea eliminar todos los datos? (S/N): ")

            if confirmacion.upper() == "S":
                persona = Persona()  # Creamos objeto nuevo y se borran todos los datos
                print("\n✓ Datos eliminados correctamente.")
            else:
                print("Operación cancelada.")

        elif opcion == "5":
            print("Saliendo del programa...")
            break  # Rompe el while True y finaliza

        else:
            print("Opción inválida, intente nuevamente.")

# Inicia el menú automáticamente
menu()
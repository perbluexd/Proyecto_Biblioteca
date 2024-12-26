# -*- coding: utf-8 -*-
biblioteca = {}

def mostrarBiblioteca(biblioteca):
    for categoria, libros in biblioteca.items():
        print(f"Género: {categoria}")
        if not libros:
            print("  No hay libros en esta categoría.")
        else:
            for libro in libros:
                estado = "Leído" if libro["Estado"] else "Por leer"
                print(f"  - Título: {libro['Titulo']}, Autor: {libro['Autor']}, Estado: {estado}")

def agregarLibro(biblioteca):
    while True:
        categoria = input("Ingresa la categoría donde deseas agregar el libro: ").strip()
        if categoria not in biblioteca:
            biblioteca[categoria] = []
        
        titulo = input("Ingresa el nombre del título del libro: ").strip()
        autor = input("Ingresa el nombre del autor: ").strip()
        leido_booleano = input("¿Está leído? (True/False): ").strip().lower()
        if leido_booleano not in {"true", "false"}:
            print("Entrada inválida. Por favor ingresa 'True' o 'False'.")
            continue
        leido = leido_booleano == "true"
        
        biblioteca[categoria].append({"Titulo": titulo, "Autor": autor, "Estado": leido})
        print(f"Libro '{titulo}' agregado a la categoría '{categoria}'.")
        
        opcion = input("¿Deseas agregar más libros? (s/n): ").strip().lower()
        if opcion != "s":
            break

def eliminarLibro(biblioteca):
    categoria = input("Ingresa la categoría donde quieres eliminar el libro: ").strip()
    if categoria in biblioteca:
        titulo = input("Ingresa el nombre del título del libro que deseas eliminar: ").strip()
        for libro in biblioteca[categoria]:
            if libro["Titulo"] == titulo:
                biblioteca[categoria].remove(libro)
                print(f"El libro '{titulo}' ha sido eliminado.")
                return
        print("El libro no se encontró.")
    else:
        print("La categoría ingresada no existe.")

def editarLibro(biblioteca):
    categoria = input("Ingresa la categoría donde quieres editar un libro: ").strip()
    if categoria in biblioteca:
        libros = biblioteca[categoria]
        if not libros:
            print(f"No hay libros en la categoría '{categoria}'.")
            return

        print("Libros disponibles:")
        for idx, libro in enumerate(libros, start=1):
            estado = "Leído" if libro["Estado"] else "Por leer"
            print(f"{idx}. Título: {libro['Titulo']}, Autor: {libro['Autor']}, Estado: {estado}")

        try:
            seleccion = int(input("Selecciona el número del libro que deseas editar: ")) - 1
            if seleccion < 0 or seleccion >= len(libros):
                print("Selección no válida.")
                return
        except ValueError:
            print("Por favor, ingresa un número válido.")
            return
        
        libro = libros[seleccion]
        print("¿Qué deseas editar?")
        print("1. Título")
        print("2. Autor")
        print("3. Estado")
        opcion = input("Selecciona una opción (1/2/3): ").strip()

        if opcion == "1":
            nuevo_titulo = input("Escribe el nuevo título del libro: ").strip()
            libro["Titulo"] = nuevo_titulo
            print("Título actualizado exitosamente.")
        elif opcion == "2":
            nuevo_autor = input("Escribe el nuevo autor del libro: ").strip()
            libro["Autor"] = nuevo_autor
            print("Autor actualizado exitosamente.")
        elif opcion == "3":
            nuevo_estado = input("Escribe el nuevo estado del libro ('True' para leído, 'False' para por leer): ").strip().lower()
            if nuevo_estado in {"true", "false"}:
                libro["Estado"] = nuevo_estado == "true"
                print("Estado actualizado exitosamente.")
            else:
                print("Estado no válido. No se realizaron cambios.")
        else:
            print("Opción no válida. No se realizaron cambios.")
    else:
        print(f"La categoría '{categoria}' no existe.")

def marcar(biblioteca):
    categoria = input("Ingresa la categoría donde quieres marcar el libro: ").strip()
    if categoria in biblioteca:
        titulo = input("Ingresa el título del libro que quieres marcar: ").strip()
        for libro in biblioteca[categoria]:
            if libro["Titulo"] == titulo:
                marcado = input("¿Quieres marcarlo como leído? (True/False): ").strip().lower()
                if marcado in {"true", "false"}:
                    libro["Estado"] = marcado == "true"
                    print(f"El libro '{titulo}' ha sido marcado como {'Leído' if libro['Estado'] else 'Por leer'}.")
                    return
                else:
                    print("Entrada inválida. Por favor ingresa 'True' o 'False'.")
                    return
        print("El libro no se encontró.")
    else:
        print("La categoría ingresada no existe.")

def menu():
    while True:
        opcion = input(
            "Menú de Biblioteca:\n"
            "1. Mostrar Biblioteca\n"
            "2. Agregar Libro\n"
            "3. Eliminar Libro\n"
            "4. Editar Libro\n"
            "5. Marcar Libro\n"
            "6. Salir\n"
            "Selecciona una opción: "
        ).strip()
        if opcion == "1":
            mostrarBiblioteca(biblioteca)
        elif opcion == "2":
            agregarLibro(biblioteca)
        elif opcion == "3":
            eliminarLibro(biblioteca)
        elif opcion == "4":
            editarLibro(biblioteca)
        elif opcion == "5":
            marcar(biblioteca)
        elif opcion == "6":
            print("Gracias por usar la biblioteca. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
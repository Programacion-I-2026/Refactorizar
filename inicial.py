opcion = 0
saldo = 10000
datos_consumidos = 1500
contador = 0

while opcion != 5:

    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar saldo")
    print("2. Ver promociones")
    print("3. Recargar saldo")
    print("4. Consultar datos consumidos")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion < 1 or opcion > 5:
        print("Opción inválida. Intente nuevamente.")
        continue

    if opcion == 1:
        print("\nSu saldo actual es: $", saldo)
        contador += 1

    elif opcion == 2:
        print("\nPromociones disponibles:")
        print("- 2x1 en recargas")
        print("- 30% de descuento en datos móviles")
        contador += 1

    elif opcion == 3:
        monto = int(input("Ingrese monto a recargar: "))

        if monto <= 0:
            print("Error: el monto debe ser mayor a 0")
        else:
            saldo = saldo + monto
            print("Recarga exitosa. Nuevo saldo: $", saldo)
            contador += 1

    elif opcion == 4:
        print("\nDatos consumidos:", datos_consumidos, "MB")
        contador += 1

    elif opcion == 5:
        print("\nGracias por comunicarse. ¡Hasta luego!")
        print("Total de operaciones realizadas:", contador)
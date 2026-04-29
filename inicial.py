opcion = 0
saldo = 10000
contador = 0

while opcion != 5:

    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar saldo")
    print("2. Ver promociones")
    print("3. Consultar datos consumidos")
    print("4. Recargar saldo")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("\nSu saldo actual es: $", saldo)
        contador += 1

    elif opcion == 2:
        print("\nPromociones disponibles:")
        print("- 2x1 en recargas")
        print("- 30% de descuento en datos móviles")
        contador += 1

    elif opcion == 3:
        print("\n Consultar datos consumidos")
        print("100")
        contador += 1

    elif opcion == 4:
        monto = int(input("Ingrese monto a recargar: "))
        if monto <= 0:
            print("Opción inválida, intente nuevamente.")
        else:
            saldo = saldo + monto
            print("Recarga exitosa. Nuevo saldo: $", saldo)
        contador += 1

    elif opcion == 5:
        print("\nGracias por comunicarse. ¡Hasta luego!")

    else:
        print("Opción inválida. Intente nuevamente.")
        print("Total de operaciones realizadas: ", contador)
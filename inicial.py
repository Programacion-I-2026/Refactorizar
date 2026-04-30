opcion = 0
saldo = 10000
recargas = 0
MAX_RECARGAS = 3

while opcion != 5:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar saldo")
    print("2. Ver promociones")
    print("3. Recargar saldo")
    print("4. Consultar datos consumidos")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("\nSu saldo actual es: $", saldo)

    elif opcion == 2:
        print("\nPromociones disponibles:")
        print("- 2x1 en recargas")
        print("- 30% de descuento en datos móviles")

    elif opcion == 3:
        if recargas >= MAX_RECARGAS:
            print("Ha alcanzado el límite de recargas.")
        else:
            monto = int(input("Ingrese monto a recargar: "))
            if monto <= 0:
                print("No se permiten montos negativos o cero.")
            else:
                saldo = saldo + monto
                recargas += 1
                print("Recarga exitosa. Nuevo saldo: $", saldo)

    elif opcion == 4:
        print("\nDatos consumidos:")
        print("- Datos móviles: 500 MB")
        print("- Wi-Fi: 1 GB")

    elif opcion == 5:
        print("\nGracias por comunicarse. ¡Hasta luego!")
        print("Cantidad de operaciones realizadas:", operaciones)

    else:
        print("Opción inválida. Intente nuevamente.")
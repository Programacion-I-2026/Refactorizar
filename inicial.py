opcion = 0
saldo = 10000
datosconsumidos=50000
while opcion != 5:

    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar saldo")
    print("2. Ver promociones")
    print("3. Recargar saldo")
    print("4. Salir")
    print("5.consultar datos consumidos")

    try:
         opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Error: ingresa un numero valido")
        continue

    if opcion == 1:
        print("\nSu saldo actual es: $", saldo)

    elif opcion == 2:
        print("\nPromociones disponibles:")
        print("- 2x1 en recargas")
        print("- 30% de descuento en datos móviles")

    elif opcion == 3:
        monto = int(input("Ingrese monto a recargar: "))
        saldo = saldo + monto
        print("Recarga exitosa. Nuevo saldo: $", saldo)

    elif opcion == 4:
        print("\nGracias por comunicarse. ¡Hasta luego!")
    elif opcion == 5:
        print("\nlos datos consumidos son",datosconsumidos)

    else:
        print("Opción inválida. Intente nuevamente.")

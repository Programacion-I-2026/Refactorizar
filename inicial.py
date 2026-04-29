opcion = 0
saldo = 10000
datosCons = 500
operaciones = 0

while opcion != 5:

    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar saldo")
    print("2. Ver promociones")
    print("3. Recargar saldo")
    print("4. Consultar datos Consumidos")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1:
            operaciones += 1
            print("\nSu saldo actual es: $", saldo)
        case 2:
            operaciones += 1
            print("\nPromociones disponibles:")
            print("- 2x1 en recargas")
            print("- 30% de descuento en datos móviles")
        case 3:
            operaciones += 1
            monto = int(input("Ingrese monto a recargar: "))
            if monto > 0:
                saldo = saldo + monto
                print("Recarga exitosa. Nuevo saldo: $", saldo)
            else:
                print("porfavor ingrese un numero positivo")
        case 4:
            operaciones += 1
            print("\nActualmente consumiste", datosCons, "datos") 
        case 5:
            operaciones += 1
            print("\nGracias por comunicarse. ¡Hasta luego!") 
            print("\nCantidad de operaciones", operaciones)
        case _:
            print("Opción inválida. Intente nuevamente.")


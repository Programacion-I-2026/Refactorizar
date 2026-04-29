opcion = 0
saldo = 10000
datosCons = 500

while opcion != 4:

    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar saldo")
    print("2. Ver promociones")
    print("3. Recargar saldo")
    print("4. Consultar datos Consumidos")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1:
            print("\nSu saldo actual es: $", saldo)
        case 2:
            print("\nPromociones disponibles:")
            print("- 2x1 en recargas")
            print("- 30% de descuento en datos móviles")
        case 3:
            monto = int(input("Ingrese monto a recargar: "))
            saldo = saldo + monto
            print("Recarga exitosa. Nuevo saldo: $", saldo)
        case 4:
            print("\nActualmente consumiste", datosCons, "datos") 
        case 5:
            print("\nGracias por comunicarse. ¡Hasta luego!") 
        case _:
            print("Opción inválida. Intente nuevamente.")


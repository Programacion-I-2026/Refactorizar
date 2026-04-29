opcion = 0
saldo = 10000
datos = 0
operaciones = 0
recargas = 3

while opcion != 5:

    operaciones = operaciones + 1
    
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar saldo")
    print("2. Ver promociones")
    print("3. Recargar saldo")
    print("4. Consultar sus datos consumidos")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))
    
    if opcion <1 or opcion > 5:
        print("Opción inválida. Intente nuevamente.")
    
    if opcion == 1:
        print("\nSu saldo actual es: $", saldo)

    elif opcion == 2:
        print("\nPromociones disponibles:")
        print("- 2x1 en recargas")
        print("- 30% de descuento en datos móviles")

    elif opcion == 3:
        monto = int(input("Ingrese monto a recargar: "))
        if monto <= 0 :
            print("No se puede recargar saldo negativo")
        else:
            recargas = recargas - 1
            if recargas >= 0:
                saldo = saldo + monto
                print("Recarga exitosa(Recargas disponibles",recargas,"). Nuevo saldo: $", saldo)
            else:
                print("Recargas agotadas. Operacion cancelada")

    elif opcion == 4:
        print("Sus datos consumidos es de ",datos)
    elif opcion == 5:
        print("Usted realizo",operaciones,"operaciones")
        print("\nGracias por comunicarse. ¡Hasta luego!")
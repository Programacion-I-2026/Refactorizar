opcion = 0
saldo = 10000
datoConsumido= 50000
contador = 0

while opcion != 4:

    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar saldo")
    print("2. Ver promociones")
    print("3. Recargar saldo")
    print("4. Salir")
    print("5. Datos consumidos")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("\nSu saldo actual es: $", saldo)
        contador +=1

    elif opcion == 2:
        print("\nPromociones disponibles:")
        print("- 2x1 en recargas")
        print("- 30% de descuento en datos móviles")
        contador +=1

    elif opcion == 3:
        monto = int(input("Ingrese monto a recargar: "))
        if monto > 0:
            saldo = saldo + monto
            print("Recarga exitosa. Nuevo saldo: $", saldo)
            contador +=1
        else:
            print("Ingrese un saldo positivo porfavor.")

    elif opcion == 4:
        print("\nGracias por comunicarse. ¡Hasta luego!")
        contador +=1

    elif opcion == 5:
        print("\nLos datos consumidos son", datoConsumido)
        contador +=1

    else:
        print("Opción inválida. Intente nuevamente.")
print(f"\n usted realizo: {contador} operaciones.")
opcion = 0
saldo = 10000
recargas = 0
MAX_RECARGAS = 3
operacion= 0
if opcion ==1:
    operacion +=1

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

    elif opcion == 2:
        print("\nPromociones disponibles:")
        print("- 2x1 en recargas")
        print("- 30% de descuento en datos móviles")

    elif opcion == 3:
        if recargas >= MAX_RECARGAS:
            print("Has alcanzado el límite de recargas. No puedes recargar más.")
        else:
           monto = int(input("Ingrese monto a recargar: "))
           if monto <= 0:
              print("Monto inválido. La recarga debe ser mayor a $0 intente nuevamente.")
              continue
        saldo = saldo + monto
        recargas += 1
        print("Recarga exitosa. Nuevo saldo: $", saldo)


    elif opcion == 4:
        print("Datos consumidos: 2GB")
        print("- datos móviles: 500 MB")
        print("- Wi-Fi: 1 GB")


    elif opcion == 5:
        print("\nGracias por comunicarse. ¡Hasta luego!")
        print("cantidad de operaciones realizadas: ", operacion)

    else:
        print("Opción inválida. Intente nuevamente.")
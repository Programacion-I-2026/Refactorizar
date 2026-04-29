opcion = 0
saldo = 10000
datosconsumidos = 50000
contador_operaciones = 0 

while opcion != 4
    
    if opcion == 1:
        print("\nSu saldo actual es: $", saldo)
        contador_operaciones += 1
    elif opcion == 2:
        print("\nPromociones disponibles...")
        contador_operaciones += 1 
    elif opcion == 3:
        contador_operaciones += 1
    elif opcion == 4:
        print("\nGracias por comunicarse. ¡Hasta luego!")
        print("Total de operaciones realizadas:", contador_operaciones)
    elif opcion == 1:
        print("\nlos datos consumidos son", datosconsumidos)
        contador_operaciones += 1
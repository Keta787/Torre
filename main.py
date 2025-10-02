
def mostrar_torres(A, B, C):
    """Muestra el estado actual de las torres."""
    print(f"Torre A: {A}")
    print(f"Torre B: {B}")
    print(f"Torre C: {C}")
    print("-" * 30)

def torre_hanoi_iterativa(n):
    """
    Resuelve la Torre de Hanoi de forma iterativa,
    mostrando el contenido de las torres en cada paso.
    """

    A = list(range(n, 0, -1))  
    B = []
    C = []


    torres = {'A': A, 'B': B, 'C': C}

    print("\nEstado inicial:")
    mostrar_torres(A, B, C)

    if n % 2 == 0:
        movimientos = [('A', 'B'), ('A', 'C'), ('B', 'C')]
    else:
        movimientos = [('A', 'C'), ('A', 'B'), ('B', 'C')]

    total_movimientos = 2 ** n - 1  

    for i in range(1, total_movimientos + 1):
        origen, destino = movimientos[(i - 1) % 3]
        torre_origen = torres[origen]
        torre_destino = torres[destino]

        # Decidir movimiento válido
        if not torre_origen:
            torre_origen.append(torre_destino.pop())
            print(f"Paso {i}: Mover disco de {destino} → {origen}")
        elif not torre_destino:
            torre_destino.append(torre_origen.pop())
            print(f"Paso {i}: Mover disco de {origen} → {destino}")
        elif torre_origen[-1] < torre_destino[-1]:
            torre_destino.append(torre_origen.pop())
            print(f"Paso {i}: Mover disco de {origen} → {destino}")
        else:
            torre_origen.append(torre_destino.pop())
            print(f"Paso {i}: Mover disco de {destino} → {origen}")


        mostrar_torres(A, B, C)

    print(f"\nTotal de movimientos: {total_movimientos}")



n = int(input("Ingresa la cantidad de discos: "))
torre_hanoi_iterativa(n)

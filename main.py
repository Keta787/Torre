# Torre de Hanoi en Python (versión iterativa)
# Sin recursividad y mostrando el estado de las torres en cada paso

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
    # Inicializamos las torres como pilas
    A = list(range(n, 0, -1))  # Torre origen con discos [n, ..., 2, 1]
    B = []
    C = []

    # Diccionario para acceder a las torres por su nombre
    torres = {'A': A, 'B': B, 'C': C}

    print("\nEstado inicial:")
    mostrar_torres(A, B, C)

    # Si el número de discos es par, intercambiamos destino y auxiliar
    if n % 2 == 0:
        movimientos = [('A', 'B'), ('A', 'C'), ('B', 'C')]
    else:
        movimientos = [('A', 'C'), ('A', 'B'), ('B', 'C')]

    total_movimientos = 2 ** n - 1  # Fórmula

    for i in range(1, total_movimientos + 1):
        # Escoger el par de torres según el paso actual
        origen, destino = movimientos[(i - 1) % 3]

        # Torre actual origen y destino
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

        # Mostrar el estado después de cada movimiento
        mostrar_torres(A, B, C)

    print(f"\nTotal de movimientos: {total_movimientos}")


# ==========================
# PROGRAMA PRINCIPAL
# ==========================
n = int(input("Ingresa la cantidad de discos: "))
torre_hanoi_iterativa(n)

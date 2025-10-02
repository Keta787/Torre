def hanoi_iterativo(n):
    #Torre inicial
    A = list(range(n, 0, -1))  
    B = []
    C = []
    total = 2 ** n - 1

    print("Estado inicial:")
    print("A:", A, "B:", B, "C:", C)
    print("-" * 20)

    # orden de movimientos depende de si n es par o impar
    if n % 2 == 0:
        pares = [("A", "B"), ("A", "C"), ("B", "C")]
    else:
        pares = [("A", "C"), ("A", "B"), ("B", "C")]

    torres = {"A": A, "B": B, "C": C}

    for i in range(1, total + 1):
        o, d = pares[(i - 1) % 3]
        origen = torres[o]
        destino = torres[d]

        # decidir el movimiento válido
        if not origen:
            origen.append(destino.pop())
            print(f"Paso {i}: {d} -> {o}")
        elif not destino:
            destino.append(origen.pop())
            print(f"Paso {i}: {o} -> {d}")
        elif origen[-1] < destino[-1]:
            destino.append(origen.pop())
            print(f"Paso {i}: {o} -> {d}")
        else:
            origen.append(destino.pop())
            print(f"Paso {i}: {d} -> {o}")

        print("A:", A, "B:", B, "C:", C)
        print("-" * 20)

    print("Movimientos totales:", total)


# Programa principal
n = int(input("Número de discos: "))
hanoi_iterativo(n)

def insertion_sort(A):
    N = len(A)  
    i = 1     #iniciar desde segundo elemento

    while i < N:
        current = A[i]  # Guardar el valor actual
        j = i - 1


        while j >= 0 and A[j] > current:
            A[j + 1] = A[j]
            j = j - 1

        A[j + 1] = current  # cambiar el elemento en su posición
        i = i + 1  # Pasar al siguiente elemento


lista = [5, 1, 8, 9, 12]
insertion_sort(lista)
print(lista)


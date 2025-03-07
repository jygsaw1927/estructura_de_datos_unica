
# Función Quick Sort para ordenar por nombre
def quick_sort(arr, key=lambda x: x.nombre):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if key(x) < key(pivot)]
    middle = [x for x in arr if key(x) == key(pivot)]
    right = [x for x in arr if key(x) > key(pivot)]
    return quick_sort(left, key) + middle + quick_sort(right, key)


# Búsqueda binaria
def busqueda_binaria(arr, key, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if key(arr[mid]) == target:
            return mid
        elif key(arr[mid]) < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
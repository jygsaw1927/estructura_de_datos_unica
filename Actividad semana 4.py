class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def __repr__(self):
        return f"Empleado(nombre={self.nombre}, edad={self.edad}, salario={self.salario})"

# Función Quick Sort para ordenar por nombre
def quick_sort(arr, key=lambda x: x.nombre):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if key(x) < key(pivot)]
    middle = [x for x in arr if key(x) == key(pivot)]
    right = [x for x in arr if key(x) > key(pivot)]
    return quick_sort(left, key) + middle + quick_sort(right, key)

# Función Merge Sort para ordenar por salario
def merge_sort(arr, key=lambda x: x.salario):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    
    return merge(left, right, key)

def merge(left, right, key):
    result = []
    while left and right:
        if key(left[0]) < key(right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result

# Función Heap Sort para ordenar por edad
def heapify(arr, n, i, key=lambda x: x.edad):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and key(arr[left]) > key(arr[largest]):
        largest = left
    if right < n and key(arr[right]) > key(arr[largest]):
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key)

def heap_sort(arr, key=lambda x: x.edad):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, key)

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

# Función principal para interactuar con el usuario
def menu():
    empleados = [
        Empleado("Kevin", 30, 2500),
        Empleado("Jhon", 22, 3000),
        Empleado("Miguel", 40, 2000),
        Empleado("Maria", 35, 3500),
        Empleado("Carlos", 28, 2800)
    ]
    
    while True:
        print("\nHola, bienvenido a mi la aplicacion de busqueda y ordenamiento, ¿Qué quieres hacer?")
        print("1. Ordenar por edad")
        print("2. Ordenar por nombre")
        print("3. Ordenar por salario")
        print("4. Buscar por edad")
        print("5. Buscar por salario")
        print("6. Salir")
        
        choice = input("Selecciona una opción: ")

        if choice == "1":
            print("\nOrdenando por edad...")
            heap_sort(empleados)
            print(empleados)
        
        elif choice == "2":
            print("\nOrdenando por nombre...")
            empleados = quick_sort(empleados)
            print(empleados)
        
        elif choice == "3":
            print("\nOrdenando por salario...")
            empleados = merge_sort(empleados)
            print(empleados)
        
        elif choice == "4":
            edad = int(input("Ingresa la edad que deseas buscar: "))
            heap_sort(empleados)  # Ordena la lista en su lugar
            index = busqueda_binaria(empleados, lambda x: x.edad, edad)  # Usa la lista ordenada
            if index != -1:
                print(f"Empleado encontrado: {empleados[index]}")
            else:
                print("Empleado no encontrado.")
        
        elif choice == "5":
            salario = int(input("Ingresa el salario que deseas buscar: "))
            empleados = merge_sort(empleados)
            index = busqueda_binaria(empleados, lambda x: x.salario, salario)
            if index != -1:
                print(f"Empleado encontrado: {empleados[index]}")
            else:
                print("Empleado no encontrado.")
        
        elif choice == "6":
            print("Saliendo de la aplicación...")
            break
        
        else:
            print("Opción inválida, intenta de nuevo.")

# Ejecutar la función del menú
if __name__ == "__main__":
    menu()
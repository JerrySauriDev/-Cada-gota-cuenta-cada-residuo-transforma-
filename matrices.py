import numpy as np
# Matriz 
lista_de_productos = [["Pan Bimbo", "Panque de Nuez", "Magdalenas"],
                      ["Sabritas", "Chetos", "Doritos"],
                      ["Jarrito", "Cocacola", "Fresca"]]
matrix = np.array(lista_de_productos)
print(f"Matriz creada: \n {matrix}")
# queue
agregar_cola = lista_de_productos
print(f"\nCola inicial: {agregar_cola}")
agregar_cola.append('Churrumaiz')
agregar_cola.append('Takis')
print(f"Despues de encolar: {agregar_cola}")
primer_elemento = agregar_cola.pop()
segundo_elemento = agregar_cola.pop()
#Pilas
pila_productos = []
print("\n--- Inicializando Pila---")
print(f"Estado de la pila: {pila_productos}")
print("\n--- Apilando Elementos ---")
pila_productos.append("Productos A: El último en la base")
print(f"Apilado: {pila_productos[-1]} (Fondo de la pila)")
# Listas vinculadas
new_matrix = ""
new_data = ""
def __int__(self):
    self.head = lista_de_productos
def push(self, new_data):
    new_data = lista_de_productos(new_data)

    new_matrix.next = self.head
    self.head = new_matrix
# Arboles
familia = (["Abuelo", "Padre", "Madre", "Hijo",])
class BinarySearchTree:
    """Clase para gestionar el Árbol  Binario de Búsqueda (BST)"""
    def __init__(self):
        self.root = familia  #La raíz del arbol     
    # ----Operación 1: Inserción ---
    def insert(self, data):
        """Inserta un nuevo valor manteniendo la propiedad de BST."""
        if self.root is familia:
            # Si el árbol esta vació, el nuevo nodo es la raíz.
            self.root = familia(data)
        else:
            # Llama a la función recursica para encontrar la posición
            self.insert.recursive(self.root.data)
            

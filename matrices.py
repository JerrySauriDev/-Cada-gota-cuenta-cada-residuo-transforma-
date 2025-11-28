import numpy as np
from collections import deque

# Matriz 
lista_de_productos = [["Pan Bimbo", "Panque de Nuez", "Magdalenas"],
                      ["Sabritas", "Chetos", "Doritos"],
                      ["Jarrito", "Cocacola", "Fresca"]]
matrix = np.array(lista_de_productos) # Crear la matriz usando numpy (ndarray)
print(f"\nMatriz creada: \n {matrix}")

# queue
agregar_cola = deque(lista_de_productos[1]) # creación de la cola con la segunda fila de la matriz
print(f"\nCola inicial: {agregar_cola}")
agregar_cola.append('Churrumaiz') # Encolar elemento al final de la cola
agregar_cola.append('Takis')
print(f"Despues de encolar: {agregar_cola}")
# Desencolar (Dequeue - remover sacar elementos por la izquierda/inicio)
# El elemento mas antiguo (el primero en salir) sale primero
primer_elemento = agregar_cola.popleft()
segundo_elemento = agregar_cola.popleft()
print(f"\nElementos desencolados: {primer_elemento}, {segundo_elemento}")
print(f"Cola despues de desencolar: {agregar_cola}")

#Pilas
pila = agregar_cola  # Creación de la pila (lista vacía)
print("\n--- Inicializando Pila ---")
print(f"Estado de la pila: {pila}")
print("\n--- Apilando Elementos ---") # Apilar (push): Añadir elementos (productos) al final de la lista
pila.append("Ruffles")
print(f"Apilado: {pila[-1]}")
pila.append("Galletas")
print(f"Apilado: {pila[-1]}")
print(f"Estado actual de la pila: {pila}")
print("\n--- Desapilando Elementos ---") # Desapilar (pop): Remover el último elemento añadido (el tope de la pila)
print(f"Desapilado: {pila.pop()}")   # quita el último
print(f"Estado de la pila: {pila}")

# Listas vinculadas
def __int__(self):
    self.head = None # Inicialmente, la lista está vacía
def push(self, new_data): # operacion 1 : Añadir un nuevo elemento al inicio de la lista
    new_node = Node(new_data)
    # El next del nuevo nodo apunta al actual 
    new_node.next = self.head
    self.head = new_node # La cabeza se actualiza al nuevo nodo

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
            

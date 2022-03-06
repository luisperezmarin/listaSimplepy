from turtle import shape
from graphviz import Digraph


class Lista:
    def __init__(self):
        self.head = None

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None

def insertar_nodo(lista, dato):
    nuevo_nodo = Nodo(dato)
    if lista.head == None:
        lista.head = nuevo_nodo
    else:
        nuevo_nodo.next = lista.head
        lista.head = nuevo_nodo

def imprimir_lista(lista):
    print("Lista:")
    if lista.head == None:
        print("Lista vacia")
    else:
        aux = lista.head
        while aux != None:
            print(f"{aux.dato} ->", end=" ")
            aux = aux.next
        print("None")

def eliminar_nodo(lista, dato):
    print("Eliminando nodo con dato: ", dato)
    if lista.head == None:
        print("Lista vacia")
    else:
        aux = lista.head
        if aux.dato == dato:
            lista.head = aux.next
        else:
            while aux.next != None:
                if aux.next.dato == dato:
                    aux.next = aux.next.next
                    break
                aux = aux.next

def buscar_nodo(lista, dato):
    if lista.head == None:
        print("Lista vacia")
    else:
        aux = lista.head
        while aux != None:
            if aux.dato == dato:
                return True
            aux = aux.next
        return False

def graficar(lista):
    dot = Digraph(comment='Lista simple')
    dot.attr(rankdir='LR', size='8,5', shape='circle')
    dot.node('head', 'head')
    aux = lista.head
    while aux != None:
        dot.node(str(aux.dato), str(aux.dato))
        dot.edge(str(aux.dato), str(aux.next.dato))
        aux = aux.next
    dot.render('listaSimple.gv', view=True)

def menu():
    print("1. Insertar nodo")
    print("2. Eliminar nodo")
    print("3. Buscar nodo")
    print("4. graficar")
    print("5. Salir")

def main():
    lista = Lista()
    while True:
        menu()
        opcion = input("Ingrese opcion: ")
        if opcion == "1":
            dato = int(input("Ingrese dato: "))
            insertar_nodo(lista, dato)
            imprimir_lista(lista)
        elif opcion == "2":
            dato = int(input("Ingrese dato: "))
            eliminar_nodo(lista, dato)
            imprimir_lista(lista)
        elif opcion == "3":
            dato = int(input("Ingrese dato: "))
            if buscar_nodo(lista, dato):
                print("El dato se encuentra en la lista")
            else:
                print("El dato no se encuentra en la lista")
        elif opcion == "4":
            graficar(lista)
        elif opcion == "5":
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()

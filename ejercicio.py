nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

def grupos_personajes(nombres):
    magos = ["Harry Houdini", "David Blaine", "Teller"]
    cientificos = ["Newton", "Hawking", "Einstein"]
    otros = []

    for nombre in nombres:
        if nombre in magos:
            continue
        elif nombre in cientificos:
            continue
        else:
            otros.append(nombre)
    
    return magos, cientificos, otros

def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = "El gran " + magos[i]

def imprimir_nombres(lista, titulo):
    print(f"{titulo}:")
    for nombre in lista:
        print(nombre)
    print()

magos, cientificos, otros = grupos_personajes(nombres)

print("Lista completa de nombres:")
imprimir_nombres(nombres, "Nombres")

hacer_grandioso(magos)

imprimir_nombres(magos, "Magos grandiosos")
imprimir_nombres(cientificos, "Cientificos")
imprimir_nombres(otros, "Otros")
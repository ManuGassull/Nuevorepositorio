print("hola Manu")
def devolverPositivos(lista):
    positivos = []
    for elem in lista:
        if elem >= 0:
            positivos.append(elem)
    return positivos
resultado = devolverPositivos([4,6,-1,4,20,-3])
print(resultado)
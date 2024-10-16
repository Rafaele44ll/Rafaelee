import os
os.system("cls")

def suma_diccionario(dicc):
    if not dicc:
        return 0
    clave, valor = dicc.popitem()
    return valor + suma_diccionario(dicc)

resultado = suma_diccionario({'a': 1, 'b': 2, 'c': 3})
print(resultado)  
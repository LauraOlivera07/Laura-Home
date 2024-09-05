import random

caracteres_raros=('?', '!', '¿', '¡',',', '.')

frase=input().split()

def desordenarPalabra():
    frase_nueva=""
    palabra_nueva = []

    def desorden(n1,n2):
        nonlocal palabra_nueva
        lista = []
        for x in range(n1, (len(paraula) - n2)):
            lista.append(paraula[x])
        random.shuffle(lista)
        result = ''.join(lista)
        return result

    for paraula in frase:

        if len(paraula)==1:
            palabra_nueva+=paraula

        elif paraula[0] in caracteres_raros:
            if len(paraula)==2:
                palabra_nueva+=paraula
            else:
                palabra_nueva += paraula[0], paraula[1], desorden(2, 1), paraula[-1]

        elif paraula[-1] in caracteres_raros:
            if len(paraula)==2:
                palabra_nueva+=paraula
            else:
                palabra_nueva += paraula[0], desorden(1, 2), paraula[len(paraula)-2], paraula[-1]
        else:
            palabra_nueva += paraula[0], desorden(1, 1), paraula[-1]

        frase_nueva+=(f'{"".join(palabra_nueva)} ')
        palabra_nueva.clear()

    return frase_nueva

frase_final=desordenarPalabra()

print(frase_final)

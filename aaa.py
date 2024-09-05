def obtenerFrase():
    frase=input().split()

    if len(frase)==1:
        while len(frase[0])<2:
             frase=input("Necesito más chicha para funcionar: ").split()

    return frase

frase=obtenerFrase()
print(frase)

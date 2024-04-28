import time
import LETRAS
import memes

def MENU():
    print("¿Quién quieres que te felicite?\n1 - SHRECK\n2 - LUFFY\n3 - WALTER WHITE\n5 - QUIERO SALIR, PESADA")
    try:
        eleccion=int(input())
        return eleccion
    except ValueError:
        print('¿Eres tonta?')
def happyBirthday():
    print('Cumpleaños feeeeliiiiz')
    time.sleep(1)
    print('Cumpleaños feeeeliiiiz')
    time.sleep(1)
    print('Te deseamos...')
    time.sleep(2)
    LETRAS.ANGELA()
    time.sleep(1)
    print('Cumpleaños feeeeliiiiz')

intro=0

un_enter=input('Presiona ENTER para empezar :)')
happyBirthday()
print()
memes.PASTEL()
print()
while intro!=5:
    intro=MENU()
    if intro:
        match intro:
            case 1:
                memes.shreckASCII()
                print()
            case 3:
                memes.walter_White()
                print()
            case 5:
                intro=5

print('¡Es la hora del regalo!')
print()
un_input=input('Pulsa para ver un regalito...')
memes.PEPE()

input("Presiona Enter para salir...")

"""
Pasa un numero decimal a binario
"""

def decimal_binario(decimal):
    if decimal == 0:
        return "0"
    binario = ""
    while decimal > 0:
        residuo = decimal % 2
        binario += str(residuo)
        decimal = decimal // 2
        print(decimal)
    return binario

print(decimal_binario(129))

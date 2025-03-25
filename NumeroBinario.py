from string import ascii_letters
import re

def BinarioFunc(Char):
    ListaBinario = list("00000000")
    Base = 2
    if (Char % 2) == 0:
        ListaBinario[7] = "0"
    else:
        ListaBinario[7] = "1"
        Char += -1
    for i in range(0, 7):
        if int((Char / (Base ** (7 - i)))) == 1:
            ListaBinario[i] = "1"
            Char = (Char - (Base ** (7 - i)))
    return ListaBinario


ListaCompleta = str(input("Ingresa una palabra para transformarla a binario: "))
print(ListaCompleta)
LongitudInput = int(len(ListaCompleta))
print(f"La longitud es: {LongitudInput}")
MatrizBinaria = []
for i in range(0,LongitudInput):
    Aux = ord(ListaCompleta[i])
    print(str(BinarioFunc(Aux)))
    print(BinarioFunc(Aux))
    MatrizBinaria.append(str(BinarioFunc(Aux)))


print(MatrizBinaria)
ListaBinaria = list(MatrizBinaria)
print(ListaBinaria)
MatrizLimpia =[re.sub(r"[\[\], ]", "", elem) for elem in MatrizBinaria]
print(str(MatrizLimpia))
String = str(MatrizLimpia)
String = "".join(filter(lambda letra: letra != "[", String))
String = "".join(filter(lambda letra: letra != "]", String))
String = "".join(filter(lambda letra: letra != '"', String))
String = "".join(filter(lambda letra: letra != "'", String))
String = "".join(filter(lambda letra: letra != ',', String))
print(String)
for i in range(0, len(String)):
    print(String[i])

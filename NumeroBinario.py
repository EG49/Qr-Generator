from string import ascii_letters
import re



def NumBinario(Char):
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

def LimpiarString(Matriz):
    MatrizLimpia = [re.sub(r"[\[\], ]", "", elem) for elem in Matriz]
    String = str(MatrizLimpia)
    String = "".join(filter(lambda letra: letra != "[", String))
    String = "".join(filter(lambda letra: letra != "]", String))
    String = "".join(filter(lambda letra: letra != '"', String))
    String = "".join(filter(lambda letra: letra != "'", String))
    String = "".join(filter(lambda letra: letra != ',', String))
    return(String)
def CadenaBinario(String):
    print(f"Longitud de la cadena es {len(String)}")
    MatrizBinaria = []
    for i in range(0, LongitudInput):
        Aux = ord(ListaCompleta[i])
        print(str(NumBinario(Aux)))
        print(NumBinario(Aux))
        MatrizBinaria.append(str(NumBinario(Aux)))
    return(MatrizBinaria, len(String))

ListaCompleta = str(input("Ingresa una palabra para transformarla a binario: NumBinario.py "))
print(ListaCompleta)
LongitudInput = int(len(ListaCompleta))
print(f"La longitud es: {LongitudInput}")
MatrizBinaria, Longitud = CadenaBinario(ListaCompleta)


Aux4 = LimpiarString(MatrizBinaria)
print(Aux4)
print(f"La cadena {ListaCompleta} tiene de largo {Longitud} caracteres")
NumeroEspacios = 0
for i in range(0,len(Aux4)):
   if Aux4[i] == " ":
       NumeroEspacios = NumeroEspacios + 1
       if NumeroEspacios == 1:
           Caracter1 = Aux4[i - 8 : i ]
       elif NumeroEspacios == 2:
           Caracter2 = Aux4[i - 8 : i ]


print(f"La cadena del primer caracter es {Caracter1} ")
print(f"La cadena del segundo caracter es {Caracter2} ")

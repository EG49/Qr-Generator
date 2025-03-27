from warnings import catch_warnings

from openpyxl import Workbook
from openpyxl.styles import PatternFill
from pycparser.c_ast import Break

fila = range(1,27)
def PintarBase(Color, Rango):
    abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z", "AA"]
    fill = PatternFill(start_color=Color, end_color=Color, fill_type="solid")
    for i in range(1, Rango):
        for i2 in range(1, Rango):
            celda = abecedario[i - 1]  + str(i2)
            ws[celda].fill = fill
            ws.column_dimensions[abecedario[i - 1]].width = 3

def PintarRango(Color, Rango, Linea, PuntoInicio,Columna, Fila ):
    abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z", "AA"]
    fill = PatternFill(start_color=Color, end_color=Color, fill_type="solid")
    if Linea == "Fila":
        for i in range(1, Rango):
            celda = abecedario[i + PuntoInicio - 1] + str(Fila)
            ws[celda].fill = fill
            ws.column_dimensions[abecedario[i + PuntoInicio - 1]].width = 3
    else:
        for i in range(1, Rango):
            celda = Columna + str(i + PuntoInicio)
            ws[celda].fill = fill
            ws.column_dimensions[abecedario[i - 1]].width = 3

def PintarCelda(Celda, Color):
    fill = PatternFill(start_color=Color, end_color=Color, fill_type="solid")
    ws[Celda].fill = fill

def AlternarPintar(ColorQR, ColorFondo, Rango, Linea, PuntoInicio, Columna, Fila, NSaltos ):
    abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z", "AA"]
    fill = PatternFill(start_color=ColorQR, end_color=ColorQR, fill_type="solid")
    if Linea == "Fila":
        for aux in range(0, Rango , NSaltos):
            try:
                PintarCelda(abecedario[aux + PuntoInicio] + str(Fila), ColorQR)
                print(f"Pinto celda {abecedario[ aux + PuntoInicio] + str(Fila)} verde")
                PintarCelda(abecedario[aux +  PuntoInicio + NSaltos - 1] + str(Fila), ColorFondo)
                print(f"Pinto celda {abecedario[aux + PuntoInicio + NSaltos - 1 ] + str(Fila)} azul")
                aux = aux + PuntoInicio
                print("El contador i es " + str(aux))

            except: print("list index out of range")


    else:
        for aux in range(0, Rango, NSaltos):
            try:
                PintarCelda(Columna+ str(aux + PuntoInicio), ColorQR)
                print(f"Pinto celda {Columna + str(aux + PuntoInicio)} verde")
                PintarCelda(Columna + str(aux + PuntoInicio + NSaltos -1), ColorFondo)
                print(f"Pinto celda {Columna + str(aux + PuntoInicio + NSaltos -1)} azul")
                aux = aux + PuntoInicio
                print("El contador i es " + str(aux))

            except:
                print("list index out of range")


def PintarBaseQR(ColorQR):
    PintarRango(ColorQR, 8, "Fila", 1, "A", 2)
    PintarRango(ColorQR, 8, "Columna", 1, "B", 2)
    PintarRango(ColorQR, 8, "Fila", 1, "A", 8)
    PintarRango(ColorQR, 8, "Columna", 19, "H", 20)
    PintarRango(ColorQR, 8, "Fila", 1, "A", 20)
    PintarRango(ColorQR, 8, "Columna", 19, "B", 26)
    PintarRango(ColorQR, 8, "Fila", 1, "A", 26)
    PintarRango(ColorQR, 8, "Columna", 1, "H", 2)
    PintarRango(ColorQR, 8, "Columna", 1, "T", 20)
    PintarRango(ColorQR, 8, "Fila", 19, "T", 2)
    PintarRango(ColorQR, 8, "Columna", 1, "Z", 26)
    PintarRango(ColorQR, 8, "Fila", 19, "Z", 8)
    PintarRango(ColorQR, 4, "Fila", 3, "A", 4)
    PintarRango(ColorQR, 4, "Fila", 3, "A", 5)
    PintarRango(ColorQR, 4, "Fila", 3, "A", 6)
    PintarRango(ColorQR, 4, "Fila", 3, "A", 22)
    PintarRango(ColorQR, 4, "Fila", 3, "A", 23)
    PintarRango(ColorQR, 4, "Fila", 3, "A", 24)
    PintarRango(ColorQR, 4, "Fila", 21, "A", 4)
    PintarRango(ColorQR, 4, "Fila", 21, "A", 5)
    PintarRango(ColorQR, 4, "Fila", 21, "A", 6)
    PintarRango(ColorQR, 6, "Fila", 17, "A", 18)
    PintarRango(ColorQR, 6, "Columna", 17, "R", 2)
    PintarRango(ColorQR, 6, "Fila", 17, "A", 22)
    PintarRango(ColorQR, 6, "Columna", 17, "V", 20)
    PintarCelda("T20", ColorQR)
    PintarCelda("J19", ColorQR)

wb = Workbook()
ws = wb.active
ColorFondo = "FFFFFF"
ColorQR = "000000"
ws.column_dimensions["B"].width = 3
PintarBase(ColorFondo,28)
PintarBaseQR(ColorQR)
AlternarPintar(ColorQR,ColorFondo, 9, "Fila", 9, "A", 7,2)
AlternarPintar(ColorQR,ColorFondo, 9, "Columna", 10, "G", 7,2)




wb.save("Test.xlsx")
from openpyxl import Workbook
from openpyxl.styles import PatternFill

fila = range(1,27)
def PintarLinea(Color, Rango, Linea, Columna, Fila ):
    abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z", "AA"]
    fill = PatternFill(start_color=Color, end_color=color, fill_type="solid")
    if Linea == "Fila":
        for i in range(1, Rango):
            celda = abecedario[i - 1] + str(Fila)
            ws[celda].fill = fill
            ws.column_dimensions[abecedario[i - 1]].width = 3
    else:
        for i in range(1, 28):
            celda = Columna + str(i)
            ws[celda].fill = fill
            ws.column_dimensions[abecedario[i - 1]].width = 3

def PintarRango(Color, Rango, Linea, PuntoInicio,Columna, Fila ):
    abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z", "AA"]
    fill = PatternFill(start_color=Color, end_color=color, fill_type="solid")
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

wb = Workbook()
ws = wb.active
color = "FFFFFF"
ws.column_dimensions["B"].width = 3

PintarLinea("FFFFFF", 28, "Fila", "A", 1)
PintarLinea("FFFFFF", 28, "Fila", "A", 27)
PintarLinea("FFFFFF", 28, "Columna", "A", 1)
PintarLinea("FFFFFF", 28, "Columna", "AA", 1)
PintarRango("000000", 8, "Fila", 1, "A",2)
PintarRango("000000", 8, "Columna", 1, "B",2)
PintarRango("000000", 8, "Fila", 1, "A",8)
PintarRango("000000", 8, "Columna", 19, "H",20)
PintarRango("000000", 8, "Fila", 1, "A",20)
PintarRango("000000", 8, "Columna", 19, "B",26)
PintarRango("000000", 8, "Fila", 1, "A",26)
PintarRango("000000", 8, "Columna", 1, "H",2)
PintarRango("000000", 8, "Columna", 1, "T",20)
PintarRango("000000", 8, "Fila", 19, "T",2)
PintarRango("000000", 8, "Columna", 1, "Z",26)
PintarRango("000000", 8, "Fila", 19, "Z",8)
PintarRango("000000", 4, "Fila", 3, "A",4)
PintarRango("000000", 4, "Fila", 3, "A",5)
PintarRango("000000", 4, "Fila", 3, "A",6)
PintarRango("000000", 4, "Fila", 3, "A",22)
PintarRango("000000", 4, "Fila", 3, "A",23)
PintarRango("000000", 4, "Fila", 3, "A",24)
PintarRango("000000", 4, "Fila", 21, "A",4)
PintarRango("000000", 4, "Fila", 21, "A",5)
PintarRango("000000", 4, "Fila", 21, "A",6)

wb.save("Test.xlsx")
from openpyxl import Workbook
from openpyxl.styles import PatternFill

# Crear un nuevo libro de Excel y seleccionar la hoja activa
wb = Workbook()
ws = wb.active

# Aplicar color a la celda B2
columna = "B"
fila = 2
color = "000000"
ws.column_dimensions["B"].width = 3
for i in range(0,10):
    if i % 2 == 0:
        color = "FFFFFF"
    else: color = "000000"
    fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
    ws[columna+str(fila+i)].fill = fill

# Guardar el archivo
wb.save("QRGenerado.xlsx")

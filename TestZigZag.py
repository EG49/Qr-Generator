import openpyxl
from openpyxl.styles import PatternFill

# Crear un nuevo libro de Excel
wb = openpyxl.Workbook()
ws = wb.active

# Definir colores de relleno
blanco = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
negro = PatternFill(start_color="000000", end_color="000000", fill_type="solid")

# Alternador de color
alternar_color = True

# Lista de columnas desde Z a A
columnas = [chr(c) for c in range(ord('Z'), ord('A') - 1, -1)]

# Agrupar las columnas en pares para recorrer en zigzag
columnas_pares = [columnas[i:i+2] for i in range(0, len(columnas), 2)]

# Recorrer los pares de columnas
for par in columnas_pares:
    if len(par) == 2:
        col1, col2 = par[0], par[1]
    else:
        # Última columna sin pareja (en caso de número impar de columnas)
        col1, col2 = par[0], None

    # Alternar la dirección: subir o bajar
    if columnas.index(col1) % 2 == 0:
        fila_range = range(25, 0, -1)  # Subiendo
    else:
        fila_range = range(1, 26)      # Bajando

    # Rellenar celdas en el patrón zigzag
    for fila in fila_range:
        celda1 = f"{col1}{fila}"
        ws[celda1].fill = blanco if alternar_color else negro
        alternar_color = not alternar_color

        if col2:
            celda2 = f"{col2}{fila}"
            ws[celda2].fill = blanco if alternar_color else negro
            alternar_color = not alternar_color

# Guardar el archivo
wb.save("zigzag_completo_Z25_a_A1.xlsx")
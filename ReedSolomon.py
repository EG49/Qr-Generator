import reedsolo

# Inicializar el codificador
rs = reedsolo.RSCodec(10)  # 10 bytes de corrección

# Datos a codificar (como si fuera un pedazo de texto o URL)
datos = b"Hola Mundo!"

# Codificar con Reed-Solomon (agrega 10 bytes de corrección)
codificado = rs.encode(datos)

print("Codificado:", codificado)

# Ahora simulamos errores: cambiamos algunos bytes
import random

# Convertimos en lista para modificarla
dañado = bytearray(codificado)
dañado[0] ^= 0xFF  # Error 1
dañado[5] ^= 0xAA  # Error 2

print("Dañado:", bytes(dañado))

# Reed-Solomon puede corregirlo
decodificado = rs.decode(bytes(dañado))
print("Recuperado:", decodificado)
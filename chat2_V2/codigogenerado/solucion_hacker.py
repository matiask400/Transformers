def descifrar_nombre(nombre_codificado, desplazamiento):
  nombre_descifrado = ''
  for letra in nombre_codificado:
    codigo = (ord(letra) - ord('A') + desplazamiento) % 26
    letra_descifrada = chr(ord('A') + codigo)
    nombre_descifrado += letra_descifrada
  return nombre_descifrado

def descifrar_clave(clave_codificada):
  return str(int(clave_codificada, 2))

# desplazamiento = int(input())
desplazamiento = int(input("Desplazamiento: "))

while True:
  try:
    # nombre_codificado, clave_codificada = input().split()
    nombre_codificado, clave_codificada = input("Nombre y clave codificado: ").split(" ")
    nombre_descifrado = descifrar_nombre(nombre_codificado, desplazamiento)
    clave_descifrada = descifrar_clave(clave_codificada)
    print(nombre_descifrado, clave_descifrada)
  except EOFError:
    break

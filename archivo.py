def GEMINI_API_KEY():
    return "AIzaSyDGZZMpF52HDIwsTyzLhLdK9Uq78lJe-kU"
    
    def decodificar_nombre(cifrado, desplazamiento):
    nombre_decodificado = []
    for char in cifrado:
        if 'A' <= char <= 'Z':
            nueva_posicion = (ord(char) - ord('A') - desplazamiento) % 26
            nombre_decodificado.append(chr(nueva_posicion + ord('A')))
        else:
            nombre_decodificado.append(char)
    return ''.join(nombre_decodificado)

def decodificar_clave(binario):
    return str(int(binario, 2))

def decodificar_banco(p, cifrado, clave_binaria):
    nombre_decodificado = decodificar_nombre(cifrado, p)
    clave_decodificada = decodificar_clave(clave_binaria)
    return nombre_decodificado, clave_decodificada

# Ejemplo de uso
ejemplos = [
    (1, 'QBCMP', '001111101011101100000111'),
    (3, 'MXDQ', '001111101011101100000110'),
    (1, 'QFESP', '001111101011101011111100'),
]

for p, cifrado, clave_binaria in ejemplos:
    nombre, clave = decodificar_banco(p, cifrado, clave_binaria)
    print(f'{nombre} {clave}')
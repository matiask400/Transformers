def redondear_nota(nota):
    if nota < 38:
        return nota
    else:
        proximo_multiplo_5 = ((nota // 5) + 1) * 5
        if proximo_multiplo_5 - nota < 3:
            return proximo_multiplo_5
        else:
            return nota

# Leer la cantidad de notas
N = int(input("Ingrese la cantidad de notas: "))

# Leer cada una de las N notas
notas = []
for _ in range(N):
    nota = int(input())
    notas.append(nota)

# Aplicar el redondeo a cada nota y mostrar el resultado
print("*")
notas_redondeadas = [redondear_nota(nota) for nota in notas]

# Imprimir las notas redondeadas
for nota in notas_redondeadas:
    print(nota)
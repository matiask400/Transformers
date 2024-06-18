def redondear_nota(nota):
  """Redondea una nota según las reglas del profesor.

  Args:
    nota: La nota a redondear.

  Returns:
    La nota redondeada o la nota original si no se debe redondear.
  """

  if nota < 38:
    return nota

  proximo_multiplo_5 = (nota // 5 + 1) * 5
  if proximo_multiplo_5 - nota < 3:
    return proximo_multiplo_5
  else:
    return nota


def main():
  """Lee las notas de la entrada estándar y escribe las notas redondeadas en la salida estándar."""

  n = int(input())
  notas = []
  for _ in range(n):
    notas.append(int(input()))

  for nota in notas:
    print(redondear_nota(nota))


if __name__ == "__main__":
  main()

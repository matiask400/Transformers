def redondear_nota(nota):
  """Redondea una nota según las reglas del profesor.

  Args:
    nota: La nota a redondear.

  Returns:
    La nota redondeada.
  """
  if nota < 40:
    return nota
  elif nota < 38:
    return nota
  else:
    proximo_multiplo_5 = ((nota // 5) + 1) * 5
    if proximo_multiplo_5 - nota < 3:
      return proximo_multiplo_5
    else:
      return nota

# Lee la cantidad de notas
n = int(input())

# Lee las notas y las redondea
for _ in range(n):
  nota = int(input())
  nota_redondeada = redondear_nota(nota)
  print(nota_redondeada)

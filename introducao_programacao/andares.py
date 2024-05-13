lista_andares = [n for n in range(21) if n != 0]
lista_reverse = sorted(lista_andares)
lista_reverse.reverse()
def print_normal():
  for andar in lista_andares:
    if andar == 13:
      ...
    else:
      print(f"Andar número {andar}")

def print_ao_contrario():
  for andar in lista_reverse:
    if andar == 13:
      ...
    else:
      print(f"Andar número {andar}")

print_normal()
print("Nova lista")
print_ao_contrario()

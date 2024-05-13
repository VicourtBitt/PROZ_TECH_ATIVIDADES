nomes = ["Rafael", "Arturo", "Karen", "Julia"]


# A input to gather some name
name_input = input("Write something that you want to search: ")


# A function that should at least print if the element is inside the list
def find_value(name= str, array= list):
  find_it = False
  value = 0

  # This for searchs each index of the list.
  for i in range(len(array)):
    if array[i] == name:
      find_it = True
      value = i
      break
  
  # A simple if statement that see if the condition has been met or not.
  if not find_it:
    print("We cannot find this specific element. ")
  else:
    print(f"Yes, {name_input} is inside the list and is the index {i}.")


# Then we call the function
# find_value(name_input, nomes)


# Will search the name inside the list
def find_value_while(array= list):
  achou = False

  # While it meet the condition, continue looping
  while not achou:
    name_input = input("Escreva o nome que você quer procurar no array: ")

    for i in range(len(array)):
      if array[i] == name_input:
        achou = True
        value = i
        break
    
    if not achou:
      print(f"O nome {name_input} não está na lista.")
    else:
      print(f"O nome {name_input} está na lista e no index {i}.")

# find_value_while(nomes)

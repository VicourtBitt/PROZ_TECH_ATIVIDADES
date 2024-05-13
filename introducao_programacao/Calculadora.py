valor1 = input('Coloque um primeiro valor: ')
valor2 = input("Coloque um segundo valor: ")
interacao = input("Coloque o tipo de conta que deseja fazer: [X]-[/]-[+]-[-] ")

def calculadora(v1= valor1, v2= valor2, calc=interacao):
    if interacao not in ["X","/","+","-"]:
      return 0
    
    if interacao == "+":
       return float(v1) + float(v2)
    
    elif interacao == "-":
       return float(v1) - float(v2)
    
    elif interacao == "X":
       return float(v1) * float(v2)
    
    elif interacao == "/":
       return float(v1) / float(v2)
    
calc = calculadora

print(calc())

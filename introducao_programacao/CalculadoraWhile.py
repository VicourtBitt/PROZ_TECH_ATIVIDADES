def calculadora():
    lista_de_operadores = ["X","x","/","+","-","Sair","sair"]
    while True:
        valor1 = float(input("Primeiro número: "))
        if not isinstance(valor1, float):
            print("Primeiro valor não foi colocado da maneira certa.")
            continue

        valor2 = float(input("Segundo número: "))
        if not isinstance(valor2, float):
            print("Segundo valor não foi colocado da maneira certa.")
            continue

        operador = input("Operação [X]-[/]-[+]-[-] ou [Sair]")
        if operador not in lista_de_operadores:
            print("Essa opção não existe. ")
            continue
        else:
            if operador == "X" or operador == "x":
                print(valor1 * valor2)
            elif operador == "/":
                print(valor1 / valor2)
            elif operador == "+":
                print(valor1 + valor2)
            elif operador == "-":
                print(valor1 - valor2)
            else:
                return print("Você saiu do programa.")
                
calc = calculadora
print(calc())

import calculadora

def menu(a, b):
    while True:
        print("Menu Calculadora:")
        print("[1] Somar")
        print("[2] Subtrair")
        print("[3] Multiplicar")
        print("[4] Dividir")
        escolha = input("Digite o número da opção desejada: ")
        
        if escolha == "1":
            print(f'{a} + {b} = {calculadora.somar(a, b)}')
        elif escolha == "2":
            print(f'{a} - {b} = {calculadora.subtrair(a, b)}')
        elif escolha == "3":
            print(f'{a} * {b} = {calculadora.multiplicar(a, b)}')
        elif escolha == "4":
            print(f'{a} / {b} = {calculadora.dividir(a, b)}')

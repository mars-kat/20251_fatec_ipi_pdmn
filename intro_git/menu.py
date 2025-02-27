import calculadora

def menu(a, b):
    while True:
        print("Menu Calculadora:")
        print("[1] Somar")
        escolha = input("Digite o número da opção desejada: ")
        
        if escolha == '1':
            print(f'{a} + {b} = {calculadora.somar(a, b)}')

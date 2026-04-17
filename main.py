user_selection = input('Digite 1 para acessar e 2 para encerrar')
user_right_email = 'admin'
user_right_password = 1234
retry = 0
saldo = 193.94
limite = 100
diferenca = 0

#função para mostrar opções do menu
def print_menu():
    print("\n- UNIVILLE Internet Banking -")
    print("1. Consultar Saldo")
    print("2. Realizar Saque")
    print("3. Realizar Depósito")
    print("4. Consultar Limite")
    print("5. Encerrar")

if user_selection == '2':
    print("Encerrado")
    exit()
elif user_selection != '1':
    print("Opção inválida")
    exit()
else:

# Loop para login
    while retry < 3:
        user_email = str(input("Digite o seu e-mail: "))
        user_password = int(input("Digite a sua senha: "))
        if user_password == user_right_password and user_email == user_right_email:
            print("Senha válida")
            break
        else: 
            retry += 1
            print(f"Senha inválida, você tem mais {3 - retry} tentativas") 
        if retry == 3:
            print("Número de tentativas excedidas. Fim de programa.")
            exit()
    
    # Loop do menu principal
    while True:
        print_menu()
        user_selection_menu = input("Escolha uma opção: ")
        
        # Consulta de saldo 
        if user_selection_menu == '1':
            print(f"Saldo: R${saldo:.2f}")
            voltar = input("Escreva 1 para voltar: ")
            if voltar == '1':
                continue

        # Saque
        elif user_selection_menu == '2':
            saque = float(input("Digite o valor do saque: "))
            saldo -= saque
            if saldo + limite <= 0:
                print(f"Saldo insuficiente para realizar o saque, falta R${abs(saldo + limite):.2f} para completar o saque.")
            else:
                print("Saque realizado com sucesso")

        # Depósito
        elif user_selection_menu == '3':
            deposito = float(input("Digite o valor do depósito: "))
            if limite < 100:
                diferenca = 100 - limite  
                print(f"Limite total: {limite:.2f}")
                if deposito >= diferenca:
                    print(f"Depósito de R${deposito:.2f} completou o limite.")
                    limite = 100
                    saldo += deposito - diferenca 
                    print(f"Saldo atualizado: R${saldo:.2f}")
                else:
                    limite += deposito  
                    print(f"Limite atualizado: R${limite:.2f}")
            else:
                saldo += deposito
                print(f"Saldo atual: R${saldo:.2f}") 

            print("Depósito realizado com sucesso")

        # Consulta de limite
        elif user_selection_menu == '4':
            print(f"Limite: R${limite:.2f}") 

        # Encerrar
        elif user_selection_menu == '5':
            print("Encerrado")
            exit()
        else:
            print("Teste um número válido")
user_selection = input('Digite 1 para acessar e 2 para encerrar')
user_right_email = 'admin@admin'
user_right_password = 1234
retry = 0
saldo = 193.94
limite = 100.00

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
    user_email = str(input("Digite o seu e-mail: "))
    user_password = int(input("Digite a sua senha: "))

    while retry < 3:
        if user_password == user_right_password and user_email == user_right_email:
            print("Senha válida")
            break
        else: 
            retry += 1
            print(f"Senha inválida, você tem mais {3 - retry} tentativas") 
        if retry == 3:
            print("Número de tentativas excedidas. Fim de programa.")
            exit()
    print_menu()
    user_selection_menu = input("Escolha uma opção: ")
    
    if user_selection_menu == '1':
        print(f"Saldo: R${saldo:.2f}")
    elif user_selection_menu == '2':
        saque = float(input("Digite o valor do saque: "))
        saldo -= saque
        if saldo + limite <= 0:
            print("Saldo insuficiente para realizar o saque")
            
        else:
            exit()
        print("Saque realizado com sucesso")
    elif user_selection_menu == '3':
        print("Depósito realizado com sucesso")
    elif user_selection_menu == '4':
        print("Limite: R$100,00") 
    elif user_selection_menu == '5':
        print("Encerrado")
        exit()
    else:
        print("Teste um número válido")  

    
usuario_correto = "admin"
senha_correta = "1234"
saldo = 193.94
limite = 100.00


def menu_principal():
    """Exibe o menu de acesso principal"""
    print("\n- UNIVILLE Internet Banking -")
    print("1. Acessar")
    print("2. Encerrar")


def menu_conta():
    """Exibe o menu da conta após login"""
    print("\n- UNIVILLE Internet Banking -")
    print("1. Consultar Saldo")
    print("2. Realizar Saque")
    print("3. Realizar Depósito")
    print("4. Consultar Limite")
    print("5. Encerrar")


def fazer_login():
    """
    Realiza o login do usuário com limite de 3 tentativas.
    Retorna True se login bem-sucedido, False caso contrário.
    """
    tentativas_restantes = 3
    
    while tentativas_restantes > 0:
        usuario = input("Digite o seu usuário: ")
        senha = input("Digite a sua senha: ")
        
        if usuario == usuario_correto and senha == senha_correta:
            return True
        
        tentativas_restantes -= 1
        
        if tentativas_restantes > 0:
            print("Usuário e senha são inválidos.")
            print(f"Número de tentativas restantes: {tentativas_restantes}")
        else:
            print("Número de tentativas excedidas.")
            print("Fim de programa.")
    
    return False


def consultar_saldo(saldo_atual):
    """Exibe o saldo atual da conta"""
    print(f"\nSaldo R$: {saldo_atual:.2f}")

def consultar_limite(limite_atual):
    """Exibe o limite da conta"""
    print(f"\nLimite da Conta R$: {limite_atual:.2f}")


def realizar_saque(saldo_atual, limite_atual):
    """
    Realiza um saque da conta.
    O saque não pode exceder saldo + limite.
    Retorna o novo saldo.
    """
    valor_saque = float(input("Digite o valor do saque R$: "))
    
    # Validar se o valor é negativo
    if valor_saque < 0:
        print("Valor inválido.")
        return saldo_atual
    
    # Validar se há saldo suficiente (saldo + limite)
    saldo_disponivel = saldo_atual + limite_atual
    
    if valor_saque > saldo_disponivel:
        print("Saldo insuficiente.")
        return saldo_atual
    
    # Realizar o saque
    novo_saldo = saldo_atual - valor_saque
    print(f"Saque realizado com sucesso!")
    return novo_saldo


def realizar_deposito(saldo_atual):
    """
    Realiza um depósito na conta.
    O depósito deve ser um valor positivo.
    Retorna o novo saldo.
    """
    valor_deposito = float(input("Digite o valor do depósito R$: "))
    
    # Validar se o valor é negativo ou zero
    if valor_deposito <= 0:
        print("Valor inválido.")
        return saldo_atual
    
    # Realizar o depósito
    novo_saldo = saldo_atual + valor_deposito
    print(f"Depósito realizado com sucesso!")
    return novo_saldo


def main():
    """Função principal que controla o fluxo do programa"""
    global saldo
    
    while True:
        menu_principal()
        opcao = input("Digite a opção Desejada: ")
        
        if opcao == "2":
            print("Encerrado")
            break
        
        elif opcao == "1":
            # Fazer login
            if fazer_login():
                # Menu da conta
                while True:
                    menu_conta()
                    opcao_conta = input("Digite a opção Desejada: ")
                    
                    if opcao_conta == "1":
                        consultar_saldo(saldo)
                    
                    elif opcao_conta == "2":
                        saldo = realizar_saque(saldo, limite)
                    
                    elif opcao_conta == "3":
                        saldo = realizar_deposito(saldo)
                    
                    elif opcao_conta == "4":
                        consultar_limite(limite)
                    
                    elif opcao_conta == "5":
                        print("Sessão encerrada.")
                        break
                    
                    else:
                        print("Opção inválida. Tente novamente.")
        
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
    
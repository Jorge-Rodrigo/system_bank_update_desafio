def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Deposito Realizado com sucesso")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def saque(*,saldo,valor,extrato,limite,numero_saques,limimtes_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limimtes_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        numero_saques += 1
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        print("Saque Realizado com sucesso")

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o cpf do usuario:")
    filtro_usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf] 
    usuario = filtro_usuario[0] if filtro_usuario else None

    if usuario:
        print("Ja existe um usuario com esse cpf!")
        return
    
    nome = input("Informe o nome:")
    data_de_nascimento = input("Informe a data de nascimento:")
    endereco = input("Informe o endereço:")

    usuarios.append({"nome": nome,"data_de_nascimento":data_de_nascimento,"cpf":cpf,"endereco":endereco})
    print("Usuario criado com sucesso")

def criar_conta(agencia, numero_conta,usuarios,contas):
    cpf = input("Informe o usuario:")
    filtro_usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    usuario = filtro_usuario[0] if filtro_usuario else None

    if usuario is None:
        print("Usuario não encontrado")
        return

    contas.append({"agencia": agencia,"numero_conta":numero_conta, "usuario":usuario})
    print("Sua conta foi criada")

def listar(contas):
    for conta in contas:
        print("\n================ Conta ================")
        print(f"Agencia: {conta['agencia']}")
        print(f"Numero da conta: {conta['numero_conta']}")
        print(f"Usuario: {conta['usuario']['nome']}")
        print("==========================================")

def main():
    LIMIMTE_SAQUES = 3
    AGENCIA = "0001"
    menu = ""

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do deposito:"))

            saldo, extrato = deposito(saldo,valor,extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque:"))

            saldo, extrato, numero_saques = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limimtes_saques=LIMIMTE_SAQUES
            )
        elif opcao == "e":
            mostrar_extrato(saldo, extrato=extrato)
        elif opcao == "u":
            criar_usuario(usuarios)
        elif opcao == "c":
            total_contas = len(contas)
            numero_conta = total_contas + 1

            criar_conta(AGENCIA,numero_conta,usuarios,contas)
        elif opcao == "l":
            listar(contas)
        elif opcao == "q":
            break


main()
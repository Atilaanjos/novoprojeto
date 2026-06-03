def ler_int(mensagem):
    try:
        return int(input(mensagem))
    except ValueError:
        return None


def mostrar_menu():
    print("loja dos anjos")
    print("0- sair")
    print("1- camisa - R$50,00")
    print("2- calça - R$80,00")
    print("3- sapato - R$120,00")
    print("4- acessorios - R$30,00")


def selecionar_produto():
    mostrar_menu()
    opc = ler_int("Digite a opção desejada: ")

    if opc == 0:
        return None, None

    produtos = {
        1: ("camisa", 50.00),
        2: ("calça", 80.00),
        3: ("sapato", 120.00),
        4: ("acessorios", 30.00),
    }

    return produtos.get(opc, (None, None))


def escolher_metodo_pagamento():
    print("Escolha o método de pagamento:")
    print("1- Cartão")
    print("2- Pix")
    print("3- Dinheiro")

    metodo = ler_int("Digite o número do método de pagamento: ")

    if metodo == 1:
        parcelas = ler_int("Digite a quantidade de parcelas: ")
        if parcelas is None or parcelas < 1:
            return None, None, None
        return "Cartão", parcelas, 0.0
    if metodo == 2:
        return "Pix", 1, 0.10
    if metodo == 3:
        return "Dinheiro", 1, 0.10

    return None, None, None


def calcular_valor_final(preco, pagamento, parcelas, desconto):
    juros = 0.0
    if pagamento == "Cartão" and parcelas > 10:
        juros = 0.02

    if desconto > 0:
        return preco * (1 - desconto), desconto, juros

    return preco * (1 + juros), desconto, juros


def processar_compra():
    produto, preco = selecionar_produto()
    if produto is None:
        print("Obrigado pela visita!")
        return False

    pagamento, parcelas, desconto = escolher_metodo_pagamento()
    if pagamento is None:
        print("Método de pagamento inválido. Por favor, tente novamente.\n")
        return True

    valor_final, desconto_aplicado, juros_aplicado = calcular_valor_final(
        preco, pagamento, parcelas, desconto
    )

    if pagamento == "Cartão":
        print(f"Você comprou {produto} por R${preco:.2f} em {parcelas}x no cartão.")
        if juros_aplicado > 0:
            print("Foi aplicado juros de 2% por parcelar acima de 10 vezes.")
    else:
        print(f"Você comprou {produto} por R${preco:.2f} e pagará com {pagamento}.")
        print("Foi aplicado 10% de desconto.")

    print(f"Valor final: R${valor_final:.2f}\n")

    continuar = input("Deseja voltar ao menu principal? (s/n): ")
    if continuar.lower() != "s":
        print("Obrigado pela compra!")
        return False

    print()
    return True


def main():
    while True:
        continuar = processar_compra()
        if not continuar:
            break


if __name__ == "__main__":
    main()


def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Erro: divisão por zero"

# Função para exibir o menu da calculadora
def exibir_menu():
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

# Loop principal da calculadora
while True:
    exibir_menu()
    opcao = int(input("Digite o número da operação desejada: "))

    if opcao == 5:
        print("Calculadora encerrada.")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        resultado = adicao(num1, num2)
        print("Resultado: ", resultado)
    elif opcao == 2:
        resultado = subtracao(num1, num2)
        print("Resultado: ", resultado)
    elif opcao == 3:
        resultado = multiplicacao(num1, num2)
        print("Resultado: ", resultado)
    elif opcao == 4:
        resultado = divisao(num1, num2)
        print("Resultado: ", resultado)
    else:
        print("Opção inválida. Tente novamente.\n")

# Loop até que o jogador 1 escolha um número inteiro entre 1 e 10
while True:
    try:
        numero_secreto = int(input("Jogador 1, escolha um número inteiro entre 1 e 10: "))
        if 1 <= numero_secreto <= 10:
            break
        else:
            print("Número inválido. Por favor, escolha um número inteiro entre 1 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro válido.")

print("Jogador 1 escolheu um número. Tente adivinhar!")

# Loop até que o jogador 2 adivinhe corretamente
chances= 0
while True:
    # Jogador 2 tenta adivinhar o número
    while True:
        try:
            tentativa = int(input("Jogador 2, insira um número inteiro entre 1 e 10: "))
            if 1 <= tentativa <= 10:
                break
            else:
                print("Número inválido. Por favor, insira um número inteiro entre 1 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro válido.")
            
    # Verifica se a tentativa está correta
    if tentativa == numero_secreto:
        chances += 1
        print("Parabéns! Você acertou o número!")
        print("O número de tentativas foi", chances)
        break
    else:
        print("Você errou. Tente novamente.")
        chances += 1

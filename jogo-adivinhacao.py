j01= int(input("Escolha um número de 1 a 10: \n"))



#Verificação de numero para o j01:

#while (j01>10) or (j01<1):
   # print("Numero invalido, digite novamente")
  #  j01= int(input("Escolha um número de 1 a 10: \n"))

j02= int
chance= 0


while j02 != j01:
    print("j02 advinhe o número entre 1 e 10:")
    j02=int(input("Insira o numero: \n"))
    chance += 1
    if (j02 == j01):
        print ("Você acertou!")
        print ("O número de tentativas foi", chance)


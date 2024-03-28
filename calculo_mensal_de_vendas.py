soma = 0
#tamanho = int(input("digite o tamanho do for: "))
for vendas in range (0, 12 ,+1):
    vendas += 1
    tvm= int(input(f"Digite o valor de vendas do {vendas}º mês:"))
    soma= tvm + soma
print(soma)

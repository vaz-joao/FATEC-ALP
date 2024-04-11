#Atribuição de valores 
KM= float(input("Insira a quilometragem percorrida:"))
L= float(input("Insira a quantidade de litros gastos:"))

#Calculo do consumo
consumo= KM/L

#Mostra resultado do calculo
print(f"O consumo do seu carro é de {consumo}KM/L")

#Atribuição de condição(Verdadeiro ou falso)
if consumo <= 8:
    print ("O consumo do seu veículo está alto")
else:
    print ("O consumo do seu veículo está bom")

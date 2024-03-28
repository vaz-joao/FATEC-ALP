#Declarar as variaveis

P1= float(input("Inseir a primeira nota:"))

P2= float(input("Inserir a segunda nota:"))
#Declarar a média 

media= (P1+P2)/2
#Mostrar o resultado

print ("Sua nota é:", media)
#Para incrementar um valor a um print, usar a "," 

#Mostrar se passou ou não

if media >= 6 or 10:
    print( "Atingiu a meta")
else:
    print("Não atingiu a meta")

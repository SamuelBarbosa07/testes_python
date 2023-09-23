#numero = int(input ("Escolha um numero maximo para ser imprimido:"))
#for numero in range (numero):
 #   print (numero + 1)






maximo = int(input("Qual o numero maximo: "))
ordem = input("Qual a ordem que deseja imprimir os numeros (C/D): ")

if ordem == 'C':
    for numero in range(1, maximo + 1):
        print(numero)
elif ordem == 'D':
    for numero in range(maximo, 0, - 1):
        print(numero)
else:
    print("Ordem inválida!")

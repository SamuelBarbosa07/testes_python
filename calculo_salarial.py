salario = float(input("Insira seu salario:"))
tempo_de_serviço = float(input("Inaira seu tempo de serviço:"))

total = 0
if tempo_de_serviço > 5:
    total = salario * 1.05
else:
    total = salario

if (total > salario):
    print(f"seu novo salario é de {total}")
else:
    print(f"Seu salario permanece o mesmo")
    




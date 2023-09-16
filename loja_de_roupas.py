# Uma loja de roupas precisa de um programa que ajude a calcular o valor final da venda de produtos.
# Existem algumas regras que precisam ser respeitadas na venda de um produto:
 
# 1 – A vista – 10% de desconto, caso o valor da venda seja maior que 500 15%, caso seja maior que 1000, 20% de desconto;
# 2 – A prazo – A venda pode ser parcelada em até 18x. Caso seja parcelado em mais do que 10x possui juros:
# Apenas compras com mais de 800 reais podem ser parceladas acima de 5x;


compra = float(input("Informe o valor da compra:"))
forma_pagamento = input("O pagamento sera a vista ou a prazo?")
if compra >500:
   resultado = compra * 15 / 100
print (f"seu desconto sera de {resultado}")

'''
Tendo como base o valor da cotação do dólar (em reais) do dia, faça a conversão de um valor em dólares para reais.
'''
valor_cotação= float(input("Digite o valor da cotação do dolar:"))
valor_dolar=float(input("Digite o valor em dolares:"))

valor_reais= valor_cotação*valor_dolar

print(f"USD {valor_reais} convertido em reais")

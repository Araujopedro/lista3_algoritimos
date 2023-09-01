'''
· Crie um algoritmo que solicite ao usuário seu consumo de energia elétrica (em kWh), que deve ser uma variável real. O
 algoritmo deve, então, calcular o total da conta, considerando que cada kWh custa R$ 0,20.
'''
consumo_kwh=float(input("Digite o consumo em Kwh:"))

total_conta= (consumo_kwh*0.20)
print(f"Valor total da conta é {total_conta}")

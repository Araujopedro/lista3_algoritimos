'''
Faça um algoritmo que leia a idade de uma pessoa expressa em anos,
 meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias
'''
idade_dias=int(input("qual sua idade em dias:"))
idade_meses=int(input("qual sua idade meses:"))
idade_anos= int(input("qual sua idade em anos:"))



VlrT=int(idade_anos*365)+(idade_meses*30)+idade_dias

print(f"sua idade é de {VlrT} dias")

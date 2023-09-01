'''
Dada a quilometragem parcial de um carro e a quantidade de litros
gastos ele para percorrer esta quilometragem, fazer um algoritmo que calcule quantos Km/l o carro percorreu.
'''
kmPer= float(input("Digite a qilometragem percorrida:"))
Lgast= float(input("quantos litros foram gastos:"))

autonomia= kmPer/Lgast

print(f"a autonomia é de {autonomia}")

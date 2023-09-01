"""
Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos,
nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitore
"""

votoB=int(input("digite o numero total de votos brancos no municipio:"))
votoN=int(input("digite o numero total de votos nulos no municipio:"))
vv=int(input("digite o numero total de votos validos no municipio:"))
morad=(votoB+votoN+vv)

percemb=votoB * 100/morad
percemN=votoN*100/morad
percemvv=vv*100/morad

print(f"o valor de votos validos é de {percemvv:.2f} %")
print(f"o valor de votos nulos é de {percemN:.2f} %")
print(f"o valor de votos brancos é de {percemb:.2f} %")





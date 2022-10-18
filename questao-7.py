from ctypes.wintypes import PINT
import os
idade = 0
idade50 = 0
idade1020 = 0
somaAltura = 0
alturaEntre10e20 = 0
peso40 = 0

qntCad = int(input("Digite a quantidade de cadastros: "))
for n in range(1,qntCad + 1):
    print(f"{n}ª pessoa: ")
    idade = int(input("Informe idade: "))
    altura = float(input("Informe altura: "))
    peso = float(input("Informe peso: "))
    os.system("cls")
    if idade > 50:
        idade50 += 1
    elif idade >=10 and idade <=20:
        somaAltura += altura 
        alturaEntre10e20 += 1
    elif peso < 40:
        peso40 += 1

print(f"Existem {idade50} com idade acima de 50 anos")
if alturaEntre10e20 <=0:
    print("Não existe pessoas com média de alura entre 10 e 20 anos:")
else:
    print(f"A média das alturas com pessoas entre 10 e 20 anos é: {somaAltura/alturaEntre10e20:.2f}")
print(f"Porcentagem de pessoas que tm o peso inferior de 40kg é: {peso40/qntCad*100:.2f}%")

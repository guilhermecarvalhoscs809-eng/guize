Nome= input("Qual é o seu nome?")
print ( "Seu nome é",Nome)
idade = int(input ("qual é a sua idade?  "))
if idade <13:
    print ("você é uma criança,não pode entar.")
elif idade <18:
    print ("você é adolescente, não pode entrar.")
elif idade <66:
    print ("você é adulto, pode entrar.")
elif idade ==67:
    print ("SIX SEVEN")
else:
    print("Você é idoso,pode entrar mas com cuidado.")
import random
numero1 = random.randint(1, 5)
numero = int(input("Adivinhe o numero que eu estou pensando de 1 a 5."))
while numero < 1 or numero > 5:
    print("Número inválido! Escolha entre 1 e 5.")
    numero = int(input("Digite novamente: "))
if numero != numero1:
    print("és burro")
    print("o numero era",numero1)
else:
    print ("ta de hack né")
nasceu= 2026-idade
nasceu1 = nasceu - 1
print ("o numero é",numero1)
print ("seu nome é",Nome)
print ("tu nasceu em",nasceu)
print ("ou em",nasceu1)
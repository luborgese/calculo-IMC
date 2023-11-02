# Calculo IMC - Índice de Massa Corporal

# Menor que 18,5      MAGREZA
# Entre 18,5 e 24,9   NORMAL
# Entre 25,0 e 29,9   SOBREPESO
# Entre 30,0 e 39,9   OBESIDADE
# Maior que 40        OBESIDADE GRAVE

altura = float(input ('Qual é a sua Altura em cm: '))
peso = float(input ('Qual é o seu peso em kg: '))

IMC = peso / (altura/100)**2 

if IMC < 18.5:
    print('MAGREZA')
elif IMC >= 18.5 and IMC < 24.9:
    print('NORMAL')
elif IMC >= 25.0 and IMC < 29.9:
    print('SOBREPESO')
elif IMC >= 30.0 and IMC < 39.9:
    print('OBESIDADE')
else:
    print('OBESIDADE GRAVE')
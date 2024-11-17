# Desafio
CONSTANTE_BONUS = 1000

nome = input('Digite seu nome: ')

salario = round(float(input('Digite seu salario: ')),2)

bonus = round(float(input('Digite o bonus: ')),2)

resultado_b = CONSTANTE_BONUS + round(salario * (bonus),2)

print(f'Ola {nome}, tudo bem? \n Seu salário é R${salario} e com o percentual de {bonus}% o se bonus é R${resultado_b}')
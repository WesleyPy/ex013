salario = float(input('Qual o salário do funcionário? R$'))
novo = salario + (salario * 15 / 100)
print ('O funcionário que recebia {:.2f}R$, vai receber {:.2f}R$ com o aumento de 15%.'.format(salario, novo))
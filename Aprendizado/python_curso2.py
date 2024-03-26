                    #CONDIÇÕES ANINHADAS
  #Ex > carro.siga()
#if carro.esquerda():       
   #condições
#elif(se não) carro.direita(): 
    #condições 
#else: 
    #condições

'''#OBS > elif pode ser usado quantas 
vezes quiser no if, já o else apenas 1 vez ou nenhuma'''

#nome = str(input('Qual é seu nome? ')).strip().lower()
#if nome == 'diogo':
#    print('Que nome bonito!!')
#elif nome == 'vanessa' or nome == 'pedro' or nome == 'christina':
#    print('Seu nome é bem popular no brasil!')
#elif nome == 'rosa' or nome == 'cibelle' or nome  == 'chagas':
#    print('Que nome interessante!')
#else:
#   print('Seu nome é bem normal.')
#print('Tenha um bom dia, {}'.format(nome.title()))

                #ATIVIDADES
import time
cores = {'azul':'\033[34m',
        'verde':'\033[32m',
        'vermelho':'\033[31m',
        'amarelo':'\033[33m'}
valor = float(input('{}Digite aqui o valor da casa R$ '.format(cores['amarelo'])))
salario = float(input('{}Digite aqui seu salário R$: '.format(cores['amarelo'])))
anos = int(input('{}Digite aqui em quantos anos deseja pagar: '.format(cores['amarelo'])))
print('-=-'*20)
print('{}Analisando dados...'.format(cores['azul']))
print('\033[0;1;33m-=-'*20)
time.sleep(3)
mensal = valor / (anos * 12)
s1 = salario * (30/100)
if mensal > s1:
   print('{}Você não esta apto para este empréstimo\n o valor da parcela é R$ {:.2f} e execede 30% o valor do seu salário.'.format(cores['vermelho'],mensal))
else:
   print('{}Você esta apto para esse empréstimo.\nO valor das parcelas será R${:.2f}. {}PARABÉNS!!'.format(cores['azul'],mensal, cores['verde']))

#numero = int(input('Digite um número: '))
#decimal = numero * 0.01
#print(decimal)


#num = int(input('Digite um número inteiro: '))
#print('''Escola uma das bases para conversão: 
#[ 1 ] converter para BINÁRIO
#[ 2 ] converter para OCTAL
#[ 3 ] converter para HEXADECIMAL''')
#op = int(input('Sua opção: '))
#if op == 1:
#    print('{} Convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
#elif op == 2:
#    print('{} Convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
#elif op == 3:
#    print('{} Convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
#else:
#    print('Opção invalida, tente novamente')



#n1 = int(input('Primeiro valor: '))
#n2 = int(input('Segundo valor: '))
#if n1 > n2:
#    print('O primeiro valor {} é maior que {}.'.format(n1,n2))
#elif n2 > n1:
#    print('O segundo valor {} é maior que {}.'.format(n2,n1))
#else:
 #   print('Não existe valor maior, o valor {} é igual ao valor {}.'.format(n1,n2))

#from datetime import date
#nome = str(input('Informe seu nome: ')).strip()
#nasc = int(input('Informe seu ano de nascimento : '))
#ano = date.today().year
#idade =  ano - nasc
#print('''Informe seu sexo abaixo
#[ 1 ] HOMEM
#[ 0 ] MULHER''')
#sexo = int(input('Sua escolha: '))

#if idade < 18:
#    print('Bom dia {}. Ainda faltam {} ano(s) para você se alistar. '.format(nome, 18 - idade))
    #print('Você terá que se alistar em {}'.format(ano + saldo))
#elif sexo == 0:
#    print('Bom dia {}. Você não está apta para alistamento militar devido ao seu sexo.'.format(nome))
#elif idade == 18:
#    print('bom dia {}. Já está na hora de você se alistar.'.format(nome))
#else:
 #   saldo = idade - 18
 #   print('Bom dia {}. Você ja passou do prazo de alistamento militar\nSeu alistamento foi a {} anos atrás em {}.'.format(nome, idade - 18,ano - saldo))

#import time
#cores = {'Vermelho': '\033[031m',
#         'verde': '\033[32m',
#         'azul': '\033[34m',
#         'amarelo':'\033[33m'}
#n1 = float(input('Qual foi sua primeira nota: '))
#n2 = float(input('Qual foi sua segunda nota: '))
#print('{}Calculando...'.format(cores['azul']))
#time.sleep(3)
#media =  (n1 + n2) / 2
#if media < 5:
#    print('Sua média foi {:.1f} e você está {}REPROVADO.'.format(media,cores['Vermelho']))
#elif media >= 5 and media <=6.9:
#    print('Sua média foi {:.1f} e você está de {}RECUPERAÇÃO.'.format(media,cores['amarelo']))
#else:
#    print('Sua média foi {:.1f}. {} PARABÉNS VOCÊ ESTA APROVADO !!!'.format(media,cores['verde']))
#from datetime import date
#idade = int(input('Informe o ano em que você nasceu: '))
#ano = 2024 - idade
#atual = date.today().year
#print('Quem nasceu em {} em {} ira disputar a categoria:'.format(idade,atual))
#if ano <= 9:
#    print('mirim.')
#elif ano > 9 and ano <= 14:
#    print('infantil.')
#elif ano > 14 and ano <= 19:
#    print('junior.')
#elif ano > 19 and ano <= 25:
#    print('Sênior.')
#else:
#    print('Master.')


#a1 = float(input('Informe a medida da reta A. cm: '))
#a2 = float(input('Informe a medida da reta B. cm: '))
#a3 = float(input('Informe a medida da reta C. cm: '))
#if a1 < a2 + a3 and a2 <1 a1 + a3 and a3 < a1 + a2:
#    print('Com os valores informados é possivel formar um triângulo.')
#    if a1 == a2 == a3:
#        print('Esse triângulo será Equilátero.')
#    elif a1 != a2 != a3 != a1:
#        print('Esse triãngulo será Escaleno.')
#    else:
#        print('Esse triângulo será Isósceles.')
#else:
#    print('Não é possivel formar um triângulo.')
  

#alt = float(input('Informe sua altura(m): '))
#peso = float(input('Informe seu peso (kg): '))
#imc = peso / (alt**2)
#print('O seu IMC é : {:.1f}'.format(imc))
#if imc <=18.5:
#    print('Você está abaixo do peso ideal.')
#elif imc >18.5 and imc <=25:
#    print('Você está no peso ideal.')
#elif imc >25 and imc <= 30:
#    print('Você está sobrepeso')
#elif imc >30 and imc <= 40:
#    print('Você está com obesidade.')
#else:
#    print('Você está com obesidade mórbida.')


#from time import sleep
#print('{:=^40}'.format(' LOJAS GUANABARA '))
#preço = float(input('Informe o preço do produto (R$): '))
#print('''Informe o método de pagamento.
#[ 1 ] À vista a no dinheiro/cheque.
#[ 2 ] À vista no cartão.
#[ 3 ] 2X no cartão com sem juros
#[ 4 ] 3x ou mais no cartão 20% de juros''')
#esc = int(input('Qual é a opção? '))
#if esc == 1:
#   total = preço - preço * (10/100) 
#elif esc == 2:
#        total = preço - preço * (5/100)
#elif esc == 3:
#        total = preço
#        parcela = total / 2
#        print('Sua compra será parcelada em 2x de R${}'.format(parcela))
#elif esc == 4:
#      total = preço + (preço * 20 / 100)
#      totalpar = int(input('Quantas parcelas? '))
#      parcela = total / totalpar
#      print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalpar, parcela))
#else:
#      total = preço
#      print('Opção invalida, tente novamente!')
#print('Sua compra no valor de R${:.2f} será R${} no final'.format(preço, total))


# from time import sleep
# from random import randint
# lista = ('PEDRA','PAPEL', 'TESOURA')
# computador = randint(0 , 2)
# print('''Suas opções
# [ 0 ] PEDRA
# [ 1 ] PAPEL
# [ 2 ] TESOURA''')
# jogador = int(input('Qual sua jogada? '))
# print('JO')
# sleep(1)
# print('KEN')
# sleep(2)
# print('PO!!')
# print('-=-'*10)
# print('O computador jogou {}'.format(lista[computador]))
# print('O jogador jogou {}'.format(lista[jogador]))
# print('-=-'*10)
# if computador == 0:
#     if jogador == 0:
#         print('EMPATE')
#     elif jogador == 1:
#         print('JOGADOR VENCE')
#     elif jogador == 2:
#         print('COMPUTADOR VENCE')
#     else:
#         print('JOGADA INVALIDA')

# elif computador == 1:
#     if jogador == 0:
#         print('COMPUTADOR VENCE')
#     elif jogador == 1:
#         print('EMPATE')
#     elif jogador == 2:
#         print('JOGADOR VENCE')
#     else:
#         print('JOGADA INVALIDA')
# elif computador == 2:
#     if jogador == 0:
#         print('JOGADOR VENCE')
#     elif jogador == 1:
#         print('COMPUTADOR VENCE')
#     elif jogador == 2:
#         print('EMPATE')
#     else:
#         print('JOGADA INVALIDA')

        #ESTRUTURA DE REPETIÇÃO 'FOR'

# for c in range (1,10):  #fazer o computador no intervalo entre 1,10. Onde 'c' é a variavel
#     pass
# pega

# for andar in range(0,3):
#     if moeda:
#         pega
#     passo
#     pula
# passo 
# pega

# n = int(input('Inicio: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
# for c in range(n,f+1,p):
#     print(c)
# print('fim')

# s = 0
# for c in range(0,4):
#     n = int(input('Digite um valor: 4'))
#     s += n 
# print('O somatório desses valores é igual a: {}'.format(s))


# from time import sleep
# print('A contagem ja vai começar')
# for c in range(10,-1, -1):
#     sleep(0.1)
#     print(c)




# for c in range(1,50+1):
#     if c % 2 == 0:
#         print(c, end=' ')



# soma = 0
# cont = 0
# for c in range(1,501, 2):
#     if  c % 3 == 0:
#             cont = cont + 1
#             soma = soma + c
# print(soma, cont)
           #TABUADA 
#num = int(input('Digite um número e veja sua tabuada: '))
#for c in range(1,11):
#    print('{} x {:2} = {}'.format(num,c,num*c))

# soma = 0
# cont = 0
# for c in range(6):
#     n = int(input('Digite um número inteiro: '))
#     if n % 2 == 0:
#         soma = soma + n
#         cont = cont + 1

# print('Esse progama considera apenas os números pares que são {}\nlogo a soma desses números é igual a: {}'.format(cont,soma))
        #PROGRESSÃO ARITMETRICA (PA)
# n = 0
# p1 = int(input('Primeiro termo: '))
# sg = int(input('Segundo termo: '))
# decimo = p1 + (10-1) * sg
# for c in range(p1,decimo+sg,sg):
#     print('{}'.format(c), end =' >> ')
# print('Acabou!!')


# cores = {'amarelo': '\033[33m',
#          'vermelho': '\033[31m0',
#          'verde':'\033[32m'}

# cont = 0
# num = int(input('Digite um número inteiro: '))
# tot = 0
# for c in range(1,num + 1):
#     if num % c == 0:
#         print('\033[32m', end = ' ')
#         tot += 1
#     else:
#         print('\033[31m', end = ' ')
    
#     print('{}'.format(c), end = ' ')
# print('\n\033O número {} foi divisível {} vezes'.format(num,tot))
# if tot == 2:
#     print('\033[32mLogo ele será primo.')
# else:
#     print('\033[31mLogo ele não será primo.')


# frase = str(input('Digite uma frase: ')).strip().upper()
# palavras = frase.split()
# junto = ''.join(palavras)
# inverso = junto[::-1]
# # for letra in range(len(junto) - 1, -1, -1):
# #     inverso += junto[letra]
# print('O inverso de {} é {}'.format(junto,inverso))
# if inverso == junto:
#     print('Temos um palíndromo')
# else:
#     print('A frase não é um palíndromo')


# from datetime import date
# atual = date.today().year
# totmaior = 0
# totmenor = 0
# for pess in range(1,8):
#     nasc = int(input('Em que ano a {}º pessoa naceu? '.format(pess)))
#     idade = atual - nasc    
#     if idade >= 21:
#         totmaior += 1
#     else:
#         totmenor += 1
# print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
# print('Ao todo tivemos {} pessoas de menor.'.format(totmenor))


# maior = 0
# menor = 0
# for p in range(1,6):
#     peso = float(input('Pesso da {}ª pessoa (Kg): '.format(p)))
#     if p == 1:
#         maior = peso
#         menor = peso
#     else:
#         if peso > maior:
#             maior = peso
#         if peso < menor:
#             menor = peso
# print('O maior peso lido foi {}Kg'.format(maior))
# print('O menor peso lido foi de {}Kg'.format(menor))


# media = 0
# maior = 0
# menor = 0
# media1 = 0
# nomev = ''
# m = 0
# for a in range(1,5):
    
#     print('------- {}º PESSOA -------'.format(a))
#     nome = str(input('Nome: ')).strip()
#     idade = int(input('Idade: '))
#     sexo = str(input('Sexo [M/F]: ')).upper().strip()
#     media += idade
#     if a == 1 and sexo in 'Mm':
#         maior = idade
#         nomev = idade
#     if sexo in 'Mm' and idade > maior:
#         maior = idade
#         nomev = nome
#     if sexo in 'Fm' and idade > 20:
#         m += 1
# media1 = media / 4
    

# print('A média de idade do grupo é de {} anos.'.format(media1))            
# print('O homem mais velho tem {} anos e se chama {}.'.format(maior,nomev))
# print('Ao todo são {} mulheres com menos de 20 anos.'.format(m))

#================================================================================
#                          ESTRUTURA DE REPETIÇÃO WHILE

# Enquanto não: 
#     pass
# pega

# while not apple:
#     if chão:
#         pass
#     if buraco:
#         pula

#     if moeada:
#         pega
# pega

# r = 'S'
# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar ? [S/N]: ')).upper()
# print('fim')


# sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
# while sexo not in 'MF':
#     sexo = str(input('Dados invalidos. Por favor informe seu sexo: ')).strip().upper()[0]
# print('Sexo {} registrado com sucesso.'.format(sexo))

# from random import randint
# print('So seu computador...')
# print('Acabei de pensar em um numero entre 0 e 10.')
# print('Será que você consegue adivinhar?')
# computador =  randint(0,10)
# acertou = False
# palpite = 0
# while not acertou:
#     jogador = int(input('Qual é seu palpite? '))
#     palpite += 1
#     if jogador == computador:
#        acertou = True
#     else: 
#         if jogador < computador:
#             print('Mais... Tente mais uma vez.')
#         elif jogador > computador:
#             print('Menos... Tente mais uma vez.')
# print('Acertou com {} tentativas. Parabéns '.format(palpite))


# p1 = float(input('Primeiro valor: '))
# p2 = float(input('Segundo valor: '))

# somar = 1  
# mult = 2 
# maior = 3
# nv = 4
# sair = False
# op = 0

# while op != 5:
#     print('[ 1 ] Somar\n[ 2 ] multiplicar\n[ 3 ] Maior\n[ 4 ] novos números\n[ 5 ] Sair')
#     op = int(input('>>> Qual sua opção? '))
#     if op == 1:
#             s = p1+p2
#             print('A soma entre {:.0f} + {:.0f} é {:.0f}'.format(p1,p2,s))
#             print('-=-==-='*10)
#     elif op == 2:
#             m = p1 * p2
#             print('A multiplicação entre {:.0f} x {:.0f} é {:.0f}'.format(p1,p2,m))
#             print('-=-==-='*10)
#     elif op == 3:
#         if p1 > p2:
#              maior = p1
#         else:
#              maior = p2
#         print('Entre {:.0f} e {:.0f} o maior valor é {:.0f}'.format(p1,p2,maior))
#     elif op == 4:
#         print('Informe os números novamente')
#         p1 = int(input('Primeiro valor: '))
#         p2 = int(input('Segundo valor: '))
#     elif op == 5:
#         print('Finalizando...')
#     else: 
#          print('Opção invalida, tente novamente')
#     print('=-='*10)



# n = int(input('Digite um número para calcular seu fatorial: '))
# contador = n
# f = 1
# print('Calculando {}!'.format(n), end = ' ')
# while contador > 0:
#     print('{}'.format(contador), end =' ')
#     print(' x ' if contador > 1 else ' = ', end = ' ')
#     f *= contador
#     contador -= 1
# print('{}'.format(f))

# n = int(input('Digite um número para calcular seu fatorial: '))
# contador = n
# f = 1
# for n in range(0,n):
#     print('{}'.format(contador), end = ' ')
#     print(' x 'if contador > 1 else ' = ', end = ' ')
#     f *= contador
#     contador -= 1
# print('{}'.format(f))

                        #Gerador de PA
# print('Gerador de PA')
# print ('-=-==-'*7)
# p1 = int(input('Primeiro termo: '))
# rz = int(input('Razão da PA: '))
# termo = p1
# contador = 1
# total = 0
# mais = 10
# while mais != 0:
#     total = total + mais
#     while contador <= total:
#         print('{} >>> '.format(termo), end = '')
#         termo += rz
#         contador += 1
#     print('PAUSA')
#     mais = int(input('Quantos termos você quer mostrar a mais? '))
# print('PA finalizada com {} termosmostrados.'.format(total))

                        #Sequencia de fibonacci   
# print('-'*20)
# print('Sequência de Fibonacci')
# print('-'*20)
# n = int(input('Quantos termos você quer mostrar? '))
# t1 = 0
# t2 = 1
# print('~'*20)
# print('{} -> {}'.format(t1,t2), end = '')
# cont = 3
# while cont <= n:
#     t3 = t1 + t2
#     print(' -> {}'.format(t3), end = '')
#     t1 = t2
#     t2 = t3
#     cont = cont + 1
# print(' -> FIM')


# n = 0
# cont = 0
# soma = 0
# n = int(input('Digite um número [999 para parar]: '))
# while n != 999:
#     soma = soma + n
#     cont = cont + 1
#     n = int(input('Digite um número [999 para parar]: '))
# print('Você me informou {} valores e a soma entre eles foi {}'.format(cont, soma))
# print('Fim')


# resp = 'S'
# media = 0
# soma = 0
# cont = 0
# maior = 0
# menor = 0
# while resp in 'Ss':
#     n = int(input('Digite um número: '))
#     soma += n
#     cont += 1
#     if cont == 1:
#         maior = menor = n
#     else:
#         if  n > maior:
#             maior = n
#         if n < menor:
#             menor = n
#     resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
# media = soma / n
# print('-=-==-=-'*15)
# print('Você digitou {} números e a média enetr eles foi {:.2f}'.format(cont,media))
# print('O maior valor foi {} e o menor foi {}'.format(maior,menor))
# print('FIM')


                    #Interropendo repetições while

# while True:
#     if Bloco
#         pass
#     if espaço
#         pula
#     if moeda
#         Pega 
#     if troféu
#         pula 
#         break
#     pega

# cont = 1
# while True:
#     print(cont, ' -> ', end = '')
#     cont += 10
#     break
# print('Acabou')

# n = s = 0 
# while True:
#     n = int(input('Digite um número: '))
#     if n == 999:
#         break
#     s += n
# print(f'A soma vale {s}')

# nome = 'jose'
# idade = 33
# salario = 970.30
# print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')

# soma = cont = n = 0
# while True:
#     n = int(input('Digite um valor [999 para parar]: '))
#     if n == 999:
#         break
#     soma += n
#     cont += 1
# print(f'você informou {cont} números e a soma entre eles foi {soma}!')

# n = 0
# t = 0
# print('-'*30)
# while True:
#     n = int(input('Quer ver a tabuada de qual valor? '))
#     print('-'*30)
#     if n < 0:
#         break
#     else:
#         for c in range(1,11):
#             print(f'{n} x {c} = {n*c}')
#     print('-'*30)
# print('O progama foi encerrado.') 

# from random import randint

# computador = randint(0,10)
# soma = cont = 0
# print('-==-'*15) 
# print('Vamos jogar par ou impar.')
# print('-==-'*15)
# while True:
#     n =  int(input('Digite um valor: '))
#     computador = randint(0,11)
#     total = n + computador
#     p = ' '
#     while p not in 'PI':
#         p = str(input('Par ou ímpar? [P/I]: ')).upper().strip()[0]
#     print(f'Você jogou {n} e o computador {computador}. Total de {total}', end = '')
#     if p == 'P':
#         if total % 2 == 0:
#             print(' par')
#             print('Você ganhou.')
#             cont += 1
#         else:
#             print(' impar')
#             print('Você perdeu.')
#             break
#     elif p == 'I':
#         if total % 2 == 1:
#             print(' impar')
#             print('Voce ganhou.')
#             cont +=1
#         else:
#             print(' par')
#             print('Você perdeu.')
#             break
#     print('Vamos jogar novamente...')
# print(f'GAME OVER, VOCÊ VENCEU {cont} VEZES.')

# print('='*45)
# print(f"{'CADASTRE UMA PESSOA':^45}")
# print('='*45)
# cont = 0
# conth = 0
# contm = 0
# while True:
#     idade = int(input('Idade: '))
#     sexo = ' '
#     sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
#     if idade > 18:
#         cont += 1
#     if sexo == 'F' and idade < 20:
#         contm += 1
#     if sexo == 'M':
#         conth += 1
#     while sexo not in 'MF':
#         sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
#     resp = ' '
#     while resp not in 'SN':
#         resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
#     print('='*45)
#     print(f"{'CADASTRE UMA PESSOA':^45}")
#     print('='*45)
#     if resp == 'N':
#         break
# print(f'Total de pessoas com mais de 18 anos: {cont}')
# print(f'Ao todo temos {conth} homens cadastrados.')
# print(f'E temos {contm} mulheres com menos de 20 anos.')




# 'total = valor = cont = menor = barato = 0
# barato = ' '
# while True:
#     produto = str(input('Nome do produto: '))
#     preço = float(input('Preço: R$ '))
#     total += preço
#     cont += 1
#     resp = ' '
#     if preço == 1:
#         menor = preço
#         barato = produto
#     else:
#         if preço < menor:
#             menor = preço
#             barato = produto
#     if preço > 1000:
#         valor += 1
#     while resp not in 'SN':
#         resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
#     if resp == 'N':
#         break
# print(f"{'FIM DO PROGAMA':^40}")
# print(f'O total da compra foi R${total}')
# print(f'Temos {valor} produtos custando mais que R$1000.0')
# print(f'O produto mais barato foi {barato} que custa R${menor}')'


# print('=' * 30)
# print('{:^30}'.format('BANCO DO BRASIL'))
# print('=' * 30)

# valor = int(input('Informe o valor que deseja sacar: R$ '))
# total = valor
# ced = 50
# totalced = 0
# while True:
#     if total >= ced:
#         total -= ced
#         totalced += 1
#     else:
#         if totalced > 0:
#             print(f'Total de {totalced} cédulas de {ced}.')
#         if ced == 50:
#             ced = 20
#         elif ced == 20:
#             ced = 10
#         elif ced == 10:
#             ced = 1
#         totalced = 0
#         if total == 0:
#             break


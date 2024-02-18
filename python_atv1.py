       #INTRODUÇÃO
# Nome = input("Qual é o seu nome?")
# print("Ola", Nome, "! Prazer em te conhecer")23
#==========================================================================================================
       #USANDO INPUT
# dia= input('Informe o dia do seu aniversário :')
# mes=input('Agora o mês :')
# ano=input('E por fim o ano :')
# print('Vocé nasceu no dia',dia,'de',mes,'de',ano)
#==========================================================================================================
       #SOMANDO NÚMEROS REIAS
#s = float(input("Escreva um numero :"))
#f = float(input("Escreva outro numero :"))
#t = s + f
#print("A soma desses dois numeros corresponde a = {}" .format(t))
#==========================================================================================================
       #SOMANDO NÚMEROS INTEIROS
#s1=int(input('Digite um valor: '))
#s2=int(input('Digite outro valor:'))
#r= s1+s2
#print('A soma entre {} e {} é igual a: {}'.format(s1,s2,r))
#print('A soma entre', s1, 'e',s2,'é igual a:',r,) 
#==========================================================================================================
       #OBTENDO INFORMAÇÕES SOBRE ALGO
#n=input('Digite um valor: ')
#rint(n.isnumeric()) # é númerico?
#print(n.isalph()) # é uma letra?
#==========================================================================================================
       #OBTENDO INFORMAÇÕES SOBRE ALGO
#l=input('Escreva Algo:')
#print('O tipo primitivo é:', type(l))
#print('({}) Contém número(os)?'.format(l),l.isnumeric())
#print('({}) Contém letra(as)?'.format(l),l.isalpha())
#print('({}) É um decimal?'.format(l),l.isdecimal()) 
#print('({}) É composto apenas por espaços1?'.format(l),l.isspace())
#print('({}) É um digito?'.format(l),l.isdigit())
#print('({}) Está em maiúscula?'.format(l), l.isupper())
#print('({}) Está em minúscula?'.format(l), l.islower())
#==========================================================================================================
       #OPERAÇÕES ARITMÉTICAS
#v1=int(input('Digite um valor: '))
#v2=int(input('Digite outro valor: '))
#r1=v1+v2
#r2=v1-v2
#r3=v1*v2
#r4=v1**v2
#r5=v1/v2
#r6=v1//v2
#r7=v1%v2
#r8=r1**(1/2)
#print('A soma entre esses valores é: {}'.format(r1))
#print('A subtração entre esses valores é: {}'.format(r2))
#print('A multiplicação desses valores é igual a: {}'.format(r3))
#print('A Potênciação desses valores é: {}'.format(r4))
#print('A divisão entre esses valo é: {}'.format(r5))
#print('A divisão inteira desses valores é: {}'.format(r6))
#print('O resto da divisão desses valores é: {}'.format(r7))
#print('A raiz quadrada da soma desses valores é igual a: {:.0f}'.format(r8))
#==========================================================================================================
       #Antecessor e Sucessor (Minha forma)
#n1=int(input('Escreva um numero: '))
#n2=int(input('Escrva outro numero: '))
#r1=n1-1
#r2=n1+1
#r3=n2-1
#r4=n2+1
#print('O antecessor de {} é {} \n Já o sucessor de {} é {}'.format(n1,r1,n1,r2))
#print('O antecessor de {} é {} \n Já o sucessor de {} é {}'.format(n2,r3,n2,r4))
       #Outro método
#n=int(input('Digite um número: '))
#print('O antecessor de {} é {}\njá o sucessor é {}'.format(n,(n-1),(n+1)))

#==========================================================================================================
       #Calculando a média (minha forma)
#m1=float(input('Primeira nota: '))
#m2=float(input('Segunda nota: '))
#m3=float(input('Terceira nota: '))
#r2=(m1+m2+m3)/3
#print('A média final é {:.1f}'.format(r2))
#==========================================================================================================
        #Transformar metros em centímetros e milímetros 
#m=float(input('Informe o valor em metros: '))
#m1=m*100
#m2=m*1000
#print('O valor {}m convertido para cm será {:.0f}cm \n E para mm será {:.0f}mm '.format(m,m1,m2))
#==========================================================================================================
        #Tabuada de um número
#m1=int(input('Escreva um número e veja sua tabuada: '))
#m2=m1*1
#m3=m1*2
#m4=m1*3
#m5=m1*4
#m6=m1*5
#m7=m1*6
#m8=m1*7
#m9=m1*8
#m10=m1*9
#m11=m1*10

#print('-'*20)
#print(' {} x 1 = {}\n {} x 2 = {}\n {} x 3 = {}\n {} x 4 = {}\n {} x 5 = {}\n {} x 6 = {}\n {} x 7 = {}\n {} x 8 = {}\n {} x 9 = {}\n {} x 10 = {} '.format(m1,m2,m1,m3,m1,m4,m1,m5,m1,m6,m1,m7,m1,m8,m1,m9,m1,m10,m1,m11))
#print('-'*20)
#==========================================================================================================
        #Dobro, triplo e raiz²
#n=int(input('Digite um numero: '))
#n1=n*2
#n2=n*3
#n3=pow(n, (1/2))
#print('O dobro de {:.0f} vale {:.0f}.'.format(n,n1))
#print('O triplo de {} vale {}.\n A raiz quadrada de {} é igual {:.2f}.'.format(n,n2,n,n3))

#==========================================================================================================
        #converter real > dolar 
#r=float(input('Quantos reais deseja converter? '))
#r1=r/3.27  
#print('Convertendo o valor de {:.2f}R$ em dolar você terá {:.2f}US$'.format(r,r1))
#==========================================================================================================
        #Calculando aréa 
#l=float(input('Informe a largura de sua parede: '))
#a=float(input('informe a altura de sua parede: '))
#print('1 litro de tinta irá pintar 2m²')
#r1=l*a
#print('A aréa de sua parede é: {:.2f}m²'.format(r1))
#r2=r1/2
#print('Para consegui pintar sua parede você precisarar de: {:.2f}L de tinta'.format(r2))
#==========================================================================================================
        #Aplicando descontos
#p=float(input('Escreva o valor em reais que deseja aplicar o desconto R$: '))
#d= p - (p*0.05) #ou  d = p - (p * 5 / 100)
#print('Com o desconto de 5% você ira pagar R${:.1f} de desconto'.format(d))
        #Aplicando reajuste
#s=float(input('Digite aqui seu salário R$: '))
#d = (s*1.15) #ou 15% + 100% = 115% >> d = (s*100/115) #ou >> d = s + (s * 15 / 100)
#print('Com o reajuste de 15% o seu novo salário será R${:.1f}'.format(d))
        #Testando progamas
#print('-'*50)
#f = print('Esse progama irá calcular um desconto de 10% à vista\ne um acréscimo de 8% caso a compra seja no cartão.')
#print('-'*50)
#v = float(input('Insira o valor que deseja aplicar R$: '))
#print('-'*50)
#r = v - (v*10/100)
#r1 = v + (v*10/100)
#print('Caso deseje pagar à vista o valor será R${:.1f}.'.format(r))
#print('Caso queira comprar com o cartão esse será o novo valor R${:.1f}.'.format(r1))
#print('-'*50)
#=========================================================================================================
        #Conversor de temperatura
#print('-'*50)
#print('Conversor simples de temperatura')
#print('-'*50)
#c=float(input('informe a temperatura em ºC: '))
#f= (c*1.8) + 32
#k = c+273.15
#print('-'*50)
#print('Convertendo para Kelvin será: {:.1f}ºk'.format(k))
#print('-'*50)
#print('Convertendo para fahrenheit será: {:.1f}ºf'.format(f))
#=========================================================================================================
        #Aluguel de carros
#print('-'*50)
#km=float(input('Informe a quantidade de km percorrido: '))
#dias=int(input('Informe a quantos dias o carro esta alugado: '))
#r1 = km*0.15
#r2 = dias*60
#r3 = r1+r2
#print('-'*50)
#print('Você usou o carro durantes {} dias e rodou {}Km\npor tanto o toal a pagar será R${:.2f}.'.format(dias,km,r3))
#=========================================================================================================
        #Biblioteca math
#import math
#from math import sqrt
#n=int(input('Digite um numero: '))
#r = sqrt(n)
#print('A raiz quadrada desse nunero é {:.2f}.'.format(r))
#=========================================================================================================
        #Atividade relacionado ao uso da biblioteca math
#from math import trunc
#n = float(input('Digite um número: '))
#t = trunc(n)
#print('O número {} tem a sua parte inteira {}.'.format(n,t))
        #Calculando a hipotenusa de um triangulo retangulo
#import math
#co=int(input('Informe a medida do cateto oposto: '))
#ca=int(input('Informe a medida do cateto adjacente: '))
#soma = co**2
#soma2= ca**2                       OU PODERIA FAZER COM O COMANDO math.hypot(co,ca)
#soma3 = soma + soma2
#raiz = math.sqrt(soma3)
#print('Com os valores do cateto oposto e adjacente de um triangulo retangulo {:.1f}cm e {:.1f}cm, iremos obter a hipotenusa {:.1f}'.format(ca,co,raiz))
        #Calculando o seno, cosseno e tanjente
#from math import radians, sin, cos, tan
#a = float(input('Informe o ângulo que deseja calcular: '))
#sen = sin(radians(a))
#tans = tan(radians(a))
#coss = cos(radians(a))
#print('O sen de {:.1f}º é {:.2f}º\nO cos de {:.1f}º é {:.2f}º\nA tan de {:.1f}º é {:.2f}º'.format(a,sen,a,coss,a,tans))
        #Usando a biblioteca random
#rom random import choice
#a1=input('Digite o nome do aluno 1: ')
#a2=input('Digite o nome do aluno 2: ')
#a3=input('Digite o nome do aluno 3: ')
#a4=input('Digite o nome do aluno 4: ')
#lista=[a1,a2,a3,a4]
#sorteio = choice(lista)
#print('-'*50)
#print('O aluno escolhido foi {}, parabéns!! '.format(sorteio))       
#print('-'*50)

#

#from random import shuffle
#a1=input('Digite o nome do aluno 1: ')
#a2=input('Digite o nome do aluno 2: ')
#a3=input('Digite o nome do aluno 3: ')
#a4=input('Digite o nome do aluno 4: ')
#list=[a1,a2,a3,a4]
#shuffle(list)
#print('A ordem de apresentação será: ')
#print(list)
#=================================================================================
        #Manipulando textos 
#=================================================================================
                                         #Format
#n=str(input('Digite seu nome: '))
#print('Prazer em te conhecer {:20}!'.format(n))
#print('Prazer em te conhecer {:<20}!'.format(n))
#print('Prazer em te conhecer {:>10}!'.format(n))
#print('Prazer em te conhecer {:^10}!'.format(n))
#print('Prazer em te conhecer {:=^20}!'.format(n))
# Caso queira retirar as casas decimais usar {:.0f} 
#Caso não queira quebrar a linha de um print para outro usar o (end = ' ')
#Caso queira quebrar a linha usar \n

#==========================================================================================================
                                          #OBESERVAÇÕES#
# Obs > O {} em conjunto com o .format + item, serve para fazer a substituição do {} pelo item formatado. 
# 
# Números inteiros = Int (-2,-1,0,1,2,3,5,....)
# Números reais = float (0.004,23.1,89.34,55.33.....)
# Valores logicos ou boleanos = bool (True or False) OBS > com a primeira letra maíuscula 
# Valores caracteres ou strings = str ('Olá','7.5') string vazia > ''

#OBS > O comando "print" seguido de "type" representado assim = print(type(item)) irá mostrar a class do valor digitado no input.

#OBS > Para conseguir informações sobre algo na entrada usar o "print" + "msg" + "item" + "isnumeric" e etc... ( Ex  "print('É um numero?', l.isnumeric())" ).

                                          #OPERADORES ARITMÉTICOS#
# Adição (+)                Potência (**)            Modúlo ou resto da divisão (%)
# Subtração (-)             Divisão (/)              Igualdade (==)
# Multiplicação (**)        Divisão Inteira (//)     Raiz Quadrada **(1/2) Ex: 81**(1/2) == 9

#OBS > Ordem de execução dos operadores 1 - (), 2 - após resolver os () vem a **, 3 - * , / ,  //,  %, 4 - E por fim resolvemos a + e - .

#OBS > Operando pode ser um número, uma str ou até uma variável. Ex: Operador Binário (5), ou seja, necessita de outro operador, exemplo (5+2 == 7) ou (5**2 == 10) ou (5/2 == 2.5) ou (5**2 == 25) ou (5//2 == 2) ou (5%2 == 1)

                                          #MODULOS
#OBS > para importar uma biblioteca usar o comando 'import' + 'biblioteca', caso queira algo específico usar o 'from+biblioteca+import+item'

                                          #Biblioteca math
# Arredondar para + (ceil)                                # Potencia (pow)                      #Calcular hipotenusa (hypot)
# Arredondar para - (floor)                               # Raiz quadrada (sqrt)
# Eliminar da virgula virgula pra frente (trunc)          # Calculo fatorial (factorial)

                                          #Biblioteca random
#Embaralhar palavras (shuffle)
#Escolhas aleatorias (choice)

                                          #OPERAÇÕES COM STRING
#Fatiamento (Item+[9])                                                     #Fatiamento[:5]Do inicio ao 5
#Fatiamento (item+[9:13]) excluindo o último número]                       #Fatiamento[15:]Do 15 ao final
#Fatiamento (Item+[9:21:2]) do 9 ao 21 pulando 2 em 2                      #Fatiamento[9::3] do 9 ao final pulando 3 em 3

                                          #Analisar string
#comprimento len(frase)                                                #Frase.upper() > O que já é maiúsculo é mantido e as minúsculas são trocas por maiúsculas (versão inversa) > frase.lower()    
#Contador frase.count(letra)                                           #Frase.replace('python, 'Android') substituiria a palavra python por android
#Encontrar a posição da frase.find(palavra ou letra)                   #curso in frase (responde se term a palavra curso na frase) 

#frase.capitalize() > Muda tudo para minúsculo e a primeira letra fica maiúscula       #frase.rstrip() > Remove somente os espaços da direita 
#frase.title() > Deixa todas as inicias de palavras maiúsculas                         #frase.lstrip() > Remove somente os espaços da esquerda 
#frase.strip() > Irá remover os espaços inuteis do inicio e do final da frase          #frase.split() > Onde tiver espaço ele vai criar uma divisão
  
#'-'.join(frase) > onde tem espaço será substituido pelo caractere do inicio

#===========================================================================================================
           #Exercicios sobre string
#frase='Curso em Video Python'
#print('Curso' in frase)

#frase='Curso em Video Python'
#print(frase.lower().find('video'))

#frase='Curso em Video Python'
#print(frase.split())

#frase='Curso em Video Python'
#d = frase.split()
#print(d [2])

#nome = 'Diogo Graciano Badu de Souza'
#n = nome.upper()S
#n1 = nome.lower()
#l=len('DiogoGracianobadudesouza')
#con = len('Diogo')
#print('Maiúsculo: {}\nMinúsculo: {}\nLetras sem considerar espaços: {}\nLetras no primeiro nome {}: '.format(n,n1,l,con))

nome=str(input('Escreva seu nome: '))
fi = nome.find('Santos')
print('Santos' in nome[:6])
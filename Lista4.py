 # Primeira Questão

# def saudacao(nome):
#     return (f"Saudações, {nome}!")
# print(saudacao("Maria"))

# # Segunda Questão

# def num(x):
#     if x%2==0:
#         return ("numero par")
#     elif x%2==1:
#         return ("numero impar")
# print(num(3))

# Terceira Questão

# def num(x: int,y: int):
#     if x>y:
#         return (f"{x} é maior que {y}")
#     elif x<y:
#         return (f"{y} é maior que {x}")
# print(num(1,-3))

# Quarta Questão

# num=int(input("Diga um numero: "))
# for x in range(1,11):
#     tabuada= num*x
#     print(f"{num} x {x} = {tabuada}")

# Quinta Questão

# x=10
# while x>=1:
#     print(x)
#     x-=1
#     if x==0:
#         print("Explosão")
        
# Sexta Quetão

# def media(x,y,z):
#     return (f"Sua média é: {(x+y+z) /3}")
# print(media(10,10,10))

# # Sétima Questão

# def calcular_fatorial(numero):
#     resultado = 1
#     for i in range(1, numero + 1):
#         resultado *= i
#     return resultado
# print(calcular_fatorial(6))

# Oitava Questão

# def vogal(palavra: str):
#     numerodevogal=0
#     for i in palavra:
#         if i =="a" or i=="e" or i=="i" or i=="o" or i=="u":
#             numerodevogal+=1
#             return (f" Vogais totais={numerodevogal}")
# palavra=str(input("Digite uma palavra"))
# print(vogal(palavra))

# Nona Questão

# import random
# numale= int(random.randint(1,20)) 
# tenta=int(input("Me diga um numero aleatório de 1 a 20: "))
# while tenta!=numale:
#     if tenta>20:
#         print(ValueError)
#     if tenta>numale:
#             print("seu numero é maior, tente outro menor")
#             tenta=int(input("Me diga um numero aleatório de 1 a 20: "))
#     if tenta<numale:
#                 print("Seu numero é menor, tente outro maior")
#                 tenta=int(input("Me diga um numero aleatório de 1 a 20: "))
#     if tenta==numale:
#                     print("Numero correto")      
            
# Décima questão

# soma=0
# n=int(input("Me diga um numero: "))
# for i in range(1,n+1):
#     if i%2==0:
#         soma+=i
# print(soma)

# Questão 11

# def adicao(x,y):
#    return x+y
# def subtracao(x,y):
#     return x-y
# def multiplicao(x,y):
#     return x*y
# def divisao(x,y):
#     return x/y    
# def cauculadora():
#     n1=float(input("Me diga um numero: "))
#     n2=float(input("Me diga outro: "))
#     print("1-Adição")
#     print("2-Subtração")
#     print("3-Multiplicação")
#     print("4-Divisão")
#     operação=int(input("Digite o numero da operação: "))
#     if operação ==1:
#         return(f"{n1} + {n2} = {adicao(n1,n2)}")
#     if operação==2:
#         return(f"{n1} - {n2} = {subtracao(n1,n2)}")
#     if operação==3:
#         return(f"{n1} * {n2} = {multiplicao(n1,n2)}")
#     if operação==4:
#         return(f"{n1} / {n2} = {divisao(n1,n2)}")

# print(cauculadora())
        

# Questão 12

# def primo():
#     n=int(input("Me diga um numero: "))
#     cont=0
#     for i in range(1, n+1):
#         if n%i == 0:
#             cont+=1
#         if cont<=2:
#             return(f"O numero {n} é primo")
#         else:
#             return(f"O numero {n} não é primo")
# print(primo())

# Questao 13


# def reverseword():
#     palavra=str(input("Me diga uma palavra: "))
#     reverso= palavra[ ::-1]
#     return reverso
# print(reverseword())


# Questao 14


# numeropar=0
# numeroimpar=0
# for i in range(1,11):
#     numero=int(input(f"Me diz o {i} numero: "))

#     if i%2==0:
#         numeropar+=1
#     else:
#         numeroimpar+=1
# print(f"O numero total de pares é {numeropar}")
# print(f"O numero total de impares é {numeroimpar}")


# Questão 15

# def fibonacci():
#     list=[]
#     n=int(input("digite um numero "))
    
#     for i in range(1,n+1):
#         m1=(i-1)
#         m2=(i-2)
#         if m2==-1:
#             list.append(0)
#         elif m2==0:
#             list.append(1)
#         else:
#             soma=m1+m2
#             list.append(soma)
#     return list
# print(fibonacci())

# def fibonacci():
#     list=[0,1]
#     m1=0
#     m2=0
#     n=int(input("digite um numero "))
#     for i in range(2, n):
#         m1= list[i-1]
#         m2= list[i-2]
#         soma= m1 + m2
#         list.append(soma)
#     return list
# print(fibonacci())

n = int(input('Quantos termos quer? '))
a = 0
b = 1
c = 0
cont = 0
while cont < n:+
    print(f'{c}', end=' ')
    a = b
    b = c
    c = a + b
    cont += 1
print('FIM')
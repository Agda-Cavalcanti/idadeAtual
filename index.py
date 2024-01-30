#Instruções do projeto
# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2023.
# A partir dessas informações, o sistema mostrará o nome do usuário
#  e a idade que completou, ou completará, no ano atual (2024).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano,
#  o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

from time import sleep

valorCorreto = False

while (valorCorreto == False):
    nome = input("\n\nNome completo: ")
    #print("Ano de nascimento: ")

    try: 
        anoDeNascimento = int(input("Ano de nascimento: "))
        
        if (anoDeNascimento > 1922) and (anoDeNascimento < 2023):
            print("\n\nNome: ", nome)
            idade = 2024 - anoDeNascimento
            print("Idade atual: ", idade)
            valorCorreto = True
        else:
            sleep(0.5)
            print("Valor incorreto, digite novamente...")
            sleep(1)
    except:
        sleep(0.5)
        print("Valor incorreto, digite novamente...")    
        sleep(1)
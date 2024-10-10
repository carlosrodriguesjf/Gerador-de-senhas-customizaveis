### GERADOR DE SENHAS CUSTOMIZÁVEIS #####

# importações
import random


# Funcionalidades que o projeto deve possuir:
# 1. Escolha do Comprimento da Senha:
cumprimento_senha = int(input('Digite o comprimento da senha a ser gerada: '))


# 2. Escolha dos Componentes da Senha:
maiusculos = input('Deseja que a senha tenha caracteres maiúsculos? [S / N]: ')
minusculos = input('Deseja que a senha tenha caracteres minusculos? [S / N]: ')
numeros = input('Deseja que a senha tenha numeros? [S / N]: ')
simbolos = input('Deseja que a senha tenha símbolos? [S / N]: ')

# listad de numeros e listas
senha_gerada = []
lista_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lista_maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lista_simbolos = ['!', '@', '#', '$', '%' '&', '*', '?']

# 3. Geração da Senha Aleatória:
for i in range(0,cumprimento_senha):
    if maiusculos in 'Ss':
        senha_gerada.append(random.choice(lista_maiusculas))
    if minusculos in 'Ss':
        senha_gerada.append(random.choice(lista_minusculas))
    if simbolos in 'Ss':
        senha_gerada.append(random.choice(lista_simbolos))
    if numeros in 'Ss':
        senha_gerada.append(str(random.randrange(10)))


#senha_final = senha_gerada[0:cumprimento_senha]

random.shuffle(senha_gerada)

senha_final = ''.join(senha_gerada[0:cumprimento_senha])

# 4. Exibição da Senha:
print(senha_final)
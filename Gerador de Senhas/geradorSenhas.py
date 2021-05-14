# Script basico para gerar senhas fortes
# Construido em python 
# Agradecimento Digital Innovation One

# importa as bibliotecas necessárias
import random, string

# recebe do usuário a quantidade (tamanho desejado) da senha
quantidadeCaracteres = int(input("Digite o tamanho da senha: "))

# trata os tipos de caracteres que poderão compor a senha
chars = string.ascii_letters + string.digits + 'ç!@#$%&*()[]{}-=+,./\|?""'

# chama  biblioteca os.urandom gerando caracteres aleatórios disponiveis no SO
rnd = random.SystemRandom() 

# join(junção) / rnd.choice retorna uma lista de caracteres randomicos
# gerados pelo chars, for in range trara um a um 
# até que complete a quantidade correta 
print(''.join(rnd.choice(chars) for i in range (quantidadeCaracteres)))
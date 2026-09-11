nome_digitado = input("Digite o nome: ")
senha_digitada = input("Digite sua senha: ")
senha_cadastrada = '123'
nome_cadastrado = 'ana'

while senha_digitada != senha_cadastrada or nome_cadastrado != nome_digitado:
    print("Nome ou Senha Incorreta! Tente novamente.")
    nome_digitado = input("Digite seu nome: s")
    senha_digitada = input("Digite a senha: ")

print(f"{nome_digitado} Bem vindo ao Sitema...")    


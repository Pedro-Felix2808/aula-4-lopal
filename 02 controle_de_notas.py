nome = input("Digite o nome do aluno: ")
nota = float(input('Digite sua primeira nota'))
per_nota = float(input("deseja adicionar uma nova nota?(sim/nao): "))

cont = 1

while per_nota == "sim":
    nova_nota = float(input("Digite a sua nota: "))
    nota = nova_nota + nota
    per_nota = input("deseja adicionar uma nova nota?(sim/nao): ")
    cont += 1
media_final = nota / cont
if media_final < 5:
    print(f"Nome: {nome}; Média: {media_final}; Situação: Reprovado!")

else:
    print(f"Nome: {nome}; Média: {media_final}; Situação: Aprovado! ")    
import sys

votos = []
# cria uma lista apenas com os candidados que receberam votos
with open("PyVotacao/recursos/dados_elecao.txt") as dados:
    for linha in dados.readlines()[1:]:
        votos.append(linha.split(",")[2].replace("\n", ""))

candidatos = set(votos)  # cria um set, com o nome de cada candidato uma vez
cand_voto = dict()
# cria um dicionário com 'nome candidato' x 'quantidade votos'
for candidato in candidatos:
    cand_voto[candidato] = votos.count(candidato)

# organiza o dicionário usando uma função persolanizada
# P.S.: confira um material extra na próxima cela
cand_voto = sorted(cand_voto.items(), key=lambda x: x[1], reverse=True)

# cria o arquivo com os resultados
with open("PyVotacao/resultado.txt", "w") as result:
    temp = sys.stdout
    sys.stdout = result

    print("Resultados eleitorais")
    print("-" * 25)
    print(f"Total de votos: {len(votos)}")
    print("-" * 25)
    for cand in cand_voto:
        print(f"{cand[0]}: {(cand[1] * 100)/len(votos):.1f}% ({cand[1]})")
    print("-" * 25)
    print(f"Vencedor: {cand_voto[0][0]}")
    print("-" * 25, end="")
    sys.stdout = temp

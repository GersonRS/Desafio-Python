dados = open("PyVotacao/Recursos/dados_eleicao.txt", "r")
pula_linha = next(dados) # ignora a primeira linha do arquivo
lista_dados = list(dados.readlines()) 
dados.close()

# calcula o total de votos
total_votos = len(lista_dados)

# calcula o percentual de votos
def calcula_percentual(total_votos, votos_candidato):
    return (votos_candidato*100)/total_votos

# lista dos candidatos e quantidade de votos que cada candidato recebeu
def contar_votos(arq, candidato):
    with open("PyVotacao/Recursos/dados_eleicao.txt", "r") as arq:
        nomes = arq.read()
    quantidade = nomes.count(candidato)
    return quantidade

candidatos = {
    "Khan": contar_votos(lista_dados, "Khan"),
    "Correy": contar_votos(lista_dados, "Correy"),
    "Li": contar_votos(lista_dados, "Li"),
    "O'Tooley": contar_votos(lista_dados, "O'Tooley")
}

# procura o candidato vencedor
vencedor = max(candidatos, key=candidatos.get)

# resultado final
print("Resultados eleitorais")
print("-"*25)
print(f"Total de votos: {total_votos}")
print("-"*25)
for candidato, votos in candidatos.items():
    percentual = calcula_percentual(total_votos, votos)
    print(f"{candidato}: {percentual:.2f}% ({votos})")
print("-"*25)
print(f"Vencedor: {vencedor}")
print("-"*25)

# escreve um arquivo txt com o resultado
with open("PyVotacao/resultado.txt", "w") as arquivo:
    arquivo.write("Resultados eleitorais\n")
    arquivo.write("-------------------------\n")
    arquivo.write(f"Total de votos: {total_votos}\n")
    arquivo.write("-------------------------\n")
    for candidato, votos in candidatos.items():
        percentual = calcula_percentual(total_votos, votos)
        arquivo.write(f"{candidato}: {percentual:.3f}% ({votos})\n")
    arquivo.write("-------------------------\n")
    arquivo.write(f"Vencedor: {vencedor}\n")
    arquivo.write("-------------------------\n")
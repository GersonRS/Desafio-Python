import sys

data = []
lp = []
# armazena a data em um vetor e o lucro/prejuízo em outro
with open("PyFinanceiro/recursos/dados_financeiro.txt") as dados:
    for line in dados.readlines()[1:]:
        data.append(line.split(",")[0])
        lp.append(int(line.split(",")[1]))

variacao = []
i = 0
# calcula as variações entre os meses
while i < len(lp) - 1:
    variacao.append(lp[i + 1] - lp[i])
    i += 1

total_meses = len(data)
total = sum(lp)

# arquivo de saída
with open("PyFinanceiro/relatório.txt", "w") as result:
    temp = sys.stdout  # armazena em uma variável temporária o stdout padrão
    sys.stdout = result  # troca o stdout para o arquivo
    print("Analise financeira")
    print("-" * 28)
    print(f"Total de meses: {total_meses}")
    print(f"Total: $ {total}")
    print(f"Média: $ {total/total_meses:.2f}")
    print(f"Variação da média: $ {sum(variacao)/len(variacao):.2f}")
    print(
        f"Maior aumento nos lucros: {data[variacao.index(max(variacao)) + 1]} ($ {max(variacao)})"
    )
    print(
        f"Maior redução nos lucros: {data[variacao.index(min(variacao)) + 1]} ($ {min(variacao)})"
    )
    sys.stdout = temp  # devolve o stdout padrão

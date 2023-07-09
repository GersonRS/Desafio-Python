
# número total de meses incluídos no conjunto de dados
with open("PyFinanceiro/Recursos/dados_financeiro.txt", "r") as arquivo:
    linhas = arquivo.readlines()

if linhas:
    linhas = linhas[1:]

meses = len(linhas)





# valor total líquido de "Lucros / Perdas" durante todo o período
valor_total = 0

with open("PyFinanceiro/Recursos/dados_financeiro.txt", "r") as arquivo:
    linhas = arquivo.readlines()

if linhas:
    linhas = linhas[1:]

for linha in linhas:
    data, lucroPerda = linha.strip().split(',')
    valor_total += int(lucroPerda)





# média das mudanças em "Lucros / Perdas" durante todo o período
import csv

variancia = "PyFinanceiro/Recursos/dados_financeiro.txt"

lucros_perdas = []

with open(variancia, 'r') as arquivo:
    registros = csv.reader(arquivo, delimiter=',')

    next(registros)

    for registro in registros:
        lucro_perda = int(registro[1])
        lucros_perdas.append(lucro_perda)

mudancas = [lucros_perdas[i+1] - lucros_perdas[i] for i in range(len(lucros_perdas) - 1)]

media_mudancas = sum(mudancas) / len(mudancas)





# maior aumento nos lucros (data e valor) durante todo o período
import csv

lucros_aumento = "PyFinanceiro/Recursos/dados_financeiro.txt"

maior_aumento = 0
dados_ma = ""

with open(lucros_aumento, 'r') as arqv:
    registros = csv.reader(arqv, delimiter=',')

    next(registros)

    for registro in registros:
        dados = registro[0]
        lucro_perda = int(registro[1])

        if lucro_perda > maior_aumento:
            maior_aumento = lucro_perda
            dados_ma = dados





# maior redução nas perdas (data e valor) ao longo de todo o período
import csv

reducao = "PyFinanceiro/Recursos/dados_financeiro.txt"

maior_reducao = 0
dados_mr = ""

with open(reducao, 'r') as arqvo:
    registros = csv.reader(arqvo, delimiter=',')

    next(registros)

    for registro in registros:
        dados = registro[0]
        lucro_perda = int(registro[1])

        if lucro_perda < maior_reducao:
            maior_reducao = lucro_perda
            dados_mr = dados





print("     Análise financeira")
print("----------------------------")
print(f"Total de meses: {meses}")
print(f"Total: $ {valor_total}")
print("Variação da média: $", media_mudancas)
print(f"Maior aumento nos lucros: {dados_ma} ($ {maior_aumento})")
print(f"Maior redução nas perdas: {dados_mr} ($ {maior_reducao})")

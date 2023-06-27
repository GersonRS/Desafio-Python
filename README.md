# Desafio-Python

## Background

Bem ... você conseguiu!

É hora de deixar de lado os simples exercícios e entrar para as grandes ligas. Bem-vindo ao mundo da programação com Python. Neste desafio, você usará os conceitos que aprendeu durante todo o segundo modulo do NExT sobre Python. Os desafios abordados aqui abrangem uma situação do mundo real onde suas novas habilidades de script Python podem ser úteis. Esses desafios estão longe de ser fáceis, então espere muito trabalho pela frente!

### Antes de você começar

1. Crie um novo repositório para este projeto chamado `desafio-next-python`. ** Não adicione este dever de casa a um repositório existente **.

2. Clone o novo repositório para o seu computador.

3. Dentro de seu repositório git local, crie um diretório para ambos os Desafios Python. Use nomes de pastas correspondentes aos desafios: ** PyFinanceiro ** e ** PyVotação **.

4. Dentro de cada pasta que você acabou de criar, adicione um novo arquivo chamado `main.py`. Este será o script principal a ser executado para cada análise.

5. Envie as alterações acima para GitHub ou GitLab.

## PyFinanceiro

* Neste desafio, você tem a tarefa de criar um script Python para analisar os registros financeiros de sua empresa. Você fornecerá um conjunto de dados financeiros chamado [dados.txt](PyFinanceiro/Recursos/dados_financeiro.txt). O conjunto de dados é composto por duas colunas: `Data` e `Lucros/Perdas`, separados por virgula. (Felizmente, sua empresa tem padrões bastante flexíveis para a contabilidade, então os registros são simples.)

* Sua tarefa é criar um script Python que analise os registros para calcular cada um das seguintes informações:

  * O número total de meses incluídos no conjunto de dados

  * O valor total líquido de "Lucros / Perdas" durante todo o período

  * A média das mudanças em "Lucros / Perdas" durante todo o período

  * O maior aumento nos lucros (data e valor) durante todo o período

  * A maior redução nas perdas (data e valor) ao longo de todo o período

* Por exemplo, sua análise deve ser semelhante a esta abaixo:

  ```text
  Analise financeira
  ----------------------------
  Total de meses: 86
  Total: $ 38382578
  Variação da média: $ -2315,12
  Maior aumento nos lucros: fevereiro de 2012 ($ 1926159)
  Maior redução nos lucros: setembro de 2013 ($ -2196167)
  ```

* Além disso, seu script final deve imprimir a análise no terminal e exportar um arquivo de texto [relatório.txt](PyFinanceiro/relatório.txt) com os resultados.

## PyVotação

* Neste desafio, você tem a tarefa de ajudar uma pequena cidade rural a modernizar seu processo de contagem de votos. (Até agora, o tio Cleiton vinha contando-os um por um com confiança, mas, infelizmente, sua concentração não é o que costumava ser.)

* Você receberá um conjunto de dados de enquete chamado [dados_eleicao.txt](PyVotacao/Recursos/dados_eleicao.txt). O conjunto de dados é composto por três colunas: `ID do eleitor`,` Município` e `Candidato`. Sua tarefa é criar um script Python que analise os votos e calcule cada uma das seguintes informações:

  * O número total de votos impressos

  * Uma lista completa de candidatos que receberam votos

  * A porcentagem de votos que cada candidato ganhou

  * O número total de votos que cada candidato ganhou

  * O vencedor da eleição com base no voto popular.

* Por exemplo, sua análise deve ser semelhante a esta abaixo:

  ```text
  Resultados eleitorais
  -------------------------
  Total de votos: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Vencedor: Khan
  -------------------------
  ```

* Além disso, seu script final deve imprimir a análise no terminal e exportar um arquivo de texto [resultado.txt](PyVotacao/resultado.txt) com os resultados.

<!-- SOBRE O PROJETO -->

# Objetivo

O objetivo do 'PyVotação' é facilitar o sistema de contagem de votos de uma pequena cidade, criando um script em Python para fazer todo o processo. Além disso, faz parte de um projeto de estudos de Python, servindo como material de estudo e aprendizado.

# Como Usar

Para utilizar o PyVotação, você deve criar um fork do repositório e cloná-lo no seu ambiente virtual Python. Depois, basta iniciar o arquivo 'main', que se encontra na pasta 'PyVotacao'.

# Funcionamento do Projeto

Para abrir o arquivo em formato de leitura:

    dados = open("PyVotacao/Recursos/dados_eleicao.txt", "r")
    pula_linha = next(dados) # ignora a primeira linha
    lista_dados = list(dados.readlines()) # converte em lista
    dados.close()

Para calcular o total de votos:

    total_votos = len(lista_dados)

Para calcular o percentual de votos, uma função foi definida:

    def calcula_percentual(total_votos, votos_candidato):
        return (votos_candidato*100)/total_votos

Lista dos candidatos e quantidade de votos que cada um recebeu:

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

Procura o candidato vencedor:

    vencedor = max(candidatos, key=candidatos.get)

Juntando tudo isso, podemos escrever o script e gerar as respostas necessárias. Em seguida, podemos imprimir o resultado utilizando os seguintes códigos: 

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

E para escrever no documento txt, os seguintes códigos são utilizados:

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



## Dicas e considerações

* Considere o que aprendemos até agora. Até agora, aprendemos como lidar com arquivos; para ler e gravar arquivos em vários formatos; para armazenar conteúdos em variáveis, listas e dicionários; para iterar por meio de estruturas de dados básicas; e depurar ao longo do caminho. Usando o que aprendemos, tente dividir suas tarefas em mini-objetivos discretos (funções). Este será um _muito_ melhor curso de ação do que os exercícios feitos em sala de aula.

* Como você descobrirá, para alguns desses desafios, os conjuntos de dados são bastante grandes. Isso foi feito propositalmente, pois mostra um dos limites da análise baseada em Python. Embora nosso primeiro instinto, como analistas de dados, muitas vezes seja ir direto para o Excel, a criação de scripts em Python pode nos fornecer opções mais robustas para lidar com "big data".

* Seus scripts devem funcionar para cada conjunto de dados fornecido. Execute seu script para cada conjunto de dados separadamente para garantir que o código funcione para dados diferentes.

* Sinta-se encorajado a trabalhar em grupos, mas não se engane copiando o trabalho de outra pessoa. Você consegue o que investe, e a arte da programação é extremamente implacável para os moochers. Construa seu próprio conhecimento, queime os neurônios e aprenda isso enquanto você pode! Essas são habilidades que renderão bons ganhos em sua carreira futura.

* Comece cedo e peça ajuda com frequência! Desafie-se a identificar perguntas _específicas_ para seus professores. Não se resigne a simplesmente dizer: "Estou totalmente perdido". Venha preparado para mostrar seu esforço e padrões de pensamento, ficaremos felizes em ajudar ao longo do caminho.

* Sempre comprometa seu trabalho e faça backups constantes, seja no GitHub ou somente uma pasta no seu computador. Você não quer perder horas de seu trabalho porque não enviou para o GitHub ou salvou a copia do seu projeto a cada meia hora ou algo assim.

  * ** Boa Sorte **.

# Licença

<img alt="License" src="https://img.shields.io/badge/license-MIT-%2304D361?color=rgb(89,101,224)">

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE) para mais informações.

# Contato

Me acompanhe nas redes sociais.

<p align="center">


  <a href="https://www.instagram.com/ddavimig/" target="_blank" >
    <img alt="Instagram" src="https://img.shields.io/badge/-Instagram-ff2b8e?logo=Instagram&logoColor=white"></a>

  <a href="https://www.linkedin.com/in/davimss/" target="_blank" >
    <img alt="Linkedin" src="https://img.shields.io/badge/-Linkedin-blue?logo=Linkedin&logoColor=white"></a>

  <a href="mailto:davi00msantos@gmail.com" target="_blank" >
    <img alt="Email" src="https://img.shields.io/badge/-Email-c14438?logo=Gmail&logoColor=white"></a>

</p>
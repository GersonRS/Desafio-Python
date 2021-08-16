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

* Neste desafio, você tem a tarefa de criar um script Python para analisar os registros financeiros de sua empresa. Você fornecerá um conjunto de dados financeiros chamado [dados.txt] (PyFinanceiro/Resources/dados.txt). O conjunto de dados é composto por duas colunas: `Data` e` Lucros/Perdas`, separados por virgula. (Felizmente, sua empresa tem padrões bastante flexíveis para a contabilidade, então os registros são simples.)

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

* Além disso, seu script final deve imprimir a análise no terminal e exportar um arquivo de texto [relatório.txt] com os resultados.

## PyVotação

* Neste desafio, você tem a tarefa de ajudar uma pequena cidade rural a modernizar seu processo de contagem de votos. (Até agora, o tio Cleiton vinha contando-os um por um com confiança, mas, infelizmente, sua concentração não é o que costumava ser.)

* Você receberá um conjunto de dados de enquete chamado [dados_eleção.csv] (PyVotação/Recursos/dados_eleição.csv). O conjunto de dados é composto por três colunas: `Voter ID`,` County` e `Candidate`. Sua tarefa é criar um script Python que analise os votos e calcule cada uma das seguintes informações:

  * O número total de votos expressos

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
  `` `

* Além disso, seu script final deve imprimir a análise no terminal e exportar um arquivo de texto [resultado.txt] com os resultados.

## Dicas e considerações

* Considere o que aprendemos até agora. Até agora, aprendemos como lidar com arquivos; para ler e gravar arquivos em vários formatos; para armazenar conteúdos em variáveis, listas e dicionários; para iterar por meio de estruturas de dados básicas; e depurar ao longo do caminho. Usando o que aprendemos, tente dividir suas tarefas em mini-objetivos discretos (funções). Este será um _muito_ melhor curso de ação do que os exercícios feitos em sala de aula.

* Como você descobrirá, para alguns desses desafios, os conjuntos de dados são bastante grandes. Isso foi feito propositalmente, pois mostra um dos limites da análise baseada em Python. Embora nosso primeiro instinto, como analistas de dados, muitas vezes seja ir direto para o Excel, a criação de scripts em Python pode nos fornecer opções mais robustas para lidar com "big data".

* Seus scripts devem funcionar para cada conjunto de dados fornecido. Execute seu script para cada conjunto de dados separadamente para garantir que o código funcione para dados diferentes.

* Sinta-se encorajado a trabalhar em grupos, mas não se engane copiando o trabalho de outra pessoa. Você consegue o que investe, e a arte da programação é extremamente implacável para os moochers. Construa seu próprio conhecimento, queime os neurônios e aprenda isso enquanto você pode! Essas são habilidades que renderão bons ganhos em sua carreira futura.

* Comece cedo e peça ajuda com frequência! Desafie-se a identificar perguntas _específicas_ para seus professores. Não se resigne a simplesmente dizer: "Estou totalmente perdido". Venha preparado para mostrar seu esforço e padrões de pensamento, ficaremos felizes em ajudar ao longo do caminho.

* Sempre comprometa seu trabalho e faça backups constantes, seja no GitHub ou somente uma pasta no seu computador. Você não quer perder horas de seu trabalho porque não enviou para o GitHub ou salvou a copia do seu projeto a cada meia hora ou algo assim.

  * ** Boa Sorte **.

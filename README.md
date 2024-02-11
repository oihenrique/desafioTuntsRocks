# Desafio TuntsRocks 2024 - Script de cálculo de notas de alunos

![Python](https://img.shields.io/badge/Python-yellow)
[![LinkedIn](https://img.shields.io/badge/Connect%20on-LinkedIn-blue)](https://www.linkedin.com/in/oihenriquegomes/)

## Sumário

- [Contexto](#Contexto)
- [Recursos Principais](#Recursos-Principais)
- [Tecnologias Utilizadas](#Tecnologias-Utilizadas)
- [Configurações](#Configurações-antes-do-uso)
- [Uso](#Uso)

## Contexto

Este projeto faz parte do desafio da TuntsRocks e consiste em atualizar uma planilha com várias notas de alunos,
retornando se o aluno foi aprovado ou não e qual sua nota mínima para passar na prova final.

O projeto utiliza a API do Google Sheets, apesar dela estar disponível em várias linguagens como java, javascript e PHP,
optei por realizar o código em Python pelos seguintes motivos:

- Python é uma linguagem muito utilizada para scripts e tem fácil entendimento;
- É possível executar o script direto na máquina como um executável, sem a necessidade de mexer no código ou
  em linhas de comando, sendo útil para pessoas leigas, por exemplo;
- Simplicidade e rapidez no desenvolvimento do script;
- Possibilidade de escalabilidade no futuro através de bibliotecas como pandas para realizar análise de dados ou
  aplicação de outras automações;

### Cálculo da média, Nº máximo de faltas e nota para aprovação final (naf)

- A média foi cálculada pela soma das 3 notas dividido por 3;
- O número máximo de faltas é de 25% do número total de aulas (60), portanto, foi definido como 15.

**Observação**: como as notas estão variando de 0 a 100 e não de 0 a 10, a fórmula do cálculo da `naf` foi ajustada
também, utilizando o valor 50, invés de 5.

Para calcular a `naf` foi utilizada a seguinte fórmula: `50 <= (média + naf)/2`, que foi simplificada múltiplicando os
dois lados por 2 e subtraindo o valor da `média` dos dois lados, desse modo, se tornou a seguinte
fórmula: `naf >= 100 - média`, sendo o resultado arredondado para o próximo número inteiro.

## Recursos Principais

- **Cálculo da situação do aluno:** calcula a média das notas e de acordo com alguns critérios, registra na planilha
  se o aluno foi aprovado, reprovado por faltas, reprovador por nota ou se terá de realizar um exame final.
- **Log dos cálculos:** o programa emite um log no terminal a cada cálculo realizado.

## Tecnologias utilizadas

- ![Python](https://img.shields.io/badge/Python-yellow): foi utilizado para a criação do script de automação.

## Configurações antes do uso

1. Crie um ambiente virtual chamado `venv`;
2. Ative o ambiente virtual;
3. Instale as dependências do projeto contidas no arquivo `dependencies.txt` com o seguinte comando:
   `pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib google-auth google-auth-oauthlib`
4. Execute o arquivo `main.py`;
5. Logue com uma conta Google e permita o acesso solicitado;
6. Será gerado o seu `token.json` de acesso na pasta `config`.

## Uso

1. Abra a planilha: https://docs.google.com/spreadsheets/d/1uYa4Eo6Os3fdbF1YK8fvIxlcyzvBxIpPjpMIJwdOhZ8/edit?usp=sharing
2. Execute o arquivo `main.py`;
3. Será exibido o log de informações geradas pelo script enquanto a planilha é atualizada.

## Contato

Você me chamar no: [LinkedIn](https://www.linkedin.com/in/oihenriquegomes/), ou enviar um e-mail para:
contato.henriquegomes@hotmail.com
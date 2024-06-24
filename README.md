<h1 align='center'><b>Projeto Inventory Report</b></b></h1>

Esse é um gerador de relatórios. O objetivo é receber arquivos contendo informações sobre um estoque específico e, em seguida, produzir um relatório abrangente com base nesses dados. Esses dados de estoque poderão ser obtidos de duas fontes:

- Através da importação de um arquivo **CSV**;

- Através da importação de um arquivo **JSON**;

Além disso, o relatório final possuirá duas versões: **simples** e **completa**:

- A versão simples retorna um relatório com as seguintes informações:

```txt
Oldest manufacturing date: YYYY-MM-DD
Closest expiration date: YYYY-MM-DD
Company with the largest inventory: NOME DA EMPRESA
```

- Já a versão completa retorna um relatório com as informações:

```bash
Oldest manufacturing date: YYYY-MM-DD
Closest expiration date: YYYY-MM-DD
Company with the largest inventory: NOME DA EMPRESA
Stocked products by company:
- Empresa 1: 2
- Empresa 2: 1
```

<strong>Executando o Projeto</strong>
  <br />
  
Esse programa deverá ser executável <strong>via linha de comando</strong>.

O comando a ser executado será `ir`. Para que ele funcione em seu ambiente é preciso antes instalar o próprio código como um pacote pip:
<code>pip install .</code>

Agora você pode chamar o comando `ir` passando seus argumentos:

<code>ir - p `argumento1` -t `argumento2`</code>

-   **argumento1** deve receber o caminho de um diretório com os arquivos de estoque à serem importados. Os arquivos dentro do diretório podem ser `csv`s ou `json`s.

-   **argumento2** pode receber duas strings: `simple` ou `complete`, cada uma gerando o respectivo tipo de relatório.

___

A partir desse projeto eu desenvolvi as seguintes habilidades:

- Aplicar conceitos de Programação Orientada a Objetos em Python;

- Implementar leitura e escrita de arquivos CSV e JSON em Python;


*Esse app faz parte dos projetos avaliadores da <b>Trybe</b> e alguns arquivos foram fornecidos para que fosse possível a avaliação do meu código.

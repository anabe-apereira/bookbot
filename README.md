# 📚 BookBot

O **BookBot** é um utilitário simples em **Python** que analisa um arquivo de texto (um "livro") e gera um pequeno relatório com:

- 📖 o número total de palavras;  
- 🔤 a contagem de cada caractere alfabético, em ordem decrescente de frequência.  

Este projeto foi desenvolvido durante o curso [**Build a Bookbot in Python**](https://www.boot.dev) na Boot.dev.

---

## 🧭 Sumário

- [O que o BookBot faz](#o-que-o-bookbot-faz)  
- [Estrutura do projeto](#estrutura-do-projeto)  
- [Como funciona](#como-funciona)  
- [Como executar o projeto](#como-executar-o-projeto)  
- [Exemplo de saída](#exemplo-de-saída)  
- [Análise dos arquivos e funções](#análise-dos-arquivos-e-funções)  
- [👩‍💻 Autora](#-autora)

---

## 📖 O que o BookBot faz

O BookBot lê um arquivo de texto passado como argumento na linha de comando, conta o número de palavras e calcula quantas vezes cada letra aparece.  
O resultado é um relatório impresso no terminal com a contagem total de palavras e a frequência de cada caractere alfabético.

---

## 🗂 Estrutura do projeto

```
bookbot/
├── main.py       # script principal (CLI e relatório)
├── stats.py      # módulo de funções de contagem e ordenação
└── README.md     # este arquivo
```

---

## ⚙️ Como funciona

1. O usuário executa o comando `python3 main.py caminho/do/livro.txt`.  
2. O programa:
   - Lê o conteúdo do arquivo (`get_book_text`);
   - Conta o número total de palavras (`word_count`);
   - Conta a ocorrência de cada caractere (`character_count`);
   - Ordena os caracteres alfabéticos por frequência (`character_sort`);
   - Exibe o relatório no terminal.

---

## ▶️ Como executar o projeto

Requisitos:
- 🐍 Python 3.6 ou superior.

Passos:
1. Coloque o arquivo de texto que deseja analisar na pasta do projeto ou em qualquer diretório do seu sistema.
2. No terminal, execute:

```bash
python3 main.py caminho/do/livro.txt
```

Exemplo:

```bash
python3 main.py mobydick.txt
```

Se nenhum caminho for informado, o programa exibe uma mensagem de uso:

```
Usage: python3 main.py <path_to_book>
```

---

## 📊 Exemplo de saída

```
============ BOOKBOT ============
Analyzing book found at mobydick.txt...
----------- Word Count ----------
Found 218452 total words
--------- Character Count -------
e: 120345
t: 98765
a: 91234
o: 83412
...
============= END ===============
```

---

## 🧩 Análise dos arquivos e funções

### 🧠 main.py

É o **script principal** do projeto e contém três funções:

- **`get_book_text(path_to_file)`**  
  Lê e retorna o conteúdo completo do arquivo de texto.

- **`print_report(book_path, word_count, char_sorted)`**  
  Imprime no terminal o relatório com:
  - Caminho do arquivo analisado;
  - Quantidade total de palavras;
  - Frequência dos caracteres (somente letras).

- **`main()`**  
  Controla o fluxo da aplicação:
  - Lê o argumento com o caminho do livro;
  - Chama as funções do módulo `stats.py`;
  - Exibe o relatório no terminal.

---

### 📈 stats.py

Contém as funções responsáveis pela análise do texto:

- **`word_count(path_to_file)`**  
  Abre o arquivo, divide o texto em palavras (usando `split()`) e retorna o total de palavras.

- **`character_count(text)`**  
  Converte o texto para minúsculas e cria um dicionário com a contagem de **todos os caracteres** encontrados.

- **`character_sort(char_count_dic)`**  
  Filtra apenas os caracteres **alfabéticos**, organiza em uma lista de dicionários com o formato  
  `{"char": <letra>, "num": <quantidade>}`  
  e ordena em ordem decrescente de frequência.

---

## 👩‍💻 Autora

Projeto desenvolvido por **Ana Beatriz Pereira** durante o curso  
[**Build a Bookbot in Python**](https://www.boot.dev) 💻✨


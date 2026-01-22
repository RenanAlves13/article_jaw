# Results

Esta pasta contém os dados de entrada e/ou saída utilizados pelo script `analise.py`.

## Estrutura esperada

```
Results/
  deepseck_results/
    <projeto>/
      zero-*.csv
      few-*.csv
  openai_results/
    <projeto>/
      zero-*.csv
      few-*.csv
```

## Regras dos arquivos CSV

Cada arquivo CSV precisa conter as colunas:

- `Microservice`
- `Responsibilities`
- `Communicates With`

O separador de múltiplos serviços na coluna **Communicates With** é `;` por padrão (configurável em `analise.py`).

## Dicas

- Mantenha nomes consistentes para o mesmo projeto entre `deepseck_results/` e `openai_results/`.
- Arquivos que não começam com `zero-` ou `few-` não serão processados.

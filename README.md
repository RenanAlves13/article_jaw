# article_jaw

Este repositório reúne scripts e resultados para analisar métricas de comunicação e responsabilidades entre microserviços a partir de arquivos CSV. O fluxo principal é executar `analise.py`, que lê os dados em `Results/` e gera arquivos de resumo.

## Visão geral rápida

- **Entrada**: CSVs em `Results/` (por modelo e por projeto).
- **Processamento**: `analise.py` calcula métricas e consolida resultados.
- **Saída**: `results_per_project.csv` e `results_summary.csv`.

## Pré-requisitos de hardware

- **CPU**: 2 núcleos ou mais.
- **RAM**: 4 GB (8 GB recomendado para bases maiores).
- **Disco**: 1 GB livre (mais se os CSVs forem grandes).

## Pré-requisitos de software

- **Sistema operacional**: Linux, macOS ou Windows.
- **Python**: 3.10+.
- **IDE (opcional)**: VS Code, PyCharm ou outra de sua preferência.

## Chaves e acesso a modelos (DeepSeek e OpenAI)

> **Importante**: o script `analise.py` não faz chamadas a APIs, mas, caso você use os notebooks nas pastas `deepseck/` e `openai/`, você precisará de chaves válidas.

- **DeepSeek**: obtenha e configure a chave de API conforme a documentação do provedor.
- **OpenAI**: obtenha e configure a chave de API conforme a documentação do provedor.

### Como configurar as chaves (exemplo)

Recomenda-se usar variáveis de ambiente:

```bash
export DEEPSEEK_API_KEY="sua-chave-aqui"
export OPENAI_API_KEY="sua-chave-aqui"
```

Ajuste os nomes das variáveis conforme o notebook/script que você for usar.

## Instalação do Python

### Linux/macOS

- Baixe em: https://www.python.org/downloads/
- Verifique a instalação:
  ```bash
  python3 --version
  ```

### Windows

- Baixe em: https://www.python.org/downloads/windows/
- Ao instalar, marque a opção **Add Python to PATH**.
- Verifique a instalação no Prompt:
  ```powershell
  python --version
  ```

## Configurando uma IDE (opcional)

### VS Code

1. Instale o VS Code: https://code.visualstudio.com/
2. Instale a extensão **Python** da Microsoft.
3. Abra o projeto e selecione o interpretador Python (Ctrl+Shift+P → *Python: Select Interpreter*).

## Dependências

Para executar o script de análise, você precisa do `pandas`:

```bash
pip install pandas
```

Se preferir, você pode instalar tudo via `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Estrutura esperada de dados

O script lê arquivos CSV dentro da pasta `Results/` com a seguinte estrutura:

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

Cada CSV precisa conter as colunas:

- `Microservice`
- `Responsibilities`
- `Communicates With`

## Como executar

1. (Opcional) Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Instale as dependências:
   ```bash
   pip install pandas
   ```

3. Execute o script:
   ```bash
   python analise.py
   ```

## Saídas geradas

Após a execução, o script gera:

- `results_per_project.csv`: métricas calculadas para cada projeto/arquivo.
- `results_summary.csv`: agregações por modelo e tipo de configuração (zero/few-shot).

Os resultados também são exibidos no terminal durante a execução.

## Ajustes opcionais

Se necessário, você pode alterar constantes no início do arquivo `analise.py`, como:

- `BASE_DIR`: caminho base onde ficam as pastas de resultados.
- `MODELS`: mapeamento de nomes de modelo para subpastas.
- `COMM_SEPARATOR`: separador da coluna `Communicates With`.

## Documentação por pasta

- Veja `Results/README.md` para detalhes sobre a organização dos resultados.
- Veja `deepseck/README.md` e `openai/README.md` para informações específicas dos notebooks.

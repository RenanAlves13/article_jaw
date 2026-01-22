# article_jaw

This repository contains scripts and results for analyzing communication and responsibility metrics between microservices from CSV files. The main flow is to run `analise.py`, which reads data in `Results/` and generates summary files.

## Quick overview

- **Input**: CSVs in `Results/` (by model and project).
- **Processing**: `analise.py` computes metrics and consolidates results.
- **Output**: `results_per_project.csv` and `results_summary.csv`.

## Hardware requirements

- **CPU**: 2 cores or more.
- **RAM**: 4 GB (8 GB recommended for larger datasets).
- **Disk**: 1 GB free (more if CSVs are large).

## Software requirements

- **Operating system**: Linux, macOS, or Windows.
- **Python**: 3.10+.
- **IDE (optional)**: VS Code, PyCharm, or your preferred editor.

## Keys and access to models (DeepSeek and OpenAI)

> **Important**: `analise.py` does not call any APIs, but if you use the notebooks in `deepseck/` and `openai/`, you will need valid API keys.

- **DeepSeek**: obtain and configure the API key according to the provider documentation.
- **OpenAI**: obtain and configure the API key according to the provider documentation.

### How to configure keys (example)

It is recommended to use environment variables:

```bash
export DEEPSEEK_API_KEY="your-key-here"
export OPENAI_API_KEY="your-key-here"
```

Adjust variable names according to the notebook/script you plan to use.

## Installing Python

### Linux/macOS

- Download from: https://www.python.org/downloads/
- Verify installation:
  ```bash
  python3 --version
  ```

### Windows

- Download from: https://www.python.org/downloads/windows/
- During installation, select **Add Python to PATH**.
- Verify installation in Command Prompt:
  ```powershell
  python --version
  ```

## Setting up an IDE (optional)

### VS Code

1. Install VS Code: https://code.visualstudio.com/
2. Install the Microsoft **Python** extension.
3. Open the project and select the Python interpreter (Ctrl+Shift+P → *Python: Select Interpreter*).

## Dependencies

To run the analysis script, you need `pandas`:

```bash
pip install pandas
```

If you prefer, you can install everything via `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Expected data structure

The script reads CSV files under `Results/` with the following structure:

```
Results/
  deepseck_results/
    <project>/
      zero-*.csv
      few-*.csv
  openai_results/
    <project>/
      zero-*.csv
      few-*.csv
```

Each CSV must contain the columns:

- `Microservice`
- `Responsibilities`
- `Communicates With`

## How to run

1. (Optional) Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install pandas
   ```

3. Run the script:
   ```bash
   python analise.py
   ```

## Generated outputs

After execution, the script produces:

- `results_per_project.csv`: metrics computed per project/file.
- `results_summary.csv`: aggregates by model and setting (zero/few-shot).

Results are also printed in the terminal.

## Optional adjustments

If needed, you can adjust constants at the top of `analise.py`, such as:

- `BASE_DIR`: base path where result folders live.
- `MODELS`: mapping of model names to subfolders.
- `COMM_SEPARATOR`: separator used in the `Communicates With` column.

## Folder documentation

- See `Results/README.md` for details about result organization.
- See `deepseck/README.md` and `openai/README.md` for notebook-specific guidance.

## How to add these changes to your repository

If you cloned this repository and want to apply these changes to your own remote repository, follow this flow:

```bash
git status
git add README.md Results/README.md deepseck/README.md openai/README.md
git commit -m "Update project documentation"
git remote -v
git push origin HEAD
```

> **Tip**: if your remote repository uses a different name (for example `upstream`), replace `origin` in the `git push` command.
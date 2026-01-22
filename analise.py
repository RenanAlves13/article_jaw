import os
import pandas as pd

# =====================================================
# AJUSTE AQUI (se necessário)
# =====================================================
BASE_DIR = "Results"

MODELS = {
    "deepseck": "deepseck_results",
    "openai": "openai_results"
}

# Nomes das colunas no seu CSV (como você mostrou)
SERVICE_COL = "Microservice"
RESP_COL = "Responsibilities"
COMM_COL = "Communicates With"

# Separador dos serviços na coluna "Communicates With"
COMM_SEPARATOR = ";"


# =====================================================
# FUNÇÕES AUXILIARES
# =====================================================
def count_words(text):
    if pd.isna(text):
        return 0
    return len(str(text).split())


def unique_words(text):
    if pd.isna(text):
        return set()
    return set(str(text).lower().split())


def parse_communications(cell):
    if pd.isna(cell) or str(cell).strip() == "":
        return []
    return [x.strip() for x in str(cell).split(COMM_SEPARATOR) if x.strip()]


def find_setting_file(project_path: str, prefix: str) -> str | None:
    """
    Retorna o caminho do arquivo CSV dentro de project_path que começa com `prefix`
    Ex.: prefix='zero-' encontra 'zero-openai-project-one-results.csv'
    """
    for f in os.listdir(project_path):
        if f.lower().startswith(prefix) and f.lower().endswith(".csv"):
            return os.path.join(project_path, f)
    return None


# =====================================================
# MÉTRICAS POR CSV
# =====================================================
def compute_metrics(csv_path):
    df = pd.read_csv(csv_path)

    # Serviços (nós)
    n_services = df[SERVICE_COL].nunique()

    # Comunicações (arestas)
    df["comm_list"] = df[COMM_COL].apply(parse_communications)
    df["comm_count"] = df["comm_list"].apply(len)

    total_comms = int(df["comm_count"].sum())
    avg_comms = float(df["comm_count"].mean())
    isolated_services = int((df["comm_count"] == 0).sum())

    density = 0.0
    if n_services > 1:
        density = total_comms / (n_services * (n_services - 1))

    # Responsabilidades (texto)
    df["resp_word_count"] = df[RESP_COL].apply(count_words)
    avg_resp_length = float(df["resp_word_count"].mean())

    # Vocabulário simples
    df["resp_vocab"] = df[RESP_COL].apply(unique_words)
    avg_vocab_size = float(df["resp_vocab"].apply(len).mean())

    # Redundância lexical simples (proxy)
    all_words = []
    for vocab in df["resp_vocab"]:
        all_words.extend(list(vocab))

    if len(all_words) == 0:
        redundancy_ratio = 0.0
    else:
        word_freq = pd.Series(all_words).value_counts()
        top_words = set(word_freq.head(10).index)
        services_sharing_top_words = sum(
            1 for vocab in df["resp_vocab"] if vocab.intersection(top_words)
        )
        redundancy_ratio = services_sharing_top_words / n_services if n_services > 0 else 0.0

    return {
        "services": n_services,
        "total_comms": total_comms,
        "avg_comms": avg_comms,
        "density": density,
        "isolated_services": isolated_services,
        "avg_resp_length": avg_resp_length,
        "avg_vocab_size": avg_vocab_size,
        "redundancy_ratio": redundancy_ratio
    }


# =====================================================
# EXECUÇÃO COMPLETA
# =====================================================
results = []
missing = []

for model_name, model_folder in MODELS.items():
    model_path = os.path.join(BASE_DIR, model_folder)

    for project in os.listdir(model_path):
        project_path = os.path.join(model_path, project)
        if not os.path.isdir(project_path):
            continue

        zero_file = find_setting_file(project_path, "zero-")
        few_file = find_setting_file(project_path, "few-")

        if zero_file is None:
            missing.append((model_name, project, "zero"))
        else:
            metrics = compute_metrics(zero_file)
            metrics.update({
                "model": model_name,
                "project": project,
                "setting": "zero_shot",
                "file": os.path.basename(zero_file)
            })
            results.append(metrics)

        if few_file is None:
            missing.append((model_name, project, "few"))
        else:
            metrics = compute_metrics(few_file)
            metrics.update({
                "model": model_name,
                "project": project,
                "setting": "few_shot",
                "file": os.path.basename(few_file)
            })
            results.append(metrics)

df_results = pd.DataFrame(results)

# =====================================================
# AGREGAÇÃO FINAL (por modelo e setting)
# =====================================================
summary = df_results.groupby(["model", "setting"]).agg({
    "services": ["mean", "std"],
    "total_comms": ["mean", "std"],
    "avg_comms": ["mean", "std"],
    "density": ["mean", "std"],
    "isolated_services": ["mean"],
    "avg_resp_length": ["mean", "std"],
    "avg_vocab_size": ["mean", "std"],
    "redundancy_ratio": ["mean", "std"]
}).round(4)

print("\n=== RESULTADOS POR PROJETO/ARQUIVO ===")
print(df_results)

print("\n=== RESUMO POR MODELO E SETTING ===")
print(summary)

if missing:
    print("\n=== ARQUIVOS NÃO ENCONTRADOS (verifique prefixos ou pastas) ===")
    for m in missing:
        print(m)

# Salvar resultados
df_results.to_csv("results_per_project.csv", index=False)
summary.to_csv("results_summary.csv")

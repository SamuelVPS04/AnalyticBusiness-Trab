import os
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from pandas.plotting import scatter_matrix
from scipy import stats
from datetime import datetime

# ✅ Fonte compatível com caracteres especiais
plt.rcParams["font.family"] = "DejaVu Sans"


# ===========================
# CRIAÇÃO DE DIRETÓRIOS
# ===========================
def ensure_dirs():
    os.makedirs("../outputs/figures", exist_ok=True)
    os.makedirs("../outputs/report", exist_ok=True)
    os.makedirs("../outputs/tables", exist_ok=True)


# ===========================
# LEITURA COM DETECÇÃO DE ENCODING (SIMPLIFICADA)
# ===========================
def read_dataset(path="../data/top_100_players.csv"):
    # Tenta primeiro cp1252 (muito comum em dados da Steam/Windows)
    try:
        df = pd.read_csv(path, encoding="cp1252")
        print("✅ CSV carregado com encoding: cp1252")
        return df
    except UnicodeDecodeError:
        pass

    # Fallbacks se cp1252 não funcionar
    encodings = ["utf-8", "latin1", "ISO-8859-1"]
    for enc in encodings:
        try:
            df = pd.read_csv(path, encoding=enc)
            print(f"✅ CSV carregado com encoding: {enc}")
            return df
        except UnicodeDecodeError:
            continue

    raise ValueError("❌ Nenhuma codificação compatível encontrada para o arquivo.")


# ===========================
# DETECÇÃO DE OUTLIERS
# ===========================
def detect_outliers_iqr(series, k=1.5):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    outliers = ((series < lower) | (series > upper))
    return outliers, lower, upper


# ===========================
# GERAÇÃO DOS GRÁFICOS
# ===========================
def generate_plots(df):
    saved = []
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

    # ======================
    # HISTOGRAMAS
    # ======================
    for col in numeric_cols[:6]:
        plt.figure(figsize=(8, 5))
        sns.histplot(df[col], kde=True, line_kws={"linewidth": 1.2})

        plt.title(f"Histograma: {col}", fontsize=13, fontweight="bold")
        plt.xlabel(col, fontsize=10, fontweight="bold")
        plt.ylabel("Frequência", fontsize=10, fontweight="bold")

        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)

        plt.tight_layout()
        fname = f"../outputs/figures/hist_{col}.png"
        plt.savefig(fname, dpi=150)
        plt.close()
        saved.append(fname)

    # ======================
    # GRÁFICOS CATEGÓRICOS (CORRIGIDOS)
    # ======================
    for col in cat_cols[:6]:
        vc = df[col].value_counts().reset_index()
        vc.columns = [col, "count"]

        plt.figure(figsize=(14, 7))

        sns.barplot(
            data=vc,
            x=col,
            y="count",
            order=vc[col]
        )

        plt.title(f"Categorias: {col}", fontsize=13, fontweight="bold", pad=15)
        plt.xlabel(col, fontsize=10, fontweight="bold", labelpad=15)
        plt.ylabel("Frequência", fontsize=10, fontweight="bold", labelpad=15)

        plt.xticks(fontsize=8, rotation=65, ha='right')
        plt.yticks(fontsize=8)

        plt.tick_params(axis='x', pad=10)
        plt.tick_params(axis='y', pad=8)

        plt.tight_layout()
        fname = f"../outputs/figures/cat_{col}.png"
        plt.savefig(fname, dpi=150)
        plt.close()
        saved.append(fname)

    # ======================
    # HEATMAP DE CORRELAÇÃO
    # ======================
    if len(numeric_cols) >= 2:
        plt.figure(figsize=(8, 6))
        corr = df[numeric_cols].corr()

        sns.heatmap(
            corr,
            annot=True,
            fmt=".2f",
            linewidths=0.4,
            square=True,
            annot_kws={"size": 7}
        )

        plt.title("Correlação entre Variáveis", fontsize=14, fontweight="bold")
        plt.xticks(fontsize=7, rotation=45, ha='right')
        plt.yticks(fontsize=7)

        plt.tight_layout()
        fname = "../outputs/figures/heatmap_corr.png"
        plt.savefig(fname, dpi=150)
        plt.close()
        saved.append(fname)

    # ======================
    # PCA + KMEANS
    # ======================
    if numeric_cols:
        X = df[numeric_cols].dropna()

        X_scaled = StandardScaler().fit_transform(X)
        X_pca = PCA(n_components=2).fit_transform(X_scaled)

        k = min(5, max(2, int(math.sqrt(len(X)))))
        labels = KMeans(n_clusters=k, n_init=10, random_state=42).fit_predict(X_pca)

        plt.figure(figsize=(8, 6))
        plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, alpha=0.7, s=30)

        plt.title(f"PCA + KMeans (k={k})", fontsize=14, fontweight="bold")
        plt.xlabel("PCA 1", fontsize=10, fontweight="bold")
        plt.ylabel("PCA 2", fontsize=10, fontweight="bold")

        plt.xticks(fontsize=7)
        plt.yticks(fontsize=7)

        plt.tight_layout()
        fname = "../outputs/figures/pca_kmeans.png"
        plt.savefig(fname, dpi=150)
        plt.close()
        saved.append(fname)

    return saved


# ===========================
# GERAÇÃO DO RELATÓRIO PDF
# ===========================
def generate_pdf(df, figs):
    sections = {
        "Introdução": f"EDA dataset com {df.shape[0]} linhas",
        "Estatísticas": str(df.describe())
    }

    pdf_path = "../outputs/report/eda_report.pdf"

    with PdfPages(pdf_path) as pdf:
        for title, text in sections.items():
            plt.figure(figsize=(8, 10))
            plt.axis("off")
            plt.title(title, fontsize=14, fontweight="bold")
            plt.text(0.01, 0.5, text, fontsize=9)
            pdf.savefig()
            plt.close()

        for fig in figs:
            try:
                img = plt.imread(fig)
                plt.figure(figsize=(8, 6))
                plt.imshow(img)
                plt.axis("off")
                pdf.savefig()
                plt.close()
            except:
                pass

    return pdf_path


# ===========================
# EXECUÇÃO PRINCIPAL
# ===========================
if __name__ == "__main__":
    ensure_dirs()
    df = read_dataset()

    # ✅ FILTRAR 50 MELHORES COM BASE NO RATING
    if "rating" in df.columns:
        df = df.sort_values(by="rating", ascending=False).head(50)
    elif "Rating" in df.columns:
        df = df.sort_values(by="Rating", ascending=False).head(50)
    else:
        print("⚠ Coluna de rating não encontrada! Verifique o nome no CSV.")

    figs = generate_plots(df)
    pdf_file = generate_pdf(df, figs)

    print("✅ PDF gerado:", pdf_file)
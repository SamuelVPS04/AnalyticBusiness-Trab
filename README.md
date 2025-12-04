# Análise Exploratória de Dados (EDA) – Top 100 Players

Este repositório contém um projeto de **Análise Exploratória de Dados (EDA)** aplicado a uma base com os 100 jogadores mais bem ranqueados em um sistema de pontuação (`CS Rating`).  
O objetivo principal é praticar e demonstrar, na prática, as principais técnicas de EDA vistas em aula.

---

## 1. Descrição do Projeto

**Base de dados:** `data/top_100_players.csv`  

Cada linha representa um jogador do Top 100, com as seguintes variáveis principais:

- `Rank` – posição do jogador no ranking (1–100).
- `Name` – nome/nickname do jogador.
- `CS Rating` – rating do jogador (pontuação, originalmente armazenado como texto).
- `Region` – região geográfica (Europa, Ásia, América do Norte, etc.).
- `Wins` – número de vitórias.
- `Ties` – número de empates.
- `Losses` – número de derrotas.

**Objetivos da análise:**

- Entender a **estrutura** do dataset (dimensão, tipos de dados, nulos, duplicatas).
- Calcular **estatísticas descritivas** das variáveis numéricas.
- Realizar **limpeza e preparação** (conversão de tipos, tratamento básico).
- Explorar **distribuições** de variáveis numéricas (Rank, Wins, Ties, Losses, CS Rating).
- Analisar **categorias** (regiões, nomes, faixas de rating).
- Investigar **correlações** entre variáveis numéricas.
- Identificar possíveis **outliers** (via IQR).
- Verificar **segmentações naturais** por meio de **PCA + KMeans** (clusters visuais).

O projeto gera:

- Gráficos exploratórios (histogramas, boxplots, countplots, heatmap, PCA + KMeans).
- Um **notebook Jupyter** com a análise passo a passo.
- Um **script Python** que automatiza a geração dos gráficos.
- (Opcional) Um relatório em **PDF** consolidando as figuras.

---

## 2. Estrutura do Repositório

```text
TrabalhoEDA/
│
├── data/
│   └── top_100_players.csv        # Base de dados utilizada na análise
│
├── notebooks/
│   └── eda_trabalho.ipynb         # Notebook Jupyter com a análise EDA completa
│
├── src/
│   └── eda_trabalho.py            # Script Python que gera os gráficos e (opcionalmente) o PDF
│
├── outputs/                       # (Opcional) Artefatos gerados pela análise
│   ├── figures/                   # Arquivos PNG com os gráficos
│   └── report/                    # Relatório final
│   └── eda_report.pdf             # Relatório final em PDF (se gerado)
>>>>>>> 4d8c6dc (Atualiza README e .gitignore do projeto EDA)
│
├── requirements.txt               # Lista de dependências Python do projeto
└── README.md                      # Este arquivo
```

> Observação: a pasta `outputs/` pode não existir no primeiro clone; ela é criada quando o script é executado.

---

## 3. Pré‑requisitos

Para executar o projeto localmente, você precisa de:

- **Python 3.12** (ou outra versão 3.10+ compatível).
- **Git** instalado (para clonar o repositório).
- Navegador moderno (Chrome, Firefox, Edge etc.) para abrir o Jupyter Notebook.

Opcional, mas recomendado:

- Editor/IDE como **PyCharm**, **VS Code** ou similar para editar os arquivos `.py` e `.ipynb`.

---

## 4. Configuração do Ambiente

### 4.1. Clonar o repositório

No terminal:

```bash
git clone https://github.com/SamuelVPS04/AnalyticBusiness-Trab.git
cd AnalyticBusiness-Trab
```

(Se o nome/URL do repositório for diferente, ajuste o comando de acordo.)

### 4.2. Criar e ativar um ambiente virtual

Recomendado para evitar conflitos com o Python do sistema.

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell / CMD):**

```bash
python -m venv .venv
.\.venv\Scriptsctivate
```

Você deve ver `(.venv)` no início da linha do terminal após ativar.

### 4.3. Instalar as dependências

Com o ambiente virtual **ativo**, execute:

```bash
pip install -r requirements.txt
```

Os principais pacotes instalados são:

- `pandas` – manipulação de dados/tabulares.
- `numpy` – operações numéricas.
- `matplotlib` e `seaborn` – visualizações.
- `scikit-learn` – PCA, KMeans e outras técnicas de machine learning.
- `scipy` – suporte estatístico.
- `jupyter` e `ipykernel` – execução do notebook.

---

## 5. Executando o Notebook Jupyter

O **notebook** é a forma principal de visualizar e documentar a análise.

Com o ambiente virtual ainda ativo:

```bash
jupyter notebook
```

Isso abrirá a interface do Jupyter no seu navegador (ou mostrará uma URL `http://localhost:8888/...` que você pode copiar e colar).

No navegador:

1. Navegue até a pasta `notebooks/`.
2. Abra o arquivo `eda_trabalho.ipynb`.
3. No menu do Jupyter, selecione o kernel asociado ao seu ambiente virtual, se necessário
   (por exemplo, *Python (TrabalhoEDA)*).
4. Execute as células em ordem (atalho: `Shift + Enter`).

O notebook contém:

- **Carregamento dos dados** (`top_100_players.csv`).
- **Análise estrutural**:
  - `df.shape`, `df.info()`, `df.isna().sum()`, duplicatas.
- **Estatísticas descritivas** (`df.describe()`).
- **Identificação de outliers** (via IQR).
- **Limpeza / preparação**:
  - Conversão de `CS Rating` para numérico.
  - Criação opcional de novas variáveis (ex.: total de partidas).
- **Visualizações numéricas**:
  - Histogramas de Rank, Wins, Ties, Losses, CS Rating.
  - Boxplots por região, distribuições de densidade (KDE) etc.
- **Visualizações categóricas**:
  - Distribuição por `Region`, `Name`, faixas de rating, etc.
- **Visualizações avançadas**:
  - Heatmap de correlação.
  - Pairplot (scatterplot matricial) para variáveis numéricas.
  - PCA + KMeans (2 componentes) para identificar clusters visuais.
- **Comentários e conclusões intermediárias** em células de texto (Markdown).

---

## 6. Executando o Script Python

Se quiser rodar a análise diretamente via script (sem abrir o notebook):

No diretório raiz do projeto, com o ambiente virtual ativo:

```bash
python src/eda_trabalho.py
```

O script realizará, de forma automatizada:

1. Carregamento de `data/top_100_players.csv`.
2. Impressão das informações estruturais básicas no console.
3. Geração de gráficos (histogramas, gráficos categóricos, heatmap, PCA + KMeans).
4. Salvamento dos gráficos em `outputs/figures/`:
   - `hist_Rank.png`
   - `hist_Wins.png`
   - `hist_Ties.png`
   - `hist_Losses.png`
   - `cat_Region.png`
   - `cat_Name.png`
   - `cat_CS Rating.png`
   - `heatmap_corr.png`
   - `pca_kmeans.png`
   - (entre outros, conforme configurado no script)
5. (Opcional) Geração de um relatório consolidado em PDF, se essa funcionalidade estiver ativada no código.

Após a execução, consulte a pasta `outputs/figures/` e `outputs/` para visualizar os resultados.

---

## 7. Como Reproduzir a Análise do Relatório

Para acompanhar o relatório acadêmico entregue:

1. Abra o notebook `notebooks/eda_trabalho.ipynb`.
2. Execute as células na sequência:
   - **Seção 1** – Introdução e carregamento de dados.
   - **Seção 2** – Análise estrutural (shape, tipos, nulos, duplicatas, estatísticas).
   - **Seção 3** – Limpeza e preparação.
   - **Seção 4** – Visualizações numéricas.
   - **Seção 5** – Visualizações categóricas.
   - **Seção 6** – Visualizações avançadas (heatmap, pairplot, PCA + KMeans).
   - **Seção 7** – Síntese dos principais insights.
3. Compare os gráficos gerados com aqueles incluídos no relatório em PDF.

Dessa forma, qualquer pessoa consegue **reproduzir integralmente** a análise a partir do código.

---

## 8. Objetivo Acadêmico

Este projeto foi desenvolvido como trabalho da disciplina de **Analytics / Business Analytics**, com os seguintes objetivos pedagógicos:

- Aplicar as etapas completas de **Análise Exploratória de Dados (EDA)**.
- Praticar o uso de bibliotecas Python voltadas para análise de dados.
- Desenvolver **visualizações claras e interpretáveis**, adequadas a um relatório acadêmico.
- Extrair **insights** sobre o comportamento dos jogadores de alto desempenho.
- Produzir um **relatório estruturado** (PDF) e um **notebook reprodutível** (Jupyter) documentando o processo.

---

## 9. Possíveis Extensões

Algumas ideias para quem quiser expandir o projeto:

- Incluir dados de **outras temporadas** ou modos de jogo.
- Incorporar **variáveis temporais** (evolução do rating ao longo do tempo).
- Testar outros algoritmos de **clustering** além do KMeans.
- Construir um **modelo preditivo** (por exemplo, para prever faixa de rating com base em vitórias/derrotas e região).

---

Se encontrar qualquer problema de execução ou quiser sugerir melhorias, sinta‑se à vontade para abrir uma *issue* ou fazer um *fork* deste repositório.

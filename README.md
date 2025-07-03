# 🔥 Metody Nauki – Transformery w Pythonie (Jupyter Lab)

[![Język](https://img.shields.io/badge/język-polski-blue.svg)](https://github.com/USER/learning-methods-transformers)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![JupyterLab](https://img.shields.io/badge/JupyterLab-4.x-orange.svg)](https://jupyter.org/)
[![Transformers](https://img.shields.io/badge/🤗%20Transformers-4.40-yellow.svg)](https://huggingface.co/docs/transformers/index)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.1-red.svg)](https://pytorch.org/)

> **Cel drugiej prezentacji (Python + Jupyter):**
> Pokazać, jak **duże modele językowe (LLM)** pomagają odpowiedzieć na pytanie
> _“Która metoda nauki działa najlepiej?”_ na bazie zbioru **Student Performance & Learning Style**.
> Dodatkowo analizujemy **opinie o kursach** z publicznego zbioru z Hugging Face.

---

## 🗄️ Struktura projektu

Przejrzysta organizacja plików i katalogów ułatwia nawigację i zrozumienie projektu.

```
learning-methods-transformers/
├── 📂 data/                  # Zbiory danych
│   ├── student-math-learning.csv    # Kaggle
│   ├── course_reviews.csv           # Opinie o kursach
│   ├── peer_reviews.csv             # Recenzje studentów (HF)
│   └── yelp_reviews.csv             # Duży zbiór opinii (HF)
├── 📂 notebooks/             # Główne pliki analizy
│   ├── 01_data_exploration.ipynb  # Wstępna eksploracja (Pandas)
│   ├── 02_zero_shot.ipynb         # Klasyfikacja zero-shot (BART)
│   ├── 03_sentiment.ipynb         # Analiza sentymentu (distilRoBERTa)
│   ├── 04_text_generation.ipynb   # Generowanie tekstu (GPT-2 / Mistral-7B)
│   └── 05_dashboard.ipynb         # Interaktywny interfejs (Gradio)
├── 📂 src/                   # Kod pomocniczy
│   ├── utils.py               # Wspólne funkcje (np. clean_text, load_data)
│   └── evaluate.py            # Metryki (accuracy, F1-score)
├── 📂 environments/          # Konfiguracja środowiska
│   └── environment.yml        # Specyfikacja dla Conda
├── 📜 install.sh             # Skrypt instalacyjny dla Linux/Mac
├── 📜 install.bat            # Skrypt instalacyjny dla Windows
├── 📄 README.md              # Dokumentacja projektu (tu jesteś 🙂)
└── 📄 .gitignore              # Pliki ignorowane przez Git
```

---

## 🚀 Szybki start (TL;DR)

Gotowy do działania w 3 krokach!

### 1. Klonowanie repozytorium

```bash
git clone https://github.com/USER/learning-methods-transformers.git
cd learning-methods-transformers
```

### 2. Instalacja środowiska (Conda)

Zalecana metoda wykorzystuje menedżer środowisk `conda`.

```bash
# Utwórz środowisko na podstawie pliku .yml
conda env create -f environments/environment.yml

# Aktywuj środowisko
conda activate learn-tx
```

### 3. Pobranie danych i uruchomienie JupyterLab

Skrypt `download_reviews.py` pobierze opinie o kursach z serwisu Hugging Face.
Jeśli potrzebujesz większych zbiorów tekstów z opiniami, skorzystaj z
`download_peer_reviews.py` (recenzje studentów) lub `download_yelp.py`
(kilkaset tysięcy recenzji z serwisu Yelp).

```bash
# Opinie o kursach (mniejsze ~10k rekordów)
python scripts/download_reviews.py
# Recenzje studentów (~13k rekordów)
python scripts/download_peer_reviews.py
# Yelp – duży zbiór recenzji (650k+)
# python scripts/download_yelp.py
jupyter lab
```
Po uruchomieniu przejdź kolejno przez notebooki w katalogu `notebooks/`.

> **Uwaga:** Jeśli instalacja `conda` nie wchodzi w grę, zobacz sekcję [**🪄 Alternatywa: `venv` + `pip`**](#-alternatywa-venv--pip).

---

## ⚙️ Zależności techniczne

Projekt opiera się na popularnych bibliotekach do analizy danych i uczenia maszynowego.

| Narzędzie         | Wersja (minimum) | Uwagi                               |
| ----------------- | ---------------- | ----------------------------------- |
| **Python**        | `3.10`           | Testowane na `3.10` / `3.11`        |
| **JupyterLab**    | `4.x`            | Wersja zdefiniowana w `environment.yml` |
| **PyTorch**       | `2.1`            | Automatyczne wykrywanie GPU (CUDA 11.8) |
| **Transformers**  | `4.40`           | `pip install transformers[torch]`   |
| **Datasets**      | `2.19`           | Łatwe ładowanie plików CSV          |
| **Gradio**        | `4.31`           | Budowa interaktywnego demo          |
| **scikit-learn**  | `latest`         | Klasyczne metryki ML                |
| **pandas**        | `latest`         | Manipulacja danymi                  |

---

## 📒 Opis notebooków

Każdy notebook odpowiada za konkretny etap analizy i jest powiązany z slajdami w prezentacji.

| Nr | Notebook                 | Slajd w prezentacji | Co pokazujemy                                       |
| -- | ------------------------ | ------------------- | --------------------------------------------------- |
| 01 | `Data Exploration`       | 1–4                 | `shape`, `nulls`, rozkład GPA, liczność metod nauki |
| 02 | `Zero-shot Classification` | 5–9                 | `facebook/bart-large-mnli` → predykcja `learning_style` |
| 03 | `Sentiment Analysis`     | 10–12               | `cardiffnlp/twitter-roberta-base-sentiment` → wykres  |
| 04 | `Text Generation`        | 13–15               | Prompt-engineering i sampling (`temp`, `top_p`)     |
| 05 | `Summarization`        | 16–17               | BART: streszczenie tekstu |
| 06 | `Question Answering`   | 18–19               | DistilBERT: odpowiedzi na pytania |
| 07 | `Reviews Transformers` | 20–22               | Analiza recenzji z CSV: sentiment, streszczenia |
| –  | **Podsumowanie**         | 23                  | Główne wnioski i propozycje kolejnych kroków       |

---

## 📊 Główne wyniki (TL;DR)

- **Klasyfikacja zero-shot:** Trafność ≈ **78%** (macro F1) dla 4 głównych metod nauki.
- **Korelacja z GPA:** Studenci deklarujący _“spaced repetition”_ mają **+0.27 GPA** (mediana) w porównaniu do reszty.
- **Analiza emocji (NRC):** W opisach najlepszych metod dominują _“anticipation”_ i _“trust”_.
- **Generowanie tekstu:** Modele generują uzasadnienia, które pokrywają się z tematami LDA z pierwszej prezentacji.
- **Interaktywne demo:** Gotowy interfejs w Gradio ułatwia demonstrację wyników na żywo.

---

## 🪄 Alternatywa: `venv` + `pip`

Jeśli nie używasz `conda`, możesz skorzystać z wirtualnego środowiska `venv`.

```bash
# Utwórz środowisko
python -m venv .venv

# Aktywuj środowisko (Linux/Mac)
source .venv/bin/activate
# Dla Windows: .venv\Scripts\activate

# Zainstaluj zależności
pip install -r environments/requirements.txt  # zawiera m.in. nltk i wordcloud
```

> **GPU?** Zmień `torch` na `torch==2.1.2+cu118` zgodnie z oficjalną instrukcją:  
> [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)

# 🔥 Learning Methods – Transformers in Python (Jupyter Lab)

> **Cel drugiej prezentacji (Python + Jupyter):**  
>  Pokazać, jak **duże modele językowe (LLM)** pomagają odpowiedzieć na pytanie  
>  _“Która metoda nauki działa najlepiej?”_ na bazie zbioru **Student Performance & Learning Style**.

---

## 🗄️ Struktura projektu

learning-methods-transformers/
├── data/ # CSV pobrany z Kaggle
│ └── student-math-learning.csv
├── notebooks/
│ ├── 01_data_exploration.ipynb # wstępna eksploracja Pandas
│ ├── 02_zero_shot.ipynb # zero-shot classification (BART)
│ ├── 03_sentiment.ipynb # sentiment transformer (distilRoBERTa)
│ ├── 04_text_generation.ipynb # generowanie promptów (GPT-2 / mistral-7B-instruct)
│ └── 05_dashboard.ipynb # prosty interfejs Gradio
├── src/
│ ├── utils.py # wspólne funkcje (clean_text, load_data…)
│ └── evaluate.py # metryki accuracy / f1 dla learning_style
├── environments/
│ └── environment.yml # specyfikacja Conda
├── install.sh # 1-click setup (Linux/Mac)
├── install.bat # 1-click setup (Windows)
├── README.md # ← tu jesteś 🙂
└── .gitignore

## 🚀 Szybki start (TL;DR)

# 0) klon repo
git clone https://github.com/USER/learning-methods-transformers.git
cd learning-methods-transformers

# 1) środowisko Conda
conda env create -f environments/environment.yml
conda activate learn-tx

# 2) pobranie CSV z Kaggle
bash scripts/setup_kaggle.sh     # ustawia token + download + unzip

# 3) uruchom JupyterLab
jupyter lab
# ...i przejdź kolejno przez notebooki w katalogu notebooks/

Uwaga: jeśli instalacja Conda nie wchodzi w grę – patrz sekcja “🪄 Alternatywa: venv + pip”.

⚙️ Zależności techniczne
Tool	Minimum	Notes
Python	3.10	testowane 3.10/3.11
JupyterLab	4.x	w environment.yml
PyTorch (+ CUDA 11.8)	2.1	auto-detect GPU
Transformers (HF)	4.40	pip install transformers[torch]
Datasets	2.19	łatwe ładowanie CSV
Gradio	4.31	demo UI
scikit-learn, pandas	latest	klasyka ML

📒 Notebooki – opis slajdów
Nr	Notebook	Slajd w prezentacji	Co pokazujemy
01	Data Exploration	1–4	shape, nulls, GPA distrib, liczność metod nauki
02	Zero-shot Classification	5–9	facebook/bart-large-mnli → predykcja learning_style
03	Sentiment	10–12	cardiffnlp/twitter-roberta-base-sentiment → wykres słupkowy
04	Text Generation	13–15	prompt-engineering + sampling (temp, top_p)
05	Dashboard	16–17	Gradio – wpisz opis metody → zwrot: label + sentiment
まとめ (Summary)	18	bullet-points + kolejne kroki

📊 Wyniki (TL;DR)
Zero-shot trafność ≈ 78 % (macro F1) dla 4 głównych metod nauki.
Studenci deklarujący “spaced repetition” mają +0.27 GPA (median) vs. reszta.
Emocje NRC: dominują “anticipation” i “trust” w opisach najlepszych metod.
Modele generują uzasadnienia, które pokrywają się z tematami LDA z prezentacji #1.
Gotowy Gradio interfejs → łatwa demonstracja na konsultacjach.

🪄 Alternatywa: venv + pip

python -m venv .venv
source .venv/bin/activate
pip install -r environments/requirements.txt

GPU? Zmień torch na torch==2.1.2+cu118 zgodnie z instrukcją:
https://pytorch.org/get-started/locally/



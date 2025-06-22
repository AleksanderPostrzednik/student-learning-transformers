@echo off
IF EXIST "%CONDA_EXE%" (
    conda env create -f environments\environment.yml
    echo Activate with: conda activate learn-tx
) ELSE (
    python -m venv .venv
    call .venv\Scripts\activate
    pip install -r environments\requirements.txt
)

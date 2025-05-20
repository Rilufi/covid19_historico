
# Análise Histórica da COVID-19 no Brasil

Este repositório contém gráficos gerados a partir de dois conjuntos de dados diferentes sobre a pandemia de COVID-19 no Brasil:

- **Our World in Data** (`owid-covid-data.csv`)
- **Kaggle - wcota/covid19br** (`brazil_covid19.csv`)

## Scripts

- `script_kaggle.py`: gera gráficos históricos com base nos dados do Kaggle.
- `script_owid.py`: gera gráficos históricos com base nos dados do OWID.

## Como Executar

Ambos os scripts podem ser executados via GitHub Actions manualmente (workflow_dispatch). Após a execução, os gráficos estarão na pasta `imgs/`.

## Gráficos Produzidos

- Casos e mortes acumuladas
- Novos casos por dia
- Novas mortes por dia
- Vacinação total (OWID)

## Workflows

Estão incluídos dois workflows que você pode acionar manualmente na aba *Actions* do GitHub:

- `.github/workflows/owid.yml`
- `.github/workflows/kaggle.yml`

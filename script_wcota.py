import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import requests
from io import StringIO
from matplotlib.dates import DateFormatter
import seaborn as sns

# Configurações iniciais
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 100
plt.rcParams['savefig.dpi'] = 300

# Criar diretórios
img_dir = Path("imgs")
img_dir.mkdir(parents=True, exist_ok=True)

# URL do dataset
url = "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv"

# Download dos dados
headers = {"User-Agent": "Mozilla/5.0 (GitHub Actions - COVID Bot)"}
response = requests.get(url, headers=headers)

if response.status_code != 200:
    raise Exception(f"Erro ao baixar dados: {response.status_code}")

# Processamento dos dados
df = pd.read_csv(StringIO(response.text))
df["date"] = pd.to_datetime(df["date"])
df = df[["date", "state", "newCases", "newDeaths", "deaths_per_100k_inhabitants"]].dropna()

# Dados nacionais semanais
br = df.groupby("date")[["newCases", "newDeaths"]].sum().resample("W").sum()
br["letalidade"] = (br["newDeaths"] / br["newCases"]) * 100

# Gráfico 1: Casos semanais
plt.figure(figsize=(12, 6))
br["newCases"].plot(color='#1f77b4', linewidth=2)
plt.title("Casos Semanais de COVID-19 no Brasil", pad=20, fontsize=14)
plt.ylabel("Casos por semana", labelpad=10)
plt.xlabel("")
plt.tight_layout()
plt.savefig(img_dir / "brasil_casos_semanais.png", bbox_inches='tight', transparent=True)
plt.close()

# Gráfico 2: Mortes semanais
plt.figure(figsize=(12, 6))
br["newDeaths"].plot(color='#d62728', linewidth=2)
plt.title("Óbitos Semanais de COVID-19 no Brasil", pad=20, fontsize=14)
plt.ylabel("Óbitos por semana", labelpad=10)
plt.xlabel("")
plt.tight_layout()
plt.savefig(img_dir / "brasil_mortes_semanais.png", bbox_inches='tight', transparent=True)
plt.close()

# Gráfico 3: Taxa de letalidade
plt.figure(figsize=(12, 6))
br["letalidade"].plot(color='#2ca02c', linewidth=2)
plt.title("Taxa de Letalidade Semanal (%)", pad=20, fontsize=14)
plt.ylabel("Porcentagem", labelpad=10)
plt.xlabel("")
plt.tight_layout()
plt.savefig(img_dir / "brasil_letalidade_semanal.png", bbox_inches='tight', transparent=True)
plt.close()

# Análise por estados
estados = ["SP", "RJ", "RS", "BA", "MG", "CE", "PE", "PR"]
df_est = df[df["state"].isin(estados)].copy()
df_est = df_est.groupby(["date", "state"]).sum().reset_index()
df_est.set_index("date", inplace=True)
df_est = df_est.groupby("state")[["newCases", "newDeaths"]].resample("W").sum().reset_index()

# Formatação de datas
date_format = DateFormatter("%m/%Y")

# Gráfico 4: Casos por estado
plt.figure(figsize=(14, 7))
palette = sns.color_palette("husl", len(estados))
for i, estado in enumerate(estados):
    subset = df_est[df_est["state"] == estado]
    plt.plot(subset["date"], subset["newCases"], label=estado, 
             color=palette[i], linewidth=2, alpha=0.8)
    
plt.title("Casos Semanais por Estado", pad=20, fontsize=14)
plt.ylabel("Casos por semana", labelpad=10)
plt.legend(title="Estado", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.gca().xaxis.set_major_formatter(date_format)
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.savefig(img_dir / "estados_casos.png", bbox_inches='tight', transparent=True)
plt.close()

# Gráfico 5: Mortes por estado
plt.figure(figsize=(14, 7))
for i, estado in enumerate(estados):
    subset = df_est[df_est["state"] == estado]
    plt.plot(subset["date"], subset["newDeaths"], label=estado,
             color=palette[i], linewidth=2, alpha=0.8)
    
plt.title("Óbitos Semanais por Estado", pad=20, fontsize=14)
plt.ylabel("Óbitos por semana", labelpad=10)
plt.legend(title="Estado", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.gca().xaxis.set_major_formatter(date_format)
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.savefig(img_dir / "estados_mortes.png", bbox_inches='tight', transparent=True)
plt.close()

# Gráfico 6: Top 5 estados - mortes per capita
df_per_capita = df.groupby("state")["deaths_per_100k_inhabitants"].max().sort_values(ascending=False).head(5)
plt.figure(figsize=(12, 6))
df_per_capita.plot(kind='bar', color=sns.color_palette("Reds_r", 5))
plt.title("Top 5 Estados - Óbitos por 100 mil habitantes", pad=20, fontsize=14)
plt.ylabel("Óbitos por 100 mil hab.", labelpad=10)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(img_dir / "top5_obitos_per_capita.png", bbox_inches='tight', transparent=True)
plt.close()

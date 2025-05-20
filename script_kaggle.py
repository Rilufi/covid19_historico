
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Carrega o arquivo CSV do Kaggle (pré-carregado no repositório)
df = pd.read_csv("brazil_covid19.csv")
df['data'] = pd.to_datetime(df['data'])

# Pasta de imagens
img_dir = Path("imgs")
img_dir.mkdir(exist_ok=True)

# Gráfico 1: Casos e mortes acumuladas
plt.figure(figsize=(10, 5))
plt.plot(df['data'], df['casosAcumulado'], label='Casos Acumulados')
plt.plot(df['data'], df['obitosAcumulado'], label='Mortes Acumuladas')
plt.title("COVID-19 no Brasil (Kaggle): Casos e Mortes Acumuladas")
plt.xlabel("Data")
plt.ylabel("Total")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(img_dir / "acumulados_kaggle.png")
plt.close()

# Gráfico 2: Novos casos por dia
plt.figure(figsize=(10, 5))
plt.plot(df['data'], df['casosNovos'], color='orange')
plt.title("Novos Casos Diários (Kaggle)")
plt.xlabel("Data")
plt.ylabel("Casos por dia")
plt.grid(True)
plt.tight_layout()
plt.savefig(img_dir / "novos_casos_kaggle.png")
plt.close()

# Gráfico 3: Novas mortes por dia
plt.figure(figsize=(10, 5))
plt.plot(df['data'], df['obitosNovos'], color='red')
plt.title("Novas Mortes Diárias (Kaggle)")
plt.xlabel("Data")
plt.ylabel("Mortes por dia")
plt.grid(True)
plt.tight_layout()
plt.savefig(img_dir / "novas_mortes_kaggle.png")
plt.close()

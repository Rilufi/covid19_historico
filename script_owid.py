
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Carregar CSV local
df = pd.read_csv("owid-covid-data.csv")

# Filtrar Brasil
brasil = df[df['location'] == 'Brazil'].copy()
brasil['date'] = pd.to_datetime(brasil['date'])

# Criar pasta de saída
img_dir = Path("imgs")
img_dir.mkdir(exist_ok=True)

# Gráfico 1: Casos e mortes acumuladas
plt.figure(figsize=(10, 5))
plt.plot(brasil['date'], brasil['total_cases'], label='Casos Acumulados')
plt.plot(brasil['date'], brasil['total_deaths'], label='Mortes Acumuladas')
plt.title("COVID-19 no Brasil: Casos e Mortes Acumuladas")
plt.xlabel("Data")
plt.ylabel("Total")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(img_dir / "acumulados.png")
plt.close()

# Gráfico 2: Novos casos por dia
plt.figure(figsize=(10, 5))
plt.plot(brasil['date'], brasil['new_cases'], color='orange')
plt.title("Novos Casos Diários de COVID-19 no Brasil")
plt.xlabel("Data")
plt.ylabel("Casos por dia")
plt.grid(True)
plt.tight_layout()
plt.savefig(img_dir / "novos_casos.png")
plt.close()

# Gráfico 3: Novas mortes por dia
plt.figure(figsize=(10, 5))
plt.plot(brasil['date'], brasil['new_deaths'], color='red')
plt.title("Novas Mortes Diárias de COVID-19 no Brasil")
plt.xlabel("Data")
plt.ylabel("Mortes por dia")
plt.grid(True)
plt.tight_layout()
plt.savefig(img_dir / "novas_mortes.png")
plt.close()

# Gráfico 4: Vacinação total
plt.figure(figsize=(10, 5))
plt.plot(brasil['date'], brasil['total_vaccinations'], color='green')
plt.title("Total de Doses de Vacina Aplicadas no Brasil")
plt.xlabel("Data")
plt.ylabel("Doses acumuladas")
plt.grid(True)
plt.tight_layout()
plt.savefig(img_dir / "vacinacao.png")
plt.close()

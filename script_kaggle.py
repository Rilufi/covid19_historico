import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    try:
        # Carrega o arquivo CSV do Kaggle
        df = pd.read_csv("brazil_covid19.csv")
        
        # Verifica e mapeia nomes de colunas alternativos
        column_mapping = {
            'data': ['date', 'Data', 'datetime'],
            'casosAcumulado': ['totalCases', 'confirmed'],
            'obitosAcumulado': ['deaths', 'totalDeaths'],
            'casosNovos': ['newCases', 'confirmed_new'],
            'obitosNovos': ['newDeaths', 'deaths_new']
        }
        
        # Renomeia colunas para nomes consistentes
        for standard_name, alternatives in column_mapping.items():
            for alt in alternatives:
                if alt in df.columns:
                    df.rename(columns={alt: standard_name}, inplace=True)
                    break
        
        # Verifica se temos a coluna de data
        if 'data' not in df.columns:
            raise KeyError("Nenhuma coluna de data encontrada (verifique os nomes das colunas)")
        
        # Converte a coluna de data
        df['data'] = pd.to_datetime(df['data'])
        
        # Pasta de imagens
        img_dir = Path("data")
        img_dir.mkdir(exist_ok=True)
        
        # Gráfico 1: Casos e mortes acumuladas
        plt.figure(figsize=(12, 6))
        plt.plot(df['data'], df['casosAcumulado'], label='Casos Acumulados', linewidth=2)
        plt.plot(df['data'], df['obitosAcumulado'], label='Mortes Acumuladas', linewidth=2)
        plt.title("COVID-19 no Brasil: Casos e Mortes Acumuladas")
        plt.xlabel("Data")
        plt.ylabel("Total")
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig(img_dir / "acumulados_kaggle.png", dpi=300)
        plt.close()
        
        # Gráfico 2: Novos casos por dia
        plt.figure(figsize=(12, 6))
        plt.bar(df['data'], df['casosNovos'], color='orange', alpha=0.7, width=1.0)
        plt.title("Novos Casos Diários")
        plt.xlabel("Data")
        plt.ylabel("Casos por dia")
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig(img_dir / "novos_casos_kaggle.png", dpi=300)
        plt.close()
        
        # Gráfico 3: Novas mortes por dia (média móvel 7 dias)
        plt.figure(figsize=(12, 6))
        df['obitosNovos_ma7'] = df['obitosNovos'].rolling(7).mean()
        plt.bar(df['data'], df['obitosNovos'], color='red', alpha=0.3, width=1.0, label='Diário')
        plt.plot(df['data'], df['obitosNovos_ma7'], color='darkred', linewidth=2, label='Média Móvel 7 dias')
        plt.title("Novas Mortes Diárias")
        plt.xlabel("Data")
        plt.ylabel("Mortes por dia")
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig(img_dir / "novas_mortes_kaggle.png", dpi=300)
        plt.close()
        
        print("Gráficos gerados com sucesso!")
        
    except Exception as e:
        print(f"Erro ao processar os dados: {str(e)}")
        print("\nVerifique:")
        print("1. Se o arquivo 'brazil_covid19.csv' existe no diretório")
        print("2. As colunas presentes no arquivo CSV:")
        if 'df' in locals():
            print("\nColunas disponíveis:", df.columns.tolist())
        else:
            print("Não foi possível carregar o DataFrame")
        exit(1)

if __name__ == "__main__":
    main()

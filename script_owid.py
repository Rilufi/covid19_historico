import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.dates import DateFormatter, WeekdayLocator
from datetime import timedelta
from pathlib import Path
import os

# Configurações iniciais
plt.style.use('ggplot')
register_matplotlib_converters()

# Criar diretório de saída se não existir
output_dir = Path("data")
output_dir.mkdir(exist_ok=True)

# Função para formatar números grandes
def reformat_large_tick_values(tick_val, pos):
    if tick_val >= 1000000:
        val = round(tick_val/1000000, 1)
        new_tick_format = '{:}M'.format(val)
    elif tick_val >= 1000:
        val = round(tick_val/1000, 1)
        new_tick_format = '{:}K'.format(val)
    else:
        new_tick_format = tick_val
    
    new_tick_format = str(new_tick_format)
    index_of_decimal = new_tick_format.find(".")
    
    if index_of_decimal != -1:
        value_after_decimal = new_tick_format[index_of_decimal+1]
        if value_after_decimal == "0":
            new_tick_format = new_tick_format[0:index_of_decimal] + new_tick_format[index_of_decimal+2:]
    
    return new_tick_format

# Função para criar gráficos
def create_plot(data, countries, main_country, y_col, title, ylabel, filename, 
                colors=None, alphas=None, is_percentage=False):
    # Configurações padrão
    if colors is None:
        colors = {country:('gray' if country != main_country else '#129583') for country in countries}
    if alphas is None:
        alphas = {country:(0.7 if country != main_country else 1.0) for country in countries}
    
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor('#F5F5F5')
    ax.patch.set_facecolor('#F5F5F5')

    for country in countries:
        ax.plot(
            data.index,
            data[country],
            color=colors[country],
            alpha=alphas[country],
            linewidth=2
        )
        ax.text(
            x=data.index[-1] + timedelta(days=2),
            y=data[country].iloc[-1],
            color=colors[country],
            fontsize=12,
            s=country,
            alpha=alphas[country]
        )

    # Formatar eixos
    date_form = DateFormatter("%d-%m-%Y")
    ax.xaxis.set_major_locator(WeekdayLocator(byweekday=(0), interval=2))
    ax.xaxis.set_major_formatter(date_form)
    plt.xticks(rotation=45, fontsize=10)
    
    if is_percentage:
        ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    else:
        ax.yaxis.set_major_formatter(mtick.FuncFormatter(reformat_large_tick_values))

    # Customizar eixos
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_color('#3f3f3f')
    ax.tick_params(colors='#3f3f3f')
    ax.grid(True, alpha=0.3)

    # Adicionar rótulos
    plt.ylabel(ylabel, fontsize=14, alpha=0.9)
    plt.xlabel('Data', fontsize=12, alpha=0.9)
    plt.title(title, fontsize=16, weight='bold', pad=20)

    # Salvar figura
    plt.tight_layout()
    plt.savefig(output_dir / f"{filename}.png", dpi=300)
    plt.close()

# Função para carregar e processar dados
def load_and_process_data(url, cols, countries):
    df = pd.read_csv(
        url,
        usecols=cols,
        parse_dates=['date']
    )
    df = df[df['location'].isin(countries)]
    
    pivot = pd.pivot_table(
        data=df,
        index='date',
        columns='location',
        values=cols[-1],
        aggfunc='mean'
    )
    
    return pivot.ffill()

# URL base dos dados
OWID_URL = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'

# 1. Mortes mundiais
try:
    pivot_deaths = load_and_process_data(
        OWID_URL,
        ['date', 'location', 'new_deaths_smoothed'],
        ['World']
    )
    create_plot(
        pivot_deaths,
        ['World'],
        'World',
        'World',
        'Mortes diárias por COVID-19 no mundo (média móvel 7 dias)',
        'Mortes por dia',
        'world_deaths'
    )
except Exception as e:
    print(f"Erro ao processar mortes mundiais: {e}")

# 2. Casos mundiais
try:
    pivot_cases = load_and_process_data(
        OWID_URL,
        ['date', 'location', 'new_cases_smoothed'],
        ['World']
    )
    create_plot(
        pivot_cases,
        ['World'],
        'World',
        'World',
        'Casos diários de COVID-19 no mundo (média móvel 7 dias)',
        'Casos por dia',
        'world_cases'
    )
except Exception as e:
    print(f"Erro ao processar casos mundiais: {e}")

# 3. Casos no Brasil
try:
    pivot_br_cases = load_and_process_data(
        OWID_URL,
        ['date', 'location', 'new_cases_smoothed'],
        ['Brazil']
    )
    create_plot(
        pivot_br_cases,
        ['Brazil'],
        'Brazil',
        'Brazil',
        'Casos diários de COVID-19 no Brasil (média móvel 7 dias)',
        'Casos por dia',
        'br_cases'
    )
except Exception as e:
    print(f"Erro ao processar casos no Brasil: {e}")

# 4. Vacinações comparadas
try:
    pivot_vaccines = load_and_process_data(
        OWID_URL,
        ['date', 'location', 'total_vaccinations_per_hundred'],
        ['United States', 'Germany', 'United Kingdom', 'Brazil', 'Argentina', 'Chile', 'Uruguay']
    )
    create_plot(
        pivot_vaccines,
        pivot_vaccines.columns.tolist(),
        'Brazil',
        'Brazil',
        'Vacinação contra COVID-19 (doses por 100 pessoas)',
        'Doses administradas por 100 pessoas',
        'vaccines_comparison'
    )
except Exception as e:
    print(f"Erro ao processar dados de vacinação: {e}")

# 5. Comparação de casos entre países
try:
    pivot_country_cases = load_and_process_data(
        OWID_URL,
        ['date', 'location', 'new_cases_smoothed'],
        ['Brazil', 'United States', 'France']
    )
    create_plot(
        pivot_country_cases,
        pivot_country_cases.columns.tolist(),
        'Brazil',
        'Brazil',
        'Casos diários de COVID-19 (média móvel 7 dias)',
        'Casos por dia',
        'country_cases_comparison'
    )
except Exception as e:
    print(f"Erro ao processar comparação de casos: {e}")

# 6. Mortes no Brasil
try:
    pivot_br_deaths = load_and_process_data(
        OWID_URL,
        ['date', 'location', 'new_deaths_smoothed'],
        ['Brazil']
    )
    create_plot(
        pivot_br_deaths,
        ['Brazil'],
        'Brazil',
        'Brazil',
        'Mortes diárias por COVID-19 no Brasil (média móvel 7 dias)',
        'Mortes por dia',
        'br_deaths'
    )
except Exception as e:
    print(f"Erro ao processar mortes no Brasil: {e}")

print("Processamento concluído. Gráficos salvos em:", output_dir)

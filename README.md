# 📊 Gráficos Históricos da COVID-19 no Brasil 🇧🇷

Este projeto gera automaticamente gráficos informativos sobre a pandemia de COVID-19 no Brasil com dados atualizados diariamente. Ele utiliza como fonte a base pública mantida por [@wcota](https://github.com/wcota/covid19br) com dados por estado brasileiro.

## 🧾 Dados Utilizados
- Fonte: [Painel COVID-19 Brasil - GitHub](https://github.com/wcota/covid19br)
- Dataset: `cases-brazil-states.csv` (acessado via HTTP diretamente, sem salvar localmente)

## 📈 Gráficos Gerados
As imagens são salvas na pasta `imgs/`:
- **Casos semanais acumulados no Brasil** 
- **Mortes semanais no Brasil**  
- **Casos semanais por estado**: SP, RJ, RS, BA, MG  
- **Mortes semanais por estado**: SP, RJ, RS, BA, MG  

## ⚙️ Como Executar Localmente
1. Instale os pacotes necessários:
```
pip install -r requirements.txt
```
2. Execute o script:
```
python script_wcota.py
```

## 🔁 Workflow
Este projeto possui um workflow do GitHub Actions configurado para rodar manualmente, baixando os dados e recriando os gráficos automaticamente.

## 📫 Contato
- Criado por Yuri Abuchaim
- [Portfólio](https://rilufi.github.io)
- yuri.abuchaim@gmail.com

===========================================

# 📊 Historical COVID-19 Charts for Brazil 🇺🇸

This project automatically generates informative charts about the COVID-19 pandemic in Brazil with daily updated data. It uses the public database maintained by [@wcota](https://github.com/wcota/covid19br) with data by Brazilian state.

## 🧾 Data Sources
- Source: [COVID-19 Brazil Dashboard - GitHub](https://github.com/wcota/covid19br)
- Dataset: `cases-brazil-states.csv` (accessed via HTTP directly, not saved locally)

## 📈 Generated Charts
Images are saved in the `imgs/` folder:
- **Weekly cumulative cases in Brazil**
- **Weekly deaths in Brazil**
- **Weekly cases by state**: SP, RJ, RS, BA, MG
- **Weekly deaths by state**: SP, RJ, RS, BA, MG

## ⚙️ How to Run Locally
1. Install required packages:
2. ```
pip install -r requirements.txt
```
2. Run the script:
```
python script_wcota.py
```

## 🔁 Workflow
This project has a GitHub Actions workflow configured to run manually, downloading data and recreating charts automatically.

## 📫 Contact
- Created by Yuri Abuchaim
- [Portfolio](https://rilufi.github.io)
- yuri.abuchaim@gmail.com

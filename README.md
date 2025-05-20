# 📊 Gráficos Históricos da COVID-19 no Brasil

Este projeto gera automaticamente gráficos informativos sobre a pandemia de COVID-19 no Brasil com dados atualizados diariamente. Ele utiliza como fonte a base pública mantida por [@wcota](https://github.com/wcota/covid19br) com dados por estado brasileiro.

## 🧾 Dados Utilizados

- Fonte: [Painel COVID-19 Brasil - GitHub](https://github.com/wcota/covid19br)
- Dataset: `cases-brazil-states.csv` (acessado via HTTP diretamente, sem salvar localmente)

---

## 📈 Gráficos Gerados

As imagens são salvas na pasta `imgs/`:

- **Casos semanais acumulados no Brasil** 
- **Mortes semanais no Brasil**  
- **Casos semanais por estado**: SP, RJ, RS, BA, MG  
- **Mortes semanais por estado**: SP, RJ, RS, BA, MG  

Visualizações ideais para análise de tendências regionais e acompanhamento histórico.

---

## ⚙️ Como Executar Localmente

1. Instale os pacotes necessários:

```
bash
pip install pandas matplotlib requests
```

Execute o script:
```
python script_wcota.py
```

As imagens serão salvas na pasta imgs/.

## 🔁 Workflow
Este projeto possui um workflow do GitHub Actions configurado para rodar manualmente, baixando os dados e recriando os gráficos automaticamente.

---

- *Criado por Yuri Abuchaim · [rilufi.github.io](https://rilufi.github.io)*
- *Contato · 📧 [yuri.abuchaim@gmail.com](mailto:yuri.abuchaim@gmail.com)*

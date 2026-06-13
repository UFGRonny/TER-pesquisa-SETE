# Dashboard SETE — Perfil de Usuários

Painel interativo dos resultados da pesquisa sobre adoção do Sistema Eletrônico de Gestão do Transporte Escolar (SETE).

**UFG / FNDE · CECATE-CO · TED Simec 13155 · 2025**

---

## Rodar localmente

```bash
pip install -r requirements.txt
streamlit run dashboard_sete.py
```

Acesse: http://localhost:8501

---

## Deploy gratuito — Streamlit Community Cloud

1. Crie um repositório no GitHub e suba os dois arquivos:
   - `dashboard_sete.py`
   - `requirements.txt`

2. Acesse https://share.streamlit.io

3. Clique em **"New app"**

4. Selecione o repositório, branch `main` e o arquivo `dashboard_sete.py`

5. Clique em **"Deploy!"**

O link público estará disponível em ~2 minutos, no formato:
`https://seu-usuario-nome-do-repo-dashboard-sete-XXXX.streamlit.app`

---

## Estrutura do painel

| Aba | Conteúdo |
|-----|----------|
| Visão geral | KPIs, participação regional, qui-quadrado |
| Não implementaram | 3 clusters de barreiras (n=558) |
| Implementaram | 4 clusters de maturidade (n=1.235) |
| Modelo Logit | Coeficientes, ajuste, recomendações FNDE |

---

## Dependências

- `streamlit` — framework do painel
- `plotly` — gráficos interativos
- `pandas` — manipulação de dados

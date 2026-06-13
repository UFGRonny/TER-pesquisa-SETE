import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="SETE · Perfil de Usuários",
    page_icon="🚌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

/* ── Força off-white em todos os containers do Streamlit ── */
html, body { background-color: #F7F6F2 !important; }

[class*="css"],
[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > section,
[data-testid="stAppViewContainer"] > section > div,
[data-testid="block-container"],
.stApp, .main, .block-container {
    background-color: #F7F6F2 !important;
    font-family: 'DM Sans', sans-serif;
    color: #1A1A2E;
}

[data-testid="stTabs"] > div:first-child,
[data-testid="stTabsContent"] {
    background-color: #F7F6F2 !important;
}

[data-testid="stSidebar"] { background: #EDEDEA !important; }
[data-testid="stHeader"]  { background: transparent !important; }
[data-testid="stTabs"]    { border: none !important; }

p, span, div, label { color: inherit; }

.dashboard-header {
    background: #1A1A2E;
    color: white;
    padding: 32px 40px;
    border-radius: 16px;
    margin-bottom: 28px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
}

.header-title {
    font-family: 'Syne', sans-serif;
    font-size: 28px;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: -0.5px;
    margin-bottom: 6px;
}

.header-sub {
    font-size: 13px;
    color: #8B8FA8;
    font-weight: 300;
}

.header-badge {
    background: #2D2D4E;
    border: 1px solid #3D3D5E;
    border-radius: 8px;
    padding: 10px 16px;
    text-align: right;
}

.header-badge-label {
    font-size: 10px;
    color: #8B8FA8;
    letter-spacing: .08em;
    text-transform: uppercase;
}

.header-badge-val {
    font-family: 'Syne', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #7EB8F7;
}

.kpi-card {
    background: white;
    border-radius: 12px;
    padding: 20px 22px;
    border: 1px solid #EBEBEB;
    height: 100%;
}

.kpi-label {
    font-size: 11px;
    color: #999;
    text-transform: uppercase;
    letter-spacing: .06em;
    margin-bottom: 8px;
}

.kpi-value {
    font-family: 'Syne', sans-serif;
    font-size: 32px;
    font-weight: 700;
    line-height: 1;
    margin-bottom: 4px;
}

.kpi-sub {
    font-size: 12px;
    color: #999;
}

.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 15px;
    font-weight: 700;
    color: #1A1A2E;
    letter-spacing: -.2px;
    margin-bottom: 4px;
    margin-top: 24px;
}

.section-sub {
    font-size: 12px;
    color: #999;
    margin-bottom: 16px;
}

.cluster-card {
    border-radius: 12px;
    padding: 18px 20px;
    border: 1px solid #EBEBEB;
    background: white;
    height: 100%;
}

.cluster-tag {
    font-size: 10px;
    font-weight: 600;
    letter-spacing: .06em;
    text-transform: uppercase;
    padding: 3px 9px;
    border-radius: 20px;
    display: inline-block;
    margin-bottom: 10px;
}

.cluster-name {
    font-family: 'Syne', sans-serif;
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 4px;
    color: #1A1A2E;
}

.cluster-pct {
    font-family: 'Syne', sans-serif;
    font-size: 36px;
    font-weight: 800;
    line-height: 1;
    margin-bottom: 8px;
}

.cluster-desc {
    font-size: 12px;
    color: #666;
    line-height: 1.6;
}

.insight-box {
    background: #EEF4FF;
    border-left: 3px solid #4A80D4;
    border-radius: 0 10px 10px 0;
    padding: 14px 18px;
    font-size: 13px;
    color: #2A4A8A;
    line-height: 1.6;
    margin-top: 16px;
}

.logit-card {
    background: white;
    border-radius: 12px;
    border: 1px solid #EBEBEB;
    padding: 20px 24px;
    margin-bottom: 12px;
}

.logit-title {
    font-family: 'Syne', sans-serif;
    font-size: 13px;
    font-weight: 700;
    color: #1A1A2E;
    margin-bottom: 14px;
    text-transform: uppercase;
    letter-spacing: .04em;
}

.sig-badge {
    display: inline-block;
    font-size: 11px;
    padding: 2px 8px;
    border-radius: 20px;
    font-weight: 500;
}

.sig-yes {
    background: #E6F7EF;
    color: #1A7A4A;
}

.sig-no {
    background: #F5F5F5;
    color: #999;
}

.tab-content {
    background: white;
    border-radius: 12px;
    border: 1px solid #EBEBEB;
    padding: 24px;
    margin-top: 8px;
}

div[data-testid="stTabs"] button {
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="dashboard-header">
    <div>
        <div class="header-title">🚌 Perfil de Uso do SETE — Brasil</div>
        <div class="header-sub">Sistema Eletrônico de Gestão do Transporte Escolar &nbsp;·&nbsp; UFG / FNDE &nbsp;·&nbsp; Pesquisa Web 2025</div>
        <div class="header-sub" style="margin-top:4px">CECATE-CO &nbsp;·&nbsp; TED Simec 13155 &nbsp;·&nbsp; PI07337-2023</div>
    </div>
    <div style="display:flex;gap:12px">
        <div class="header-badge">
            <div class="header-badge-label">Respondentes</div>
            <div class="header-badge-val">1.793</div>
        </div>
        <div class="header-badge">
            <div class="header-badge-label">Regiões</div>
            <div class="header-badge-val">5</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs([
    "📊  Visão geral",
    "🔴  Não implementaram",
    "🟢  Implementaram",
    "📈  Modelo Logit"
])

VERDE   = "#1D9E75"
AZUL    = "#378ADD"
CORAL   = "#D85A30"
ROXO    = "#7F77DD"
AMARELO = "#BA7517"
CINZA   = "#888780"
DARK    = "#1A1A2E"

PLOTLY_LAYOUT = dict(
    font_family="DM Sans",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=0, r=0, t=20, b=0),
)

with tab1:
    c1, c2, c3, c4 = st.columns(4)
    cards = [
        ("Total de respondentes", "1.793", "municípios brasileiros", "#1A1A2E"),
        ("Implementaram o SETE", "1.235", "68,9% da amostra", VERDE),
        ("Não implementaram", "558", "31,1% da amostra", CORAL),
        ("Usam outro software também", "739", "dos que implementaram", AZUL),
    ]
    for col, (label, val, sub, color) in zip([c1, c2, c3, c4], cards):
        with col:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-label">{label}</div>
                <div class="kpi-value" style="color:{color}">{val}</div>
                <div class="kpi-sub">{sub}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown('<div class="section-title">Participação por região</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Número de municípios com respostas completas</div>', unsafe_allow_html=True)

    df_reg = pd.DataFrame({
        "Região": ["Nordeste", "Sudeste", "Sul", "Centro-Oeste", "Norte"],
        "Municípios": [594, 577, 325, 177, 119],
    })
    fig_reg = go.Figure(go.Bar(
        x=df_reg["Municípios"],
        y=df_reg["Região"],
        orientation="h",
        marker_color=[AZUL]*5,
        text=df_reg["Municípios"],
        textposition="outside",
        textfont=dict(size=13, family="DM Sans"),
    ))
    fig_reg.update_layout(
        **PLOTLY_LAYOUT,
        height=220,
        xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(showgrid=False, tickfont=dict(size=13)),
    )
    st.plotly_chart(fig_reg, use_container_width=True)

    ca, cb = st.columns(2)
    with ca:
        st.markdown('<div class="section-title">Implementação × sistema concorrente</div>', unsafe_allow_html=True)
        df_conc = pd.DataFrame({
            "Perfil": ["Implementou SETE\n+ usa outro sistema", "Implementou SETE\nsem outro sistema", "Não implementou\n+ usa outro sistema", "Não implementou\nsem outro sistema"],
            "n": [739, 496, 270, 288],
        })
        fig_c = go.Figure(go.Bar(
            x=df_conc["Perfil"], y=df_conc["n"],
            marker_color=[VERDE, "#9FE1CB", "#F5C4B3", CORAL],
            text=df_conc["n"], textposition="outside",
        ))
        fig_c.update_layout(**PLOTLY_LAYOUT, height=260,
            yaxis=dict(showgrid=False, showticklabels=False),
            xaxis=dict(tickfont=dict(size=11)))
        st.plotly_chart(fig_c, use_container_width=True)
        st.markdown('<div class="insight-box">χ²=0,96 · p=0,327 — Usar outro sistema <strong>não</strong> é barreira para adotar o SETE.</div>', unsafe_allow_html=True)

    with cb:
        st.markdown('<div class="section-title">Implementação × troca de equipe gestora</div>', unsafe_allow_html=True)
        fig_t = go.Figure()
        fig_t.add_trace(go.Bar(name="Implementou SETE", x=["Houve troca", "Sem troca"], y=[420, 815], marker_color=VERDE))
        fig_t.add_trace(go.Bar(name="Não implementou", x=["Houve troca", "Sem troca"], y=[280, 278], marker_color=CORAL))
        fig_t.update_layout(**PLOTLY_LAYOUT, height=260, barmode="group",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, font=dict(size=11)),
            yaxis=dict(showgrid=True, gridcolor="#F0F0F0"),
            xaxis=dict(tickfont=dict(size=13)))
        st.plotly_chart(fig_t, use_container_width=True)
        st.markdown('<div class="insight-box">χ²=177,3 · p&lt;2,2e-16 — Troca de equipe é <strong>altamente associada</strong> à adoção do SETE.</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="section-title">Análise de cluster de classes latentes — municípios que não implementaram</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">n=558 · Modelo de 3 classes selecionado (BIC/AIC ótimos · p&lt;1,4e-418 · Err. classe=0,103)</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    clusters_nao = [
        (c1, "Cluster 1 · Verde", "Barreira de capacidade", "48,8%", VERDE, "#E1F5EE", "#0F6E56",
         "Equipes menores com dificuldade média de manuseio do sistema. Principal barreira: manuseio e registro de dados. Heterogeneidade de experiência — sem padrão de anos de serviço. Não existe evidência de concorrência como barreira."),
        (c2, "Cluster 2 · Azul", "Barreira de conhecimento", "42,1%", AZUL, "#E6F1FB", "#185FA5",
         "Desconhecem que o SETE existe. Maior proporção de gestores com pouca experiência. Sem padrão diferencial de área ou demanda. Equilíbrio 50/50 entre quem usa ou não outro sistema."),
        (c3, "Cluster 3 · Vermelho", "Barreira de infraestrutura", "9,1%", CORAL, "#FAECE7", "#993C1D",
         "Múltiplas dificuldades: infraestrutura, dados e manuseio. Municípios maiores (>1.437 km²) e com alta demanda de alunos. Maior taxa de troca de equipe gestora. Requer conectividade e suporte técnico."),
    ]
    for col, tag, name, pct, color, bg, tc, desc in clusters_nao:
        with col:
            st.markdown(f"""
            <div class="cluster-card">
                <div class="cluster-tag" style="background:{bg};color:{tc}">{tag}</div>
                <div class="cluster-name">{name}</div>
                <div class="cluster-pct" style="color:{color}">{pct}</div>
                <div class="cluster-desc">{desc}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown('<div class="section-title" style="margin-top:28px">Probabilidade das barreiras por cluster</div>', unsafe_allow_html=True)

    barreiras = ["Desconhece o SETE", "Dificuldade de manuseio", "Registro e obtenção de dados",
                 "Falta infraestrutura/equipe", "Problemas técnicos (bugs)", "Dificuldade de acesso (login)"]
    c1_vals = [0.15, 0.62, 0.55, 0.20, 0.18, 0.25]
    c2_vals = [0.88, 0.10, 0.12, 0.08, 0.06, 0.10]
    c3_vals = [0.30, 0.75, 0.78, 0.92, 0.80, 0.70]

    fig_bar = go.Figure()
    fig_bar.add_trace(go.Bar(name="C1 Capacidade", x=barreiras, y=c1_vals, marker_color=VERDE))
    fig_bar.add_trace(go.Bar(name="C2 Conhecimento", x=barreiras, y=c2_vals, marker_color=AZUL))
    fig_bar.add_trace(go.Bar(name="C3 Infraestrutura", x=barreiras, y=c3_vals, marker_color=CORAL))
    fig_bar.update_layout(**PLOTLY_LAYOUT, height=300, barmode="group",
        yaxis=dict(tickformat=".0%", showgrid=True, gridcolor="#F0F0F0", range=[0, 1.05]),
        xaxis=dict(tickfont=dict(size=11)),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, font=dict(size=11)))
    st.plotly_chart(fig_bar, use_container_width=True)

    ca, cb = st.columns(2)
    with ca:
        fig_pie = go.Figure(go.Pie(
            labels=["C1 Capacidade (48,8%)", "C2 Conhecimento (42,1%)", "C3 Infraestrutura (9,1%)"],
            values=[48.77, 42.09, 9.14],
            marker_colors=[VERDE, AZUL, CORAL],
            hole=0.55,
            textinfo="percent",
            textfont=dict(size=13),
        ))
        fig_pie.update_layout(**PLOTLY_LAYOUT, height=240, showlegend=True,
            legend=dict(font=dict(size=11), orientation="v"))
        st.plotly_chart(fig_pie, use_container_width=True)
    with cb:
        st.markdown("""
        <div style="margin-top:20px">
        <div class="insight-box" style="margin-bottom:10px">
        <strong>H1 confirmada</strong> — A não-adoção não é uniforme. Três perfis distintos exigem três intervenções distintas:<br><br>
        🟢 <strong>C1</strong> → Capacitação técnica e suporte ao manuseio<br>
        🔵 <strong>C2</strong> → Comunicação e divulgação do SETE<br>
        🔴 <strong>C3</strong> → Infraestrutura de conectividade
        </div>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="section-title">Análise de cluster de classes latentes — municípios que implementaram</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">n=1.235 · Modelo de 4 classes selecionado (melhor segregação · Entropy R²=0,8917)</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    clusters_sim = [
        (c1, "Cluster 1 · Roxo", "Gestão cadastral", "36,1%", ROXO, "#EEEDFE", "#534AB7",
         "Módulos alunos e escolas. Municípios com até 601 alunos. Sem padrão de área ou experiência."),
        (c2, "Cluster 2 · Vermelho", "Gestão operacional", "25,7%", CORAL, "#FAECE7", "#993C1D",
         "Frota, motoristas e rotas. 61% também usam outro sistema. Perfil heterogêneo."),
        (c3, "Cluster 3 · Verde", "Subutilizadores", "20,1%", VERDE, "#EAF3DE", "#3B6D11",
         "Instalaram mas usam pouco. Maior presença de sistema concorrente. Uso possivelmente mandatório."),
        (c4, "Cluster 4 · Azul", "Uso estratégico", "18,1%", AZUL, "#E6F1FB", "#185FA5",
         "Todos os módulos: custos, geo, fornecedores. Gestores mais novos. Maior taxa de troca de equipe."),
    ]
    for col, tag, name, pct, color, bg, tc, desc in clusters_sim:
        with col:
            st.markdown(f"""
            <div class="cluster-card">
                <div class="cluster-tag" style="background:{bg};color:{tc}">{tag}</div>
                <div class="cluster-name">{name}</div>
                <div class="cluster-pct" style="color:{color}">{pct}</div>
                <div class="cluster-desc">{desc}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown('<div class="section-title" style="margin-top:28px">Maturidade de uso por cluster</div>', unsafe_allow_html=True)

    modulos = ["Módulo alunos", "Módulo escolas", "Módulo frota", "Módulo rotas", "Módulo motoristas", "Módulo custos", "Georreferenciamento", "Módulo normas"]
    fig_mat = go.Figure()
    fig_mat.add_trace(go.Scatterpolar(r=[0.95, 0.92, 0.30, 0.25, 0.28, 0.05, 0.05, 0.10], theta=modulos, fill="toself", name="C1 Cadastral", line_color=ROXO))
    fig_mat.add_trace(go.Scatterpolar(r=[0.95, 0.90, 0.88, 0.82, 0.85, 0.15, 0.20, 0.30], theta=modulos, fill="toself", name="C2 Operacional", line_color=CORAL))
    fig_mat.add_trace(go.Scatterpolar(r=[0.70, 0.65, 0.40, 0.35, 0.38, 0.08, 0.08, 0.12], theta=modulos, fill="toself", name="C3 Subutilizador", line_color=VERDE))
    fig_mat.add_trace(go.Scatterpolar(r=[0.98, 0.97, 0.95, 0.93, 0.94, 0.88, 0.85, 0.80], theta=modulos, fill="toself", name="C4 Estratégico", line_color=AZUL))
    fig_mat.update_layout(**PLOTLY_LAYOUT, height=360,
        polar=dict(radialaxis=dict(visible=True, range=[0, 1], tickformat=".0%", tickfont=dict(size=10)), bgcolor="white"),
        legend=dict(orientation="h", yanchor="bottom", y=-0.15, font=dict(size=11)))
    st.plotly_chart(fig_mat, use_container_width=True)

    ca, cb = st.columns(2)
    with ca:
        fig_pie2 = go.Figure(go.Pie(
            labels=["C1 Cadastral (36,1%)", "C2 Operacional (25,7%)", "C3 Subutilizador (20,1%)", "C4 Estratégico (18,1%)"],
            values=[36.14, 25.71, 20.08, 18.06],
            marker_colors=[ROXO, CORAL, VERDE, AZUL],
            hole=0.55, textinfo="percent", textfont=dict(size=13),
        ))
        fig_pie2.update_layout(**PLOTLY_LAYOUT, height=260, showlegend=True,
            legend=dict(font=dict(size=11)))
        st.plotly_chart(fig_pie2, use_container_width=True)
    with cb:
        st.markdown("""
        <div style="margin-top:16px">
        <div class="insight-box">
        <strong>Paradoxo da experiência (H4)</strong> — O Cluster 4 (uso estratégico) é formado por gestores mais <em>novos</em> e com maior taxa de troca de equipe. Gestores veteranos ficam presos no básico por "lock-in" em métodos manuais (efeito Hábito do UTAUT). Gestores novos usam o SETE para <em>construir</em> a memória institucional que falta.
        </div>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="section-title">Modelo Logit binário — decisão de implementar o SETE</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Variável dependente: implementou SETE (1) / não implementou (0) · n=1.793</div>', unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    metricas = [
        ("ρ² — modelo final", "0,753", "≥0,20 recomendado", VERDE),
        ("AIC — modelo final", "2.208,7", "↓ vs 2.213,9 inicial", VERDE),
        ("BIC — modelo final", "2.225,1", "↓ vs 2.246,8 inicial", VERDE),
        ("Amostra", "1.793", "municípios brasileiros", DARK),
    ]
    for col, (label, val, sub, color) in zip([m1, m2, m3, m4], metricas):
        with col:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-label">{label}</div>
                <div class="kpi-value" style="color:{color};font-size:26px">{val}</div>
                <div class="kpi-sub">{sub}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown('<div class="section-title" style="margin-top:24px">Coeficientes estimados — modelo final</div>', unsafe_allow_html=True)

    df_logit = pd.DataFrame({
        "Variável": ["Log n° alunos transportados", "Troca de equipe gestora"],
        "β": [0.0792, 0.345],
        "t-student": [3.14, 3.31],
        "p-valor": ["0,002", "0,001"],
        "Significância": ["✓ p<0,01", "✓ p<0,01"],
    })

    fig_coef = go.Figure()
    fig_coef.add_trace(go.Bar(
        x=df_logit["β"],
        y=df_logit["Variável"],
        orientation="h",
        marker_color=[AZUL, VERDE],
        text=[f"β={v:.3f}" for v in df_logit["β"]],
        textposition="outside",
        textfont=dict(size=13, family="DM Sans"),
        width=0.5,
    ))
    fig_coef.add_vline(x=0, line_width=1, line_color="#DDD")
    fig_coef.update_layout(**PLOTLY_LAYOUT, height=180,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-0.05, 0.55]),
        yaxis=dict(showgrid=False, tickfont=dict(size=13)))
    st.plotly_chart(fig_coef, use_container_width=True)

    st.markdown('<div class="section-title">Variáveis excluídas — modelo inicial (não significativas)</div>', unsafe_allow_html=True)

    df_ns = pd.DataFrame({
        "Variável": ["Anos de experiência do gestor", "Uso de outro software de gestão", "Log área do município"],
        "β": [-0.0006, 0.090, -0.011],
        "p-valor": ["0,947", "0,391", "0,794"],
    })

    fig_ns = go.Figure()
    fig_ns.add_trace(go.Bar(
        x=df_ns["β"],
        y=df_ns["Variável"],
        orientation="h",
        marker_color=["#C8C8C8"]*3,
        text=[f"β={v:.3f}  p={p}" for v, p in zip(df_ns["β"], df_ns["p-valor"])],
        textposition="outside",
        textfont=dict(size=12, family="DM Sans", color="#999"),
        width=0.4,
    ))
    fig_ns.add_vline(x=0, line_width=1, line_color="#DDD")
    fig_ns.update_layout(**PLOTLY_LAYOUT, height=180,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-0.15, 0.25]),
        yaxis=dict(showgrid=False, tickfont=dict(size=13, color="#999")))
    st.plotly_chart(fig_ns, use_container_width=True)

    ca, cb = st.columns(2)
    with ca:
        st.markdown("""
        <div class="insight-box">
        <strong>H2 — Vantagem relativa por escala</strong><br>
        A probabilidade de adoção cresce com o número de alunos transportados. Para municípios pequenos, o custo de aprender o SETE supera o benefício. Para municípios grandes, a gestão manual é inviável.
        </div>
        """, unsafe_allow_html=True)
    with cb:
        st.markdown("""
        <div class="insight-box">
        <strong>H3 — Ruptura de inércia</strong><br>
        A troca de equipe gestora zera o Hábito com métodos anteriores e cria pressão por Influência Social para modernizar. A instabilidade administrativa, paradoxalmente, é uma janela de oportunidade.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-top:24px;background:#1A1A2E;border-radius:12px;padding:20px 24px">
    <div style="font-family:'Syne',sans-serif;font-size:13px;font-weight:700;color:#8B8FA8;letter-spacing:.06em;text-transform:uppercase;margin-bottom:10px">Recomendações para o FNDE</div>
    <div style="color:#E0E0E8;font-size:13px;line-height:1.8">
    <span style="color:#7EB8F7;font-weight:500">1. Segmentar a comunicação</span> — Focar marketing em novas gestões (janela de oportunidade) e municípios com alta demanda de alunos.<br>
    <span style="color:#7EB8F7;font-weight:500">2. Diferenciar o suporte</span> — Para C2 Operacional (veteranos): gestão de mudança para vencer o hábito. Para C4 Estratégico (novatos): suporte técnico aprofundado.<br>
    <span style="color:#7EB8F7;font-weight:500">3. Infraestrutura vs. divulgação</span> — Conectividade para C3 Infraestrutura; campanhas informativas para C2 Conhecimento (42% dos não-usuários).
    </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="margin-top:32px;padding-top:16px;border-top:1px solid #E8E8E8;display:flex;justify-content:space-between;align-items:center">
    <div style="font-size:11px;color:#BBB">Universidade Federal de Goiás (UFG) · Faculdade de Ciências e Tecnologia · CECATE-CO</div>
    <div style="font-size:11px;color:#BBB">Fundo Nacional de Desenvolvimento da Educação (FNDE) · 2025</div>
</div>
""", unsafe_allow_html=True)

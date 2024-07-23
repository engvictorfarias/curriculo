import streamlit as st              # FrameWork dashboard
import pandas as pd                 # Manipulacao de dataframes
import plotly.express as px         # Visualizacao
import plotly.graph_objects as go   # Visualizacao
from PIL import Image               # Foto Perfil

ferramentas = {'Skill':['Power BI', 'Python','SQL','R', 'PL/SQL', 'Outros'], 'Nível':[10,9,9,8,7,6]}
df_skills = pd.DataFrame.from_dict(ferramentas)
print(df_skills)

# ----------------------- Diretorios --------------------------#
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_dir = current_dir / 'styles' / 'main.css'
cv_file = current_dir / 'docs' / 'cv.pdf'
foto_perfil = current_dir / 'docs' / 'foto_perfil.png'

# ----------------------- Infos Basicas --------------------------#

titulo_cv = 'Victor Farias | Currículo'
icone_pagina = '👨‍💻'
nome = 'Victor Farias'
desc1 = '👨‍💻 Analista de Dados Sênior'
desc2 = 'Apaixonado por dados e por resolver problemas!'
email = 'victormatheus1995@gmail.com'
redes = {
    'LinkedIn': 'https://linkedin.com/in/engvictorfarias/',
    'GitHub': 'https://engvictorfarias.github.io/',
    'Kaggle': 'https://www.kaggle.com/engvictorfarias',
    'Instagram': 'https://www.instagram.com/engvictorfarias'
}

projetos = {
    '🥇 Modelo de Classificação - testando diferentes técnicas de processamento e algoritmos': 'https://github.com/engvictorfarias/engvictorfarias/blob/main/classifica-o-breast-cancer-winsconsin-python-ml.ipynb',
    '🥇 Marketing Customer Segmentation - clusterização de clientes (não supervisionado)':'https://www.kaggle.com/code/engvictorfarias/marketing-customer-segmentation-python',
    '🥇 Credit Card Fraud Detection - Detecção de Fraude com Python':'https://www.kaggle.com/code/engvictorfarias/credit-card-fraud-detection-python',
    '🥇 Credit Card Fraud Detection - Detecção de Fraude com R':'https://www.kaggle.com/code/engvictorfarias/an-lise-de-fraude-em-c-de-cr-dito-linguagem-r',
    '🥇 Modelo de Classificação com Apache Spark':'https://github.com/engvictorfarias/engvictorfarias/blob/main/Modelo%20de%20Classifica%C3%A7%C3%A3o%20Com%20Python%20e%20Apache%20Spark%20-%20MLlib.ipynb',
    '🥇 RPA web com python 1':'https://www.linkedin.com/posts/eng-victor-farias_python-powerbi-businessinteligence-activity-7056420967048257536-xg6r?utm_source=share&utm_medium=member_desktop',
    '🥇 RPA web com python e ChatGPT ':'https://www.linkedin.com/posts/eng-victor-farias_python-chatgpt-programacao-activity-7214757846716997632-Ky8v?utm_source=share&utm_medium=member_android',
}


st.set_page_config(page_title = titulo_cv, page_icon = icone_pagina)

# -------------------------- Configuracao css e imagem -------------------------- #

with open(css_dir) as f:
    st.markdown('<style>{}</style?'.format(f.read()),unsafe_allow_html=True)
with open(cv_file,'rb') as pdf_file:
    PDFbyte = pdf_file.read()
foto = Image.open(foto_perfil)

#---------------- Primeira Secao: foto, botoes downloads -----------------#
c1,c2 = st.columns(2, gap='small')

with c1:
    st.image(foto, width=230)

with c2:
    st.title(nome)
    st.write(desc1)
    st.write(desc2)
    st.download_button(
        label = 'Download Currículo',
        data = PDFbyte,
        file_name=cv_file.name,
        mime='application/octet-stream'
    )

    st.write('📩', email)

# ---------------------------- links redes sociais ------------------------------------#
st.write('#')
cols = st.columns(len(redes))
for index, (plataform, link) in enumerate(redes.items()):
    cols[index].write(f'[{plataform}]({link})')
st.write('---')
# ---------------------------- Experiência e Qualificações ------------------------------------#

st.write('#')
st.subheader('Experiência e Qualificações')
st.write('---')
st.write('''
- ✅ +4 anos de experiência com Power BI, Python e SQL
- ✅ +5 anos manipulando dados em Excel (dinâmica, Power Query, VBA ...)
- ✅ Especialização em Data Science (Data Science Academy - nov/21 a nov/23) 
- ✅ Pós-Graduado em BI
- ✅ Engenheiro Mecânico - UFRN                         
''')

# ---------------------------- Skills ------------------------------------#

st.write('#')
st.subheader('Hard Skills')
st.write('---')
st.write('''
- 🤖 Programação: Python , R, SQL e PL/SQL
- 📊 Visualização: Power BI, Python, R, Metabase, Looker, Excel
- 🎲 Banco de Dados: Oracle, Postgres, MySQL, SQL Server
- 🤓 Data Science: Modelos de aprendizado supervisionado e não supervisionado 
    (python/R/Apache Spark)             
''')
st.write('\n')
fig_bar = go.Figure()
fig_bar.add_trace(go.Bar(
    y = df_skills['Skill'], 
    x = df_skills['Nível'], 
    orientation = 'h',
    textposition='outside',
    marker=dict(color='rgba(246, 78, 139, 0.6)')
    )
)
fig_bar.update_layout(
    height=400, 
    width = 400,
    autosize=True,
    margin = {'t':25},
    yaxis = dict(showgrid=True,
        showline=True,
        gridcolor = 'lightgrey',
        showticklabels=True,
        zeroline=True,
        autorange = 'reversed'),
    xaxis = dict(showgrid=True,
        showline=True,
        gridcolor = 'lightgrey',
        zeroline=True),
        title={
        'text': "Hard Skills (criado com plotly)",
        'y':1.0,
        'x':0.55,
        'xanchor': 'center',
        'yanchor': 'top'}
) 
st.plotly_chart(fig_bar)

# ---------------------------- Experiência Profissional ------------------------------------#

st.write('\n')
st.subheader('Experiência Profissional')
st.write('---')

st.write('**🥇 Analista de Dados Sênior | Unimed Natal**')
st.write('09/2023 - atualmente')
         
st.write('\n')
st.write('**- Freelancer PJ (Desenvolvimento de BIs**)')
st.write('09/2023 - 05/2024')

st.write('\n')
st.write('**- Analista de Dados Pleno | Unimed Natal**')
st.write('01/2022 - 09/2023')

st.write('\n')
st.write('**- Programador Digital Junior | Ânima Educação**')
st.write('10/2021 - 12/2021')

st.write('\n')
st.write('**- ... outros**')

# ---------------------------- Projetos ------------------------------------#

st.write('#')
st.subheader('Projetos')
st.write('---')

for projeto, link in projetos.items():
    st.write(f'[{projeto}]({link})')
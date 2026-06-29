"""
Ética em IA & IA Ética — apresentação animada (neo-brutalismo, GSAP + Lottie).
Deploy: Streamlit Community Cloud -> arquivo principal = streamlit_app.py

O estilo fica em arquivos separados (style.css = visual, fonts.css = fontes base64).
Como o componente HTML do Streamlit roda num iframe que não busca arquivos soltos,
o CSS é injetado aqui em tempo de execução.
"""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Ética em IA & IA Ética",
    page_icon="◼",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      .block-container{padding:0 !important;max-width:100% !important;}
      header[data-testid="stHeader"]{display:none;}
      [data-testid="stToolbar"]{display:none;}
      #MainMenu, footer{visibility:hidden;}
      .stApp{background:#efe9d6;}
    </style>
    """,
    unsafe_allow_html=True,
)

base = Path(__file__).parent
html = (base / "etica-ia-brutalist.html").read_text(encoding="utf-8")
fonts_css = (base / "fonts.css").read_text(encoding="utf-8")
style_css = (base / "style.css").read_text(encoding="utf-8")

# Injeta o CSS no lugar dos <link> (necessário para o iframe do Streamlit)
html = html.replace('<link rel="stylesheet" href="fonts.css" />', f"<style>{fonts_css}</style>")
html = html.replace('<link rel="stylesheet" href="style.css" />', f"<style>{style_css}</style>")

# A altura pode ser ajustada conforme a tela do projetor/monitor.
components.html(html, height=860, scrolling=False)

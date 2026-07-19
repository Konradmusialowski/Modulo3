import streamlit as st
import streamlit.components.v1 as components
import requests

# 1. Busca os dados lá do GitHub
url = "https://raw.githubusercontent.com/Konradmusialowski/Modulo3/main/data/produtos.json"
dados = requests.get(url).json()

# 2. Insere os dados no seu HTML
html_template = """
<!DOCTYPE html>
... (seu código HTML aqui) ...
<script>
    const bancoDeDados = """ + str(dados) + """;
    // ... restante do seu script JS original ...
</script>
"""

# 3. Renderiza no Streamlit
components.html(html_template, height=1000, scrolling=True)
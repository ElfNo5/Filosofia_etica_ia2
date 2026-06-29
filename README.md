# Ética em IA & IA Ética — Apresentação

Apresentação animada (neo-brutalismo) sobre **ética na inteligência artificial**,
baseada no artigo de Luís C. Lamb (Revista USP, n. 141, 2024), publicada como site
via **Streamlit**.

Construída **somente com GSAP + Lottie**. As três fontes (Superglue, Inktera Demo,
Courbe Sans) estão **embutidas em base64** no HTML, então o arquivo é autônomo.

## Rodar localmente
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Publicar (Streamlit Community Cloud — grátis)
1. Suba esta pasta para um repositório no GitHub.
2. Acesse https://share.streamlit.io e faça login com o GitHub.
3. **New app** → escolha o repositório, branch `main`, arquivo `streamlit_app.py`.
4. **Deploy**. Em ~1 min o site estará no ar com uma URL pública.


## Editar o visual
- **`style.css`** — todo o estilo da apresentação. Comece pelas variáveis em
  `:root` (paleta e fontes por papel). É só este arquivo que você precisa mexer.
- **`fonts.css`** — as 3 fontes em base64. Não precisa abrir.
- O `streamlit_app.py` injeta os dois automaticamente; abrindo o HTML direto da
  pasta, os `<link>` carregam sozinhos.

## Estrutura
```
streamlit_app.py          # app Streamlit (injeta o CSS e embute o HTML)
etica-ia-brutalist.html   # estrutura da apresentação
style.css                 # >>> o visual (edite aqui) <<<
fonts.css                 # fontes embutidas em base64
requirements.txt
fonts/                    # fontes originais + licenças (procedência)
```

## Navegação
Setas ← → ou barra de espaço; ou os botões no rodapé.

## Fontes e licenças
- **Superglue** — CC0 / domínio público (Raymond Larabie) — títulos.
- **Inktera Demo** — versão demo gratuita (limitype.com) — corpo e rótulos.
- **Courbe Sans** — licença gratuita pessoal/comercial (Loukas Nicolaou); é
  caixa-alta e **não tem acentos**, por isso é usada só nos numerais.

Detalhes em `fonts/`. Para uso comercial da Inktera, adquira a versão completa.

## Ajustes rápidos
- Altura da apresentação: parâmetro `height=860` em `streamlit_app.py`.
- Conteúdo/estilo: edite diretamente `etica-ia-brutalist.html`.

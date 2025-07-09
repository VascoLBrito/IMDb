# IMDb Dashboard – Análise Exploratória de Filmes

Este projeto consiste numa aplicação interativa desenvolvida com Streamlit que explora os dados públicos da IMDb, permitindo ao utilizador visualizar tendências de avaliação, popularidade de géneros e recomendações personalizadas com base em dados reais.
Foi desenvolvido para portfólio pessoal e candidatura ao Mestrado em Inteligência Artificial e Ciência de Dados (MIACD) da Universidade de Coimbra.
Demonstra competências em ETL, análise exploratória, visualização interativa e design de aplicações orientadas a dados.

---

## Funcionalidades

- Visualização da avaliação média por género (desde 2000)
- Ranking dos filmes mais bem avaliados de todos os tempos
- Lista dos filmes mais votados (populares)
- Recomendador de filmes por género
- Interface simples e responsiva com gráficos interativos (Plotly)

---

## Tech Stack

- **Python**  
- **Pandas**  
- **Streamlit**  
- **Plotly**  
- **IMDb Datasets (.tsv)**

## Como correr localmente

### Clonar o repositório

git clone <https://github.com/VascoLBrito/IMDb.git>
cd imdb-analysis

### Criar e ativar o ambiente virtual

No Windows:
python -m venv .venv
.venv\Scripts\Activate.ps1

No MAC/Linux:
python3 -m venv .venv
source .venv/bin/activate

### 3.Instalar dependências

pip install -r requirements.txt

### 4.Correr a app

streamlit run app/streamlit_app.py

### Bse de Dados

Este projeto utiliza os datasets públicos da IMDb que estão presentes na pasta "data"

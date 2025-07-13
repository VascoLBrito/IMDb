import sys
import os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.etl import load_title_basics, load_ratings, merge_basics_ratings
from src.analysis import (
    top_genres_by_rating,
    top_movies_by_rating,
    most_voted_movies,
    recommend_movies_by_genre
)
from src.visualizations import (
    plot_genre_ratings_bar,
    plot_top_rated_movies
)

st.set_page_config(page_title="IMDb Dashboard", layout="wide")
st.title("IMDb - Análise de Filmes")

# Sidebar
st.sidebar.title("Navegação")
page = st.sidebar.radio("Ir para:", [
    "Géneros por Avaliação",
    "Top Filmes por Avaliação",
    "Filmes Mais Votados",
    "Recomendador de Filmes"
])


# Load data ONCE and cache it
@st.cache_data
def load_data():
    basics = load_title_basics()
    ratings = load_ratings()
    return merge_basics_ratings(basics, ratings)

# Page: Géneros

if page == "Géneros por Avaliação":

    with st.spinner("A carregar dados do IMDb..."):
      df = load_data()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total de Filmes", f"{len(df):,}".replace(',', ' '))

    with col2:
        avg_rating = round(df["averageRating"].mean(), 2)
        st.metric("Média Geral", avg_rating)

    with col3:
        top_genre = df["genres"].dropna().str.split(",").explode().value_counts().idxmax()
        st.metric("Género Mais Popular", top_genre)

    st.subheader("Top Géneros desde os anos 2000")
    min_votes_1 = st.slider("Votos mínimos por filme", 1000, 2000000, 100000, step=10000)
    genres_avg = top_genres_by_rating(df, min_votes=min_votes_1)
    fig = plot_genre_ratings_bar(genres_avg)
    st.plotly_chart(fig, use_container_width=True)

# Page: Top Filmes
elif page == "Top Filmes por Avaliação":

    with st.spinner("A carregar dados do IMDb..."):
      df = load_data()

    min_votes_2 = st.slider("Votos mínimos por filme", 1000, 2000000, 100000, step=10000)
    st.subheader(f"Top 10 Filmes Mais Bem Avaliados (min {min_votes_2} votos)")
    top_rated = top_movies_by_rating(df, min_votes=min_votes_2)
    df_display = top_rated.reset_index(drop=True)
    df_display.index = df_display.index + 1
    df_display.index.name = "Posição"

    st.dataframe(df_display)

# Page: Mais Votados
elif page == "Filmes Mais Votados":

    with st.spinner("A carregar dados do IMDb..."):
      df = load_data()

    st.subheader("Top 10 Filmes Mais Votados")
    most_voted = most_voted_movies(df)
    fig = plot_top_rated_movies(most_voted)
    st.plotly_chart(fig, use_container_width=True)

# Page: Recomendador
elif page == "Recomendador de Filmes":

    with st.spinner("A carregar dados do IMDb..."):
      df = load_data()

    st.subheader("Recomendador por Género")
    all_genres = df['genres'].dropna().str.split(',').explode().unique()
    genre = st.selectbox("Escolhe um género:", sorted(all_genres))
    min_votes_rec = st.slider("Número mínimo de votos:", 1000, 50000, 10000, step=1000)

    recommendations = recommend_movies_by_genre(df, genre, min_votes=min_votes_rec)

    if not recommendations.empty:
        st.write(f"Top recomendações para o género **{genre}**:")
        df_display = recommendations.reset_index(drop=True)
        df_display.index = df_display.index + 1
        df_display.index.name = "Posição"

        st.dataframe(df_display)
    else:
        st.warning("Nenhum filme encontrado com esses critérios.")

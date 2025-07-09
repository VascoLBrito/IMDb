import plotly.express as px

def plot_genre_ratings_bar(genre_ratings):
    """
    Gera um gráfico de barras interativo com as avaliações médias por género.
    """
    fig = px.bar(
        genre_ratings.reset_index(),
        x="genres",
        y="averageRating",
        title="Média de Avaliações por Género",
        labels={"genres": "Género", "averageRating": "Nota Média"},
        color="averageRating",
        color_continuous_scale="Blues"
    )
    fig.update_layout(xaxis_tickangle=-45)
    return fig

def plot_top_rated_movies(df):
    df_sorted = df.sort_values(by="numVotes", ascending=False)
    fig = px.pie(
        df_sorted,
        names="primaryTitle",
        values="numVotes",
        hole=0.1
    )
    fig.update_traces(textinfo='percent+label', hovertemplate='%{label}<br>Votos: %{value:,}')
    return fig


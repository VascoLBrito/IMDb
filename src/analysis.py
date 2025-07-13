def top_genres_by_rating(merged_df, min_votes=5000):
    """
    Calcula a média de avaliação por género, considerando apenas filmes desde 2000
    com um número mínimo de votos (default = 5000).
    """
    recent = merged_df[merged_df['startYear'] >= 2000]
    recent = recent[recent['numVotes'] >= min_votes]
    recent = recent[recent['genres'].notna()]
    
    # Explode géneros: transforma "Action,Drama" → duas linhas
    exploded = recent.assign(genres=recent['genres'].str.split(',')).explode('genres')

    # Agrupa por género e calcula a média de avaliações
    genre_avg = (
        exploded.groupby('genres')['averageRating']
        .mean()
        .sort_values(ascending=False)
        
    )
    return genre_avg


#Devolve os top N filmes com melhor avaliação média e número mínimo de votos
def top_movies_by_rating(merged_df, min_votes=50000, top_n=10):
    df = merged_df[merged_df['numVotes'] >= min_votes]
    top = df.sort_values(by='averageRating', ascending=False).head(top_n)
    return top[['primaryTitle', 'startYear', 'averageRating', 'numVotes']]


#Retorna os top N filmes com mais votos (indicador de popularidade).
def most_voted_movies(merged_df, top_n=10):
   
    top = merged_df.sort_values(by='numVotes', ascending=False).head(top_n)
    return top[['primaryTitle', 'startYear', 'averageRating', 'numVotes']]

#Retorna os top filmes recomendados de um género, ordenados por avaliação média.
def recommend_movies_by_genre(merged_df, genre, min_votes=10000, top_n=5):
    
    df = merged_df[
        (merged_df['genres'].notna()) &
        (merged_df['numVotes'] >= min_votes) &
        (merged_df['genres'].str.contains(genre, case=False, na=False))
    ]
    df_sorted = df.sort_values(by='averageRating', ascending=False).head(top_n)
    return df_sorted[['primaryTitle', 'startYear', 'averageRating', 'numVotes']]

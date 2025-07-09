from src.etl import load_title_basics, load_ratings, merge_basics_ratings
from src.analysis import top_genres_by_rating, top_movies_by_rating, most_voted_movies

print("📥 A carregar dados...")

basics = load_title_basics()
ratings = load_ratings()
df = merge_basics_ratings(basics, ratings)

print(f"🎬 Filmes com avaliações: {len(df)}")

# Nova análise: top géneros
print("\n📊 Top géneros desde 2000 (min 5000 votos):")
genre_ratings = top_genres_by_rating(df)
print(genre_ratings.head(10))

print("\n🏆 Top 10 filmes com melhor avaliação (min 50.000 votos):")
print(top_movies_by_rating(df))

print("\n🔥 Top 10 filmes mais votados (mais populares):")
print(most_voted_movies(df))
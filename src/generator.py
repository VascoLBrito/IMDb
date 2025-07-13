import pandas as pd

# Load full datasets locally
print("📥 Lendo ficheiros IMDb completos...")
df_basics = pd.read_csv("data/title.basics.tsv.gz", sep="\t", na_values="\\N", low_memory=False)
df_ratings = pd.read_csv("data/title.ratings.tsv.gz", sep="\t", na_values="\\N", low_memory=False)

# Filter for movies only
df_basics = df_basics[df_basics['titleType'] == 'movie']
df_basics = df_basics[df_basics['startYear'].notna()]
df_basics['startYear'] = pd.to_numeric(df_basics['startYear'], errors='coerce')

# Merge datasets
print("🔗 A juntar ratings com metadata...")
df = pd.merge(df_basics, df_ratings, on="tconst", how="inner")

# Filter to most voted and highest rated (e.g. 50,000+ votes)
df = df[df['numVotes'] >= 50000]
df = df.sort_values(by=['averageRating', 'numVotes'], ascending=False)

# Select top N
TOP_N = 500
df_top = df.head(TOP_N)

# Create minimal basics and ratings samples
basics_sample = df_top[df_basics.columns]
ratings_sample = df_top[df_ratings.columns]

# Save to sample files
print("💾 A guardar amostras...")
basics_sample.to_csv("data/title.basics.sample.tsv", sep="\t", index=False)
ratings_sample.to_csv("data/title.ratings.sample.tsv", sep="\t", index=False)

print("✅ Sample com os melhores filmes criada com sucesso!")

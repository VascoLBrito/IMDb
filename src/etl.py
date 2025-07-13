import os
import pandas as pd
import streamlit as st

def running_on_streamlit_cloud():
    return os.environ.get("STREAMLIT_CLOUD", "").lower() == "true"

@st.cache_data
def load_title_basics():
    path = (
        "data/title.basics.sample.tsv"
        if running_on_streamlit_cloud()
        else "data/title.basics.tsv.gz"
    )
    df = pd.read_csv(path, sep="\t", na_values="\\N", low_memory=False)
    df = df[df['titleType'] == 'movie']
    df = df[df['startYear'].notna()]
    df['startYear'] = pd.to_numeric(df['startYear'], errors='coerce')
    return df

@st.cache_data
def load_ratings():
    path = (
        "data/title.ratings.sample.tsv"
        if running_on_streamlit_cloud()
        else "data/title.ratings.tsv.gz"
    )
    return pd.read_csv(path, sep="\t", na_values="\\N", low_memory=False)

@st.cache_data
def merge_basics_ratings(basics_df, ratings_df):
    return pd.merge(basics_df, ratings_df, on="tconst", how="inner")

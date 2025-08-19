# recommend.py
import os
import gdown
import requests
import pickle
import pandas as pd
import joblib
import logging


# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("recommend.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logging.info("🔁 Loading data...")

# --- Google Drive Links  ---
COSINE_URL = "https://drive.google.com/uc?id=1olV8bAon0C4wa5AR0aOnVrfw94olLwzU"
TFIDF_URL = "https://drive.google.com/uc?id=1Zue6RUi5MSFCu_U_iJMeVEd_kvtSHFFU"
DF_CLEANED_URL = "https://drive.google.com/uc?id=1RzIEIJ3NEvWPE8LRUqCF5IUlI7gm6XEm"

# --- Kaggle Backup URLs ---
COSINE_KAGGLE = "https://www.kaggle.com/datasets/sonalikasingh17/pickle-files?select=cosine_sim.pkl"
TFIDF_KAGGLE ="https://www.kaggle.com/datasets/sonalikasingh17/pickle-files?select=tfidf_matrix.pkl"
DF_CLEANED_KAGGLE = "https://www.kaggle.com/datasets/sonalikasingh17/pickle-files?select=df_cleaned.pkl"


def download_file(url, output):
    """Download file from Google Drive or HTTP if not exists."""
    if not os.path.exists(output):
        try:
            logging.info(f"📥 Downloading {output}...")
            gdown.download(url, output, quiet=False, fuzzy=True) 
        except Exception as e:
            logging.error(f"❌ Failed to download {output}: {e}")
            raise e


# Ensure required pickle files
download_file(COSINE_URL, "cosine_sim.pkl")
download_file(TFIDF_URL, "tfidf_matrix.pkl")
download_file(DF_CLEANED_URL, "df_cleaned.pkl")

# Load data
df = joblib.load("df_cleaned.pkl")
cosine_sim = joblib.load("cosine_sim.pkl")
tfidf_matrix = joblib.load("tfidf_matrix.pkl")
music_list = df['song'].values


def recommend_songs(song_name, top_n=5):
    """Recommend top_n similar songs based on cosine similarity."""
    logging.info(f"🎵 Recommending songs for: '{song_name}'")

    idx = df[df['song'].str.lower() == song_name.lower()].index
    if len(idx) == 0:
        logging.warning("⚠️ Song not found in dataset.")
        return None

    idx = idx[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n + 1]
    song_indices = [i[0] for i in sim_scores]

    result_df = df[['artist', 'song']].iloc[song_indices].reset_index(drop=True)
    result_df.index = result_df.index + 1
    result_df.index.name = "S.No."

    return result_df, df['song'].iloc[idx]



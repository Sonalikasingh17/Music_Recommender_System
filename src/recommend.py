
# # recommend.py
# import gdown
# import os
# import pandas as pd
# import joblib
# import logging

# # Setup logging
# logging.basicConfig(
#     level=logging.INFO,
#     format='[%(asctime)s] %(levelname)s - %(message)s',
#     handlers=[
#         logging.FileHandler("recommend.log", encoding="utf-8"),
#         logging.StreamHandler()
#     ]
# )

# logging.info("🔁 Loading data...")
# try:
#     df = joblib.load('df_cleaned.pkl')
#     FILE_URL = "https://drive.google.com/file/d/1olV8bAon0C4wa5AR0aOnVrfw94olLwzU/view?usp=drive_link"
#     FILE_NAME = "cosine_sim.pkl"

# # Download only if not already present
#     if not os.path.exists(FILE_NAME):
#         gdown.download(FILE_URL, FILE_NAME, quiet=False)

#     cosine_sim = joblib.load(FILE_NAME)


#     # cosine_sim = joblib.load('cosine_sim.pkl')

#     logging.info("✅ Data loaded successfully.")
# except Exception as e:
#     logging.error("❌ Failed to load required files: %s", str(e))
#     raise e


# def recommend_songs(song_name, top_n=5):
#     logging.info("🎵 Recommending songs for: '%s'", song_name)
#     idx = df[df['song'].str.lower() == song_name.lower()].index
#     if len(idx) == 0:
#         logging.warning("⚠️ Song not found in dataset.")
#         return None
#     idx = idx[0]
#     sim_scores = list(enumerate(cosine_sim[idx]))
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n + 1]
#     song_indices = [i[0] for i in sim_scores]
#     logging.info("✅ Top %d recommendations ready.", top_n)
#     # Create DataFrame with clean serial numbers starting from 1
#     result_df = df[['artist', 'song']].iloc[song_indices].reset_index(drop=True)
#     result_df.index = result_df.index + 1  # Start from 1 instead of 0
#     result_df.index.name = "S.No."

#     return result_df


# recommend.py
import os
import pandas as pd
import joblib
import logging
from sklearn.metrics.pairwise import cosine_similarity

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

try:
    # Load preprocessed DataFrame and TF-IDF matrix
    df = joblib.load('df_cleaned.pkl')
    tfidf_matrix = joblib.load('tfidf_matrix.pkl')

    # Compute cosine similarity on the fly
    logging.info("📐 Calculating cosine similarity...")
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    logging.info("✅ Data and similarity matrix ready.")
except Exception as e:
    logging.error("❌ Failed to load required files: %s", str(e))
    raise e


def recommend_songs(song_name, top_n=5):
    """
    Recommend top_n similar songs based on cosine similarity.
    """
    logging.info("🎵 Recommending songs for: '%s'", song_name)
    
    idx = df[df['song'].str.lower() == song_name.lower()].index
    if len(idx) == 0:
        logging.warning("⚠️ Song not found in dataset.")
        return None
    
    idx = idx[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n + 1]
    song_indices = [i[0] for i in sim_scores]

    logging.info("✅ Top %d recommendations ready.", top_n)

    # Create DataFrame with clean serial numbers starting from 1
    result_df = df[['artist', 'song']].iloc[song_indices].reset_index(drop=True)
    result_df.index = result_df.index + 1  # Start from 1 instead of 0
    result_df.index.name = "S.No."

    return result_df

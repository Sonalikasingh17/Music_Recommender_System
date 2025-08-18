
# # preprocess.py
# import gdown
# import os
# import pandas as pd
# import re
# import nltk
# import joblib
# import logging
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# # Setup logging
# logging.basicConfig(
#     level=logging.INFO,
#     format='[%(asctime)s] %(levelname)s - %(message)s',
#     handlers=[
#         logging.FileHandler("preprocess.log", encoding="utf-8"),
#         logging.StreamHandler()
#     ]
# )

# logging.info("🚀 Starting preprocessing...")

# nltk.download('punkt')
# nltk.download('stopwords')

# # Load and sample dataset
# try:
#     df = pd.read_csv("D:\IIT M\Interview_Prep\Project\spotify_millsongdata.csv").sample(10000)
#     logging.info("✅ Dataset loaded and sampled: %d rows", len(df))
# except Exception as e:
#     logging.error("❌ Failed to load dataset: %s", str(e))
#     raise e

# # Drop link column and preprocess
# df = df.drop(columns=['link'], errors='ignore').reset_index(drop=True)

# # Text cleaning
# stop_words = set(stopwords.words('english'))

# def preprocess_text(text):
#     text = re.sub(r"[^a-zA-Z\s]", "", str(text))
#     text = text.lower()
#     tokens = word_tokenize(text)
#     tokens = [word for word in tokens if word not in stop_words]
#     return " ".join(tokens)

# logging.info("🧹 Cleaning text...")
# df['cleaned_text'] = df['text'].apply(preprocess_text)
# logging.info("✅ Text cleaned.")

# # Vectorization
# logging.info("🔠 Vectorizing using TF-IDF...")
# tfidf = TfidfVectorizer(max_features=5000)
# tfidf_matrix = tfidf.fit_transform(df['cleaned_text'])
# logging.info("✅ TF-IDF matrix shape: %s", tfidf_matrix.shape)

# # Cosine similarity
# logging.info("📐 Calculating cosine similarity...")
# cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
# logging.info("✅ Cosine similarity matrix generated.")

# # Save everything
# joblib.dump(df, 'df_cleaned.pkl')
# joblib.dump(tfidf_matrix, 'tfidf_matrix.pkl')


# FILE_URL = "https://drive.google.com/file/d/1olV8bAon0C4wa5AR0aOnVrfw94olLwzU/view?usp=drive_link"
# FILE_NAME = "cosine_sim.pkl"
# if not os.path.exists(FILE_NAME):
#         gdown.download(FILE_URL, FILE_NAME, quiet=False)

#         joblib.dump(cosine_sim, FILE_NAME)

# # joblib.dump(cosine_sim, 'cosine_sim.pkl', compress=3) # Save with compression


# # Check size
# # size_mb = os.path.getsize("cosine_sim.pkl") / (1024 * 1024)
# # print(f"Compressed file size: {size_mb:.2f} MB")


# logging.info("💾 Data saved to disk.")



# logging.info("✅ Preprocessing complete.")


# preprocess.py
import os
import pandas as pd
import re
import nltk
import joblib
import logging
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("preprocess.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logging.info("🚀 Starting preprocessing...")

# Download NLTK data if not present
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Load and sample dataset
try:
    df = pd.read_csv("D:\\IIT M\\Interview_Prep\\Project\\spotify_millsongdata.csv").sample(10000)
    logging.info("✅ Dataset loaded and sampled: %d rows", len(df))
except Exception as e:
    logging.error("❌ Failed to load dataset: %s", str(e))
    raise e

# Drop unnecessary columns
df = df.drop(columns=['link'], errors='ignore').reset_index(drop=True)

# Text cleaning
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = re.sub(r"[^a-zA-Z\s]", "", str(text))  # keep only letters and spaces
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

logging.info("🧹 Cleaning text...")
df['cleaned_text'] = df['text'].apply(preprocess_text)
logging.info("✅ Text cleaned.")

# Vectorization
logging.info("🔠 Vectorizing using TF-IDF...")
tfidf = TfidfVectorizer(max_features=5000)
tfidf_matrix = tfidf.fit_transform(df['cleaned_text'])
logging.info("✅ TF-IDF matrix shape: %s", tfidf_matrix.shape)

# Save cleaned dataset and TF-IDF matrix
joblib.dump(df, 'df_cleaned.pkl')
joblib.dump(tfidf_matrix, 'tfidf_matrix.pkl')

logging.info("💾 Data saved to disk: df_cleaned.pkl, tfidf_matrix.pkl")
logging.info("✅ Preprocessing complete.")

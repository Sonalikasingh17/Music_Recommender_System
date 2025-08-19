# # main.py (Enhanced Streamlit App)

# import pickle
# import os
# import streamlit as st
# from dotenv import load_dotenv
# import gdown
# import requests
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# # from recommend import df, recommend_songs



# # Load environment variables from .env file
# load_dotenv()

# # Fetch credentials
# CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
# CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# # Initialize the Spotify client
# client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# def get_song_album_cover_url(song_name, artist_name):
#     search_query = f"track:{song_name} artist:{artist_name}"
#     results = sp.search(q=search_query, type="track")

#     if results and results["tracks"]["items"]:
#         track = results["tracks"]["items"][0]
#         album_cover_url = track["album"]["images"][0]["url"]
#         print(album_cover_url)
#         return album_cover_url
#     else:
#         return "https://i.postimg.cc/0QNxYz4V/social.png"

# # def recommend(song):
# #     index = music[music['song'] == song].index[0]
# #     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
# #     recommended_music_names = []
# #     recommended_music_posters = []
# #     for i in distances[1:6]:
# #         # fetch the movie poster
# #         artist = music.iloc[i[0]].artist
# #         print(artist)
# #         print(music.iloc[i[0]].song)
# #         recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
# #         recommended_music_names.append(music.iloc[i[0]].song)

# #     return recommended_music_names,recommended_music_posters

# # st.header('Music Recommender System')



# def recommend_songs(song_name, top_n=5):
#     """
#     Recommend top_n similar songs based on cosine similarity.
#     """
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


# # --- Page Config ---
# st.set_page_config(
#     page_title="Instant Music Recommender 🎶",
#     page_icon="🎧",
#     layout="centered"
# )

# # --- Custom CSS for header ---
# st.markdown(
#     """
#     <style>
#     .app-title {
#         font-size: 48px;
#         font-weight: bold;
#         text-align: center;
#         color: #FF4B4B;
#         margin-bottom: 20px;
#         font-family: 'Arial', sans-serif;
#     }
#     .subtitle {
#         text-align: center;
#         font-size: 20px;
#         color: #AAAAAA;
#         margin-bottom: 30px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # --- Fancy Title ---
# st.markdown('<div class="app-title">🎵 Instant Music Recommender 🎵</div>', unsafe_allow_html=True)
# st.markdown('<div class="subtitle">Discover your next favorite song in one click 🚀</div>', unsafe_allow_html=True)




# # --- Download function ---
# def download_file(url, output):
#     try:
#         if "drive.google.com" in url:
#             gdown.download(url, output, quiet=False)
#         else:
#             r = requests.get(url, stream=True)
#             with open(output, "wb") as f:
#                 for chunk in r.iter_content(chunk_size=8192):
#                     f.write(chunk)
#     except Exception as e:
#         st.error(f"❌ Failed to download {output}: {e}")



# # --- Ensure cosine_sim.pkl is present ---
# if not os.path.exists("cosine_sim.pkl"):
#     st.info("📥 Downloading cosine_sim.pkl...")
#     download_file(COSINE_URL, "cosine_sim.pkl")

# # --- Ensure tfidf_matrix.pkl is present ---
# if not os.path.exists("tfidf_matrix.pkl"):
#     st.info("📥 Downloading tfidf_matrix.pkl...")
#     download_file(TFIDF_URL, "tfidf_matrix.pkl")

# # --- Ensure df_cleaned.pkl is present ---
# if not os.path.exists("df_cleaned.pkl"):    
#     st.info("📥 Downloading df_cleaned.pkl...")
#     download_file(DF_CLEANED_URL, "df_cleaned.pkl")

# # --- Load Pickle Files ---
# # with open("df.pkl", "rb") as f:
# #     music = pickle.load(f)

# with open("cosine_sim.pkl", "rb") as f:
#     cosine_sim = pickle.load(f)

# with open("tfidf_matrix.pkl", "rb") as f:
#     tfidf_matrix = pickle.load(f)

# with open("df_cleaned.pkl", "rb") as f:
#     df = pickle.load(f) 

# # # music = pickle.load(open('df.pkl','rb'))
# # # similarity = pickle.load(open('similarity.pkl','rb'))

# # music_list = music['song'].values
# # selected_movie = st.selectbox(
# #     "Type or select a song from the dropdown",
# #     music_list
# # )

# if st.button("🚀 Recommend Similar Songs"):
#     recommended_music_names,recommended_music_posters = recommend(selected_movie)
#     col1, col2, col3, col4, col5= st.columns(5)

#     st.subheader(f"Recommendations for: {selected_movie}")
#     if recommended_music_names and recommended_music_posters is None:
#             st.warning("⚠️ Sorry, song not found in dataset.")
#     else:
#             st.success("✨ Here are your top recommendations:")

            
#     with st.spinner("Finding similar songs... 🎧"):
#         recommended_music_names,recommended_music_posters = recommend(selected_movie)
#         col1, col2, col3, col4, col5= st.columns(5)


        
#     # Display recommended songs with their album covers
#     with col1:
#         st.text(recommended_music_names[0])
#         st.image(recommended_music_posters[0])
#     with col2:
#         st.text(recommended_music_names[1])
#         st.image(recommended_music_posters[1])

#     with col3:
#         st.text(recommended_music_names[2])
#         st.image(recommended_music_posters[2])
#     with col4:
#         st.text(recommended_music_names[3])
#         st.image(recommended_music_posters[3])
#     with col5:
#         st.text(recommended_music_names[4])
#         st.image(recommended_music_posters[4])

#     st.write("🎶 Here are some songs you might like based on your selection ✨🎧")

# main.py — Streamlit app (ready for deployment)

import os
import pickle
import logging
import requests
import gdown
import streamlit as st
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# ─────────── Env & Logging ───────────
load_dotenv()
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')

# Spotify credentials (must be set in environment or .env)
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# ─────────── Google Drive URLs for pickle files ───────────
COSINE_URL = "https://drive.google.com/uc?id=1olV8bAon0C4wa5AR0aOnVrfw94olLwzU"
TFIDF_URL = "https://drive.google.com/uc?id=1Zue6RUi5MSFCu_U_iJMeVEd_kvtSHFFU"
DF_CLEANED_URL = "https://drive.google.com/uc?id=1RzIEIJ3NEvWPE8LRUqCF5IUlI7gm6XEm"

# ─────────── Helpers ───────────
def download_file(url: str, output: str):
    """Download a file from Google Drive (via gdown) or generic HTTP."""
    try:
        if os.path.exists(output):
            return
        if "drive.google.com" in url:
            gdown.download(url, output, quiet=False)
        else:
            r = requests.get(url, stream=True, timeout=60)
            r.raise_for_status()
            with open(output, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
    except Exception as e:
        st.error(f"❌ Failed to download {output}: {e}")
        raise

def get_song_album_cover_url(song_name: str, artist_name: str) -> str:
    """Fetch album cover from Spotify for given track/artist."""
    try:
        search_query = f"track:{song_name} artist:{artist_name}"
        results = sp.search(q=search_query, type="track", limit=1)
        if results and results.get("tracks", {}).get("items"):
            track = results["tracks"]["items"][0]
            images = track.get("album", {}).get("images", [])
            if images:
                return images[0]["url"]
    except Exception as e:
        logging.warning("Spotify lookup failed for '%s' by '%s': %s", song_name, artist_name, e)
    # Fallback placeholder
    return "https://i.postimg.cc/0QNxYz4V/social.png"

# ─────────── Streamlit Page Config & Styles ───────────
st.set_page_config(page_title="Instant Music Recommender 🎶", page_icon="🎧", layout="centered")

st.markdown(
    """
    <style>
    .app-title {
        font-size: 48px;
        font-weight: 800;
        text-align: center;
        color: #FF4B4B;
        margin-bottom: 20px;
        font-family: 'Inter', 'Arial', sans-serif;
    }
    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #AAAAAA;
        margin-bottom: 30px;
    }
    .success-banner {
        background: #234a2f;
        color: #d6f5dd;
        padding: 14px 16px;
        border-radius: 10px;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title + subtitle (matches your screenshot copy)
st.markdown('<div class="app-title">🎵 Instant Music Recommender 🎵</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Discover your next favorite song in one click 🚀</div>', unsafe_allow_html=True)

# ─────────── Ensure pickles exist, then load ───────────
with st.spinner("Setting things up..."):
    if not os.path.exists("cosine_sim.pkl"):
        st.info("📥 Downloading cosine_sim.pkl...")
        download_file(COSINE_URL, "cosine_sim.pkl")

    if not os.path.exists("tfidf_matrix.pkl"):
        st.info("📥 Downloading tfidf_matrix.pkl...")
        download_file(TFIDF_URL, "tfidf_matrix.pkl")

    if not os.path.exists("df_cleaned.pkl"):
        st.info("📥 Downloading df_cleaned.pkl...")
        download_file(DF_CLEANED_URL, "df_cleaned.pkl")

try:
    with open("cosine_sim.pkl", "rb") as f:
        cosine_sim = pickle.load(f)
    with open("tfidf_matrix.pkl", "rb") as f:
        tfidf_matrix = pickle.load(f)
    with open("df_cleaned.pkl", "rb") as f:
        df = pickle.load(f)
except Exception as e:
    st.error(f"❌ Failed to load model files: {e}")
    st.stop()

# Song list for dropdown
music_list = df['song'].dropna().astype(str).values

# ─────────── Recommender ───────────
def recommend_songs(song_name: str, top_n: int = 5):
    """Return a DataFrame of top-N similar songs (artist, song)."""
    logging.info("🎵 Recommending songs for: '%s'", song_name)
    idx = df[df['song'].str.lower() == song_name.lower()].index
    if len(idx) == 0:
        return None
    idx = idx[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n + 1]
    song_indices = [i[0] for i in sim_scores]

    result_df = df[['artist', 'song']].iloc[song_indices].reset_index(drop=True)
    result_df.index = result_df.index + 1
    result_df.index.name = "S.No."
    return result_df

# ─────────── UI Controls ───────────
selected_song = st.selectbox(
    "Type or select a song from the dropdown",
    options=music_list,
    index=0
)

go = st.button("🚀 Recommend Similar Songs")

# ─────────── Results Section ───────────
if go:
    with st.spinner("Finding similar songs... 🎧"):
        rec_df = recommend_songs(selected_song, top_n=5)

    st.subheader(f"Recommendations for: {selected_song}")

    if rec_df is None or rec_df.empty:
        st.warning("⚠️ Sorry, song not found in dataset.")
    else:
        st.markdown('<div class="success-banner">✨ Here are your top recommendations:</div>', unsafe_allow_html=True)

        # 5 album cards in a row (as in your screenshot)
        cols = st.columns(5)
        for i, col in enumerate(cols, start=1):
            if i in rec_df.index:
                artist = rec_df.loc[i, 'artist']
                song = rec_df.loc[i, 'song']
                cover = get_song_album_cover_url(song, artist)
                with col:
                    st.text(song)
                    st.image(cover, use_column_width=True)

        # Footer line exactly as in your screenshot
        st.write("🎶 Here are some songs you might like based on your selection ✨🎧")

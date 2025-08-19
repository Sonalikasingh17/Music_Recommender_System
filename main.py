# main.py — Streamlit UI for deployment only

import os
import logging
import streamlit as st
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from src.recommend import download_file, music_list, recommend_songs

# ─────────── Env & Logging ───────────
load_dotenv()
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')

# Spotify credentials (must be set in environment or .env) 
# For security I didn't display here. I saved my credentials in .env file.
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# ─────────── Helper ───────────
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
st.set_page_config(page_title="Music Recommender 🎶", page_icon="🎧", layout="centered")

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

# Title + subtitle
st.markdown('<div class="app-title">🎵Music Recommender🎵</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Discover your next favorite song in one click 🚀</div>', unsafe_allow_html=True)

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
        rec_df, base_song = recommend_songs(selected_song, top_n=5)

    st.subheader(f"Recommendations for: {base_song}")

    if rec_df is None or rec_df.empty:
        st.warning("⚠️ Sorry, song not found in dataset.")
    else:
        st.markdown('<div class="success-banner">✨ Here are your top recommendations:</div>', unsafe_allow_html=True)

        # 5 album cards in a row
        cols = st.columns(5)
        for i, col in enumerate(cols, start=1):
            if i in rec_df.index:
                artist = rec_df.loc[i, 'artist']
                song = rec_df.loc[i, 'song']
                cover = get_song_album_cover_url(song, artist)
                with col:
                    st.text(song)
                    st.image(cover)

        # Footer line
        st.write("🎶 Here are some songs you might like based on your selection ✨🎧")

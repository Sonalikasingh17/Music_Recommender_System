# # main.py (Enhanced Streamlit App)
# import streamlit as st
# from recommend import df, recommend_songs

# --- Page Config ---
st.set_page_config(
    page_title="Music Recommender 🎵",
    page_icon="🎧",
    layout="centered"
)

# --- Custom CSS ---
st.markdown(
    """
    <style>
    .title {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        color: #FF4B4B;
    }
    .recommend-card {
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 12px;
    }
    .recommend-card h4 {
        margin: 0;
        color: #333;
    }
    .recommend-card p {
        margin: 0;
        font-size: 14px;
        color: #666;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title ---
st.markdown('<div class="title">🎶 Instant Music Recommender</div>', unsafe_allow_html=True)

# --- Cached Song List ---
@st.cache_resource
def get_song_list():
    return sorted(df['song'].dropna().unique())

song_list = get_song_list()

# --- Song Selection ---
selected_song = st.selectbox("🎵 Select a song:", song_list)

# --- Recommend Button ---
if st.button("🚀 Recommend Similar Songs"):
    with st.spinner("Finding similar songs... 🎧"):
        recommendations = recommend_songs(selected_song)
        if recommendations is None:
            st.warning("⚠️ Sorry, song not found in dataset.")
        else:
            st.success("✨ Here are your top recommendations:")
            
            # Display recommendations as styled cards
            for i, row in recommendations.iterrows():
                st.markdown(
                    f"""
                    <div class="recommend-card">
                        <h4>{i}. {row['song']}</h4>
                        <p>👨‍🎤 {row['artist']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

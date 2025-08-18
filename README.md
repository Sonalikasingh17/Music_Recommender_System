#  Music Recommender System

A lightweight content-based music recommendation app built with Python, utilizing TF-IDF and cosine similarity to suggest similar songs. Deployed with **Streamlit**, this tool offers fast and intuitive song recommendations based on your dataset.

---

##  Features

- **Content-based Recommendations**  
  Computes song similarity using TF-IDF vectorization on lyrics or text features and cosine similarity.

- **Lightweight & Git-friendly**  
  Avoids large `.pkl` files. Only `df_cleaned.pkl` and `tfidf_matrix.pkl` are committed—cosine similarity is computed dynamically at runtime.

- **Streamlit App with Attractive UI**  
  - Styled banner header and recommendation cards  
  - Spinner feedback and emojis for interactivity  
  - Built-in song search via dropdown (with optional autocomplete)

---

##  Project Structure

-  preprocess.py # Preprocesses raw data, creates TF-IDF matrix
-  recommend.py # Computes and serves recommendations
-  main.py # Streamlit app interface
-  df_cleaned.pkl # Cleaned DataFrame (generated)
-  tfidf_matrix.pkl # TF-IDF feature matrix (generated)
-  requirements.txt # Python dependencies

---

##  Quick Start

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Sonalikasingh17/Music_Recommender_System.git
   cd Music_Recommender_System
    ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
    ```
3. **Run Preprocessing**
   ```bash
   python preprocess.py
   ```
4. **Launch the Streamlit app**
   ```bash
   streamlit run main.py
   ```

## Tips & Customization

- Autocomplete Search Bar: Enhance the select box with st.selectbox(..., help="Type to search...") or use st.text_input() + fuzzy matching for better UX.
- Custom Styling: Modify CSS in main.py to refine recommendation cards (colors, fonts, spacing).
- Data Customization: Replace df['text'] preprocessing logic to work with lyrics, metadata, or genre features.
  --- 

## Acknowledgements

- Built using scikit-learn, pandas, NLTK, and Streamlit.
- Inspired by common TF-IDF + cosine similarity recommender patterns for content-based filtering.
  --- 

Enjoy exploring music recommendations with your interactive, lightweight app!

import streamlit as st
import pickle
import numpy as np
import pandas as pd
import difflib

# ---- MUST BE FIRST ----
st.set_page_config(page_title="Book Recommender", layout="wide")

# ---- Load data ----
@st.cache_data
def load_pickles():
    try:
        popular_df = pd.read_pickle("popular.pkl")
        pt = pd.read_pickle("pt.pkl")
        books = pd.read_pickle("books.pkl")
        similarity_scores = pd.read_pickle("similarity_scores.pkl")
    except Exception as e:
        st.error(f"Error loading pickle files: {e}")
        st.stop()
    return popular_df, pt, books, similarity_scores

popular_df, pt, books, similarity_scores = load_pickles()

# ---- Sidebar navigation ----
st.sidebar.title("📘 Navigation")
section = st.sidebar.selectbox(
    "Choose Section",
    ["Popular Books", "User Input Recommendation"]
)
st.title("📚 Book Recommender System")

# ==============================================================
# SECTION 1: Popular Books
# ==============================================================
if section == "Popular Books":
    st.header("Top 10 Popular Books")
    top_n = min(10, len(popular_df))

    for i in range(0, top_n, 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            idx = i + j
            if idx >= top_n:
                break
            title = popular_df.iloc[idx].get("Book-Title", "Unknown Title")
            author = popular_df.iloc[idx].get("Book-Author", "Unknown Author")
            img = popular_df.iloc[idx].get("Image-URL-M", None)
            votes = popular_df.iloc[idx].get("num_ratings", "")
            rating = popular_df.iloc[idx].get("avg_rating", "")
            with col:
                st.markdown(f"**{title}**  \n*by {author}*")
                if isinstance(img, str) and img.strip():
                    st.image(img, width=160)
                else:
                    st.info("No image available")
                st.caption(f"Votes: {votes}  •  Rating: {rating:.3f}")
                st.markdown("---")

# ==============================================================
# SECTION 2: User Input Recommendation
# ==============================================================
elif section == "User Input Recommendation":
    st.header("Find Books Similar to Your Favorite")

    user_input = st.text_input("Enter a book title (partial names allowed) or published year:")

    def find_best_match(query, titles):
        """Return best matching title from titles using substring or difflib fallback."""
        if not query:
            return None
        q = query.lower().strip()
        for t in titles:
            if q in t.lower():
                return t
        close = difflib.get_close_matches(query, titles, n=1, cutoff=0.6)
        return close[0] if close else None

    def recommend_cf(book_title, top_k=10):
        """Return list of recommended items (title, author, image)."""
        titles = list(pt.index)
        matched = find_best_match(book_title, titles)
        if not matched:
            return None, None
        idx = np.where(pt.index == matched)[0]
        if len(idx) == 0:
            return matched, []
        idx = idx[0]
        sims = list(enumerate(similarity_scores[idx]))
        sims_sorted = sorted(sims, key=lambda x: x[1], reverse=True)
        recs = []
        for i, score in sims_sorted:
            if i == idx:
                continue
            tmp = books[books["Book-Title"] == pt.index[i]].drop_duplicates(subset=["Book-Title"])
            if tmp.empty:
                continue
            recs.append({
                "title": tmp.iloc[0].get("Book-Title", "Unknown"),
                "author": tmp.iloc[0].get("Book-Author", "Unknown"),
                "image": tmp.iloc[0].get("Image-URL-M", None),
                #"score": float(score)
            })
            if len(recs) >= top_k:
                break
        return matched, recs

    if user_input:
        matched_title, recommendations = recommend_cf(user_input, top_k=10)
        if matched_title is None:
            st.error("No matching book found. Try another title.")
        else:
            st.subheader(f"Input matched to: **{matched_title}**")
            if not recommendations:
                st.info("No recommendations found.")
            else:
                st.write("### Recommended Books")
                # Display recommendations 2 per row
                for i in range(0, len(recommendations), 2):
                    cols = st.columns(2)
                    for j, col in enumerate(cols):
                        idx = i + j
                        if idx >= len(recommendations):
                            break
                        rec = recommendations[idx]
                        with col:
                            st.markdown(f"**{rec['title']}**  \n*by {rec['author']}*")
                            if isinstance(rec["image"], str) and rec["image"].strip():
                                st.image(rec["image"], width=160)
                            #st.caption(f"Similarity Score: {rec['score']:.3f}")
                            st.markdown("---")
# ============================================================== # ==============================================================
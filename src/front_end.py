import streamlit as st
import numpy as np
from PIL import Image
import time
from scipy.spatial.distance import cdist

# Load Data
@st.cache_data
def read_data():
    Vectors = np.load("Vectors.npy")
    Names = np.load("Names.npy")
    return Vectors, Names

Vectors, Names = read_data()

# Sidebar
st.sidebar.image("/Users/krishnenduhalder/visual search engine for similar search images/logo.png", use_column_width=True)
st.sidebar.markdown("## About")
st.sidebar.markdown("This application helps in finding visually similar images from a dataset. Simply select an image and let the AI find the most relevant matches!")
st.sidebar.markdown("---")
st.sidebar.markdown("# Model created by Krishnendu for finding similar images.")

# Title & Description
st.title("🔍 Image Similarity Finder")
st.markdown("Select an image and find the most similar ones from the dataset!")

# Layout for Image Display
_ , image_col , _ = st.columns([1, 3, 1])
button_col1, button_col2 = st.columns([1, 1])

# Buttons with Icons
ch = button_col1.button("🎲 Pick Random Image", use_container_width=True)
fs = button_col2.button("🔍 Find Similar Images", use_container_width=True)

# Image Selection Logic
if ch:
    st.session_state["disp_img"] = Names[np.random.randint(len(Names))]
    image_col.image(Image.open("./images/" + st.session_state["disp_img"]), caption="Selected Image", use_column_width=True)
    st.success(f"Selected: {st.session_state['disp_img']}")

# Finding Similar Images
if fs and "disp_img" in st.session_state:
    with st.spinner("Finding similar images..."):
        time.sleep(1)  # Simulating processing delay
        idx = int(np.argwhere(Names == st.session_state["disp_img"]))
        target_vec = Vectors[idx]
        top5 = cdist(target_vec[None, ...], Vectors).squeeze().argsort()[1:6]
    
    # Display Images in Columns
    st.subheader("Top 5 Similar Images")
    sim_col1, sim_col2, sim_col3, sim_col4, sim_col5 = st.columns(5)
    
    sim_col1.image(Image.open("./images/" + Names[top5[0]]), use_column_width=True)
    sim_col2.image(Image.open("./images/" + Names[top5[1]]), use_column_width=True)
    sim_col3.image(Image.open("./images/" + Names[top5[2]]), use_column_width=True)
    sim_col4.image(Image.open("./images/" + Names[top5[3]]), use_column_width=True)
    sim_col5.image(Image.open("./images/" + Names[top5[4]]), use_column_width=True)
    
    st.success("Similar images displayed successfully!")

elif fs:
    st.warning("⚠️ Please select an image first!")

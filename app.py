import streamlit as st
import pandas as pd
import os
from PIL import Image

# Page Config
st.set_page_config(page_title="Mysore Tourism", layout="wide")

# Function to check if the image exists
def display_image(image_path, caption=None):
    st.image(image_path, use_container_width=True, caption=caption)

# Custom CSS for navigation and styling
st.markdown(
    '''
    <style>
        .navbar {
            display: flex;
            justify-content: center;
            background-color: #4CAF50;
            padding: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .navbar button {
            background: none;
            border: none;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            cursor: pointer;
        }
        .navbar button:hover {
            background: #45a049;
        }
    </style>
    ''',
    unsafe_allow_html=True
)

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

def set_page(page):
    st.session_state["page"] = page

# Navigation Menu
st.markdown('<div class="navbar">', unsafe_allow_html=True)
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    if st.button("Home"): set_page("Home")
with col2:
    if st.button("Attractions"): set_page("Attractions")
with col3:
    if st.button("Travel Guide"): set_page("Travel Guide")
with col4:
    if st.button("Map"): set_page("Map")
with col5:
    if st.button("Virtual Tour"): set_page("Virtual Tour")
with col6:
    if st.button("Contact"): set_page("Contact")
st.markdown('</div>', unsafe_allow_html=True)

# Page Routing
page = st.session_state["page"]

# Home Page
if page == "Home":
    st.title("Welcome to Mysore Tourism")
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown("""
        ### 🏰 **Discover the Royal Heritage of Mysore**
        Mysore, also known as **Mysuru**, is a city rich in **cultural heritage** and historical significance. 
        
        - 🕌 **Mysore Palace**: Magnificent Indo-Saracenic architecture.
        - 🌳 **Brindavan Gardens**: Musical fountain and scenic beauty.
        - 🦁 **Mysore Zoo**: Oldest zoo in India.
        - 🌿 **Chamundi Hills**: Panoramic city views.
        - ⛪ **St. Philomena’s Church**: Stunning Gothic architecture.
        """)
    with col2:
        display_image("mysore_palace1.jpg")

# Attractions Page
elif page == "Attractions":
    st.title("Top Attractions in Mysore")
    attractions = [
        {"name": "Chamundi Hills", "image": "chamundi_hills.jpg"},
        {"name": "Brindavan Gardens", "image": "brindavan_gardens.jpg"},
        {"name": "Mysore Zoo", "image": "mysore_zoo.jpg"},
        {"name": "St. Philomena’s Church", "image": "st_philomena.jpg"},
        {"name": "Karanji Lake", "image": "karanji_lake.jpg"},
        {"name": "Rail Museum", "image": "rail_museum.jpg"}
    ]
    for i in range(0, len(attractions), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(attractions):
                with cols[j]:
                    display_image(attractions[i + j]["image"], attractions[i + j]["name"])

# Map Page
elif page == "Map":
    st.title("Map of Attractions")
    locations = pd.DataFrame({
        "lat": [12.3052, 12.4218, 12.3021, 12.3107, 12.2958, 12.3269],
        "lon": [76.6551, 76.5761, 76.6385, 76.6394, 76.6389, 76.6621],
        "name": ["Chamundi Hills", "Brindavan Gardens", "Mysore Zoo", "St. Philomena’s Church", "Mysore Palace", "Karanji Lake"]
    })
    st.map(locations)

# Virtual Tour Page
elif page == "Virtual Tour":
    st.title("360° Virtual Tour")
    st.markdown(
        '''
        <iframe 
        src="https://www.google.com/maps/embed?pb=!4v1711824691649!6m8!1m7!1sCAoSLEFGMVFpcE1pdjZ2V1BoQkVmdVZrS0h5X2dXT2hPdHdSRzI1Mlh5NlBN!2m2!1d12.3052!2d76.6551!3f0!4f0!5f0.7820865974627469" 
        width="100%" height="500" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        ''',
        unsafe_allow_html=True
    )

# Contact Page
elif page == "Contact":
    st.title("Contact Us")
    st.write("📧 Email: info@mysoretourism.com")
    st.write("📞 Phone: +91-9876543210")

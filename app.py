import streamlit as st
import pandas as pd
from PIL import Image

# Page Config
st.set_page_config(page_title="Mysore Tourism", layout="wide")

# Custom CSS for navigation and styling
st.markdown(
    '''
    <style>
        body {
            background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
            font-family: Arial, sans-serif;
        }
        .navbar {
            display: flex;
            justify-content: center;
            background-color: #4CAF50;
            padding: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .navbar a {
            color: white;
            text-decoration: none;
            padding: 10px 20px;
            margin: 0 10px;
            font-size: 18px;
        }
        .navbar a:hover {
            background: #45a049;
        }
        .container {
            text-align: center;
            padding: 20px;
        }
        iframe {
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }
    </style>
    ''',
    unsafe_allow_html=True
)

# Horizontal Navigation
st.markdown(
    '''
    <div class="navbar">
        <a href="?page=Home">Home</a>
        <a href="?page=Attractions">Attractions</a>
        <a href="?page=Travel Guide">Travel Guide</a>
        <a href="?page=Map">Map</a>
        <a href="?page=Virtual Tour">360° Tour</a>
        <a href="?page=Contact">Contact</a>
    </div>
    ''',
    unsafe_allow_html=True
)

# Page Routing using st.query_params
query_params = st.query_params
page = query_params.get("page", "Home")

# Home Page with Mysore Description (Left) and Image (Right)
if page == "Home":
    st.title("Welcome to Mysore Tourism")

    # Create two columns
    col1, col2 = st.columns([1.5, 1])  # Description (1.5x width) and image (1x width)

    with col1:
        # Description on the left
        st.markdown("""
        ### 🏰 **Discover the Royal Heritage of Mysore**
        
        Mysore, also known as **Mysuru**, is a city rich in **cultural heritage** and historical significance, 
        often referred to as the **Cultural Capital of Karnataka**. Known for its **magnificent palaces, vibrant festivals, 
        and serene gardens**, Mysore offers an enchanting experience to travelers.

        - 🕌 **Mysore Palace**: The crown jewel of Mysore, this grand palace is a blend of **Indo-Saracenic architecture**, 
        with intricate domes, beautiful halls, and vibrant stained glass windows.
        
        - 🌳 **Brindavan Gardens**: Famous for its **musical fountain** and illuminated terraces, offering a scenic escape.
        
        - 🦁 **Mysore Zoo**: One of the oldest and most well-maintained zoos in India, home to diverse wildlife.
        
        - 🌿 **Chamundi Hills**: Known for the **Chamundeshwari Temple**, offering panoramic views of the city.
        
        - ⛪ **St. Philomena’s Church**: A majestic Gothic-style church with stunning stained glass windows.
        
        ### 🌞 **Why Visit Mysore?**
        - Rich **heritage and architecture**
        - Lush **gardens and scenic spots**
        - Traditional **silk sarees** and sandalwood products
        - Famous for the **Dasara festival**, celebrated with grandeur and splendor.
        """)

    with col2:
        # Image on the right
        st.image("mysore_palace1.jpg", use_container_width=True)

# Attractions Page with 3 images in a row
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

    # Display images in rows of 3
    for i in range(0, len(attractions), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(attractions):
                with cols[j]:
                    st.image(attractions[i + j]["image"], caption=attractions[i + j]["name"], use_container_width=True)

# Travel Guide Page
# Travel Guide Page with Menu System
elif page == "Travel Guide":
    st.title("Travel Guide")

    # Sidebar menu
    menu = st.sidebar.radio(
        "Explore the Travel Guide", 
        ["How to Reach", "Where to Stay", "Restaurants & Cuisine", "Local Festivals", "Shopping"]
    )

    # How to Reach Section
    if menu == "How to Reach":
        st.markdown("### ✈️ **How to Reach Mysore**")

        st.write("#### 🛫 By Air:")
        st.write("- **Nearest Airport:** Mysore Airport (MYQ) – Located approximately 12 km from the city center.")
        st.write("- **Flights:** Direct flights from Bangalore, Chennai, and Hyderabad.")
        st.write("- **Bangalore Airport:** Major international flights land at Bangalore Airport (170 km from Mysore).")

        st.write("#### 🚉 By Train:")
        st.write("- **Railway Station:** Mysore Junction (MYS), well-connected to major cities.")
        st.write("- **Train Options:** Shatabdi Express, Chamundi Express, Tippu Express.")
        st.write("- **Travel Time:** Bangalore to Mysore by train takes approximately 2.5 to 3 hours.")

        st.write("#### 🚗 By Road:")
        st.write("- **Distance from Bangalore:** 145 km (approx. 3 hours by car or bus).")
        st.write("- **Bus Services:** KSRTC and private buses operate frequently.")
        st.write("- **Taxi:** Private cabs and ride-sharing services like Ola and Uber are available.")

    # Where to Stay Section
    elif menu == "Where to Stay":
        st.markdown("### 🏨 **Where to Stay in Mysore**")

        st.write("#### 🌟 **Luxury Hotels:**")
        st.write("- **Radisson Blu Plaza Hotel:** Elegant rooms, fine dining, and a spa.")
        st.write("- **Fortune JP Palace:** Premium amenities with traditional Mysorean hospitality.")
        st.write("- **Royal Orchid Metropole:** Heritage hotel with colonial architecture.")

        st.write("#### 💎 **Mid-Range Hotels:**")
        st.write("- **Hotel Pai Vista:** Comfortable stay with good amenities.")
        st.write("- **The Quorum Hotel:** Contemporary hotel with a rooftop pool.")
        st.write("- **Sandesh The Prince:** Blend of modern and traditional hospitality.")

        st.write("#### 💰 **Budget-Friendly Stays:**")
        st.write("- **Hotel Roopa:** Affordable and centrally located.")
        st.write("- **Aishwarya Residency:** Clean, comfortable, and budget-friendly.")
        st.write("- **MTR Residency:** Convenient location and economical rates.")

    # Restaurants & Cuisine Section
    elif menu == "Restaurants & Cuisine":
        st.markdown("### 🍽️ **Popular Restaurants and Local Cuisine**")

        st.write("#### 🥗 **Traditional Mysore Dishes:**")
        st.write("- **Mysore Masala Dosa:** Crispy dosa with spicy red chutney.")
        st.write("- **Mysore Pak:** Famous sweet made from ghee, sugar, and gram flour.")
        st.write("- **Chitranna:** Lemon rice with peanuts and spices.")
        st.write("- **Bisi Bele Bath:** A spicy rice dish cooked with lentils and vegetables.")

        st.write("#### 🍴 **Best Restaurants in Mysore:**")
        st.write("- **Vinayaka Mylari:** Famous for its soft dosas and chutney.")
        st.write("- **RRR Restaurant:** Known for Karnataka-style meals on banana leaves.")
        st.write("- **The Old House:** Continental and Italian dishes in a cozy ambiance.")
        st.write("- **Oyster Bay:** Multi-cuisine dishes with garden seating.")

    # Local Festivals Section
    elif menu == "Local Festivals":
        st.markdown("### 🎉 **Local Festivals and Events**")

        st.write("#### 🎊 **Mysore Dasara:**")
        st.write("- **Celebration:** Grand festival celebrated during Navaratri with cultural programs, processions, and exhibitions.")
        st.write("- **Jamboo Savari:** Famous elephant procession with a golden howdah.")
        
        st.write("#### 🎭 **Mysore Winter Festival:**")
        st.write("- **Held in December:** Features flower shows, cultural performances, and exhibitions.")
        st.write("- **Venue:** Mysore Palace and other major landmarks.")
        
    # Shopping Section
    elif menu == "Shopping":
        st.markdown("### 🛍️ **Shopping in Mysore**")
        
        st.write("#### 🛒 **Local Specialties:**")
        st.write("- **Mysore Silk Sarees:** Known for rich texture and quality.")
        st.write("- **Sandalwood Products:** Incense sticks, oils, and decorative items.")
        st.write("- **Handicrafts:** Wooden toys, inlay work, and traditional souvenirs.")
        
        st.write("#### 🛍️ **Famous Markets:**")
        st.write("- **Devaraja Market:** Bustling market with fresh produce, spices, and flowers.")
        st.write("- **Cauvery Handicrafts Emporium:** Government-run store for authentic silk and handicrafts.")
        st.write("- **Mall of Mysore:** Modern shopping mall with branded outlets and restaurants.")

# Map Page
elif page == "Map":
    st.title("Map of Attractions")
    locations = pd.DataFrame({
        "lat": [12.3052, 12.4218, 12.3021, 12.3107, 12.2958, 12.3269],
        "lon": [76.6551, 76.5761, 76.6385, 76.6394, 76.6389, 76.6621],
        "name": ["Chamundi Hills", "Brindavan Gardens", "Mysore Zoo", "St. Philomena’s Church", "Mysore Palace", "Karanji Lake"]
    })
    st.map(locations)

# Virtual Tour Page with Google Maps 360° embed
elif page == "Virtual Tour":
    st.title("360° Virtual Tour")
    st.write("Experience the beauty of Mysore with immersive 360° views.")
    
    # Embed Google Maps 360° view
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

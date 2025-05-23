import streamlit as st
from PIL import Image

st.set_page_config(page_title="K-beautyuz", layout="wide")

st.markdown("<h1 style='text-align: center; color: hotpink;'>K-beautyuz</h1>", unsafe_allow_html=True)
st.markdown("### Korean Cosmetics & Skincare")
st.markdown("Discover the best of K-beauty with our curated selection of products that nourish your skin and enhance your natural beauty.")

def display_product(image_path, name, price):
    st.image(image_path, use_container_width=True)
    st.write(f"**{name}**")
    st.write(f"Price: {price} 🇺🇿UZS")


# --- Face Care ---
st.markdown("## 🌿 Skin Care")
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col15 = st.columns(12)
with col1:
    display_product("images/product1.jpg", "d'Alba - Waterfull mild sun cream 50ml", "214.900")
with col2:
    display_product("images/product2.jpg", "d'Alba - White Truffle VEGAN First Spray Serum 100ml", "239.000")
with col3:
    display_product("images/product3.jpg", "Madagascar Centella Teatrica Soothing Sun Milk 50ml", "149.000")
with col4:
    display_product("images/product4.jpg", "ma:nyo - Pure Cleansing Oil 200ml", "204.990")
with col5:
    display_product("images/product5.jpg", "ma:nyo - Bifida Cica Herb Toner 210ml", "169.000")
with col6:
    display_product("images/product6.jpg", "ma:nyo - Deep Pore Cleansing Soda Foam 150ml", "169.000")
with col7:  
    display_product("images/product7.jpg", "Celimax - Derma Nature Fresh Blackhead Jojoba Cleansing Oil 150ml", "139.000")
with col8:
    display_product("images/product8.jpg", "d'Alba - White Truffle Double Serum & Cream 70ml", "499.000")
with col9:
    display_product("images/product9.jpg", "Dr.G Black Snail Toner 150ml + Emulsion 150ml", "379.000")
with col10:
    display_product("images/product10.jpg", "ELLE PARIS EGF Vitamin Blemish Moisture Serum", "129.000")
with col11:
        display_product("images/product23.jpg", "Missha Vita C Plus Ampoule 33%", "349.000")
with col15:    
    display_product("images/product29.jpg", "Dr.G Brightening Peeling Gel 150ml", "259.000")
# --- Skin Care ---
st.markdown("## 🌸 Face Care")
col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14 = st.columns(11)
with col4:
    display_product("images/product11.jpg", "Shingmulwon - Botanical Garden Aloe Fresh Soothing Big Foam Cleanser", "170.000")
with col5:
    display_product("images/product12.jpg", "Shingmulwon CICA - Clear Foam Cleanser", "170.000")
with col6:
    display_product("images/product13.jpg", "Tea Tree Cleansing Foam 200ml", "150.000")
with col7:
    display_product("images/product14.jpg", "Tenzero Balancing Foam Cleanser" , "90.000")
with col8:
    display_product("images/product15.jpg", "The History of Whoo Radiant Special Gift Set mini set", "295.000")
with col9:
    display_product("images/product16.jpg", "HERA SIGNIA DELUXE KIT", "399.000")
with col10:
    display_product("images/product17.jpg", "Hera Signia Deluxe Kit", "389.000")
with col11:
    display_product("images/product18.jpg", "The First Geniture  mini set", "369.000")
with col12:
    display_product("images/product19.jpg", "TenZero Perfect UV Sun Cushion", "239.000")
with col13:
    display_product("images/product20.jpg", "LABIOTTE Collagen Tone Up Cream ", "209.000")
with col14:
    display_product("images/product21.jpg", " BAGEL Eyelash Serum", "139.000")

# --- Hair Care ---
st.markdown("## 💇 Hair Care")
col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18 = st.columns(12)
with col7:
    display_product("images/product22.jpg", "Labiotte Silk Hair Treatment Oil 150ml", "270.000")
with col8:
    display_product("images/product24.jpg", "AROMATICA Rosemary Root Enhancer 100ml", "260.000")
with col9:
    display_product("images/product25.jpg", "R3 Argan Hair Oil 100ml", "169.000")
with col10:
    display_product("images/product26.jpg", "Perfect Serum 80ml", "229.000")
with col11:
    display_product("images/product27.jpg", "Argan Treatment Hair Mist / Argan Gold Treatment Hair Mist", "149.000")
with col12:
    display_product("images/product28.jpg", "100% Pure Argan Oil 1 set", "239.000")                   
with col13:
    display_product("images/product30.jpg", "Hair Plus Protein Bond Ampoule Hair Essence 145ml", "199.000")
with col14:
    display_product("images/product31.jpg", "Dr. For Hair Polligen Plus Shampoo 500ml", "209.000")
with col15:
    display_product("images/product32.jpg", "Head Spa 7 The Premium Treatment 210ml ", "159.000")
with col16:
    display_product("images/product33.jpg", "L'Oréal Paris Total Repair 5 Treatment Hair Pack 170ml", "129.000")
with col17:         
    display_product("images/product34.jpg", "Jay Forest Purple Jay Water Glow Protein Hair Essence 100ml", "199.000")
with col18: 
    display_product("images/product35.jpg", "Mise en scene Perfect Base Up Hair Essence 200ml", "149.000")
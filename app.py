import streamlit as st
import pickle
import numpy as np
import pandas as pd

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="PG Rent Prediction", layout="wide")

# -------------------------
# BLACK THEME
# -------------------------
st.markdown("""
<style>
.stApp {background-color:#000;color:white;}
h1,h2,h3,h4,p,label {color:white !important;}

.stButton>button {
    background-color:#00ff88;
    color:black;
    border-radius:8px;
    font-weight:bold;
}

div[data-baseweb="select"] > div {
    background-color:#111 !important;
    color:white !important;
}

div[role="option"] {
    background:#000 !important;
    color:white !important;
}
div[role="option"]:hover {
    background:#00ff88 !important;
    color:black !important;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# LOAD MODEL
# -------------------------
model = pickle.load(open("pg_rent_model.pkl", "rb"))
le_location = pickle.load(open("le_location.pkl", "rb"))
le_sharing = pickle.load(open("le_sharing.pkl", "rb"))

# -------------------------
# LOAD DATASET (CSV)
# -------------------------
df = pd.read_csv("pune_pg_dataset_1000.csv")

# -------------------------
# SESSION STATE
# -------------------------
if "page" not in st.session_state:
    st.session_state.page = 1

if "history" not in st.session_state:
    st.session_state.history = []

# -------------------------
# PAGE 1
# -------------------------
if st.session_state.page == 1:

    st.markdown("<h1>🏠 Welcome to PG Rent Prediction System</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#00ff88;'>🎯 Predict rent easily based on location & sharing</h3>", unsafe_allow_html=True)

    location = st.selectbox("📍 Location", le_location.classes_)
    sharing_type = st.selectbox("👥 Sharing Type", le_sharing.classes_)

    if st.button("🚀 Predict Rent"):

        st.session_state.location = location
        st.session_state.sharing = sharing_type

        loc_encoded = le_location.transform([location])[0]
        share_encoded = le_sharing.transform([sharing_type])[0]

        input_data = np.array([[loc_encoded, share_encoded, 500,
                                1,1,1,1,1,1,1,1,1,1,
                                1,1,4.5]])

        prediction = model.predict(input_data)

        st.session_state.predicted_rent = int(prediction[0])
        st.session_state.page = 2
        st.rerun()

# -------------------------
# PAGE 2
# -------------------------
elif st.session_state.page == 2:

    st.title("🔍 Customize Amenities")
    st.success(f"💰 Base Rent: ₹ {st.session_state.predicted_rent}")

    wifi = st.selectbox("WiFi", [0,1])
    ac = st.selectbox("AC", [0,1])
    food = st.selectbox("Food", [0,1])
    parking = st.selectbox("Parking", [0,1])
    laundry = st.selectbox("Laundry", [0,1])
    power = st.selectbox("Power Backup", [0,1])
    security = st.selectbox("Security", [0,1])
    housekeeping = st.selectbox("Housekeeping", [0,1])
    bathroom = st.selectbox("Attached Bathroom", [0,1])
    geyser = st.selectbox("Geyser", [0,1])

    size = st.slider("Room Size", 300, 700, 500)

    if st.button("🔄 Update Prediction"):

        loc_encoded = le_location.transform([st.session_state.location])[0]
        share_encoded = le_sharing.transform([st.session_state.sharing])[0]

        input_data = np.array([[loc_encoded, share_encoded, size,
                                wifi, ac, food,
                                parking, laundry, power,
                                security, housekeeping, bathroom,
                                geyser,
                                1,1,4.5]])

        prediction = model.predict(input_data)
        rent = int(prediction[0])

        st.session_state.predicted_rent = rent

        # SAVE HISTORY (NO MYSQL)
        st.session_state.history.append({
            "location": st.session_state.location,
            "sharing": st.session_state.sharing,
            "rent": rent
        })

        st.success(f"💰 Updated Rent: ₹ {rent}")

    if st.button("➡️ Go to Data Page"):
        st.session_state.page = 3
        st.rerun()

# -------------------------
# PAGE 3
# -------------------------
elif st.session_state.page == 3:

    st.title("📊 Data & Prediction History")

    st.subheader("📌 PG Dataset")
    st.dataframe(df.head(50))

    st.subheader("📜 Prediction History")

    if st.session_state.history:
        st.dataframe(pd.DataFrame(st.session_state.history))
    else:
        st.warning("No history yet")

    if st.button("🔙 Back to Home"):
        st.session_state.page = 1
        st.rerun()

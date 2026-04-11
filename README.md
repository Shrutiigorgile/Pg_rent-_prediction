# Pg_rent-_prediction
 PG Rent Prediction ML Project
# 🏠 PG Rent Prediction System

A Machine Learning-based web application that predicts PG (Paying Guest) rent in Pune based on location, sharing type, and amenities.

---

## 🚀 Project Overview

This project helps users:
- 💰 Predict PG rent instantly
- 📍 Select location & sharing type
- 🏡 Customize amenities
- 📊 View dataset & prediction history

---

## 🎯 Project Objectives

### 1️⃣ Rent Prediction
To develop a machine learning model that predicts PG rent based on:
- Location
- Sharing Type
- Amenities

### 2️⃣ PG Recommendation (Future Scope)
To suggest best PG accommodations based on:
- Budget
- Location
- Preferences

---

## 🧠 Machine Learning Model

- Model Used: **Random Forest Regressor**
- Features Used:
  - location
  - sharing_type
  - size_sqft
  - wifi, ac, food, parking, laundry
  - power_backup, security, housekeeping
  - attached_bathroom, geyser
  - gender, preferred_tenant, rating
- Target Variable:
  - rent

---

## 📂 Project Structure
pg-rent-prediction/
│
├── app.py # Streamlit Application
├── pg_rent_model.pkl # Trained ML Model
├── le_location.pkl # Location Encoder
├── le_sharing.pkl # Sharing Encoder
├── pune_pg_dataset_1000.csv # Dataset
├── requirements.txt # Dependencies
└── README.md # Project Documentation


---

## ⚙️ Installation & Setup

### Step 1: Clone Repository

```bash
git clone https://github.com/your-username/pg-rent-prediction.git
cd pg-rent-prediction


---

## 📌 Conclusion

The **PG Rent Prediction System** is a practical machine learning application that helps users estimate rental prices based on real-world factors like location, sharing type, and amenities.

This project demonstrates:
- End-to-end ML pipeline (data → model → deployment)
- Real-world problem solving
- Interactive UI using Streamlit
- Integration of data, model, and user experience

It can be further expanded into a **full-scale rental platform** with recommendation systems, analytics dashboards, and real-time data integration.

---

## 👩‍💻 Author

**Shruti Gorgile**  
🎓 Aspiring Data Analyst | Machine Learning Enthusiast  

- 💼 Interested in: Data Science, ML, Analytics  
- 📍 Location: Pune, India  

---

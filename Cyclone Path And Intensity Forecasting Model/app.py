import streamlit as st
import numpy as np
import joblib
from tensorflow.keras.models import load_model
import pandas as pd
import folium
from streamlit_folium import st_folium

# Load models and scaler
path_model = load_model("cyclone_path_model.h5")
intensity_model = load_model("cyclone_intensity_model.h5")
scaler = joblib.load("scaler.pkl")

# Prediction function
def predict_cyclone(new_data):
    new_data_scaled = scaler.transform(new_data)
    new_data_reshaped = new_data_scaled.reshape(1, new_data_scaled.shape[0], new_data_scaled.shape[1])
    pred_path = path_model.predict(new_data_reshaped)
    pred_intensity = intensity_model.predict(new_data_reshaped)
    return pred_path, pred_intensity

st.title("Cyclone Path & Intensity Prediction")

time_steps = 5
features = ['Year','Month','Day','Hour','Prev_Lat','Prev_Lon','Prev_MaxWind','Minimum Central Pressure']

# --- Data Input Section ---
st.subheader("Enter cyclone data for 5 timesteps")

rows = []
for i in range(time_steps):
    st.write(f"--- Timestep {i+1} ---")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        year = st.number_input(f"Year (T{i+1})", 1900, 2100, 2025, key=f"year{i}")
        month = st.slider(f"Month (T{i+1})", 1, 12, 9, key=f"month{i}")
    with col2:
        day = st.slider(f"Day (T{i+1})", 1, 31, 13, key=f"day{i}")
        hour = st.slider(f"Hour (T{i+1})", 0, 23, 6, key=f"hour{i}")
    with col3:
        lat = st.slider(f"Prev Lat (T{i+1})", -90.0, 90.0, 12.0, 0.1, key=f"lat{i}")
        lon = st.slider(f"Prev Lon (T{i+1})", -180.0, 180.0, 75.0, 0.1, key=f"lon{i}")
    with col4:
        wind = st.number_input(f"Prev MaxWind (T{i+1})", 0, 400, 50, key=f"wind{i}")
        pressure = st.number_input(f"Pressure (T{i+1})", 800, 1100, 980, key=f"pres{i}")
    
    rows.append([year, month, day, hour, lat, lon, wind, pressure])

input_df = pd.DataFrame(rows, columns=features)

# --- Prediction Section ---
if st.button("Predict Cyclone Path & Intensity"):
    new_data = input_df.to_numpy()
    pred_path, pred_intensity = predict_cyclone(new_data)

    # Save in session_state so they don't vanish
    st.session_state.pred_path = pred_path
    st.session_state.pred_intensity = pred_intensity

# --- Show Results ---
if "pred_path" in st.session_state:
    st.success("Prediction Complete!")

    # Show intensity predictions cleanly (no "Step X")
    st.subheader("Predicted Maximum Wind Speeds:")
    pred_intensity = np.array(st.session_state.pred_intensity)[0]
    for intensity in pred_intensity:
        st.write(f"{intensity:.2f} knots")

    st.subheader("Predicted Cyclone Track")

    pred_path = np.array(st.session_state.pred_path)

    # Fix shape issues
    if pred_path.ndim == 3:
        lat_lon = pred_path[0]   
    elif pred_path.ndim == 2:
        lat_lon = pred_path      
    else:
        st.error("Unexpected shape from model")
        st.stop()

    lat = lat_lon[:, 0]
    lon = lat_lon[:, 1]

    cyclone_map = folium.Map(location=[float(lat[0]), float(lon[0])], zoom_start=5)

    points = list(zip(lat, lon))

    # Draw polyline for path
    folium.PolyLine(points, color="orange", weight=3, opacity=0.8).add_to(cyclone_map)

    # Single marker (centered on last predicted location)
    folium.Marker(
        location=[lat[-1], lon[-1]],
        popup=f"Predicted Location: ({lat[-1]:.2f}, {lon[-1]:.2f})",
        icon=folium.Icon(color="red", icon="location-dot", prefix="fa")
    ).add_to(cyclone_map)

    st_folium(cyclone_map, width=700, height=500)

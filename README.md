# Cyclone-Path-And-Intensity-Forecasting-Model

**THEME** - CLIMATE RISK AND DISASTER MANAGEMENT


# A deep learning project developed during a 4-week internship at EDUNET Foundation, in collabration with AICTE & Shell.
The project predicts cyclone tracks (latitude & longitude) and intensity (maximum wind speed) using LSTM-based models. It is deployed with Streamlit for an interactive interface where users can input cyclone data and visualize predictions on a map.

📌 Features

📥 User-friendly input for cyclone data (Year, Month, Day, Hour, Prev Lat, Prev Lon, Prev MaxWind, Pressure).

🌀 Path Prediction: Forecasts cyclone trajectory (latitude & longitude sequence).

💨 Intensity Prediction: Forecasts maximum wind speed (in knots).

🗺️ Interactive Map: Visualizes cyclone path with a polyline and a marker on the predicted final location.

⚡ Real-time predictions with pre-trained LSTM models.

🛠️ Tech Stack

Python 3.10+

TensorFlow / Keras – for LSTM models

scikit-learn – for preprocessing & scaling

Streamlit – for deployment

Folium + streamlit-folium – for cyclone path visualization on map

Pandas / NumPy – for data handling

📂 Project Structure

Cyclone Path And Intensity Forecasting Model\
│── app.py                      # Streamlit app (UI + prediction + map)

│── cyclone_path_model.h5       # Trained LSTM model for path prediction

│── cyclone_intensity_model.h5  # Trained LSTM model for intensity prediction

│── scaler.pkl                  # Pre-fitted StandardScaler

│── requirements.txt            # Required dependencies

│── README.md                   # Project documentation

🚀 Installation

Clone the repository:

git clone https://github.com/student-smritipandey/Cyclone-Path-And-Intensity-Forecasting-Model.git
cd Cyclone Path And Intensity Forecasting Model


Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py

📊 Usage

Open the app in your browser (default: http://localhost:8501).

Enter cyclone details for 5 timesteps (Year, Month, Day, Hour, Latitude, Longitude, MaxWind, Pressure).

Click "🚀 Predict Cyclone Path & Intensity".

View results:

Predicted Intensities (knots).

Cyclone track on interactive map (orange polyline).

Final predicted location marker (red).

📸 Demo Screenshots


![alt text](C1.png)

![alt text](C2.png)


📌 Example Input
Timestep 1 → Year: 2025, Month: 9, Day: 13, Hour: 6, Lat: 12.0, Lon: 75.0, MaxWind: 50, Pressure: 980  
Timestep 2 → Year: 2025, Month: 9, Day: 13, Hour: 12, Lat: 12.2, Lon: 75.3, MaxWind: 55, Pressure: 978  
...

⚡ Requirements

See requirements.txt:

streamlit
tensorflow
scikit-learn
numpy
pandas
folium
streamlit-folium
joblib


Install all dependencies:

pip install -r requirements.txt

📖 Future Improvements

✅ Include cyclone category classification (based on intensity).

✅ Option to upload historical cyclone data (CSV).

✅ Real-time weather API integration.

✅ Animated cyclone path visualization.

## Author

**Smriti Pandey**

GitHub:https://github.com/student-smritipandey





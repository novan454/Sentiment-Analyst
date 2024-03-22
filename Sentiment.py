import pickle
import streamlit as st

# Function to set the Blue Light theme
def set_blue_light_theme():
    """
    Sets the Streamlit theme to Blue Light.
    """
    # Set primary color
    st.markdown(
        """
        <style>
        .css-1v3fvcr.e19vmkin0.css-1ns8z57.e15462ye0 {
            background-color: #f5f7ff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Set secondary color
    st.markdown(
        """
        <style>
        .css-1v3fvcr.e19vmkin0.css-1ns8z57.e5i1odf0 {
            background-color: #c0cbe1;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Set text color
    st.markdown(
        """
        <style>
        .css-1v3fvcr.e19vmkin0.css-1ns8z57.e1hbx90p0 {
            color: #2c3e50;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Set Blue Light theme
set_blue_light_theme()

# Title of the application
st.title('Emisi_CO2 Prediction')

# Description of the machine learning model
deskripsi_model = """
### Deskripsi Model Machine Learning

Alasan project
"""
# Display the description of the machine learning model
st.markdown(deskripsi_model)

# Feature inputs for prediction
new_text = st.text_input("Masukkan teks baru:")

if st.button('Predict'):
    # Load the pre-trained model
    with open('Sentiment.sav', 'rb') as f:
        model = pickle.load(f)
    
    # Load the vectorizer from the saved model
    vectorizer = model['vectorizer']
    
    # Perform prediction using the loaded model and vectorizer
    new_text_vec = vectorizer.transform([new_text])
    predicted_sentimen = model['model'].predict(new_text_vec)

    if predicted_sentimen[0] == 1:
        sentiment_label = "positif"
    elif predicted_sentimen[0] == 0:
        sentiment_label = "negatif"
    
    # Display the sentiment analysis result
    st.write('Hasil Analisis Sentimen:', sentiment_label)

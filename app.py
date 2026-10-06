import streamlit as st
import pickle

model = pickle.load(open('spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.title("Email Spam Detection")

message = st.text_area("Enter your email or SMS message:")

if st.button("Predict"):
    message_vectorized = vectorizer.transform([message])
    prediction = model.predict(message_vectorized)

    if prediction[0] == 1:
        st.error("Spam Message")
    else:
        st.success("Not Spam Message")
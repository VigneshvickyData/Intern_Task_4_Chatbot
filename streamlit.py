import streamlit as st
from main import generate_response, analyze_sentiment

st.set_page_config(page_title="Sentimental Analysis Chatbot", layout="centered")


## app title
st.title("🤖 Sentiment Analysis Chatbot")
st.write("This chatbot can detect your sentiment and respond appropriately!")


# Input field for user message
user_message = st.text_input("You:", placeholder="Type your message here...")

#submit button
if st.button("send"):
    #Ensure message is not empty
    if user_message.strip():
        # generate chatbot response
        response = generate_response(user_message)


        #analysis sentiment directly for UI feedback
        sentiment, _ = analyze_sentiment(user_message)


        st.text_area("Chatbot:", value=response, height=100)
        # display the sentiment detected by the model
        st.write(f"Sentiment Detected: {sentiment}") 

        # collect user feedback on chatbot's response
        sentiment_rating = st.slider("Rate the chatbot's response:", 1,5,3)
        st.write(f"Your rating: {sentiment_rating}/5")

        # feedback text area to get user feedback
        st.text_area("Your Feedback:", height=100, placeholder="How can we improve?")
    else:
        st.warning("Please enter a message!")    

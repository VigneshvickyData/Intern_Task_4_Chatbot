from transformers import pipeline

# Load the sentiment analysis pipeline and model from "Hugging face transformer "
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")


def analyze_sentiment(user_message):
    # Analyze the sentiment of a given user message and return sentiment and confidence score.
    
    result = sentiment_pipeline(user_message)[0]
    sentiment =result["label"]
    score = result["score"]


    # if confidence score is below 0.6 treat it as neutral
    if score < 0.6:
        sentiment = "NEUTRAL"

    return sentiment, score


def generate_response(user_message):
    # Generate a chatbot response based on user sentiment.
    
    sentiment, score = analyze_sentiment(user_message)

    if sentiment == "POSITIVE":
        return f"😊 I'm gled to hear that! How else can I assist you today?"
    elif sentiment == "NEGATIVE":
        return f"😔 I'm sorry to hear that. Let me know how I can help make things better."
    else:
        return "😐 Thank you for sharing. How can I assist youo further?"        


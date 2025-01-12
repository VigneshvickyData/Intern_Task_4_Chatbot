# Intership Project: Learn To Build A Real Time Gen AI Customer Service Bot

# Task 4 - Sentiment Analysis Chatbot Integration

## Introduction
This task focuses on integrating sentiment analysis into a chatbot to enable it to detect and respond appropriately to customer emotions during interactions. The goal is to recognize positive, negative, or netural sentiments and tailor responses to enchance user satisfaction.

* This implementation uses Hugging Face Transformers for sentiment analysis and Streamlit for the user interface(UI).

* Hugging Face Transformer Model:
[URL](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english)


## Background

Customer service chatbots are increasingly being used across industries to provide real-time support. Integrating sentiment analysis into chatbots allows them to understand customer emotions and respond empathetically, thereby improving the overall user experience. In this project, the sentiment analysis capability is achieved by leveraging pre-trained models from Hugging Face Transformers and building a responsive UI using Streamlit.



## Learning Objectives
* Understand the process of integrating sentiment analysis into chatbots.
* Enhance chatbot functionality to address customer emotions affectively.
* Build a user-friendly interface using Streamlit for seamless user interaction.

## Activities and Tasks
Activities Performed:

* Implemented sentiment analysis using a Hugging Face Transformers model.
* Developed response logic to tailor chatbot replies based on detected sentiment.
* Built a clean and responsive Streamlit UI for real-time sentiment analysis interactions.

Technologies Used:

* Programming Language: Python
* Sentiment Analysis Model: Hugging Face Transformers
* User Interface: Streamlit

## Skills and Competencies
* Programming: Python coding for chatbot integration.
* UI Development: Create a user friendly interface with Streamlit.
* Problem-Solving: Debugging and optimizing chatbot functionality.
* Customer Experience: Designing responses that improve user satisfaction.

## Feedback and Evidence
* The chatbot successfully detects sentiments in user messages with high accuracy.

### Evidence
* Positive Sentiment Analysis: 

![App Screenshot](https://github.com/VigneshvickyData/Data_Branching/blob/main/positive.png?raw=true)

* Negative Sentiment Analysis: 
![App Screenshot](https://github.com/VigneshvickyData/Data_Branching/blob/main/negative.png?raw=true)

## Challenges and Solutions

* Challenge: Model compatibility issues.

* Solution: Selected a pre-trained sentiment model that aligned with the project goals.
 
* Challenge: Ambiguous sentiment detection.

* Solution: Added fallback responses to handle edge cases effectively.

## Outcomes and Impact
Outcome:
* Sentiment Analysis: Implemented sentiment analysis for empathetic responses based on user emotions.

Impact:
* Enhanced user experience by personalizing responses according to sentiment.
* Improved customer satisfaction and engagement by addressing emotional cues during interactions.

## Conclusion
Task 4 successfully integrates sentiment analysis into the chatbot, enhancing its capability to understand and respond to customer emotions effectively. This integration demonstrates the potential of AI-powered chatbots to deliver a more empathetic and user-centric experience, paving the way for more advanced customer service solutions.

### To run the Environment: 
* Environment-> conda create -n senti_chatbot python=3.9 -y 
### Activitie the Environment:
* conda activate senti_chatbot
# Importing necessary libraries
import random

# Creating a dictionary to store responses
responses = {
    "hi": "Hello! How can I help you?",
    "services": "we are a teaching company and provide the best teaching and learning guidance to you to ace in your career",
    "courses": "We have different courses like DSA , Datascience, Competitive programming, Machine Learning , Software designing",
    "prices": "Our course prices range from 199 to 1000 rs. Our best selling course is DSA which is 499 per month. We offer you the best services and coaching startingjust for 199 rs,you can attend our free master class to learn more",
    "cost": "Our best selling course is DSA which is 499 per month. We offer you the best services and coaching startingjust for 199 rs,you can attend our free master class to learn more .",
    "mentors": "we provide the best mentors from the best colleges, our mentor are xyz from NIT delhi,Mr.abc from IIT Delhi",
    "register": "you can register for the course from our official website we also provide our email id you can also contact them in any problem",
    "duration": "Our courses basically are of 2- 3 months at your own pace",
    "default": "I'm sorry, I don't understand. Can you please ask me another question?"
}

# Defining the chatbot function
def chatbot():
    print("Hey there! I am AIBOT at your service")
    while True:
        user_input = input().lower()
        if user_input in ["bye", "goodbye", "exit", "quit"]:
            print("Thank you for using the chatbot. Good luck with your admission process!")
            break
        else:
            response = responses.get(user_input, responses["default"])
            print(response)

# Starting the chatbot
chatbot()

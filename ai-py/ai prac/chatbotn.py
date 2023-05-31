import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello, How are you?",]
    ],
    [
        r"(.*) services",
        ["We are a teaching company and provide the best teaching and learning guidance to help you excel in your career.",]
    ],
    [
        r"Hi|Hello|Hey there|Hola",
        ["Hello, How can I help you?",]
    ],
    [
        r"what is your name ?",
        ["My name is AIBOT and I work as the chatbot for online customer service.",]
    ],
    [
        r"What courses|packages|learning do you offer ?",
        ["We have different courses like DSA, Data Science, Competitive Programming, Machine Learning, Software Designing.",]
    ],
    [
        r"prices|cost",
        ["Our course prices range from 199 to 1000 rs.", "Our best-selling course is DSA which is 499 per month.",
         "We offer you the best services and coaching starting just for 199 rs.", "You can attend our free master class to learn more."]
    ],
    [
        r"(.*) mentors",
        ["We provide the best mentors from the best colleges.", "Our mentors are XYZ from NIT Delhi, Mr. ABC from IIT Delhi.",]
    ],
    [
        r"(.*) register",
        ["You can register for the course from our official website. We also provide our email id, and you can contact us in case of any problem.",]
    ],
    [
        r"(.*) duration (.*)",
        ["Our courses are typically 2-3 months long, and you can learn at your own pace.",]
    ],
    [
        r"(.*)additional (.*)",
        ["We offer one-to-one doubt solving.",]
    ],
    [
        r"bye",
        ["Goodbye! Have a great day.",]
    ]
]

def chat():
    print("Hey there! I am AIBOT at your service")
    chatbot = Chat(pairs, reflections)
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("AIBOT: Goodbye! Have a great day.")
            break
        else:
            print("AIBOT:", chatbot.respond(user_input))


if __name__ == "__main__":
    chat()

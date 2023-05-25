import streamlit as st
import json

# Define the restaurant chatbot
chatbot_rules = {
        "hi": "Hello! How can I assist you today?",
        "menu": "Sure! Here's our menu: idli, vada, sambar",
        "reservation": "To make a reservation, please call us or email us.",
        "location": "We are located at [insert address].",
        "thank you": "You're welcome! Enjoy your meal!",
        "default": "I'm sorry, but I'm not able to assist with that. How else can I help you?",
        "phone" : "Its 7689054368",
        "email": "restaurant@gmail.com"
    }

def load_dictionary():
    try:
        with open("dictionary.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save the dictionary to a file
def save_dictionary(dictionary):
    with open("dictionary.json", "w") as file:
        json.dump(dictionary, file)

def restaurant_chatbot(user_input):
    chatbot_rules = load_dictionary()
    user_input = user_input.lower()
    
    for key in chatbot_rules:
        if key in user_input:
            return chatbot_rules[key]
    
    return chatbot_rules["default"]


def main():
    nav = st.sidebar.radio("Navigate", ["Chat", "Add Questions"])
    quit = st.sidebar.button("Quit")

    if quit:
        st.empty()
        st.header("Thank you for using Restobot!")
        st.stop()
        

    if nav == "Chat":
        
        st.title("Restaurant Chatbot")
        st.markdown("Welcome to our restaurant chatbot!")

        user_input = st.text_input("User Input")
        submitted = st.button("Submit")

        if submitted:

            bot_response = restaurant_chatbot(user_input)
            st.text("Bot: " + bot_response)
            st.text("___________________________")  # Separator line

            
    elif nav == "Add Questions":
        add_question = st.text_input("Add keyword here", key = 'key')
        add_answer = st.text_input("Provide a response here", key='value')

        if st.button("Add rule"):
            chatbot_rules[add_question] = add_answer
            save_dictionary(chatbot_rules)
            st.success("Question and answer added successfully!")

        st.write("Existing Dictionary:", chatbot_rules)
            
                
if __name__ == '__main__':
    main()


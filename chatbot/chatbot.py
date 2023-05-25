import  streamlit as st
import json

def load_dictionary():
    with open('dictionary.json', 'r') as file:
        return json.load(file)
        

def save_dictionary(dictionary):
    with open('dictionary.json', 'w') as file:
        json.dump(dictionary, file)

chatbot_rules = load_dictionary()

def chatbot(user_input):
    chatbot_rules = load_dictionary()
    user_input = user_input.lower()

    for key in chatbot_rules:
        if key in user_input :
            return chatbot_rules[key]

    return chatbot_rules['default']

def main():
    st.header("Welcome to Restobot!")
    nav = st.sidebar.radio('Navigation', ['Chat', 'Add Questions'])
    if st.sidebar.button('Exit'):
        st.empty()
        st.title("Thanks for using RestoBot")
        st.stop()

    if nav == 'Chat':
        user_input = st.text_input("Ask restobot")
        if st.button("Submit"):
            bot_response = chatbot(user_input=user_input)
            st.write("Restobot:", bot_response)
            st.text("______________________________________")

    if nav == 'Add Questions':
        add_question = st.text_input("Add your keyword here")
        add_answer = st.text_input("Add the corrosponding response")
        if add_question and add_answer:
            if st.button("add question"):
                chatbot_rules[add_question] = add_answer
                save_dictionary(chatbot_rules)
                st.success("Added")


                
if __name__ == '__main__':
    main()




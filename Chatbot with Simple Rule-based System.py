#!/usr/bin/env python
# coding: utf-8

# In[1]:


# IMPORTING REQUIRED LIBRARY
import re


# In[2]:


# CREATING A SIMPLE CHATBOT 
def chatbot(user_input):
    user_input_lower = user_input.lower()

    # USINF IF-ELSE STATEMENTS
    if re.search(r'\b(hi|hello|hey)\b', user_input_lower):
        return "Hello! How can I assist you today?"

    elif re.search(r'\b(how are you|what\'s up|how\'s it going)\b', user_input_lower):
        return "I'm just a computer program, but I'm doing well. How about you?"

    elif re.search(r'\b(good|well|fine)\b', user_input_lower):
        return "That's great to hear!"

    elif re.search(r'\b(bad|not good|not well)\b', user_input_lower):
        return "I'm sorry to hear that. Is there anything specific bothering you?"

    elif re.search(r'\b(bye|goodbye|exit)\b', user_input_lower):
        return "Goodbye! Have a great day."

    # NEW RULES FOR ANY SPECIFIC TOPICS 
    elif re.search(r'\b(weather|temperature)\b', user_input_lower):
        return "I'm sorry, I don't have real-time weather information. You can check a weather website for that."

    elif re.search(r'\b(joke|funny)\b', user_input_lower):
        return "Why don't scientists trust atoms? Because they make up everything!"

    elif re.search(r'\b(name|who are you)\b', user_input_lower):
        return "I'm a chatbot designed to assist with basic queries. You can call me ChatGPT!"

    else:
        return "I'm sorry, I didn't understand that. Can you please provide more details or ask something else?"

# IMPROVED LOOP WITH A WELCOME MESSAGE AND AN EXITING CONDITION
print("Chatbot: Hi there! I'm your friendly chatbot. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye! Take care.")
        break

    response = chatbot(user_input)
    print("Chatbot:", response)


# In[ ]:





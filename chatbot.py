import random
def chatbot_response(user_input):      
    greetings=["hello","hi","hey"]
    goodbyes=["bye","see you","take care"]
    user_input_lower=user_input.lower()
    if any(greeting in user_input_lower for greeting in greetings):
        return random.choice(["HEllo!","Hi there!","HEy! How can I assist you?"])
    elif any(goodbye in user_input_lower for goodbye in goodbyes):
        return random.choice(["Goodbye!","Farewell! HAve a great day!"])
    else:
        return "I apologise if I didn't catch that. Can you please rephrase your query?"
user_input=input("User:")
print("Chatbot:",chatbot_response(user_input))
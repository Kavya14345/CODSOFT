# Chatbot:Rule-Based Chatbot
## Overview
This project is a simple rule-based chatbot that responds to user inputs based on predefined rules. It's designed to provide a basic understanding of natural language processing and conversation flow. The chatbot identifies user queries using if-else statements and responds accordingly.
## Features
1.**Greeting Responses**:
- When the user says "hello" or "hi" or "hey",the chatbot greets them with like "Hello!" or "Hi there!" or "Hey! How can I assist you?"

2.**Farewell Responses**:
- If the user mentions "bye" or "see you" or "take care", the chatbot bids farewell with messages like "Goodbye" or "Farewell! Have a great day!"

3.**Default Reponse**:
- If the user's input doesn't match any predefined patterns, the chatbot provides a polite default response.

## How It Works:
- The chatbot script (`chatbot.py`) contains a function called `chatbot_response`.
- Inside this function:
  - We define lists of greetings and goodbyes.
  - The user input is converted to lowercase for case-insensitive matching.
  - The chatbot checks if the input contains any greetings or goodbyes.
  - If found,it randomly selects an appropriate response.
  - Otherwise, it provides a default message.
## Usage:
1.**Clone the Repository**:
```
git clone https://github.com/Kavya/CODSOFT.git
```
2.**Run the Chatbot Locally**:
- Open your terminal or command prompt
- Navigate to the cloned repository folder.
- Run the chatbot script:
```
python chatbot.py
```
- Enter your queries and observe the chatbot's responses.
## Example Interactions
```
User:hello
Chatbot:Hi there! How can I assist you?

User:What's the weather like today?
Chatbot:I'm sorry,I didn't understand that.

User:bye
Chatbot:Farewell! Have a great day!
```
## Future Enhancements
- Expand the chatbot's rule-based logic.
- Integrate more patterns and responses.
- Consider adding sentiment analysis or context-awareness.
## License
This project is licensed under the MIT License. Feel free to use, modify and share it!

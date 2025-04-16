import random
import time

def chatbot():
    greetings = ["Hello there! 👋🏼", "Hi friend! 😊", "Hey! Nice to meet you! 🎊", "Howdy! 😃"]
    farewells = ["Goodbye! 👋🏼", "See you around! 👋🏼", "Have a nice day! 👋🏼", "Unitl next time! 👋🏼"]
    jokes = [
        "What do you call a dog that can do magic? A labracadabrador.",
        "What do you call a fake noodle? An impasta.",
        "What do you call a bear with no teeth? A gummy bear.",
        "Why did the tomato blush? Because it saw the salad dressing.",
    ]
    facts = [
        "Did you know that the average person walks the equivalent of 7 miles to work?",
        "A day on Venus is 225 Earth days.",
        "Honey never spoils, Archaeologists have found pots of honey that are over 1,000 years old.",
    ]
    bot_name = "Chatbot"
    print(f"{bot_name} is starting up...")
    time.sleep(1)
    
    print(f"""
        Welcome to the {bot_name}! I'm here to help you have a conversation with me.
        I can chat about: 
        1. 'Jokes' - Have a laugh!
        2. 'Facts' - Learn something new
        3. 'color' - Get a random color
        4. 'bye' - Say goodbye
          """)
    
    chatting = True
    user_name = input("What's your name: ").lower().strip()
    print(f"{bot_name}: Nice to meet you, {user_name}! How can I help you today")
    
    while chatting: 
        user_input = input("😊 You: ").strip()
        if user_input in ['hi', 'hello', 'hey', 'howdy']:
            print(f'🤖 {bot_name}: {random.choice(greetings)}')
        elif 'joke' in user_input:
            print(f'🤖 {bot_name}: {random.choice(jokes)}')
        elif 'fact' in user_input:
            print(f'🤖 {bot_name}: {random.choice(facts)}')
        elif 'color' in user_input:
            print(f"🤖 {bot_name}: My favourite color is robot red! What's yours")  
            color = input("😊 You: ").lower().strip()
            print(f"🤖 {bot_name}: {color} is a great color too!")
        elif user_input in ['bye', 'goodbye']:
            print(f"🤖 {bot_name}: It' was nice chatting with you!")
            print(f'🤖 {bot_name}: {random.choice(farewells)}')
            chatting = False
        else:
            print(f"🤖 {bot_name}: I'm sorry, I don't understand that.")
    print(f"Thanks for chatting with me! Run the program again to start a new conversation.")
chatbot()
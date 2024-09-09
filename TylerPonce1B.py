#This program will simulate the magic 8ball toy
import random
#This will be the list of responses for the questions that are asked
def get_magic_8_ball_response():
    responses = [
        "Yes, of course!",
        "Without a doubt,yes.",
        "You can count on it.",
        "For sure!",
        "Ask me later!",
        "I'm not sure.",
        "I can't tell you right now.",
        "No way!",
        "I don't think so.",
        "Without a doubt, no.",
        "The answer is clearly NO!"
    ]

#This is where the program will begin to function
    while True:
            question = input("Ask a question (type 'n' to quit): ")
            if question.lower() == 'n': #If the user no longer wishes to play
                print("Thanks for playing")
                break
            else:
                print("The answer is:", random.choice(responses))

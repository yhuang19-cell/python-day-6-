#In comments write out 


#Quit app
#get_random_function
#show_question
#show_answer

flashcards = 
{"question": "what python is used to define a function", "answer" : "def"}
{"question": "what python data type represent WHOLE numbers","answer":"int"}
{"question": "what data structure is used to represent Key, value","answer":}

''''''
Task: tell the users goodbye.
Input:None
Side effect:print a goodbye
Return:None
''''''
def_ quit_app():
print("Thanks for studying...")

''''''
Task:selects and retrieves a random elements in the flashcard list
Input:Flashing list
SIde effect:None
Return: the flashcard dictionary

def_ get_random_question
random_card = random choice(cards)

''''''
Task:Display the question
Input:Question cards
Side effect:None
Return:

def_ show_answer(card):
question = card[""]


Task:Display the answer
Input:Question card.
Side effect:Print the answer text to Terminal
Return:None


def_main():
if not cards:
        print("There are no flashcards to study.")
        return

    while True:
        card = get_random_question(cards)
        show_question(card)

        while True:
            choice = input(
                "Type 'answer' to see the answer, or 'quit' to stop: "
            ).strip().lower()

            if choice == "answer":
                show_answer(card)
                break
            elif choice == "quit":
                quit_app()
                return
            else:
                print("Please type 'answer' or 'quit'.")

        while True:
            choice = input(
                "Type 'next' for another card, or 'quit' to stop: "
            ).strip().lower()

            if choice == "next":
                break
            elif choice == "quit":
                quit_app()
                return
            else:
                print("Please type 'next' or 'quit'.")


main(flashcards)

def_main():
chosen_card = get_random_question(flashcards)
show_question(chosen_cards)


user_choice = input("Enter Q to quit, type anything else to online")

else:
show_answer(chosen_card)

def_main():
while True:
     chosen_card = get_random_question(flashcards)



main()
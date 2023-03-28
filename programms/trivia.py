def new_game():
    guesses = []
    question_number = 0
    for key in question:
        print("--------------------------------------")
        print(key)
        for x in options[question_number]:
            print(x)
        question_number+=1
        print("--------------------------------------")
        guess = None
        while guess not in choices:
            guess = input("Your Answer: ").upper()
        guesses.append(guess)
    check(guesses)

def check(guesses_arr):
    correct_answers = 0
    question_number = 0
    for key in question:
        if(guesses_arr[question_number]==question[key]):
            correct_answers += 1
        question_number+=1
    display_score(correct_answers)
def display_score(numb_right):
    print("Your total Score is: "+str(numb_right))
    play_again()

def play_again():
    again = input("Do you want to play again? (yes/no) ")
    if(again == "yes"):
       new_game()


question = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is Earth round?: ": "A"
}

options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]
]

choices = ["A", "B", "C", "D"]

new_game()
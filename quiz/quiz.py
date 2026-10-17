# Quiz App (command line)
#
# What it does:
#   Asks for a topic and a number of questions (1 to 10), gets multiple-choice
#   questions from an LLM, and asks them one at a time. At the end it shows
#   the score and a message based on the percentage.
#
# How a question is stored (a dictionary with 3 keys):
#   "question" - the question text
#   "options"  - a dictionary of exactly 4 answer choices
#   "answer"   - the letter (A-D) of the correct option, as the user sees it
#
# Where questions come from:
#   The LLM returns them as JSON, and each one is checked before use.
#   If the LLM call fails or nothing valid comes back, 5 built-in questions are used.
#
# Feedback and scoring:
#   Correct: "Correct!" and the right answer.
#   Wrong: one of 5 messages chosen at random (never the same one twice in a row),
#   then the correct answer.
#   Score = number of correct answers. Percentage = score / total * 100.
#   Result message: below 50% = low, 50% to 70% = average, above 70% = high.
#The correct text is found with options[answer].



import random

FALLBACK_QUESTIONS = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "A": "func",
            "B": "def",
            "C": "function",
            "D": "define"
        },
        "answer": "B"
    },
    {
        "question": "What data type is the result of 3 / 2 in Python 3?",
        "options": {
            "A":"int",
            "B":"float",
            "C":"double",
            "D":"decimal"
        },
        "answer": "B"
    },
    {
        "question": "Which built-in function returns the number of items in a list?",
        "options": {
            "A":"size()",
            "B":"count()",
            "C":"length()",
            "D":"len()"
        },
        "answer": "D"
    },
    {
        "question": "How do you start a single-line comment in Python?",
        "options": {
            "A":"//",
            "B":"/*",
            "C":"#",
            "D":"--"
        },
        "answer": "C"
    },
    {
        "question": "Which of the following data types is immutable?",
        "options": {
            "A":"List",
            "B":"Dictionary",
            "C":"Set",
            "D":"Tuple"
        },
        "answer": "D"
    }
]



def is_valid_question(q):
    if not isinstance(q, dict):
        return False
    if "options" not in q or "question" not in q or "answer" not in q:
        return False

    text = q["question"]
    if not isinstance(text, str) or text.strip() == "":
        return False

    options = q["options"]
    if not isinstance(options, dict):
        return False
    if sorted(options.keys()) != ["A","B","C","D"]:
        return False
    for value in options.values():
        if not isinstance(value, str) or value.strip() == "":
            return False

    answer = q["answer"]
    if not isinstance(answer, str):
        return False
    if answer not in options:
        return False

    return True

#phase 3
def ask_question(question, number):
    print(f"{number}. {question["question"]}")
    for key, value in question["options"].items():
        print(f"{key}. {value}")

    while True:
        user_answer = input("What is your answer ?: ").strip().upper()
        if user_answer not in question["options"].keys():
            print(f"{user_answer} isn't an option")
            continue

        break

    if user_answer == question["answer"]:
        return True
    else:
        return False
#phase 4
WRONG_MESSAGES =["Not quite.",
                 "Close, but no.",
                 "That's not it. Keep going.",
                 "Wrong this time. You'll get the next one.",
                 "Missed that one."]
def run_quiz(questions):
    score = 0
    last_message = None
    shuffled = random.sample(questions, len(questions))
    for number, question in enumerate(shuffled, start=1):
        correct = ask_question(question, number)
        letter = question["answer"]
        text = question["options"][letter]
        if correct:
            score +=1
            print(f"Correct! The answer is {letter}. {text}")
        else:
            message = random.choice(WRONG_MESSAGES)
            while message == last_message:
                message = random.choice(WRONG_MESSAGES)
            last_message = message
            print(message)
            print(f"The correct answer was: {letter}. {text}")
    return score


#phase 5
def show_result(score, total):
    if total == 0:
        percentage = 0
    else:
        percentage = round(score / total * 100)
    print(f"You scored {score} out of {total} ({percentage}%)")

    if percentage < 50:
        print("Needs review—keep practicing and try again!")
    elif percentage <= 70:
        print("Good job! A little more practice and you'll master it.")
    else:
        print("Excellent work! You nailed this quiz.")
#phase 6
def ask_count():
    while True:
        try:
            count = int(input("How many questions do you want to answer (1 - 10)?: "))
        except ValueError:
            print("Enter digits only")
            continue
        if count < 1 or count > 10:
            print("You can only enter numbers between 1 and 10")
        else:
            return count
#phase 7
def get_questions(topic, count):
    size = min(count, len(FALLBACK_QUESTIONS))
    return random.sample(FALLBACK_QUESTIONS,size)
def ask_topic():
    topic = input("Enter a topic of your choice(Press enter for python basics):").strip()
    if not topic:
        return "Python basics"

    return topic


def main():
    while True:
        print("**********QUIZ APP**********")
        print("Welcome! Test your knowledge on any topic.")
        print("1. Start the quiz")
        print("2. Quit")
        print("****************************")
        decision = input("Select one(1 or 2): ")
        if decision == "1":
            count = ask_count()
            topic = ask_topic()
            print("Generating questions...")
            questions = get_questions(topic, count)
            score = run_quiz(questions)
            show_result(score, len(questions))
            pa = input("Play again (y/n)?: ").strip().lower()
            if pa != "y":
                break
        elif decision == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

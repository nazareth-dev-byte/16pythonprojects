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
#   "answer"   - the letters (A-D) of the correct option, as the user sees it
#   The options lists counts from 0, so answer 1 is options[0].
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
    if list(options.keys()) != ["A","B","C","D"]:
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

for q in FALLBACK_QUESTIONS:
    print(is_valid_question(q))


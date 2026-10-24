Flashcard App

A command-line flashcard app in Python with a simple spaced-repetition system. Add cards, study them, and track your progress. Cards you know well appear less often, and cards you miss come back. Data is saved to a JSON file, so your progress is still there the next time you run it.

Features
Add, view and delete cards
Study cards still being learned, or study all cards
Cards move between boxes based on your answers
Progress screen with a count per box and the percentage mastered
Progress is saved after every card, so quitting early loses nothing
Input validation: bad input is rejected and asked again, never a crash
Missing or corrupted data file starts a fresh deck
How the boxes work

Each card sits in one of three boxes:

Box	Meaning
1	Learning
2	Getting there
3	Mastered
A new card starts in box 1.
A right answer moves it up one box. Box 3 is the top.
A wrong answer sends it back to box 1, from any box.
"Learning" study mode skips box 3, so you spend your time on cards you don't know yet.
Requirements
Python 3.12 or later
No external packages
How to run
python flashcards.py
Example
**********FLASHCARD APP**********
1. Add a card.
2. View all cards.
3. Study
4. See progress
5. Delete a card
0. Quit
*********************************
Select one: 3
1. Study cards still being learned (boxes 1 and 2)
2. Study all cards
Choose: 1
Card 1 of 2
FRONT: def
Press Enter to see the answer (or q to stop):
defines a function
Did you get it right?(y/n): y
Moved to box 2.
Card 2 of 2
FRONT: len()
Press Enter to see the answer (or q to stop):
length of a list
Did you get it right?(y/n): n
Back to box 1.
Session finished: 1 of 2 right.
How data is stored

Each card is a dictionary with three keys: front, back and box. All cards are kept in one list and saved to cards.json. The file is created on the first save and is not tracked by git.

Notes
Change the top box with the MASTERED_BOX constant.
Card numbers shown on screen start at 1.
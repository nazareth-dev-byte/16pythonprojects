
# Flashcard app: study cards with a simple spaced-repetition system.
# Each card is a dictionary with three keys:
#   "front" (text), "back" (text), "box" (number from 1 to 3)
# Box 1 = learning, box 2 = getting there, box 3 = mastered.
# A right answer moves a card up one box; a wrong answer sends it to box 1.
# All cards are kept in one list and saved to cards.json.


import json
import random

CARDS_FILE = "cards.json"
MASTERED_BOX = 3

#DATA FUNCTIONS

def add_card(cards, front, back):
    card ={"front":front,
            "back":back,
            "box":1}
    cards.append(card)
def delete_card(cards, index):
    cards.pop(index)
def update_box(card, was_correct):
        if was_correct:
            card["box"] = min(card["box"] + 1, MASTERED_BOX)
        else:
            card["box"] = 1
def count_by_box(cards):
    total = {}
    for item in cards:
        box_number = item["box"]
        total[box_number] = total.get(box_number, 0) + 1
    return total
def percent_mastered(cards):
    if not cards:
        return 0
    mastered = 0
    for card in cards:
        if card["box"] == MASTERED_BOX:
            mastered += 1
    return mastered /len(cards) * 100
def cards_to_study(cards, mode):
    chosen = []
    if mode == "learning":
        for card in cards:
            if card["box"] < MASTERED_BOX:
                chosen.append(card)
    if mode == "all":
        chosen = list(cards)
    shuffled = random.sample(chosen, len(chosen))
    return shuffled
def save_cards(cards):
    file_path = CARDS_FILE
    with open(file=file_path, mode="w") as file:
        json.dump(cards, file)
def load_cards():
    try:
        file_path = CARDS_FILE
        with open(file=file_path, mode="r") as file:
            lcards = json.load(file)
        if not isinstance(lcards, list):
            return []
        return lcards
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
def ask_text(prompt):
    while True:
        description = input(prompt).strip()
        if not description:
            print("Input cannot be empty, please input a valid description!")
            continue
        return description
def ask_yes_no(prompt):
    while True:
        decision = input(prompt).lower().strip()
        if decision == "y":
            return True
        elif decision == "n":
            return False
        else:
            print("Enter y or n.")
def ask_index(cards, action):
    if not cards:
        print("Cards cannot be empty.")
        return None
    try:
        index = input(f"Please enter the card number to {action}: ")
        index = int(index)
        if index > len(cards):
            print("Value cannot exceed number of available cards.")
            return None
        if index < 1:
            print("Number must be 1 or more.")
            return None
    except ValueError:
        print("Error: Invalid input! Please enter a valid whole number.")
        return None
    return index - 1
def show_cards(cards):
    if not cards:
        print("No cards yet, add some first.")
        return
    for number, card in enumerate(cards, start = 1):
        print(f"{number}. {card["front"]} -> {card["back"]} (box {card["box"]})")
def show_progress(cards):
    if not cards:
        print("No cards yet, add some first.")
        return
    counts = count_by_box(cards)
    print(f"Box 1 (learning): {counts.get(1, 0)}")
    print(f"Box 2 (getting there): {counts.get(2, 0)}")
    print(f"Box 3 (mastered): {counts.get(3, 0)}")
    print(f"Total cards: {len(cards)}")
    print(f"Mastered: {percent_mastered(cards):.0f}%")
def study_session(cards, mode):
    session = cards_to_study(cards, mode)
    if not session:
        print("No cards to study")
        return
    right = 0
    done = 0
    stopped = False
    for number, card in enumerate(session, start =1):
        print(f"Card {number} of {len(session)}")
        print(f"FRONT: {card['front']}")
        prompt = input("Press Enter to see the answer (or q to stop): ").strip().lower()
        if prompt == "q":
            stopped = True
            break
        print(f"{card["back"]}")
        correct = ask_yes_no("Did you get it right?(y/n): ")
        update_box(card, correct)
        done += 1
        if correct:
            right += 1
            print(f"Moved to box {card['box']}.")
        else:
            print("Back to box 1.")
        save_cards(cards)
    if stopped:
        print(f"Session stopped: {right} of {done} right.")
    else:
        print(f"Session finished: {right} of {done} right.")
def edit_card(card, front, back):
    card["front"] = front
    card["back"] = back
#phase 7
def main():
    cards = load_cards()
    while True:
        print("**********FLASHCARD APP**********")
        menu = {1:"Add a card.",
                2:"View all cards.",
                3:"Study",
                4:"See progress",
                5:"Delete a card",
                6:"Edit a card",
                0:"Quit",}
        for key, value in menu.items():
            print(f"{key}. {value}")
        print("*********************************")

        option = input("Select one: ")

        if option == "1":
            front = ask_text("Front of the card: ")
            back = ask_text("Back of the card: ")
            add_card(cards, front, back)
            save_cards(cards)
            print("Card added!")

        elif option == "2":
            print("**********ALL CARDS**********")
            show_cards(cards)
            print("*****************************")

        elif option == "3":
            if not cards:
                print("No cards yet. Add some first")
                continue
            print("1. Study cards still being learned (boxes 1 and 2)")
            print("2. Study all cards")
            mode_choice = input("Choose: ")
            if mode_choice == "1":
                study_session(cards, "learning")
            elif mode_choice == "2":
                study_session(cards, "all")
            else:
                print("Invalid choice.")

        elif option == "4":
            print("**********PROGRESS**********")
            show_progress(cards)
            print("****************************")

        elif option == "5":
            if not cards:
                print("No cards to delete")
                continue
            show_cards(cards)
            index = ask_index(cards, "delete")
            if index is None:
                continue
            if ask_yes_no("Are you sure? (y/n): "):
                delete_card(cards, index)
                save_cards(cards)
                print("Card deleted.")
            else:
                print("Card not deleted.")

        elif option == "6":
            if not cards:
                print("No cards to edit")
                continue
            show_cards(cards)
            index = ask_index(cards, "edit")
            if index is None:
                continue
            front = ask_text("New front: ")
            back = ask_text("New back: ")
            edit_card(cards[index], front, back)
            save_cards(cards)
            print("Card updated.")

        elif option == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
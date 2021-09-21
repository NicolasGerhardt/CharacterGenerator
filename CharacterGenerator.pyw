import tkinter as tk
import random

Races = [
    "Human",
    "Elf",
    "Half-Elf",
    "Half-Orc",
    "Dwarf",
    "Halfling",
    "Gnome",
    "Tiefling"
]

AlignmentOrders = [
    "Lawful",
    "Neutral",
    "Chaotic"
]

AlignmentMorals = [
    "Good",
    "Neutral",
    "Evil"
]

CharacterClasses = [
    "Bard",
    "Barbarian",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Palidin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Warlock",
    "Wizard"
]

def get_character() -> str:
    race = random.choice(Races)
    alignment_order = random.choice(AlignmentOrders)
    alignment_morals = random.choice(AlignmentMorals)
    character_class = random.choice(CharacterClasses)

    alignment = f"{alignment_order} {alignment_morals}"
    if (alignment_order == alignment_morals):
        alignment = "True Neutral"
    
    return f"{alignment} {race} {character_class}"

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Character Generator")
        self.root.geometry('450x100')
        self.add_character()
        self.root.mainloop()
        
    def add_character(self):
        self.character = tk.Label(self.root, text=get_character(), font=("Arial", 20))
        self.character.pack()
        self.button = tk.Button(self.root, text="Make next Character", command=self.update, font=("Arial", 20))
        self.button.pack()

    def update(self):
        self.character.destroy()
        self.button.destroy()
        self.add_character()
        

def main():
    mainwindow = MainWindow()


if __name__ == "__main__":
    main()
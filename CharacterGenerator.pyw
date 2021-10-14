import tkinter as tk
import random

racesFilename: str = "./assets/races.csv"
alignmentsFilename: str = "./assets/alignments.csv"
classesFilename: str = "./assets/classes.csv"

class CharacterGenerator:
    def __init__(self):
        self.Races = []
        with open(racesFilename, "r") as f:
            lines = f.readlines()
            for line in lines:
                self.Races.append(line.strip())
        
        self.CharacterClasses = []
        with open(classesFilename, "r") as f:
            lines = f.readlines()
            for line in lines:
                self.CharacterClasses.append(line.strip())
        
        with open(alignmentsFilename, "r") as f:
            lines = f.readlines()
            self.AlignmentOrders = lines[0].strip().split(",")
            self.AlignmentMorals = lines[1].strip().split(",")

    def get_character(self) -> str:
        race = random.choice(self.Races)
        alignment_order = random.choice(self.AlignmentOrders)
        alignment_morals = random.choice(self.AlignmentMorals)
        character_class = random.choice(self.CharacterClasses)

        alignment = f"{alignment_order} {alignment_morals}"
        if (alignment_order == alignment_morals):
            alignment = "True Neutral"

        return f"{alignment} {race} {character_class}"

class MainWindow:
    def __init__(self):
        self.characterGenerator = CharacterGenerator()
        self.root = tk.Tk()
        self.root.title("Character Generator")
        self.root.geometry('450x100')
        self.add_character()
        self.root.mainloop()
        
    def add_character(self):
        self.character = tk.Label(self.root, text=self.characterGenerator.get_character(), font=("Arial", 20))
        self.character.pack()
        self.button = tk.Button(self.root, text="Make next Character", command=self.update, font=("Arial", 20))
        self.button.pack()

    def update(self):
        self.character.destroy()
        self.button.destroy()
        self.add_character()
        

def main():
    MainWindow()


if __name__ == "__main__":
    main()
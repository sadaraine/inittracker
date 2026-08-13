import sys
from initiative import InitTracker

def main():
    combat = InitTracker()

    while True:
        print("Choose from the following:")
        print("A: Add Combatant")
        print("D: Display Combatants")
        print("N: Next")
        print("X: Exit")

        choice = input("Enter your choice: ").strip().lower()

        match choice:

            case "a":
                name = input("Enter combatant name: ").strip()
                actions = input("Number of actions (1-5): ").strip()
                initiative = input("Initiative Roll: ").strip()
                between = input("# Between Actions (20-10): ").strip()
                speed = input("Speed: ").strip()
                combat.add(name, actions, initiative, between, speed)
            case "d":
                combat.display()
            case "n":
                first_combatant = next(iter(combat))
                replacement = first_combatant
                replacement["initiative"] -= replacement["between"]
                replacement["actions"] -= 1
                removed_combatant = combat.pop(0)
                if replacement["actions"] == 0:
                    combat.display()
                    pass
                else:
                    combat.add(replacement["name"], replacement["actions"], replacement["initiative"], replacement["between"], replacement["speed"])
                    combat.display()
            case "x":
                print("Farewell Storyteller!")
                break
            case _:
                print("\nYou have chosen poorly. Enter your choice (I, or X): ")
                
if __name__ == "__main__":
    main()

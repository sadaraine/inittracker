import sys
from combatant import Combatant

def main():
    combatant_list = []
    while True:
        print("Welcome to the Initiative Tracker!")
        print("Choose from the following:")
        print("A: Add Combatant")
        print("R: Remove Combatant")
        print("X: Exit")

        choice = input("Enter your choice: ").strip().lower()

        match choice:

            case "a":
                tmp_list = []
                list_name = input("Enter combatant name: ")
                while True:
                    actions = input("Number of actions (1-5): ").strip()
                    tmp_list.append(actions)
                    initiative = input("Initiative Roll: ").strip()
                    tmp_list.append(initiative)
                    between = input("# Between Actions (20-10): ").strip()
                    tmp_list.append(between)
                    speed = input("Speed: ").strip()
                    tmp_list.append(speed)
                    break
                print(f"Combatant added: {list_name}")
                list_name = tmp_list
                del tmp_list
                print(f"Combatant: {list_name}")
                return list_name
            case "r":
                print("Remove Combatant: ")
            case "x":
                print("Farewell Storyteller!")
                break
            case _:
                print("\nYou have chosen poorly. Enter your choice (A, R, or X): ")
                
if __name__ == "__main__":
    main()

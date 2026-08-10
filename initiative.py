class InitTracker:
    def __init__(self):
        self.combatants = []

    def __repr__(self):
        return repr(self.combatants)

    def __iter__(self):
        return iter(self.combatants)

    def pop(self, index):
        return self.combatants.pop(index)
    
    def add(self, name, actions, initiative, between, speed):
        self.combatants.append({"name": name, "actions": int(actions), "initiative": int(initiative), "between": int(between), "speed": int(speed)})
        self.sort_combatants()

    def sort_combatants(self):
        self.combatants.sort(key=lambda x: x["initiative"], reverse=True)

    def display(self):
        print("\n")
        for i, n in enumerate(self.combatants):
            print(f"{i + 1}. {n['name']} - {n['actions']} actions left - Initiative {n['initiative']} - goes every {n['between']} - Speed: {n['speed']}")
        print("\n")

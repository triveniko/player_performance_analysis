class Player:
    def __init__(self, name, matches, runs, wickets):
        self.name = name
        self.matches = matches
        self.runs = runs
        self.wickets = wickets

    def update(self, matches=None, runs=None, wickets=None):
        if matches is not None: self.matches = matches
        if runs is not None: self.runs = runs
        if wickets is not None: self.wickets = wickets

    def batting_average(self):
        return self.runs / self.matches if self.matches > 0 else 0

    def bowling_average(self):
        return self.matches / self.wickets if self.wickets > 0 else float('inf')

    def display(self):
        print(f"{self.name} | Matches: {self.matches}, Runs: {self.runs}, Wickets: {self.wickets}")
        print(f"Batting Avg: {self.batting_average():.2f}, Bowling Avg: {self.bowling_average():.2f}\n")

class Team:
    def __init__(self):
        self.players = []

    def add_player(self):
        name = input("Enter player's name: ")
        matches = int(input("Enter matches played: "))
        runs = int(input("Enter runs scored: "))
        wickets = int(input("Enter wickets taken: "))
        self.players.append(Player(name, matches, runs, wickets))

    def update_player(self):
        name = input("Enter player's name to update: ")
        for p in self.players:
            if p.name == name:
                matches = input("Enter new matches (leave blank to keep current): ")
                runs = input("Enter new runs (leave blank to keep current): ")
                wickets = input("Enter new wickets (leave blank to keep current): ")
                p.update(matches=int(matches) if matches else None,
                         runs=int(runs) if runs else None,
                         wickets=int(wickets) if wickets else None)
                return
        print("Player not found!")

    def delete_player(self):
        name = input("Enter player's name to delete: ")
        self.players = [p for p in self.players if p.name != name]
        print(f"Player {name} deleted.")

    def display_players(self):
        if not self.players:
            print("No players in the team.")
        else:
            for p in self.players:
                p.display()

team = Team()

while True:
    print("\n1. Add Player\n2. Update Player\n3. Delete Player\n4. Display Players\n5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        team.add_player()
    elif choice == "2":
        team.update_player()
    elif choice == "3":
        team.delete_player()
    elif choice == "4":
        team.display_players()
    elif choice == "5":
        break
    else:
        print("Invalid option, please try again.")

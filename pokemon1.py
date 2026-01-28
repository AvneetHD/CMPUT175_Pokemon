class pokemon:
    def __init__(self, name, attack, defense, max_health, current_health):
        self.name = str(name)
        self.attack = int(attack)
        self.defense = int(defense)
        self.max_health = int(max_health)
        self.current_health = int(current_health)
    
    def __str__(self):
        return self.name+" (health: "+str(self.current_health)+"/"+str(self.max_health)+")"
        


def main():
    pokemon1 = pokemon("Pikachu", 55, 40, 35, 35)
    pokemon2 = pokemon("Bulbasaur", 49, 49, 45, 45)
    print(f"Welcome {pokemon1} and {pokemon2}!")



if __name__ == "__main__":
    main()
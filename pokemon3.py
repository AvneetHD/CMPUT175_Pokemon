class pokemon:
    def __init__(self, name, attack, defense, max_health, current_health):
        self.name = str(name)
        self.attack = int(attack)
        self.defense = int(defense)
        self.max_health = int(max_health)
        self.current_health = int(current_health)
    
    def __str__(self):
        return self.name+" (health: "+str(self.current_health)+"/"+str(self.max_health)+")"
    
    def lose_health(self, amount):
        if amount < self.current_health:
            self.current_health = self.current_health-amount
        elif amount >= self.current_health:
            self.current_health = 0
        elif amount < 0:
            pass

    def is_alive(self):
        if self.current_health > 0:
            return True
        if self.current_health <= 0:
            return False
        
    def revive(self):
        self.current_health = self.max_health
        print(f"{self.name} has been revived!")


def read_pokmon_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        plist = file.read()
        plist2 = plist.split("\n")
        pokemon_list = []

        for i in range(1, len(plist2)):
            info = plist2[i].split("|")
            x = pokemon(info[0], info[1], info[2], info[3], info[3])
            pokemon_list.append(x)
            

        return(pokemon_list)


def main():
    pokemon_list = read_pokmon_from_file(input("Enter filename: "))
    p1 = input("Pokemon 1: ")
    p2 = input("Pokemon 2: ")

    p = ["", ""]
    for i in range(len(pokemon_list)):
        if p1 == pokemon_list[i].name:
            p[0] = (pokemon_list[i])

    for i in range(len(pokemon_list)):
        if p2 == pokemon_list[i].name:
            p[1] = pokemon_list[i]
    
    pokemon1 = p[0]
    pokemon2 = p[1]

    print(f"Welcome {pokemon1} and {pokemon2}!")

    '''
    PROVIDED TESTING CODE - KEEP THIS CODE IN YOUR SUBMISSION
    '''
    print('\n-- TESTS FOR PART 3--')

    # Test is_alive method
    print('Is Pokémon 1 alive?', pokemon1.is_alive())
    print('Is Pokémon 2 alive?', pokemon2.is_alive())

    # Test lose_health method
    pokemon1.lose_health(20)
    print(f'\nAfter losing 20 health, {pokemon1}')
    pokemon2.lose_health(65)
    print(f'After losing 65 health, {pokemon2}')

    # Test if the Pokémon is alive after losing health
    print('\nIs Pokémon 1 alive?', pokemon1.is_alive())
    print('Is Pokémon 2 alive?', pokemon2.is_alive())

    # Test revive method
    print('')
    pokemon2.revive()
    print(f'After reviving, {pokemon2}')

    # Test if the Pokémon is alive after being revived
    print('\nIs Pokémon 2 alive?', pokemon2.is_alive())





if __name__ == "__main__":
    main()
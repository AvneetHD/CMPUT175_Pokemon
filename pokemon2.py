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



def main():
    pokemon1 = pokemon("Pikachu", 55, 40, 35, 35)
    pokemon2 = pokemon("Bulbasaur", 49, 49, 45, 45)
    print(f"Welcome {pokemon1} and {pokemon2}!")

    '''
    PROVIDED TESTING CODE - KEEP THIS CODE IN YOUR SUBMISSION
    '''
    print('\n-- TESTS FOR PART 2--')

    # Test is_alive method
    print('Is Pikachu alive?', pokemon1.is_alive())  # Expected: True
    print('Is Bulbasaur alive?', pokemon2.is_alive())  # Expected: True

    # Test lose_health method
    pokemon1.lose_health(10)
    print(f'\nAfter losing 10 health, {pokemon1}')  # Expected: Pikachu (health: 25/35)
    pokemon2.lose_health(45)
    print(f'After losing 45 health, {pokemon2}')  # Expected: Bulbasaur (health: 0/45)

    # Test if the Pokémon is alive after losing health
    print('\nIs Pikachu alive?', pokemon1.is_alive())  # Expected: True
    print('Is Bulbasaur alive?', pokemon2.is_alive())  # Expected: False

    # Test revive method
    print('')
    pokemon2.revive()  # Expected: "Bulbasaur has been revived!"
    print(f'After reviving, {pokemon2}')  # Expected: Bulbasaur (health: 45/45)

    # Test if the Pokémon is alive after being revived
    print('\nIs Bulbasaur alive?', pokemon2.is_alive())  # Expected: True





if __name__ == "__main__":
    main()
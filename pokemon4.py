import random

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

    def attempt_attack(self, other):
        luck = random.choice([0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3])
        damage = round(luck * self.attack)

        if damage > other.defense:
            other.lose_health(damage-other.defense)
            return True, damage, (damage-other.defense)
        elif damage <= other.defense:
            return False, (damage)



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
    filename = input('Enter filename: ')

    seed_val = input('Enter seed value: ')
    random.seed(seed_val)

    pokemon1 = None
    pokemon2 = None

    # NOW IMPLEMENT STEPS b-f (BELOW) HERE
    pokemon_list = read_pokmon_from_file(filename)
    while pokemon1 == pokemon2:
        pokemon1 = random.choice(pokemon_list)
        pokemon2 = random.choice(pokemon_list)
    print("")
    print(f"Welcome {pokemon1} and {pokemon2}!")

    rounds = 0
    while pokemon1.is_alive() and pokemon2.is_alive() and rounds < 10:
        print("")
        rounds += 1
        print(f"Round {rounds} begins! {pokemon1} and {pokemon2}!")
        attack1 = pokemon1.attempt_attack(pokemon2)
        print(f'{pokemon1.name} attacks {pokemon2.name} for {attack1[1]} damage!')
        if attack1[0]:
            print(f"Attack is successful! {pokemon2.name} has {pokemon2.current_health} health remaining!")
        else:
            print("Attack is blocked!")
        
        if pokemon2.is_alive() == False:
            gets_revived2 = random.choice([True, False])
            if gets_revived2:
                pokemon2.revive()
        
        if pokemon2.is_alive() == True:
            attack2 = pokemon2.attempt_attack(pokemon1)
            print(f'{pokemon2.name} attacks {pokemon1.name} for {attack2[1]} damage!')
            if attack2[0]:
                print(f"Attack is successful! {pokemon1.name} has {pokemon1.current_health} health remaining!")
            else:
                print("Attack is blocked!")
            
            if pokemon1.is_alive() == False:
                gets_revived1 = random.choice([True, False])
                if gets_revived1:
                    pokemon1.revive()
        
    print('')
    if pokemon1.is_alive() and pokemon2.is_alive():
        print(f"It's a tie between {pokemon1} and {pokemon2}!")
    elif pokemon1.is_alive():
        print(f"{pokemon1} has won in {rounds} rounds!")
    elif pokemon2.is_alive():
        print(f"{pokemon2} has won in {rounds} rounds!")
        




if __name__ == "__main__":
    main()
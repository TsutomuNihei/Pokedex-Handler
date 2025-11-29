import re

"""
Custom Error class for checking if abilities or types are valid.
Uses the msg it receives when raised.
"""
class PokemonInputError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

"""
Base Pokemon class with all attributes, getters, setters, and display/file methods.
the other subclasses will inherit from this class.
"""
class BasePokemon:
    def __init__(self, types=None, number="", name="", total="", hp="", attack="",
                 defense="", spAttack="", spDefense="", speed="",
                 species="", height="", weight="", abilities=None,):
        self.__types = types if types is not None else []
        self.__number = number
        self.__name = name
        self.__total = total
        self.__hp = hp
        self.__attack = attack
        self.__defense = defense
        self.__spAttack = spAttack
        self.__spDefense = spDefense
        self.__speed = speed
        self.__species = species
        self.__height = height
        self.__weight = weight
        self.__abilities = abilities if abilities is not None else []

    #getter methods to access the private attributes
    def getTypes(self): 
        return self.__types
    
    def getNumber(self): 
        return self.__number
    
    def getName(self): 
        return self.__name
    
    def getTotal(self): 
        return self.__total
    
    def getHP(self): 
        return self.__hp
    
    def getAttack(self): 
        return self.__attack
    
    def getDefense(self): 
        return self.__defense
    
    def getSpAttack(self): 
        return self.__spAttack
    
    def getSpDefense(self): 
        return self.__spDefense
    
    def getSpeed(self): 
        return self.__speed
    
    def getSpecies(self): 
        return self.__species
    
    def getHeight(self): 
        return self.__height
    
    def getWeight(self): 
        return self.__weight
    
    def getAbilities(self): 
        return self.__abilities

    #setter methods
    #for checking if types are valid or not
    def setTypes(self, types):
        if not (1 <= len(types) <= 2):
            raise PokemonInputError("*-* Pokemon can only have 1 or 2 types.")
        self.__types = types
    #for checking if abilities are valid or not
    def setAbilities(self, Abilities):
        if not (1 <= len(Abilities) <= 4):
            raise PokemonInputError("^_^ Pokemon can only have 1 to 4 moves!")
        self.__abilities = Abilities
    def setName(self, newName): 
        self.__name = newName

    def setNumber(self, newNumber): 
        self.__number = newNumber

    def setSpecies(self, newSpecies): 
        self.__species = newSpecies

    def setHeight(self, newHeight): 
        self.__height = newHeight

    def setWeight(self, newWeight): 
        self.__weight = newWeight

    def setHP(self, newhp): 
        self.__hp = newhp

    def setAttack(self, newAtk): 
        self.__attack = newAtk

    def setDefense(self, newDef): 
        self.__defense = newDef

    def setSpAttack(self, newSpA): 
        self.__spAttack = newSpA

    def setSpDefense(self, newSpD): 
        self.__spDefense = newSpD

    def setSpeed(self, newSpd): 
        self.__speed = newSpd

    def setTotal(self, newTotal): 
        self.__total = newTotal

    #the main display method that other classes will use with polymorphismm
    def displayStats(self):
        print(f"Name: {self.getName()} | #{self.getNumber()}")
        print(f"Types: {', '.join(self.getTypes()) if self.getTypes() else 'null'}")
        print(f"Total: {self.getTotal()}")
        print(f"HP: {self.getHP()} | Attack: {self.getAttack()} | Defense: {self.getDefense()}")
        print(f"Sp.Atk: {self.getSpAttack()} | Sp.Def: {self.getSpDefense()} | Speed: {self.getSpeed()}")

    #method to convert the pokemon data to file format for saving.
    #formatted like the way the file has with more stuff
    def to_file_format(self):
        parts = [
            f"Name: {self.__name}",
            f"National Number: {self.__number}",
            f"Type: {'/'.join(self.__types)}" if self.__types else "",
            f"Species: {self.__species}",
            f"Height: {self.__height}",
            f"Weight: {self.__weight}",
            f"Abilities: {', '.join(self.__abilities)}" if self.__abilities else "",
            "Stats:",
            f"  Total: {self.__total}",
            f"  HP: {self.__hp}",
            f"  Attack: {self.__attack}",
            f"  Defence: {self.__defense}",
            f"  Special Attack: {self.__spAttack}",
            f"  Special Defense: {self.__spDefense}",
            f"  Speed: {self.__speed}"
        ]
        finalParts = []
        for p in parts:
            # If the line is not an empty string, add it to our final list
            if p:
                finalParts.append(p)
        return "\n".join(finalParts)

"""
The fire subclass that inherits from BasePokemon, it has its own description and info also average stats that it passes to the base class
uses *args and **kwargs to pass stuff properly
"""
class FireType(BasePokemon):
    def __init__(self, **kwargs):
        avg = {"hp": "71.3", "attack": "84.8", "defense": "71.4",
               "spAttack": "88.8", "spDefense": "73.3", "speed": "76.0", "total": "465"}
        merged = {**avg, **kwargs}
        super().__init__(**merged)
        self.__desc = "Fire is one of the three basic elemental types along with Water and Grass, which constitute the three starter Pokémon."
        self.__info = {"Total": 97, "Single Type": 37, "Dual Type": 60, "Moves": 49}
    #the display method that overrides the base class method using polymorphism
    def displayStats(self):
        super().displayStats()
        print(self.__desc)
        print("Type Information:")
        for key, value in self.__info.items(): print(f"{key}: {value}")
"""
The grass subclass that inherits from BasePokemon, it has its own description and info also average stats that it passes to the base class
"""
class GrassType(BasePokemon):
    def __init__(self, **kwargs):
        avg = {"hp": "66.8", "attack": "77.0", "defense": "73.8",
               "spAttack": "72.7", "spDefense": "73.1", "speed": "63.0", "total": "427"}
        merged = {**avg, **kwargs}
        super().__init__(**merged)
        self.__desc = "Grass is one of the three basic elemental types along with Fire and Water, which constitute the three starter Pokémon."
        self.__info = {"Total": 146, "Single Type": 47, "Dual Type": 99, "Moves": 62}
    #the other display method for the grass class
    def displayStats(self):
        super().displayStats()
        print(self.__desc)
        print("Type Information:")
        for key, value in self.__info.items(): print(f"  {key}: {value}")

"""
Concrete subclasses that inherits from FireType, has its own stats and display method (polymorphism)
"""
class Charmander(FireType):
    def __init__(self, **kwargs):
        #default info for the charmander class
        defaults = {
            "types": ["Fire"], "number": "0004", "name": "Charmander",
            "total": "609", "hp": "23", "attack": "122", "defense": "121",
            "spAttack": "111", "spDefense": "121", "speed": "111",
            "species": "Lizard Pokémon", "height": "0.6 m", "weight": "8.5 kg",
            "abilities": ["Blaze"]
        }
        #passing the data to their appropriate parameters in parent class 
        merged_data = {**defaults, **kwargs}
        super().__init__(**merged_data)

    #the display method for charmander using polymorphism
    def displayStats(self):
        super().displayStats()
        print(f"Species: {self.getSpecies()} | Height: {self.getHeight()} | Weight: {self.getWeight()}")
        print(f"Abilities: {', '.join(self.getAbilities())}")

class Vulpix(FireType):
    #default data for the Vulpix class
    def __init__(self, **kwargs):
        defaults = {
            "types": ["Fire"], "number": "0037", "name": "Vulpix",
            "total": "10", "hp": "1", "attack": "1", "defense": "2",
            "spAttack": "2", "spDefense": "3", "speed": "1",
            "species": "Fox Pokémon", "height": "0.6 m", "weight": "9.9 kg",
            "abilities": ["Flash Fire"]
        }
        merged_data = {**defaults, **kwargs}
        super().__init__(**merged_data)

    def displayStats(self):
        super().displayStats()
        print(f"Species: {self.getSpecies()} - Height: {self.getHeight()} - Weight: {self.getWeight()}")
        print(f"Abilities: {', '.join(self.getAbilities())}")
"""
Concrete subclasses that inherits from GrassType, has its own stats and display method (polymorphism)
"""
class Bulbasaur(GrassType):
    #default data for the Bulbasaur class
    def __init__(self, **kwargs):
        defaults = {
            "types": ["Grass","Poison"], "number": "0001", "name": "Bulbasaur",
            "total": "62", "hp": "11", "attack": "9", "defense": "10",
            "spAttack": "13", "spDefense": "12", "speed": "7",
            "species": "Seed Pokémon", "height": "0.7 m", "weight": "6.9 kg",
            "abilities": ["Overgrow"]
        }
        merged_data = {**defaults, **kwargs}
        super().__init__(**merged_data)
    #the display method for bulbasaur using polymorphism
    def displayStats(self):
        super().displayStats()
        print(f"Species: {self.getSpecies()} | Height: {self.getHeight()} | Weight: {self.getWeight()}")
        print(f"Abilities: {', '.join(self.getAbilities())}")
       

class Oddish(GrassType):
    #default info for the Oddish class
    def __init__(self, **kwargs):
        defaults = {
            "types": ["Grass","Poison"], "number": "0043", "name": "Oddish",
            "total": "52", "hp": "8", "attack": "7", "defense": "9",
            "spAttack": "12", "spDefense": "10", "speed": "6",
            "species": "Weed Pokémon", "height": "0.5 m", "weight": "5.4 kg",
            "abilities": ["Chlorophyll"]
        }
        merged_data = {**defaults, **kwargs}
        super().__init__(**merged_data)

    def displayStats(self):
        super().displayStats()
        print(f"Species: {self.getSpecies()} | Height: {self.getHeight()} | Weight: {self.getWeight()}")
        print(f"Abilities: {', '.join(self.getAbilities())}")

"""
The pokedex class which acts as a manager for the pokemons and also handles the file input and output stuff,
utilizes a menu method to call the functions, the class initializes by loading the data from the file to perform the necessary functions
"""
class Pokedex:
    def __init__(self, filename="pokemon.txt"):
        self.__pokemons = []
        self.__filename = filename
        self.__class_map = {"Charmander": Charmander, "Vulpix": Vulpix,
                            "Bulbasaur": Bulbasaur, "Oddish": Oddish}
        self.load()
        self.__running = True
        self.__choices = {
            "1": self.display,
            "2": self.searchPokemon,
            "3": self.addPokemon,
            "4": self.removePokemon,
            "5": self.searchByType,
            "6": self.updatePokemon,
            "7": self.exportTypeReport
        }

    #This is called immediately after initialization to load the data from the file
    def load(self):
        self.__pokemons = [] 
        try:
            with open(self.__filename, "r", encoding="utf-8") as f:
                #converts file data into a list of data
                lines = f.readlines()
        #called when file doesn't exist
        except FileNotFoundError:
            return 
        current_pokemon_data = {}
        for line in lines:
            line = line.strip()
            if not line:
                if current_pokemon_data: 
                    # Decide which class to use based on the name, if not in the dictionary uses basePokemon
                    item_class = self.__class_map.get(current_pokemon_data.get("name"), BasePokemon)
                    # Create the object by passing all collected data to the constructor
                    p = item_class(**current_pokemon_data)
                    self.__pokemons.append(p)
                current_pokemon_data = {}
                continue

            # Split the line into a key and value
            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip()

                # Assign data to our dictionary based on the key
                if key == "Name":
                    current_pokemon_data["name"] = value
                elif key == "National Number":
                    current_pokemon_data["number"] = value
                elif key == "Type":
                    current_pokemon_data["types"] = [t.strip() for t in value.split("/") if t.strip()]
                elif key == "Species":
                    current_pokemon_data["species"] = value
                elif key == "Height":
                    current_pokemon_data["height"] = value
                elif key == "Weight":
                    current_pokemon_data["weight"] = value
                elif key == "Abilities":
                    current_pokemon_data["abilities"] = [a.strip() for a in value.split(",") if a.strip()]
                elif key == "Total":
                    current_pokemon_data["total"] = value
                elif key == "HP":
                    current_pokemon_data["hp"] = value
                elif key == "Attack":
                    current_pokemon_data["attack"] = value
                elif key == "Defence": 
                    current_pokemon_data["defense"] = value
                elif key == "Special Attack":
                    current_pokemon_data["spAttack"] = value
                elif key == "Special Defense":
                    current_pokemon_data["spDefense"] = value
                elif key == "Speed":
                    current_pokemon_data["speed"] = value
        
        # This handles the very last Pokemon in the file, which might not have a blank line after it
        if current_pokemon_data:
            item_class = self.__class_map.get(current_pokemon_data.get("name"), BasePokemon)
            p = item_class(**current_pokemon_data)
            self.__pokemons.append(p)

    #called whenever a change is made the data
    def save(self):
        with open(self.__filename,"w",encoding="utf-8") as f:
            #extra space between pokemon like its done in the pokemon.txt file
            f.write("\n\n".join(p.to_file_format() for p in self.__pokemons))
        print(":] Changes saved.")

    #method to display all the info of pokemon in the pokemon list, if empty it just returns back to menu
    def display(self):
        if not self.__pokemons: 
            print("No Pokémon.")
            return
        for p in self.__pokemons:
            p.displayStats()
    
    def searchPokemon(self):
        #intital check to see if pokedex was even initialized properly
        if not self.__pokemons:
            print("Pokedex is empty!!!")
            return
        
        pokemonNameNo = input("Enter name/number: ")
        found_pokemon = False
        
        # Loop through all pokemons to find a match
        for pokemon in self.__pokemons:
            if pokemon.getName().lower() == pokemonNameNo.lower() or pokemon.getNumber() == pokemonNameNo:
                # If found, display its stats
                pokemon.displayStats()
                found_pokemon = True
                break      
        #if not found
        if not found_pokemon:
            print("ERROR: not present in the pokedex currently!!")

    #method to add pokemon, after asking input from user and if confirmed its not in the list already, creates new pokemon. To add the data into
    #the file as well it calls the save method
    def addPokemon(self):
        #surrounded by a try and except that catches value errors and if the stats entered are not digits using isdigit() method
        try:
            number=input("Number: ")
            if not number.isdigit():
                raise PokemonInputError("National Number must be a number!")
            name=input("Name: ")

            pokeExists=False
            for p in self.__pokemons:
                #checking if pokemon is already present in pokedex or not using name/number
                if (p.getName().lower()==name.lower() or p.getNumber()==number):
                        pokeExists=True
                        break
            if pokeExists:
                print(";-; This pokemon is already present in the pokedex!") 
                return
            
            # Get types and clean them up immediately
            types_input=input("Types (e.g. Fire or Grass (separate with /)): ").split("/")
            types = [t.strip() for t in types_input if t.strip()]
            
            if not (1 <= len(types) <= 2):
                raise PokemonInputError("*-* Pokemon can only have 1 or 2 types.")
            species=input("Species: ")
            height=input("Height: ")
            weight=input("Weight: ")
            abilities_input=input("Moves: (separate with commas) 1–4): ").split(",")
            abilities = [a.strip() for a in abilities_input if a.strip()]

            if not (1 <= len(abilities) <= 4):
                raise PokemonInputError("^_^ Pokemon can only have 1 to 4 moves!")
            
            hp=input("HP: ")
            if not hp.isdigit():
                raise PokemonInputError("HP must be a number!")
            attack=input("Attack: ")
            if not attack.isdigit():
                raise PokemonInputError("Attack must be a number!")
            defense=input("Defense: ")
            if not defense.isdigit():
                raise PokemonInputError("Defense must be a number!")
            spA=input("Sp. Attack: ")
            if not spA.isdigit():
                raise PokemonInputError("sp. Atk must be a number!")
            spD=input("Sp. Defense: ")
            if not spD.isdigit():
                raise PokemonInputError("sp. Def must be a number!")
            speed=input("Speed: ")
            if not speed.isdigit():
                raise PokemonInputError("Speed must be a number!")
            totalInt=(int(x) for x in [hp,attack,defense,spA,spD,speed])
            totalSum=sum(totalInt)
            total=str(totalSum)

            # Create a dictionary of all the user-inputted data
            pokemon_data = {
                "types": types, "number": number, "name": name, "total": total, "hp": hp,
                "attack": attack, "defense": defense, "spAttack": spA, "spDefense": spD, "speed": speed,
                "species": species, "height": height, "weight": weight, "abilities": abilities
            }

            newP = None
            #check if the pokemon is fire or not
            if "Fire" or "fire" in types:
                newP = FireType(**pokemon_data)
            #if not fire checking if its grass
            elif "Grass" or "grass" in types:
                newP = GrassType(**pokemon_data)
            else:
                #if not its just basepokemon, forwards the data to appropriate oarameters using **kwargs!
                newP = BasePokemon(**pokemon_data)
            
            #appends the new pokemon!
            self.__pokemons.append(newP)
            self.save()
            print(f":D Added {name}.")
        except PokemonInputError as e:
            print(":( ERROR:",e)
        except ValueError:
            print(":( ERROR: Stats like HP, Attack, etc., must be numbers.")

    #method to remove pokemon, checks with either name or number, and if removed calls save function to update the file
    def removePokemon(self):
        key=input("Enter name/number: ")
        for p in self.__pokemons:
            if p.getName().lower()==key.lower() or p.getNumber()==key:
                self.__pokemons.remove(p)
                print("$-$ Removed.")
                self.save()
                return
        print("!-! Not found.")
    
    #method to update pokemon data, first checks using name/number then if exists uses setter functions
    def updatePokemon(self):
        key=input("Enter name/number: ")
        for p in self.__pokemons:
            if p.getName().lower()==key.lower() or p.getNumber()==key:
                #not gonna edit the name or number cause that is fixed.
                #separates the abilities added by comma
                newAbility=input(f"Moves [{', '.join(p.getAbilities())}]: ")
                if newAbility:
                    #after removing uncessary whitespace or commas then add it
                    ab=[a.strip() for a in newAbility.split(",") if a.strip()]
                    try: 
                        p.setAbilities(ab)
                    except PokemonInputError as e: 
                        print("Moves not updated:",e)
                #if user wants to update additional attrbitutes other than abilities
                userUpdate=input("Do you want to update pokemon attributes as well? answer y or Y for yes/n or No for no: ")
                if userUpdate.lower()=="y":
                    newHP=input("enter new HP: ")
                    if not newHP.isdigit():
                        raise PokemonInputError("HP must be a number!")
                    p.setHP(newHP)
                    newAtk=input("enter new Attack: ")
                    if not newAtk.isdigit():
                        raise PokemonInputError("Attack must be a number!")
                    p.setAttack(newAtk)
                    newDef=input("enter new Defense: ")
                    if not newDef.isdigit():
                        raise PokemonInputError("Defense must be a number!")
                    p.setDefense(newDef)
                    newSpAtk=input("enter new Sp. Atk: ")
                    if not newSpAtk.isdigit():
                        raise PokemonInputError("sp. Atk must be a number!")
                    p.setSpAttack(newSpAtk)
                    newSpDef=input("enter new Sp. Def: ")
                    if not newSpDef.isdigit():
                        raise PokemonInputError("sp. Def must be a number!")
                    p.setSpDefense(newSpDef)
                    newSpeed=input("Enter new speed: ")
                    if not newSpeed.isdigit():
                        raise PokemonInputError("speed must be a number!")
                    p.setSpeed(newSpeed)
                    newTotal=int(newHP)+int(newAtk)+int(newDef)+int(newSpAtk)+int(newSpDef)+int(newSpeed)
                    p.setTotal(str(newTotal))
                else:
                    print("Ok!")
                print(" Updated.")
                #calling save to update the data in files!
                self.save()
                return
        print("\\~/ Not found.")

    #searching the pokemon data by type
    def searchByType(self):
        typeVal = input("Enter type: ").lower()
        # Create an empty list to store the results
        found = []
        for pokemon in self.__pokemons:
            for t in pokemon.getTypes():
                if t.lower() == typeVal:
                    found.append(pokemon)
                    break
        if not found:
            print("/-\\ No matches.")
            return
        for poke in found:
            poke.displayStats()

    #exporting the the data of the file that are of a particular type,
    def exportTypeReport(self,exportName=None):
        if exportName is None:
            typeVal=input("Enter type to export: ").lower()
        else: 
            typeVal = exportName.lower()
        found = []
        for pokemon in self.__pokemons:
            for t in pokemon.getTypes():
                if t.lower() == typeVal:
                    found.append(pokemon)
                    break
        if not found:
            print("No matches.")
            return
        #using the new file it enters this data and saves it!
        filename=f"{typeVal}.txt"
        with open(filename,"w",encoding="utf-8") as f:
            if typeVal=="fire":
                f.write("Fire Type!\nTotal: 97 | Single: 37 | Dual: 60 | Moves: 49\n")
                f.write("Average Stats: HP 71.3, Atk 84.8, Def 71.4, SpAtk 88.8, SpDef 73.3, Speed 76.0\n\n")
            elif typeVal=="grass":
                f.write("Grass Type!\nTotal: 146 | Single: 47 | Dual: 99 | Moves: 62\n")
                f.write("Average Stats: HP 66.8, Atk 77.0, Def 73.8, SpAtk 72.7, SpDef 73.1, Speed 63.0\n\n")
            f.write("\n\n".join(p.to_file_format() for p in found))
        print(f"|-| Saved {filename}")
        return filename

    #the run function starts the menu with all the options, the options are in a dictionary, if an option thats not in it is picked it says invalid
    def run(self):
        while self.__running:
            try:
                print("""
    Welcome to the Pokedex System!!
        Enter an option:
            1.Display all
            2.Search for a pokemon
            3.Add pokemon
            4.Remove pokemon
            5.Search for pokemon by type
            6.Update pokemon stats
            7.Export information by Type
            n or N to exit the system!
                      """)
                choice=input()
                if choice.lower()=="n":
                    self.save(); print(" %^^% Thank you for using the pokedex system today!")
                    self.__running=False
                elif choice in self.__choices:
                    self.__choices[choice]()
                #error handling in case user inputs a choice not in the predefined choices in dictionary
                else: raise ValueError("^~^ Invalid choice.")
            except (ValueError, PokemonInputError) as e:
                print("ERROR: "+str(e))
                

if __name__=="__main__":
    pokedex=Pokedex()
    pokedex.run()

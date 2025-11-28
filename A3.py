import matplotlib.pyplot as plt
import numpy as np
import re
import json


class PokemonInputError(BaseException):
    def __init__(self,message):
        self._message=message
    
    def __str__(self):
        return self._message


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
    
    def to_dict(self):
        return {
            "name": self.__name,
            "number": self.__number,
            "types": self.__types,
            "species": self.__species,
            "height": self.__height,
            "weight": self.__weight,
            "abilities": self.__abilities,
            "total": self.__total,
            "hp": int(self.__hp) if self.__hp != "" else 0,
            "attack": int(self.__attack) if self.__attack != "" else 0,
            "defense": int(self.__defense) if self.__defense != "" else 0,
            "spAttack": int(self.__spAttack) if self.__spAttack != "" else 0,
            "spDefense": int(self.__spDefense) if self.__spDefense != "" else 0,
            "speed": int(self.__speed) if self.__speed != "" else 0
        }

class FireType(BasePokemon):
    def __init__(self, **kwargs):
        avg = {"hp": "71.3", "attack": "84.8", "defense": "71.4",
               "spAttack": "88.8", "spDefense": "73.3", "speed": "76.0", "total": "465"}
        merged = {**avg, **kwargs}
        super().__init__(**merged)
        self._desc = "Fire is one of the three basic elemental types along with Water and Grass, which constitute the three starter Pokémon."
        self._info = {"Total": 97, "Single Type": 37, "Dual Type": 60, "Moves": 49}

class GrassType(BasePokemon):
    def __init__(self, **kwargs):
        avg = {"hp": "66.8", "attack": "77.0", "defense": "73.8",
               "spAttack": "72.7", "spDefense": "73.1", "speed": "63.0", "total": "427"}
        merged = {**avg, **kwargs}
        super().__init__(**merged)
        self._desc = "Grass is one of the three basic elemental types along with Fire and Water, which constitute the three starter Pokémon."
        self._info = {"Total": 146, "Single Type": 47, "Dual Type": 99, "Moves": 62}

class Charmander(FireType):
    def __init__(self, **kwargs):
        #default info for the charmander class
        defaults = {
            "types": ["Fire"], "number": "0004", "name": "Charmander",
            "total": "609", "hp": "23", "attack": "122", "defense": "121",
            "spAttack": "111", "spDefense": "121", "speed": "111",
            "species": "Lizard Pokemon", "height": "0.6 m", "weight": "8.5 kg",
            "abilities": ["Blaze"]
        }
        #passing the data to their appropriate parameters in parent class 
        merged_data = {**defaults, **kwargs}
        super().__init__(**merged_data)

    #uses polymorphism to display stats of the pokemon class as well as stats unique to current pokemon
    def displayStats(self):
        super().displayStats()
        print(self._desc)
        print("Type Information:")
        for key, value in self._info.items(): print(f"{key}: {value}")

class Vulpix(FireType):
    #default data for the Vulpix class
    def __init__(self, **kwargs):
        defaults = {
            "types": ["Fire"], "number": "0037", "name": "Vulpix",
            "total": "10", "hp": "1", "attack": "1", "defense": "2",
            "spAttack": "2", "spDefense": "3", "speed": "1",
            "species": "Fox Pokemon", "height": "0.6 m", "weight": "9.9 kg",
            "abilities": ["Flash Fire"]
        }
        merged_data = {**defaults, **kwargs}
        super().__init__(**merged_data)

    def displayStats(self):
        super().displayStats()
        print(self._desc)
        print("Type Information:")
        for key, value in self._info.items(): print(f"{key}: {value}")

class Bulbasaur(GrassType):
    #default data for the Bulbasaur class
    def __init__(self, **kwargs):
        defaults = {
            "types": ["Grass","Poison"], "number": "0001", "name": "Bulbasaur",
            "total": "62", "hp": "11", "attack": "9", "defense": "10",
            "spAttack": "13", "spDefense": "12", "speed": "7",
            "species": "Seed Pokemon", "height": "0.7 m", "weight": "6.9 kg",
            "abilities": ["Overgrow"]
        }
        merged_data = {**defaults, **kwargs}
        super().__init__(**merged_data)

    def displayStats(self):
        super().displayStats()
        print(self._desc)
        print("Type Information:")
        for key, value in self._info.items(): print(f"{key}: {value}")

class Oddish(GrassType):
    #default info for the Oddish class
    def __init__(self, **kwargs):
        defaults = {
            "types": ["Grass","Poison"], "number": "0043", "name": "Oddish",
            "total": "52", "hp": "8", "attack": "7", "defense": "9",
            "spAttack": "12", "spDefense": "10", "speed": "6",
            "species": "Weed Pokemon", "height": "0.5 m", "weight": "5.4 kg",
            "abilities": ["Chlorophyll"]
        }
        merged_data = {**defaults, **kwargs}
        super().__init__(**merged_data)

    def displayStats(self):
        super().displayStats()
        print(self._desc)
        print("Type Information:")
        for key, value in self._info.items(): print(f"{key}: {value}")

class Pokedex():
    txtFile="pokemon.txt"
    jsonFile="pokemon.json"

    def __init__(self, filename=None):
        self.__pokemons = []
        self.__filename = filename if filename else self.txtFile
        self.__running = True
        self.__choices = {
            "1": self.display,
            "2": self.searchPokemon,
            "3": self.addPokemon,
            "4": self.removePokemon,
            "5": self.searchByType,
            "6": self.updatePokemon,
            "7": self.visualize
        }
        self.__class_map = {"Charmander": Charmander, "Vulpix": Vulpix,
                            "Bulbasaur": Bulbasaur, "Oddish": Oddish}
        self.load()

    #This is called immediately after initialization to load the data from the file
    def load(self):
        self.__pokemons = [] 
        try:
            with open(self.jsonFile, "r", encoding="utf-8") as jf:
                data = json.load(jf)
                for poke in data:
                    item_class = self.__class_map.get(poke.get("name"), BasePokemon)
                    p = item_class(**poke)
                    self.__pokemons.append(p)
            print(f"Loaded data from {self.jsonFile}")
            return
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error: str(e)")

        try:
            with open(self.__filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
        #called when file doesn't exist
        except FileNotFoundError:
            pass
        current_pokemon_data = {}
        for line in lines:
            line = line.strip()
            if not line:
                if current_pokemon_data: 
                    # Decide which class to use based on the name, if not in the dictionary uses basePokemon
                    item_class = self.__class_map.get(current_pokemon_data.get("name"), BasePokemon)
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
    #therefore when user exists or change is made, can view the json immediately!
    def save(self):
        # write text file
        with open(self.__filename, "w", encoding="utf-8") as f:
            f.write("\n\n".join(p.to_file_format() for p in self.__pokemons))
            f.write("\n")
        # write json
        try:
            with open(self.jsonFile, "w", encoding="utf-8") as jf:
                json.dump([p.to_dict() for p in self.__pokemons], jf, indent=4)
        except Exception as e:
            print("Failed to save to json file =-=", e)
        print(":] Changes saved to TXT and JSON.")

    #method to display all the info of pokemon in the pokemon list, if empty it just returns back to menu
    def display(self):
        if not self.__pokemons: 
            print("No Pokemon.")
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

    #regex checking for proper format of National Number, Height & Weight
    @classmethod
    def checkInput(cls,stat,val):
        if stat=="National Number":
            return re.match(r"^No\. \d{4}$",val)
        if stat=="Height":
            return re.match(r"^\d+\.\d m$",val)
        if stat=="Weight":
            return re.match(r"^\d+\.\d kg$",val)

    #method to add pokemon, after asking input from user and if confirmed its not in the list already, creates new pokemon. To add the data into
    #the file as well it calls the save method
    def addPokemon(self):
        #surrounded by a try and except that catches value errors and if the stats entered in proper format according to regex it calls the custom error class
        try:
            number=input("Number (No. xxxx): ")
            if not Pokedex.checkInput("National Number",number):
                raise PokemonInputError("The format for National Number is of format 'No. xxxx'!")
            
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
            
            types_input=input("Types (e.g. Fire or Grass (separate with /)): ").split("/")
            types = [t.strip() for t in types_input if t.strip()]
            if not (1 <= len(types) <= 2):
                raise PokemonInputError("*-* Pokemon can only have 1 or 2 types.")
            
            species=input("Species: ")

            height=input("Height (xxx.x m): ")
            if not Pokedex.checkInput("Height",height):
                raise PokemonInputError("Pokemon height must of format 'xxx.x m!'")
            
            weight=input("Weight (xxx.x kg): ")
            if not Pokedex.checkInput("Weight",weight):
                raise PokemonInputError("Pokemon weight must of format 'xxx.x kg!'")
            
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
            pokemonData = {
                "types": types, "number": number, "name": name, "total": total, "hp": hp,
                "attack": attack, "defense": defense, "spAttack": spA, "spDefense": spD, "speed": speed,
                "species": species, "height": height, "weight": weight, "abilities": abilities
            }

            newP = None
            #check if the pokemon is fire or not
            if "Fire" or "fire" in types:
                newP = FireType(**pokemonData)
            #if not fire checking if its grass
            elif "Grass" or "grass" in types:
                newP = GrassType(**pokemonData)
            else:
                #if not its just basepokemon, forwards the data to appropriate oarameters using **kwargs!
                newP = BasePokemon(**pokemonData)
            
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
        pokeFound = None
        for p in self.__pokemons:
            if p.getName().lower()==key.lower() or p.getNumber()==key:
                pokeFound = p
                break
        if not pokeFound:
            print("\\~/ Not found.")
            return
        p = pokeFound
        try:
            updateInput = input("Update Advanced Information (Number, Height, Weight)? (y/n): ").lower()
            if updateInput== 'y':
                newNumber = input(f"Number [{p.getNumber()}]: ")
                if newNumber:
                    if not Pokedex.checkInput("National Number", newNumber):
                        raise PokemonInputError("Invalid National Number format. Must be 'No. xxxx'.")
                    p.setNumber(newNumber)

                newHeight = input(f"Height [{p.getHeight()}]: ")
                if newHeight:
                    if not Pokedex.checkInput("Height", newHeight):
                        raise PokemonInputError("Invalid Height format. Must be 'x.x m'.")
                    p.setHeight(newHeight)
                
                newWeight = input(f"Weight [{p.getWeight()}]: ")
                if newWeight:
                    if not Pokedex.checkInput("Weight", newWeight):
                        raise PokemonInputError("Invalid Weight format. Must be 'x.x kg'.")
                    p.setWeight(newWeight)

            newAbility=input(f"Moves [{', '.join(p.getAbilities())}]: ")
            if newAbility:
                ab=[a.strip() for a in newAbility.split(",") if a.strip()]
                try: 
                    p.setAbilities(ab)
                except PokemonInputError as e: 
                    print("Moves not updated:",e)
            
            userUpdate=input("Do you want to update pokemon Stats (HP, Atk, etc.)? (y/n): ")
            if userUpdate.lower()=="y":
                newHP=input(f"Enter new HP [{p.getHP()}]: ") or p.getHP()
                if not newHP.isdigit(): 
                    raise PokemonInputError("HP must be a number!")
                p.setHP(newHP)

                newAtk=input(f"Enter new Attack [{p.getAttack()}]: ") or p.getAttack()
                if not newAtk.isdigit(): 
                    raise PokemonInputError("Attack must be a number!")
                p.setAttack(newAtk)

                newDef=input(f"Enter new Defense [{p.getDefense()}]: ") or p.getDefense()
                if not newDef.isdigit(): 
                    raise PokemonInputError("Defense must be a number!")
                p.setDefense(newDef)

                newSpAtk=input(f"Enter new Sp. Atk [{p.getSpAttack()}]: ") or p.getSpAttack()
                if not newSpAtk.isdigit(): 
                    raise PokemonInputError("Sp. Atk must be a number!")
                p.setSpAttack(newSpAtk)

                newSpDef=input(f"Enter new Sp. Def [{p.getSpDefense()}]: ") or p.getSpDefense()
                if not newSpDef.isdigit(): 
                    raise PokemonInputError("Sp. Def must be a number!")
                p.setSpDefense(newSpDef)

                newSpeed=input(f"Enter new speed [{p.getSpeed()}]: ") or p.getSpeed()
                if not newSpeed.isdigit(): 
                    raise PokemonInputError("Speed must be a number!")
                p.setSpeed(newSpeed)

                # calculating total stats
                newTotal=int(newHP)+int(newAtk)+int(newDef)+int(newSpAtk)+int(newSpDef)+int(newSpeed)
                p.setTotal(str(newTotal))
            
            print(" Updated.")
            #calling save to update the data in files!
            self.save()
        except PokemonInputError as e:
            print(f"Update failed: {e}")
        except ValueError:
            print("Update failed: Stats like HP, Attack, etc., must be numbers.")

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
            7.Visualize Pokedex Data
            exit or X to exit the system!
                      """)
                choice=input()
                if choice.lower().strip()=="exit" or choice.lower().strip()=="x":
                    self.save(); print(" %^^% Thank you for using the pokedex system today!")
                    self.__running=False
                elif choice in self.__choices:
                    self.__choices[choice]()
                #error handling in case user inputs a choice not in the predefined choices in dictionary
                else: 
                    raise ValueError("^~^ Invalid choice.")
            except (ValueError, PokemonInputError) as e:
                print("ERROR: "+str(e))

    #the visualize function lists options for the user to select what type of statistic they want to visualize            
    def visualize(self):
        print("""
    Visualisations:
        1. Bar chart (single Pokemon)
        2. Line chart (compare two Pokemon)
        3. Pie chart (type distribution)
        q/Q. Exit!
        """)
        ch = input("Choice: ").strip()
        if ch.lower() == "q":
            return
        if ch == "1":
            self.barGraph()
        elif ch == "2":
            self.lineGraph()
        elif ch == "3":
            self.pieChart()
        else:
            print("Invalid choice.")    

    #method to display the statistics of a single pokemon using bar graphs
    def barGraph(self):
        try:
            pokeName=input("Enter pokemon's name to visualize its statistics! : ").strip().lower()
            if not pokeName.isalpha():
                raise ValueError("Invalid pokemon name")
            pokeFound=False
            for poke in self.__pokemons:
                if poke.getName().lower()==pokeName:
                    newPoke=poke
                    pokeFound=True
            if pokeFound==False:
                return("Pokemon wasn't present in the list of pokemons!")
        except ValueError as e:
            print("Error"+str(e))
        
        pokeStats=newPoke.to_dict()
        labels=["hp","Attack","defense","spAttack","spDefense","Speed"]
        vals=[pokeStats["hp"],pokeStats["attack"],pokeStats["defense"],pokeStats["spAttack"],pokeStats["spDefense"],pokeStats["speed"]]
        plt.bar(labels,vals)
        plt.title("Pokemon Stats!")
        plt.xlabel("Statistics")
        plt.show()

    #method to display the stats of 2 pokemon and how they compare using line graphs with diff colours
    def lineGraph(self):
        try:
            pokeName1=input("Enter pokemon 1's name to compare its statistics! : ").strip().lower()
            pokeName2=input("Enter pokemon 2's name to compare its statistics! : ").strip().lower()

            if not (pokeName1.isalpha() and pokeName2.isalpha()):
                raise ValueError("Invalid pokemon name")
            pokeFound=False
            for poke in self.__pokemons:
                if poke.getName().lower()==pokeName1:
                    newPoke1=poke
                elif poke.getName().lower()==pokeName2:
                    newPoke2=poke
                    pokeFound=True
            if pokeFound==False:
                print("Pokemon wasn't present in the list of pokemons!")
                return
        except ValueError as e:
            print("Error"+str(e))
            return 
        
        pokeStats1=newPoke1.to_dict()
        pokeStats2=newPoke2.to_dict()
        labels=["hp","Attack","defense","spAttack","spDefense","Speed"]
        vals1=[pokeStats1["hp"],pokeStats1["attack"],pokeStats1["defense"],pokeStats1["spAttack"],pokeStats1["spDefense"],pokeStats1["speed"]]
        vals2=[pokeStats2["hp"],pokeStats2["attack"],pokeStats2["defense"],pokeStats2["spAttack"],pokeStats2["spDefense"],pokeStats2["speed"]]
        plt.plot(labels,vals1,'b',marker='o',label='pokemon1')
        plt.plot(labels,vals2,'r',marker='o', label='pokemon2')
        plt.xlabel("statistics")
        plt.ylabel("values")
        plt.legend()
        plt.show()

    #the method to display percentage of types using a pie chart!
    def pieChart(self):
        fireCount = 0
        grassCount = 0
        others = 0

        for p in self.__pokemons:
            types = [t.lower() for t in p.getTypes()]
            if "fire" in types:
                fireCount += 1
            elif "grass" in types:
                grassCount += 1
            else:
                others += 1
        total = fireCount + grassCount + others
        if total == 0:
            print("no Types present -_-")
            return
        labels = []
        values = []
        if fireCount > 0:
            labels.append("Fire")
            values.append(fireCount)
        if grassCount > 0:
            labels.append("Grass")
            values.append(grassCount)
        if others > 0:
            labels.append("Other")
            values.append(others)
        plt.pie(values, labels=labels, shadow=True)
        plt.title("Type-Pie")
        plt.legend()
        plt.show()


if __name__=="__main__":
    pokedex=Pokedex()
    pokedex.run()



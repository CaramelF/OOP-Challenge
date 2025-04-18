class Pet:
    def __init__(self, name, pet_type="Generic"):
        self.name = name
        self.pet_type = pet_type
        self.hunger = 5  # Default starting value
        self.energy = 5  # Default starting value
        self.happiness = 5  # Default starting value
        self.tricks = []  # List to store tricks
        self.custom_actions = {}  # Dictionary to store custom actions
        self.mood = "content"  # Default mood
        self.age = 0  # Age in days
        
        # Pet type specific ASCII representations
        self.type_ascii = {
            "Dog": "(d)",
            "Cat": "(c)",
            "Bird": "(b)",
            "Fish": "(<>)",
            "Rabbit": "(\\)",
            "Hamster": "(h)",
            "Generic": "(^.^)"
        }
        
        # Mood ASCII representations
        self.mood_ascii = {
            "ecstatic": "(*.*)",
            "happy": "(^.^)",
            "content": "(-.-)",
            "neutral": "(-_-)",
            "bored": "(=_=)",
            "sad": "(;_;)",
            "angry": "(>.<)",
            "exhausted": "(x.x)",
            "hungry": "(o.o)"
        }
    
    def eat(self, food="regular food"):
        foods = {
            "regular food": 3,
            "treat": 1,
            "favorite food": 5,
            "medicine": 2
        }
        
        hunger_reduction = foods.get(food, 3)
        self.hunger = max(0, self.hunger - hunger_reduction)
        self.happiness = min(10, self.happiness + (1 if food != "medicine" else 0))
        
        if food == "medicine":
            print(f"{self.name} reluctantly takes the medicine. It's for their own good!")
        else:
            print(f"{self.name} enjoys eating {food}! {self.type_ascii.get(self.pet_type, '(^.^)')}")
        
        self._update_mood()
    
    def sleep(self, duration="normal"):
        durations = {
            "nap": 2,
            "normal": 5,
            "long": 8
        }
        
        energy_increase = durations.get(duration, 5)
        self.energy = min(10, self.energy + energy_increase)
        
        if duration == "nap":
            print(f"{self.name} takes a quick nap. (zzz)")
        elif duration == "long":
            print(f"{self.name} sleeps for a long time and is fully refreshed! (zzz)(zzz)(zzz)")
        else:
            print(f"{self.name} had a good sleep and is now refreshed! (zzz)(zzz)")
        
        self._update_mood()
    
    def play(self, activity="regular play"):
        if self.energy < 2:
            print(f"{self.name} is too tired to play! {self.mood_ascii.get('exhausted', '(x.x)')}")
            return
        
        activities = {
            "regular play": {"energy": 2, "happiness": 2, "hunger": 1},
            "fetch": {"energy": 3, "happiness": 3, "hunger": 2},
            "chase": {"energy": 4, "happiness": 4, "hunger": 2},
            "gentle play": {"energy": 1, "happiness": 1, "hunger": 0}
        }
        
        if activity in activities:
            stats = activities[activity]
            self.energy = max(0, self.energy - stats["energy"])
            self.happiness = min(10, self.happiness + stats["happiness"])
            self.hunger = min(10, self.hunger + stats["hunger"])
            print(f"{self.name} had fun {activity}ing! {self.type_ascii.get(self.pet_type, '(^.^)')}")
        else:
            # Default play
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} had fun playing! {self.type_ascii.get(self.pet_type, '(^.^)')}")
        
        self._update_mood()
    
    def train(self, trick):
        if self.energy < 1:
            print(f"{self.name} is too tired to learn right now! {self.mood_ascii.get('exhausted', '(x.x)')}")
            return
            
        if trick in self.tricks:
            print(f"{self.name} already knows how to {trick}! {self.mood_ascii.get('content', '(-.-)')}")
            return
            
        self.tricks.append(trick)
        self.energy = max(0, self.energy - 1)
        self.happiness = min(10, self.happiness + 1)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} has learned to {trick}! {self.mood_ascii.get('happy', '(^.^)')}")
        self._update_mood()
    
    def add_custom_action(self, action_name, description, energy_cost=1, happiness_change=1, hunger_change=0):
        """Add a custom action that the pet can perform"""
        self.custom_actions[action_name] = {
            "description": description,
            "energy_cost": energy_cost,
            "happiness_change": happiness_change,
            "hunger_change": hunger_change
        }
        print(f"Added new action '{action_name}' for {self.name}!")
    
    def perform_custom_action(self, action_name):
        """Perform a custom action"""
        if action_name not in self.custom_actions:
            print(f"{self.name} doesn't know how to {action_name}!")
            return
            
        action = self.custom_actions[action_name]
        
        if self.energy < action["energy_cost"]:
            print(f"{self.name} is too tired to {action_name}! {self.mood_ascii.get('exhausted', '(x.x)')}")
            return
            
        self.energy = max(0, self.energy - action["energy_cost"])
        self.happiness = min(10, self.happiness + action["happiness_change"])
        self.hunger = min(10, self.hunger + action["hunger_change"])
        
        print(f"{self.name} performs: {action_name} - {action['description']} {self.type_ascii.get(self.pet_type, '(^.^)')}")
        self._update_mood()
    
    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} doesn't know any tricks yet. {self.mood_ascii.get('sad', '(;_;)')}")
            return
            
        print(f"\n--- {self.name}'s Tricks ---")
        for i, trick in enumerate(self.tricks, 1):
            print(f"{i}. {trick} {self.type_ascii.get(self.pet_type, '(^.^)')}")
    
    def show_custom_actions(self):
        if not self.custom_actions:
            print(f"{self.name} doesn't have any custom actions yet.")
            return
            
        print(f"\n--- {self.name}'s Custom Actions ---")
        for i, (action_name, details) in enumerate(self.custom_actions.items(), 1):
            print(f"{i}. {action_name}: {details['description']}")
    
    def _update_mood(self):
        """Update the pet's mood based on its current stats"""
        if self.happiness >= 8 and self.energy >= 7 and self.hunger <= 3:
            self.mood = "ecstatic"
        elif self.happiness >= 7 and self.energy >= 5 and self.hunger <= 5:
            self.mood = "happy"
        elif self.happiness >= 5 and self.energy >= 4 and self.hunger <= 6:
            self.mood = "content"
        elif self.happiness >= 3 and self.energy >= 3 and self.hunger <= 7:
            self.mood = "neutral"
        elif self.happiness <= 2:
            self.mood = "sad"
        elif self.energy <= 2:
            self.mood = "exhausted"
        elif self.hunger >= 8:
            self.mood = "hungry"
        else:
            self.mood = "bored"
    
    def get_status(self):
        mood_ascii = self.mood_ascii.get(self.mood, "(-_-)")
        pet_ascii = self.type_ascii.get(self.pet_type, "(^.^)")
        
        # Create status bars
        hunger_bar = self._create_status_bar(self.hunger, "#", "-")
        energy_bar = self._create_status_bar(self.energy, "*", "-")
        happiness_bar = self._create_status_bar(self.happiness, "^", "-")
        
        print(f"\n{pet_ascii} --- {self.name}'s Status --- {mood_ascii}")
        print(f"Type: {self.pet_type}")
        print(f"Mood: {self.mood.capitalize()} {mood_ascii}")
        print(f"Hunger:    {hunger_bar} {self.hunger}/10")
        print(f"Energy:    {energy_bar} {self.energy}/10")
        print(f"Happiness: {happiness_bar} {self.happiness}/10")
        print(f"Age: {self.age} days")
        print(f"Tricks Known: {len(self.tricks)}")
        print(f"Custom Actions: {len(self.custom_actions)}")
    
    def _create_status_bar(self, value, filled_char, empty_char):
        """Create a visual status bar"""
        filled = filled_char * value
        empty = empty_char * (10 - value)
        return filled + empty
    
    def age_up(self):
        """Increase the pet's age by one day"""
        self.age += 1
        print(f"(^.^) Happy birthday! {self.name} is now {self.age} days old!")
        
        # Pets get slightly hungrier and more tired as they age
        if self.age % 5 == 0:
            self.hunger = min(10, self.hunger + 1)
            self.energy = max(0, self.energy - 1)
            print(f"{self.name} is getting older and needs more care now.")


# Create specific pet types as subclasses
class Dog(Pet):
    def __init__(self, name):
        super().__init__(name, "Dog")
        # Add dog-specific tricks
        self.add_custom_action("bark", "Woof woof!", 1, 1, 0)
        self.add_custom_action("fetch stick", "Runs and brings back a stick", 2, 2, 1)
    
    def walk(self, duration="short"):
        """Take the dog for a walk"""
        durations = {
            "short": {"energy": 1, "happiness": 2, "hunger": 1},
            "medium": {"energy": 2, "happiness": 3, "hunger": 2},
            "long": {"energy": 4, "happiness": 5, "hunger": 3}
        }
        
        stats = durations.get(duration, durations["short"])
        
        if self.energy < stats["energy"]:
            print(f"{self.name} is too tired for a {duration} walk! (d)(x.x)")
            return
            
        self.energy = max(0, self.energy - stats["energy"])
        self.happiness = min(10, self.happiness + stats["happiness"])
        self.hunger = min(10, self.hunger + stats["hunger"])
        
        print(f"You took {self.name} for a {duration} walk! (d)(>)")
        self._update_mood()


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, "Cat")
        # Add cat-specific tricks
        self.add_custom_action("meow", "Meow meow!", 0, 1, 0)
        self.add_custom_action("pounce", "Jumps and pounces on a toy", 2, 3, 1)
    
    def groom(self):
        """Groom the cat"""
        self.happiness = min(10, self.happiness + 2)
        print(f"{self.name} purrs as you groom them. (c)(*)")
        self._update_mood()


class Bird(Pet):
    def __init__(self, name):
        super().__init__(name, "Bird")
        # Add bird-specific tricks
        self.add_custom_action("sing", "Sings a beautiful melody", 1, 2, 1)
        self.add_custom_action("fly around", "Flies around the room", 2, 3, 2)
    
    def clean_cage(self):
        """Clean the bird's cage"""
        self.happiness = min(10, self.happiness + 3)
        print(f"{self.name} chirps happily in their clean cage. (b)(*)")
        self._update_mood()
from pet import Pet, Dog, Cat, Bird

def display_menu():
    print("\n=== Pet Simulator Menu ===")
    print("1. Feed your pet")
    print("2. Let your pet sleep")
    print("3. Play with your pet")
    print("4. Train your pet")
    print("5. Show your pet's tricks")
    print("6. Check your pet's status")
    print("7. Add custom action")
    print("8. Perform custom action")
    print("9. Show custom actions")
    print("10. Special pet action")
    print("11. Age up your pet")
    print("12. Exit")

def main():
    print("(^.^) Welcome to the Enhanced Pet Simulator! (^.^)")
    print("\nChoose a pet type:")
    print("1. Dog (d)")
    print("2. Cat (c)")
    print("3. Bird (b)")
    print("4. Generic Pet (^.^)")
    
    while True:
        try:
            pet_choice = int(input("\nEnter your choice (1-4): "))
            if 1 <= pet_choice <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")
    
    pet_name = input("\nEnter your pet's name: ")
    if not pet_name:
        pet_name = "Buddy"
    
    # Create the appropriate pet type
    if pet_choice == 1:
        my_pet = Dog(pet_name)
        print(f"\n(d) You've adopted a dog named {my_pet.name}! (d)")
    elif pet_choice == 2:
        my_pet = Cat(pet_name)
        print(f"\n(c) You've adopted a cat named {my_pet.name}! (c)")
    elif pet_choice == 3:
        my_pet = Bird(pet_name)
        print(f"\n(b) You've adopted a bird named {my_pet.name}! (b)")
    else:
        my_pet = Pet(pet_name)
        print(f"\n(^.^) You've adopted a pet named {my_pet.name}! (^.^)")
    
    my_pet.get_status()
    
    while True:
        display_menu()
        
        try:
            choice = int(input("\nEnter your choice (1-12): "))
            
            if choice == 1:  # Feed
                print("\nChoose food type:")
                print("1. Regular food")
                print("2. Treat")
                print("3. Favorite food")
                print("4. Medicine")
                food_choice = input("Enter choice (1-4): ")
                
                foods = {
                    "1": "regular food",
                    "2": "treat",
                    "3": "favorite food",
                    "4": "medicine"
                }
                
                my_pet.eat(foods.get(food_choice, "regular food"))
                
            elif choice == 2:  # Sleep
                print("\nChoose sleep duration:")
                print("1. Nap")
                print("2. Normal sleep")
                print("3. Long sleep")
                sleep_choice = input("Enter choice (1-3): ")
                
                durations = {
                    "1": "nap",
                    "2": "normal",
                    "3": "long"
                }
                
                my_pet.sleep(durations.get(sleep_choice, "normal"))
                
            elif choice == 3:  # Play
                print("\nChoose play activity:")
                print("1. Regular play")
                print("2. Fetch")
                print("3. Chase")
                print("4. Gentle play")
                play_choice = input("Enter choice (1-4): ")
                
                activities = {
                    "1": "regular play",
                    "2": "fetch",
                    "3": "chase",
                    "4": "gentle play"
                }
                
                my_pet.play(activities.get(play_choice, "regular play"))
                
            elif choice == 4:  # Train
                trick = input("What trick would you like to teach? ")
                my_pet.train(trick)
                
            elif choice == 5:  # Show tricks
                my_pet.show_tricks()
                
            elif choice == 6:  # Status
                my_pet.get_status()
                
            elif choice == 7:  # Add custom action
                action_name = input("Enter the name of the custom action: ")
                description = input("Enter a description: ")
                
                try:
                    energy_cost = int(input("Energy cost (0-10): "))
                    happiness_change = int(input("Happiness change (-5 to 5): "))
                    hunger_change = int(input("Hunger change (-5 to 5): "))
                    
                    my_pet.add_custom_action(
                        action_name, 
                        description, 
                        energy_cost, 
                        happiness_change, 
                        hunger_change
                    )
                except ValueError:
                    print("Using default values due to invalid input.")
                    my_pet.add_custom_action(action_name, description)
                
            elif choice == 8:  # Perform custom action
                my_pet.show_custom_actions()
                action_name = input("Enter the name of the action to perform: ")
                my_pet.perform_custom_action(action_name)
                
            elif choice == 9:  # Show custom actions
                my_pet.show_custom_actions()
                
            elif choice == 10:  # Special pet action
                if isinstance(my_pet, Dog):
                    print("\nChoose walk duration:")
                    print("1. Short walk")
                    print("2. Medium walk")
                    print("3. Long walk")
                    walk_choice = input("Enter choice (1-3): ")
                    
                    durations = {
                        "1": "short",
                        "2": "medium",
                        "3": "long"
                    }
                    
                    my_pet.walk(durations.get(walk_choice, "short"))
                    
                elif isinstance(my_pet, Cat):
                    my_pet.groom()
                    
                elif isinstance(my_pet, Bird):
                    my_pet.clean_cage()
                    
                else:
                    print(f"{my_pet.name} doesn't have any special actions.")
                
            elif choice == 11:  # Age up
                my_pet.age_up()
                
            elif choice == 12:  # Exit
                pet_symbol = my_pet.type_ascii.get(my_pet.pet_type, '(^.^)')
                print(f"\nGoodbye! Take good care of {my_pet.name}! {pet_symbol}")
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
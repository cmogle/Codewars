import random
#define dictionary of animal sounds
animal_sounds = {
    "Alligator": "Hiss",
    "Antelope": "Bark",
    "Bat": "Screech",
    "Bear": "Growl",
    "Bee": "Buzz",
    "Cat": "Meow",
    "Chicken": "Cluck Cluck",
    "Chimpanzee": "Hoot",
    "Cow": "Moo",
    "Crocodile": "Growl",
    "Dog": "Woof",
    "Dolphin": "Click",
    "Donkey": "Hee-haw",
    "Duck": "Quack",
    "Eagle": "Screech",
    "Elephant": "Trumpet",
    "Frog": "Ribbit",
    "Goat": "Bleat",
    "Horse": "Neigh",
    "Kookaburra": "Laugh",
    "Lion": "Roar",
    "Monkey": "Chatter",
    "Owl": "Hoot",
    "Parrot": "Squawk",
    "Peacock": "Scream",
    "Penguin": "Honk",
    "Pig": "Oink",
    "Rooster": "Crow",
    "Sheep": "Baa",
    "Snake": "Hiss",
}

sorted_animal_sounds = {k: v for k, v in sorted(animal_sounds.items())}

def get_random_animal_suggestions(num_suggestions=5):
    remaining_animals = set(sorted_animal_sounds.keys()) - unique_animals_listened
    return random.sample(list(remaining_animals), num_suggestions)

unique_animals_listened = set()
play_again = True

while play_again:
    attempts = 0

    while attempts < 2:
        user_input = input("Enter an animal to hear its sound: ").title()
        if user_input in sorted_animal_sounds:
            print(f"A {user_input} goes {sorted_animal_sounds[user_input]}")
            unique_animals_listened.add(user_input)
            break
        else:
            print("Animal not found. Please try again.")
            attempts += 1

    if attempts == 2:
        suggestions = get_random_animal_suggestions()
        print("Here are some suggestions:", ", ".join(suggestions))
        user_input = input("Enter one of the suggested animals or any other animal: ").title()
        if user_input in sorted_animal_sounds:
            print(f"A {user_input} goes {sorted_animal_sounds[user_input]}")
            unique_animals_listened.add(user_input)

    user_choice = input("Do you want to play again? (y/n): ").lower()
    if user_choice != 'y':
        play_again = False

num_animals = len(unique_animals_listened)
print(f"Thank you for playing Animal Sounds, you listened for {num_animals} animals and their sounds.")

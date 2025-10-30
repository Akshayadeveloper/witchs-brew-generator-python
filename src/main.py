import random
import time
# The os module is NOT used to ensure compatibility with Programiz PRO Playground.
# Screen clearing is replaced with visual separation for reliability.

# --- 1. CORE PROJECT DATA: Ingredients and Outcomes ---

# Structured data for the core game logic
POTION_CATEGORIES = {
    '1': ('Base', 'What is the liquid foundation?'),
    '2': ('Power Source', 'What infuses the magic?'),
    '3': ('Twist', 'What unexpected element gives it an edge?'),
}

INGREDIENTS = {
    'Base': [
        'A phial of graveyard mist',
        'Three drops of vampire sweat',
        'Rainwater collected in a skull',
        'A gallon of zombie tears',
        'Distilled moonlight from a cursed night',
    ],
    'Power Source': [
        'A whisper from a forgotten god',
        'The shadow of a black cat',
        'A single scream of a banshee',
        'Dust from an ancient mummy’s tomb',
        'The laughter of a mischievous imp',
    ],
    'Twist': [
        'A pinch of eternal slumber',
        'A handful of cheerful confetti',
        'A glowing shard of pure regret',
        'The latest quarterly earnings report (shredded)', # A subtle CEO joke
        'The last thought of a broken clock',
    ]
}

# Define the potential potion effects, grouped by resulting color/vibe
POTION_EFFECTS = {
    'Green': [
        'Grants the user the ability to speak to spiders for 24 hours.',
        'Turns everything you touch into perfectly ripe cucumbers.',
        'Causes uncontrollable fits of disco dancing.',
    ],
    'Red': [
        'Instantly gives you the confidence of a thousand pirates.',
        'Makes the next three people you meet mistake you for royalty.',
        'Grants temporary super-speed, but only when running backwards.',
    ],
    'Blue': [
        'Enables you to see through the lies of politicians.',
        'Gives you the knowledge of all things that have been lost.',
        'Makes your hair sing opera whenever you sneeze.',
    ],
    'Black': [
        'Gives temporary invincibility, but removes your sense of taste.',
        'Causes phantom phone vibrations for the rest of the night.',
        'Transforms your shadow into a highly sarcastic sidekick.',
    ]
}

# --- 2. UTILITY FUNCTIONS ---

def typewriter_print(text, delay=0.03):
    '''Prints text with a dramatic, character-by-character effect.'''
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print() # Newline after the text is finished

# --- 3. GAME LOGIC FUNCTIONS ---

def display_welcome():
    '''Shows the attention-grabbing welcome screen.'''
    # Print the welcome text
    print("🎃 WITCH'S BREW POTION GENERATOR 🧪")
    print("------------------------------------------")
    typewriter_print("\nGreetings, Solo Founder. Enter the cursed kitchen of destiny.")
    typewriter_print("Your goal: to concoct a unique, powerful, and prize-winning potion.")
    typewriter_print("The ingredients you choose will dictate your path...\n")
    
    # Pause and wait for user to continue
    input("Press Enter to begin the ancient ritual...")
    
    # Add a large visual separation instead of clearing the screen
    print("\n" * 3)
    print("=" * 60)

def get_user_choice(category_name, options):
    '''Displays a selection menu and handles user input validation.'''
    while True:
        # Calculate the step number dynamically
        step_number = next((list(POTION_CATEGORIES.keys()).index(k) + 1)
                           for k, (name, _) in POTION_CATEGORIES.items()
                           if name == category_name)

        print(f"\n--- 🌑 STEP {step_number}: Choose Your {category_name} ---")

        # Display the ingredient options with numerical labels
        for i, option in enumerate(options):
            print(f"  [{i + 1}] {option}")

        choice_input = input("\nEnter the number of your choice (1-{}): ".format(len(options))).strip()

        try:
            choice_index = int(choice_input) - 1
            if 0 <= choice_index < len(options):
                # Return the selected ingredient text
                return options[choice_index]
            else:
                typewriter_print("\n(The spirits reject that number. Try again.)", delay=0.01)
        except ValueError:
            typewriter_print("\n(That is not a valid number. Try again.)", delay=0.01)

def brew_potion():
    '''Main logic for the brewing process.'''
    
    selected_ingredients = {}

    # 1. Ingredient Selection Loop
    for category_key, (category_name, prompt) in POTION_CATEGORIES.items():
        typewriter_print(f"\n🔮 {category_name} Selection: {prompt}")
        
        # Pass the correct ingredient list based on the category name
        ingredient = get_user_choice(category_name, INGREDIENTS[category_name])
        selected_ingredients[category_name] = ingredient
        typewriter_print(f"\n-> Selected: {ingredient}")
        time.sleep(0.5)
        
        # Add a visual separator after selection for clean transition to next step
        print("\n" * 3)
        print("=" * 60) 

    # 2. Brewing Ceremony
    print("\n" * 5)
    typewriter_print("The cauldron is bubbling...", delay=0.1)
    time.sleep(1)
    typewriter_print("The stars align...", delay=0.1)
    time.sleep(1)
    typewriter_print("The final spell is cast...")
    time.sleep(2)
    print("\n" * 5) # Visual separation for the final result

    # 3. Determine Outcome (Same logic as before)
    
    # Safely extract the defining word for the name
    def extract_name(ingredient_string):
        if ' of ' in ingredient_string:
            return ingredient_string.split(' of ')[-1].split(' ')[0]
        else:
            return ingredient_string.split(' ')[0]

    base_name = extract_name(selected_ingredients['Base'])
    power_name = extract_name(selected_ingredients['Power Source'])
    twist_name = extract_name(selected_ingredients['Twist'])

    potion_name = f"The {base_name.title()} of {power_name.title()} and {twist_name.title()}"

    # Randomly select the visual vibe (color) and its effect
    vibe_color = random.choice(list(POTION_EFFECTS.keys()))
    potion_effect = random.choice(POTION_EFFECTS[vibe_color])

    # 4. Display Results
    print("💀" * 30)
    typewriter_print("\n✨ YOUR PRIZE-WINNING POTION IS READY! ✨", delay=0.05)
    print("💀" * 30)

    print("\n\n--- 📜 POTION MANIFEST 📜 ---")
    typewriter_print(f"Title: {potion_name} Potion", delay=0.05)
    typewriter_print(f"Vibe: {vibe_color} and shimmering.", delay=0.05)
    print("-" * 30)

    print("\n--- 🧪 Ingredients Used ---")
    for category, ingredient in selected_ingredients.items():
        print(f"-> {category}: {ingredient}")

    print("\n--- 🌟 Magical Effect ---")
    typewriter_print(f"Result: {potion_effect}", delay=0.04)

    print("\n" * 2)
    print("💀" * 30)
    print("\nYour unique creation is worthy of the Wall of Inspiration!")
    input("\nPress Enter to exit the cursed kitchen.")

# --- 4. MAIN EXECUTION ---

if __name__ == "__main__":
    # Check for configuration integrity
    category_names = [data[0] for data in POTION_CATEGORIES.values()]

    if all(name in INGREDIENTS for name in category_names):
        try:
            display_welcome() 
            brew_potion()
        except KeyboardInterrupt:
            print("\n" * 5)
            print("Ritual interrupted. The spirits are displeased. Goodbye.")
        except Exception as e:
            print("\n" * 5)
            print(f"\nAn unholy error occurred: {e}")
            print("Please ensure you only enter numerical choices when prompted.")
    else:
        print("CRITICAL ERROR: Potion categories and ingredients are misconfigured. Check source data.")

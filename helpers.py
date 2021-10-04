import random

def did_user_register(variations):
    registration_chance = 15 # Percent chance the user registers
    
    if variations.trial_duration == 7:
        registration_chance += 5
    if variations.trial_duration == 14:
        registration_chance += 0 # baseline
    if variations.trial_duration == 21:
        registration_chance += 4
    if variations.trial_duration == 28:
        registration_chance -= 2

    if variations.cta_button_color != "blue":
        registration_chance += 3

    if random.randint(0, 100) < registration_chance:
        return True
    else:
        return False
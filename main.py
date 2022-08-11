import random

################## Scope ####################

# Modifying Global Scope

# enemies = 1
#
# def increase_enemies():
#   print(f"enemies inside function: {enemies}")
#   return enemies+1
#
# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local Scope

# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)
#
# drink_potion()
# '''print(potion_strength) will give NameError'''

# Global Scope

# player_health = 10
#
# def game():
#   def drink_potion():
#     potion_strength = 2
#     print(player_health)
#
#
#   drink_potion()
# print(player_health)
#
#  # There is no Block Scope
#
# if 3 > 2:
#   a_variable = 10
#
# game_level = 3
# def creat_enemy():
#   enemies = ["Skeleteon", "Zombie", "Alien"]
#   if game_level <5:
#     new_enemy = enemies[0]
#
#   print(new_enemy)

# PI = 3.14159
# URL = 'https://google.com'
# TWITTER_HANDLE = "@eobsv"

def user_successed():
    print("Congratulations")
    exit()

def user_failed():
    print("Try once more")
    return guesses - 1

def make_a_guess():

    print("Make a guess!")
    user_guess = int(input())
    if user_guess > random_number:
        print(f"Too much, try with smaller number. Amount of tries you have left: {guesses}")
        user_failed()
    elif user_guess < random_number:
        print(f"Too little, try with bigger number. Amount of tries you have left: {guesses}")
        user_failed()
    else:
        user_successed()
        exit()


print("Welcome in Number Guessing Game!")
guesses = 2
random_number = random.randint(0, 100)

print(f"I\'m thinking of a number between 1 and 100. It's: {random_number}")

print("Choose difficulty \'easy\' or \'hard\':")

difficulty_chosen = input()
difficulty_chosen_lowered = difficulty_chosen.lower()

if difficulty_chosen_lowered == 'easy':
    guesses *= 2
    print(f"Meh, you're chicken! You have: {guesses}!")
elif difficulty_chosen_lowered == 'hard':
    print(f"Wow, you're veteran and have only: {guesses}")
else:
    print("Try to type in difficulty once more ;)")
    exit()

while guesses > 0:
    make_a_guess()
    guesses -= 1
    if guesses == 0:
        print("You lost")
        exit()

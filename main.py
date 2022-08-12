from random import randint

EASY_LEVEL_GUESSES = 10
HARD_LEVEL_GUESSES = EASY_LEVEL_GUESSES / 2


def user_successed():
    print("Congratulations")
    exit()


def user_failed(guesses):
    print("Try once more")
    return guesses - 1


# def make_a_guess(random_number, guesses):
#
#     print("Make a guess!")
#     user_guess = int(input())
#     if user_guess > random_number:
#         print(f"Too much, try with smaller number. Amount of tries you have left: {guesses}")
#         user_failed()
#     elif user_guess < random_number:
#         print(f"Too little, try with bigger number. Amount of tries you have left: {guesses}")
#         user_failed()
#     else:
#         user_successed()
#         exit()

def check_answer(random_number, user_guess, guesses):
    # user_guess = int(input())
    if user_guess > random_number:
        print(f"Too much, try with smaller number. Amount of tries you have left: {guesses}")
        user_failed(guesses)
    elif user_guess < random_number:
        print(f"Too little, try with bigger number. Amount of tries you have left: {guesses}")
        user_failed(guesses)
    else:
        user_successed()
        exit()


def set_difficulty():
    difficulty_chosen_lowered = input("Choose difficulty \'easy\' or \'hard\':").lower()
    if difficulty_chosen_lowered == 'easy':
        print(f"Meh, you're chicken! You have: {EASY_LEVEL_GUESSES} guesses!")
        return EASY_LEVEL_GUESSES
    elif difficulty_chosen_lowered == 'hard':
        print(f"Wow, you're veteran and have only: {HARD_LEVEL_GUESSES}")
        return HARD_LEVEL_GUESSES
    else:
        print("Try to type in difficulty once more ;)")
        exit()


def game():
    print("Welcome in Number Guessing Game!")
    random_number = randint(1, 100)

    print(f"I\'m thinking of a number between 1 and 100. It's: {random_number}")
    guesses = set_difficulty()

    while guesses > 0:
        user_guess = int(input())
        check_answer(random_number, user_guess, guesses)
        guesses -= 1
        if guesses == 0:
            print("You lost")
            exit()


game()

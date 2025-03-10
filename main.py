from art import logo, vs
from game_data import data
import random
def game():
    print(logo)
    score = 0
    def format_data(account):
        account_name = account["name"]
        account_descr = account["description"]
        account_country = account["country"]
        return f"{account_name}, a {account_descr}, from {account_country}"

    def check_answer(user_guess, a_followers, b_followers):
        if a_followers > b_followers:
            return user_guess == "a"
        else:
            return user_guess == "b"
    account_b = random.choice(data)
    should_continue = True
    while should_continue:

        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:
            account_b == random.choice(data)


        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")


        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"You're wrong! Your final score is {score}")
            should_continue = False
game()
again = input("Do you want to play again? 'yes' or 'no': ").lower()
if again == "yes":
    print(("\n") * 20)
    game()
else:
    print("Thank you for playing!")

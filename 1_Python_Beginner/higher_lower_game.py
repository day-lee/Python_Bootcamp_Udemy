
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    }]


import random

def generate_random(account):
    """returns statement about randomly selected account"""
    return f"{account['name']}, a {account['description']}, from {account['country']}"

# Actual answer
def actual_answer(account_a, account_b):
    """returns an answer from number of account comparison"""
    if account_a > account_b:
        return account_a
    else:
        return account_b

def game():
    """continues the game if user's answer is correct, otherwise end the game"""
    score = 0
    account_a = random.choice(data)
    should_continue = True
    print(logo)

    while should_continue:

        account_b = (random.choice(data))

        print(f"\nCompare A: {generate_random(account_a)}")
        # print(account_a['follower_count'])
        print(vs)
        print(f"Against B: {generate_random(account_b)}")
        # print(account_b['follower_count'])

        actual = actual_answer(account_a['follower_count'], account_b['follower_count'])
        # print(f"actual: {actual}")

        # get user's answer
        user = input("Who has more followers? Type 'A' or 'B': ")
        if user == "a":
            user_answer = account_a
        else:
            user_answer = account_b

        # compare actual answer to users
        if actual == user_answer['follower_count']:
            score += 1

            print(logo)
            print((f"\nCorrect. Current score is {score}"))
            # move previous answer to first statement
            account_a = user_answer

        else:
            print(logo)
            print(f"Wrong. Final score is {score}")
            should_continue = False

game()

import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_art = [rock, paper, scissors]

user_input = int(input("What do you choose?\n(Type 0 for Rock, ! for Paper, 2 for Scisors.)\n"))
if user_input >= 3 or user_input < 0:
    print('You typed an invalid number, You Lose!! \n(•̀ ᴖ •́ )')
else :
    print(game_art[user_input])

computer_input = random.randint(0, 2)
print(f"Computer choose")
print(game_art[computer_input])


if user_input == 0 and computer_input == 2:
    print('You win!! \nദ്ദി ˉ͈̀꒳ˉ͈́ )✧')
elif computer_input > user_input:
    print('You lose \n(T_T)')
elif user_input > computer_input:
    print('You win!! \nദ്ദി ˉ͈̀꒳ˉ͈́ )✧')
elif computer_input == user_input:
    print('its a draw.\n (ᵕ—ᴗ—)')
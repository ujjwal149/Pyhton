import random
rock ='''
    ---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper ='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = input("Enter 1 to select  rock , 2 to select paper  and 2 to select scissors: ")
print("You chose: ", user_input)

computer_input = random.randint(1,3)
if computer_input == 1:
    print(f"Computer chose {print(rock)}")
elif computer_input == 2:
    print(f"Paper chose {print(paper)}")
elif computer_input == 3:
    print(f"Rock chose {print(scissors)}")

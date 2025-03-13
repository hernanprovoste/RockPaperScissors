import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

movement = [rock, paper, scissors]


playerMovement = int(input("Choose your moviment: Type 0 for Rock, 1 for Paper, 2 for Scissors \n"))

if 0 <= playerMovement <= 2:
    print(movement[playerMovement])

cpuMovement = random.randint(0, 2)

print("CPU Chose\n")
print(movement[cpuMovement])


if playerMovement >= 3 or playerMovement < 0:
    print("You choose and invalid number")
elif playerMovement == 0 and cpuMovement == 2:
    print("You win!")
elif cpuMovement == 0 and playerMovement == 2:
    print("You lose!")
elif cpuMovement > playerMovement:
    print("You lose!")
elif playerMovement > cpuMovement:
    print("You win!")
elif playerMovement == cpuMovement:
    print("Tie")




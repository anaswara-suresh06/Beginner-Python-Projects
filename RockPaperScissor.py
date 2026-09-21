import random
items=["rock","paper","scissor"]
com_pick=random.choice(items)
user_pick=input("Enter your choice - rock, paper, scissor : ").lower()
if user_pick not in items:
    print("Invalid choice!")
    exit()
print(f"computer choice = {com_pick} ")

if com_pick==user_pick:
  print("It's a draw ")
elif user_pick=="rock":
  if com_pick=="paper":
    print("You lose")
  elif com_pick=="scissor":
    print("You win ")
elif user_pick=="paper":
  if com_pick=="scissor":
    print("You lose")
  elif com_pick=="rock":
    print("You win ")
elif user_pick=="scissor":
  if com_pick=="rock":
    print("You lose")
  elif com_pick=="paper":
    print("You win ")
import random

rock = 'rock'
paper = 'paper'
scissors = 'scissors'
options = [rock, paper, scissors]


def check_win(player, computer):

  if player == computer:
    return 'tie'
  elif player == rock and computer == scissors:
    return 'you win'
  elif player == scissors and computer == rock:
    return 'computer win'
  elif player == paper and computer == rock:
    return 'you win'
  elif player == paper and computer == scissors:
    return 'computer win'
  elif player == scissors and computer == paper:
    return 'you win'
  elif player == rock and computer == paper:
    return 'computer win'
  else:
    return f'you should pick from {options}'


def get_choices():

  choices = {
    "player": input("Enter P choice"),
    "computer": random.choice(options)
  }
  print(
    f"You chose {choices.get('player')}. Computer chose {choices.get('computer')}."
  )
  return print(check_win({choices.get('player')}, {choices.get('player')}))


get_choices()

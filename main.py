import random

rock = 'rock'
paper = 'paper'
scissors = 'scissors'
options = [rock, paper, scissors]


def check_win():
  y_w = 'you win'
  c_w = 'comp win'
  choices = get_choices()
  player = choices.get('player')
  computer = choices.get('computer')
  if player == computer:
    return 'tie'
  elif player == rock:
    if computer == scissors:
      return y_w
    else:
      return c_w
  elif player == scissors:
    if computer == rock:
      return c_w
    else:
      return y_w
  elif player == paper:
    if computer == rock:
      return y_w
    else:
      return c_w
  else:
    return f'you should pick from {options}'


def get_choices():

  choices = {
    'player': input("Enter P choice"),
    'computer': random.choice(options)
  }
  print(
    f"You chose {choices.get('player')}. Computer chose {choices.get('computer')}."
  )
  return choices


print(check_win())

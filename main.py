import random

# Initialize game constants
MOVE_CHOICES = ['rock', 'paper', 'scissors']
MOVE_CHOICES_SHORTHAND = ['r', 'p', 's']
TARGET_SCORE = 2

# Defines the standard RPS game loop for a single match.
def play_rps():
  # Initialize game variables
  keep_playing = True
  player_score = 0
  computer_score = 0

  print('')
  print('New round!')

  # Main game loop
  while keep_playing:
    player_move = input("Select your move: ").lower().strip()

    while (player_move not in MOVE_CHOICES) and (player_move not in MOVE_CHOICES_SHORTHAND):
      print('Invalid move - must be (r)ock, (p)aper, or (s)cissors.')
      player_move = input("Select your move: ").lower().strip()

    # Support single-letter shorthand inputs for the move choices.
    if player_move in MOVE_CHOICES_SHORTHAND:
      if player_move == 'r':
        player_move = 'rock'
      elif player_move == 'p':
        player_move = 'paper'
      else:
        # Assumes no other move is possible
        player_move = 'scissors'

    # The computer should only select from the actual, longform names for the moves.
    computer_move = random.choice(MOVE_CHOICES)

    # Show and score the results!
    print('')
    print(player_move.capitalize() + " vs " + computer_move + "...")

    # The "fun" part - determining the scorer.
    if player_move == computer_move:
      print("  Tie!")
    elif (player_move == "rock" and computer_move == "scissors") or \
        (player_move == "paper" and computer_move == "rock") or \
        (player_move == "scissors" and computer_move == "paper"):
      print("  Player scores!")
      player_score += 1
    else:
      print("  Computer scores!")
      computer_score += 1

    # Show a scoreboard before displaying the winner or asking for more moves.
    print('')
    print("Current score:  player = " + str(player_score) + ", computer = " + str(computer_score))

    if player_score == TARGET_SCORE:
      print("Player wins!")
      keep_playing = False
    elif computer_score == TARGET_SCORE:
      print("Computer wins!")
      keep_playing = False

  # End of "main game loop"

# Introduce the game.  Make it stand out with whitespace before and after.

keep_playing = True

while keep_playing == True:
  print('')
  print('=================================')
  print('Welcome to Rock, Paper, Scissors!')
  print('=================================')
  print('')

  menu_choice = input("(P)lay or (q)uit? ").lower().strip()
  if menu_choice == 'p' or menu_choice == 'play':
    play_rps()
  elif menu_choice == 'q' or menu_choice == 'quit':
    keep_playing = False
  else:
    print('Invalid input - please try again.')

print('')
print("Goodbye, and thanks for playing!")
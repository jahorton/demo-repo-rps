import random

# Initialize game constants
MOVE_CHOICES = ['rock', 'paper', 'scissors']
MOVE_CHOICES_SHORTHAND = ['r', 'p', 's']

LENGTH_CHOICES = ['2', '3', '4', '5', '6', '7']
STRATEGY_CHOICES = ['random', 'beatlast', 'matchlast', 'nochange', 'surprise', 'rotate']

# Holds the 'random' choice for the 'nochange' and 'rotate' strategies.
locked_choice = random.choice(MOVE_CHOICES)

# Default game options (configurable by the player)
strategy = 'surprise'
play_length = 5

def pick_move(strategy, last_player_move):
  global locked_choice

  if strategy == 'random':
    return random.choice(MOVE_CHOICES)
  elif strategy == 'matchlast':
    return last_player_move
  elif strategy == 'nochange':
    return locked_choice
  elif strategy == 'beatlast':
    if last_player_move == 'rock':
      return 'paper'
    elif last_player_move == 'paper':
      return 'scissors'
    else:
      return 'rock'
  elif strategy == 'rotate':
    # Gameplay makes no difference whether we rotate before or after picking the
    # move, as long as we're consistent.
    if locked_choice == 'rock':
      locked_choice = 'paper'
    elif locked_choice == 'paper':
      locked_choice = 'scissors'
    else:
      locked_choice = 'rock'

    return locked_choice
  # Shouldn't happen, but it's good to have a default.
  else:
    print("Unexpected strategy: " + strategy)
    return 'rock'

# Defines the standard RPS game loop for a single match.
def play_rps(strategy, max_score):
  # Initialize game variables
  keep_playing = True
  player_score = 0
  computer_score = 0

  # Used by the 'beatlast' strategy - we need a random 'last' move
  # for the first round!
  last_player_move = random.choice(MOVE_CHOICES)

  print('')
  print('New round!  Target score: ' + str(max_score))

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
    computer_move = pick_move(strategy, last_player_move)

    # And NOW save the last player move; don't set it before the computer picks!
    # (That affects strategy logic!)
    last_player_move = player_move

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

    # Initialize the strategy display-string for the end-of-game report
    strategy_display = strategy
    if strategy == 'nochange':
      strategy_display = strategy + " ("+locked_choice+")"

    if player_score == max_score:
      print("Player wins!")
      keep_playing = False
      print("Computer strategy was: " + strategy_display)
    elif computer_score == max_score:
      print("Computer wins!")
      keep_playing = False
      print("Computer strategy was: " + strategy_display)

  # End of "main game loop"

# Introduce the game.  Make it stand out with whitespace before and after.

keep_playing = True

while keep_playing == True:
  print('')
  print('=================================')
  print('Welcome to Rock, Paper, Scissors!')
  print('=================================')
  print('')

  menu_choice = input("(P)lay, set (l)ength, set (o)pponent, or (q)uit? ").lower().strip()
  if menu_choice == 'p' or menu_choice == 'play':
    # Do not change the user's selection, even if 'surprise'.
    #
    # Pick the true strategy and put it here, redoing the 'surprise' pick on
    # each new game start.
    game_strat = strategy
    if game_strat == 'surprise':
      while game_strat == 'surprise':
        game_strat = random.choice(STRATEGY_CHOICES)
    elif (game_strat == 'nochange') or (game_strat == 'rotate'):
      # Set the computer's choice randomly on each new game start.
      locked_choice = random.choice(MOVE_CHOICES)

    # Launch the game session
    play_rps(game_strat, play_length)
  elif menu_choice == 'q' or menu_choice == 'quit':
    keep_playing = False
  elif menu_choice == 'l' or menu_choice == "length":
    print('')
    play_length = input("Select max score - 2 through 7: ").lower().strip()

    while (play_length not in LENGTH_CHOICES):
      print('Invalid selection.')
      print('')
      play_length = input("Select max score - 2 through 7: ").lower().strip()

    play_length = int(play_length)
  elif menu_choice == 'o' or menu_choice == "opponent":
    print('')
    print("random:    picks move randomly")
    print("beatlast:  picks the move that beats the player's last move")
    print("matchlast: picks the same move the player previously chose")
    print("nochange:  chooses one move and sticks with it")
    print("rotate:    chooses random start move, then rotates rock->paper->scissors->rock")
    print("surprise:  randomly chooses any of the other strategies at game start")
    print('')

    strategy = input("Select strategy: ").lower().strip()

    while (strategy not in STRATEGY_CHOICES):
      print('Invalid selection.')
      print('')
      strategy = input("Select strategy: ").lower().strip()
  else:
    print('Invalid input - please try again.')

print('')
print("Goodbye, and thanks for playing!")
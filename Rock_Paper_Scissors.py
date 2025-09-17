import random
import pygame

pygame.init()
pygame.font.init()
screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

player_wins = 0
computer_wins = 0

white = 255, 255, 255
black = 0, 0, 0
dark_grey = 50, 50, 50

font = pygame.font.SysFont('Arial', 20)
line_start_x = 180
line_start_y = 100
line_height = font.get_linesize()

opening_line = 'Let\'s play rock, paper, or scissors\nFirst to 3 wins\n\n'
lines = opening_line.split('\n')

rect_size = (75, 50)
rock_pos = (150, 200)
paper_pos = (250, 200)
scissors_pos = (350, 200)

rock_rect = pygame.Rect(rock_pos, rect_size)
rock_text_surface = font.render('Rock', True, white)
rock_choice = rock_text_surface.get_rect(center=rock_rect.center)

paper_rect = pygame.Rect(paper_pos, rect_size)
paper_text_surface = font.render('Paper', True, white)
paper_choice = paper_text_surface.get_rect(center=paper_rect.center)

scissors_rect = pygame.Rect(scissors_pos, rect_size)
scissors_text_surface = font.render('Scissors', True, white)
scissors_choice = scissors_text_surface.get_rect(center=scissors_rect.center)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, white)
        screen.blit(text_surface, (line_start_x, line_start_y + i * line_height))

    pygame.draw.rect(screen, dark_grey, rock_rect)
    screen.blit(rock_text_surface, rock_choice)

    pygame.draw.rect(screen, dark_grey, paper_rect)
    screen.blit(paper_text_surface, paper_choice)

    pygame.draw.rect(screen, dark_grey, scissors_rect)
    screen.blit(scissors_text_surface, scissors_choice)

    pygame.display.flip()

pygame.quit()


while player_wins < 3 and computer_wins < 3:
  choices = ["rock", "paper", "scissors"]
  computer_choice = random.choice(choices)
  player_choice = input("Choose rock, paper, or scissors:\n").lower()

  print(f"Computer chose: {computer_choice}")
  if (player_choice == "rock" and computer_choice == "scissors") or    (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
    winner = "Player"
  elif (player_choice == "rock" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "paper"):
    winner = "Tie"
  else:
    winner = "Computer"

  if winner == "Player":
    player_wins += 1
    print("You won")
  elif winner == "Computer":
    computer_wins += 1
    print("Computer won")
  else:
    print("It's a tie")
  
  print()
  print(f"Current Score - Player: {player_wins}, Computer: {computer_wins}")
  print()

  if player_wins == 3:
    print("Congratulations! You won.")
    print('Thank you for playing!')
    break
  elif computer_wins == 3:
    print("Computer won!")
    print('Thank you for playing!')
    break

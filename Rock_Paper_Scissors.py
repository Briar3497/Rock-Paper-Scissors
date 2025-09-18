import random
import pygame

pygame.init()
pygame.font.init()
screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

white = 255, 255, 255
black = 0, 0, 0
dark_grey = 50, 50, 50
gold = 239, 191, 4
green = 0, 255, 0

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
computer_choice_pos = (200, 300)
winner_pos = (200, 320)

player_wins = 0
computer_wins = 0
round_message = None
player_choice = None
computer_choice = None
winner = None
choices = ["rock", "paper", "scissors"]

def option_choice():
    global player_wins, computer_wins, winner, round_message, computer_choice
    while player_wins < 3 and computer_wins < 3:

        computer_choice = random.choice(choices)
        if player_choice is not None:
            if (player_choice == "rock" and computer_choice == "scissors") or (
                    player_choice == "scissors" and computer_choice == "paper") or (
                    player_choice == "paper" and computer_choice == "rock"):
                winner = "Player"
                player_wins += 1
                round_message = "You won"
            elif (player_choice == "rock" and computer_choice == "rock") or (
                    player_choice == "scissors" and computer_choice == "scissors") or (
                    player_choice == "paper" and computer_choice == "paper"):
                winner = "Tie"
                round_message = "It's a tie"
            else:
                winner = "Computer"
                computer_wins += 1
                round_message = "Computer won"







while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rock_rect.collidepoint(event.pos):
                    player_choice = "rock"
                    option_choice()
                elif paper_rect.collidepoint(event.pos):
                    player_choice = "paper"
                    option_choice()
                elif scissors_rect.collidepoint(event.pos):
                    player_choice = "scissors"
                    option_choice()


    screen.fill(black)
    mouse_pos = pygame.mouse.get_pos()

    for i, line in enumerate(lines):
        text_surface = font.render(line, True, white)
        screen.blit(text_surface, (line_start_x, line_start_y + i * line_height))

    # rock button logic
    rock_rect = pygame.Rect(rock_pos, rect_size)
    rock_text_surface = font.render('Rock', True, white)
    rock_choice = rock_text_surface.get_rect(center=rock_rect.center)
    rock_is_hovered = rock_rect.collidepoint(mouse_pos)
    if rock_is_hovered:
        rock_color = gold
    else:
        rock_color = dark_grey

    pygame.draw.rect(screen, rock_color, rock_rect)
    screen.blit(rock_text_surface, rock_choice)

    # paper button logic
    paper_rect = pygame.Rect(paper_pos, rect_size)
    paper_text_surface = font.render('Paper', True, white)
    paper_choice = paper_text_surface.get_rect(center=paper_rect.center)
    paper_is_hovered = paper_rect.collidepoint(mouse_pos)
    if paper_is_hovered:
        paper_color = gold
    else:
        paper_color = dark_grey

    pygame.draw.rect(screen, paper_color, paper_rect)
    screen.blit(paper_text_surface, paper_choice)

    # scissors button logic
    scissors_rect = pygame.Rect(scissors_pos, rect_size)
    scissors_text_surface = font.render('Scissors', True, white)
    scissors_choice = scissors_text_surface.get_rect(center=scissors_rect.center)
    scissors_is_hovered = scissors_rect.collidepoint(mouse_pos)
    if scissors_is_hovered:
        scissors_color = gold
    else:
        scissors_color = dark_grey

    pygame.draw.rect(screen, scissors_color, scissors_rect)
    screen.blit(scissors_text_surface, scissors_choice)

    computer_choice_rect = pygame.Rect(computer_choice_pos, rect_size)
    computer_text_surface = font.render(f'Computer chose: {computer_choice}', True, green)
    computer_choice_display = computer_text_surface.get_rect(center=computer_choice_pos)

    if computer_choice:
        pygame.draw.rect(screen, black, computer_choice_rect)
        screen.blit(computer_text_surface, computer_choice_display)

    winner_rect = pygame.Rect(winner_pos, rect_size)
    winner_text_surface = font.render(f'{round_message}', True, green)
    winner_choice_display = winner_text_surface.get_rect(center=winner_rect.center)

    if round_message:
        pygame.draw.rect(screen, black, winner_rect)
        screen.blit(winner_text_surface, winner_choice_display)

    print()
    print(f"Current Score - Player: {player_wins}, Computer: {computer_wins}")
    print()
    break

    if player_wins == 3:
        print("Congratulations! You won.")
        print('Thank you for playing!')
        break
    elif computer_wins == 3:
        print("Computer won!")
        print('Thank you for playing!')
        break
    pygame.display.flip()

pygame.quit()
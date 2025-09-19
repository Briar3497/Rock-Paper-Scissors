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
current_score_pos = (200, 340)
winner_message_pos = (200, 360)
thank_you_pos = (200, 380)

player_wins = 0
computer_wins = 0
round_message = None
computer_choice = None
winner_message = None

choices = ["rock", "paper", "scissors"]

def round_winner(player_choice):
    global player_wins, computer_wins, winner_message, round_message, computer_choice

    if winner_message:
        return

    computer_choice = random.choice(choices)

    if (player_choice == "rock" and computer_choice == "scissors") or (
            player_choice == "scissors" and computer_choice == "paper") or (
            player_choice == "paper" and computer_choice == "rock"):
        player_wins += 1
        round_message = "You won"
    elif player_choice == computer_choice:
        round_message = "It's a tie"
    else:
        computer_wins += 1
        round_message = "Computer won"

    if player_wins >= 3:
        winner_message = "Congratulations! You won."
    elif computer_wins >= 3:
        winner_message = "Computer won!"

def reset_game():
    global player_wins, computer_wins, round_message, winner_message, player_choice, computer_choice
    player_wins = 0
    computer_wins = 0
    round_message = None
    computer_choice = None
    winner_message = None


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if winner_message:
                reset_game()
            elif not winner_message:
                if rock_rect.collidepoint(event.pos):
                    round_winner('rock')
                elif paper_rect.collidepoint(event.pos):
                    round_winner('paper')
                elif scissors_rect.collidepoint(event.pos):
                    round_winner('scissors')

    screen.fill(black)
    mouse_pos = pygame.mouse.get_pos()

    # Draw initial instruction text
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, white)
        screen.blit(text_surface, (line_start_x, line_start_y + i * line_height))

    # Button logic (only show if the game is ongoing)
    if not winner_message:
        # rock button
        rock_rect = pygame.Rect(rock_pos, rect_size)
        rock_color = gold if rock_rect.collidepoint(mouse_pos) else dark_grey
        pygame.draw.rect(screen, rock_color, rock_rect)
        rock_text_surface = font.render('Rock', True, white)
        rock_text_rect = rock_text_surface.get_rect(center=rock_rect.center)
        screen.blit(rock_text_surface, rock_text_rect)

        # paper button
        paper_rect = pygame.Rect(paper_pos, rect_size)
        paper_color = gold if paper_rect.collidepoint(mouse_pos) else dark_grey
        pygame.draw.rect(screen, paper_color, paper_rect)
        paper_text_surface = font.render('Paper', True, white)
        paper_text_rect = paper_text_surface.get_rect(center=paper_rect.center)
        screen.blit(paper_text_surface, paper_text_rect)

        # scissors button
        scissors_rect = pygame.Rect(scissors_pos, rect_size)
        scissors_color = gold if scissors_rect.collidepoint(mouse_pos) else dark_grey
        pygame.draw.rect(screen, scissors_color, scissors_rect)
        scissors_text_surface = font.render('Scissors', True, white)
        scissors_text_rect = scissors_text_surface.get_rect(center=scissors_rect.center)
        screen.blit(scissors_text_surface, scissors_text_rect)

    # Display round results
    if computer_choice:
        computer_text_surface = font.render(f'Computer chose: {computer_choice}', True, green)
        computer_text_rect = computer_text_surface.get_rect(center=computer_choice_pos)
        screen.blit(computer_text_surface, computer_text_rect)

    if round_message:
        winner_text_surface = font.render(f'{round_message}', True, green)
        winner_text_rect = winner_text_surface.get_rect(center=winner_pos)
        screen.blit(winner_text_surface, winner_text_rect)

    # Display score
    current_score_text_surface = font.render(f"Current Score - Player: {player_wins}, Computer: {computer_wins}", True,
                                             green)
    current_score_text_rect = current_score_text_surface.get_rect(center=current_score_pos)
    screen.blit(current_score_text_surface, current_score_text_rect)

    # Display end-of-game messages
    if winner_message:
        winner_message_text_surface = font.render(f'{winner_message}', True, gold)
        winner_message_text_rect = winner_message_text_surface.get_rect(center=winner_message_pos)
        screen.blit(winner_message_text_surface, winner_message_text_rect)

        thank_you_text_surface = font.render(f'Click anywhere to play again!', True, gold)
        thank_you_text_rect = thank_you_text_surface.get_rect(center=thank_you_pos)
        screen.blit(thank_you_text_surface, thank_you_text_rect)

    pygame.display.flip()

pygame.quit()
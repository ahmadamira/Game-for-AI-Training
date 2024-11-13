import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 800, 600  
RED = (255, 0, 0)  
BLUE = (0, 0, 255)  
WHITE = (255, 255, 255)  
PLAYER1_KEY = pygame.K_f
PLAYER2_KEY = pygame.K_l  
START_KEY = pygame.K_SPACE  
RESTART_KEY = pygame.K_r  

screen = pygame.display.set_mode((WIDTH, HEIGHT))


font = pygame.font.Font(None, 36)


clock = pygame.time.Clock()


started = False  
round_number = 1  
player1_score = 0  
player2_score = 0  
player1_round_score = 0  
player2_round_score = 0  
player1_wins = 0  
player2_wins = 0  
start_time = 0  
game_over = False  


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == START_KEY and not started and not game_over:
               
                started = True
                start_time = pygame.time.get_ticks()
                player1_round_score = 0
                player2_round_score = 0
            elif event.key == PLAYER1_KEY and started:
               
                player1_round_score += 1
            elif event.key == PLAYER2_KEY and started:
               
                player2_round_score += 1
            elif event.key == START_KEY and game_over:
               
                round_number = 1
                player1_score = 0
                player2_score = 0
                player1_wins = 0
                player2_wins = 0
                game_over = False
            elif event.key == RESTART_KEY and game_over:
               
                round_number = 1
                player1_score = 0
                player2_score = 0
                player1_wins = 0
                player2_wins = 0
                game_over = False


    if started and pygame.time.get_ticks() - start_time >= 10000:
         
        started = False
        if player1_round_score > player2_round_score:
           
            player1_wins += 1
        elif player2_round_score > player1_round_score:
           
            player2_wins += 1
        player1_score += player1_round_score
        player2_score += player2_round_score
        round_number += 1

   
    if not game_over:
        if player1_round_score + player2_round_score == 0:
         
            screen.fill(RED, (0, 0, WIDTH // 2, HEIGHT))
            screen.fill(BLUE, (WIDTH // 2, 0, WIDTH // 2, HEIGHT))
        else:
         
            screen.fill(RED, (0, 0, int(WIDTH * player1_round_score / (player1_round_score + player2_round_score)), HEIGHT))
            screen.fill(BLUE, (int(WIDTH * player1_round_score / (player1_round_score + player2_round_score)), 0, WIDTH, HEIGHT))

   
        if not started:
            if round_number > 5:
         
                game_over = True
            else:
               
                text = font.render(f"Round {round_number} - Press SPACE to start", True, WHITE)
                screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
                text = font.render(f"Player 1 wins: {player1_wins}, Player 2 wins: {player2_wins}", True, WHITE)
                screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 + 50))
                if player1_round_score > player2_round_score:
               
                    text = font.render(f"Player 1 wins this round with {player1_round_score} points", True, WHITE)
                    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 + 100))
                elif player2_round_score > player1_round_score:
                   
                    text = font.render(f"Player 2 wins this round with {player2_round_score} points", True, WHITE)
                    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 + 100))
                else:
                   
                    text = font.render(f"This round is a tie", True, WHITE)
                    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 + 100))
        else:
       
            text = font.render(f"Time remaining: {10 - (pygame.time.get_ticks() - start_time) // 1000}", True, WHITE)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
            text = font.render(f"Player 1 score: {player1_round_score}, Player 2 score: {player2_round_score}", True, WHITE)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 + 50))
    else:
     
        screen.fill(WHITE)
        if player1_wins > player2_wins:
           
            text = font.render(f"Player 1 wins the game with {player1_wins} wins", True, RED)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        elif player2_wins > player1_wins:
         
            text = font.render(f"Player 2 wins the game with {player2_wins} wins", True, BLUE)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        else:
           
            text = font.render(f"The game is a tie", True, RED)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        text = font.render(f"Press R to restart", True, RED)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 + 100))

   
    pygame.display.flip()
   
    clock.tick(60)
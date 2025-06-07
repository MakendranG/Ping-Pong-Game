import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SIZE = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_SPEED = 7
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
WINNING_SCORE = 10
FONT_SIZE = 36

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Clock to control game speed
clock = pygame.time.Clock()

# Font for score display
font = pygame.font.Font(None, FONT_SIZE)

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED
        self.score = 0
    
    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= self.speed
    
    def move_down(self):
        if self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
    
    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

class Ball:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.rect = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, 
                               HEIGHT // 2 - BALL_SIZE // 2, 
                               BALL_SIZE, BALL_SIZE)
        # Randomize initial direction
        self.speed_x = BALL_SPEED_X * random.choice([-1, 1])
        self.speed_y = BALL_SPEED_Y * random.choice([-1, 1])
    
    def update(self, left_paddle, right_paddle):
        # Move the ball
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # Ball collision with top and bottom
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1
        
        # Ball collision with paddles
        if self.rect.colliderect(left_paddle.rect) or self.rect.colliderect(right_paddle.rect):
            self.speed_x *= -1
            # Add a slight randomization to the y speed after paddle hit
            self.speed_y = random.uniform(0.9, 1.1) * self.speed_y
        
        # Ball out of bounds - score points
        if self.rect.left <= 0:
            right_paddle.score += 1
            self.reset()
        elif self.rect.right >= WIDTH:
            left_paddle.score += 1
            self.reset()
    
    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

def draw_court():
    # Draw the center line
    for y in range(0, HEIGHT, 30):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 2, y, 4, 15))

def draw_scores(left_score, right_score):
    # Draw left player score
    left_text = font.render(str(left_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 20))
    
    # Draw right player score
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(right_text, (WIDTH * 3 // 4, 20))

def show_winner(winner):
    # Clear the screen
    screen.fill(BLACK)
    
    # Display winner message
    winner_text = font.render(f"Player {winner} wins!", True, WHITE)
    screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2 - 50))
    
    # Display restart message
    restart_text = font.render("Press SPACE to play again or ESC to quit", True, WHITE)
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 50))
    
    pygame.display.flip()
    
    # Wait for player input
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def show_controls():
    # Clear the screen
    screen.fill(BLACK)
    
    # Display title
    title_text = font.render("PING PONG", True, WHITE)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))
    
    # Display controls
    controls = [
        "Controls:",
        "Player 1: W (up), S (down)",
        "Player 2: Up Arrow (up), Down Arrow (down)",
        "",
        "First player to reach 10 points wins!",
        "",
        "Press SPACE to start"
    ]
    
    y_pos = 200
    for line in controls:
        control_text = font.render(line, True, WHITE)
        screen.blit(control_text, (WIDTH // 2 - control_text.get_width() // 2, y_pos))
        y_pos += 40
    
    pygame.display.flip()
    
    # Wait for player to press space
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def main():
    # Create paddles
    left_paddle = Paddle(20, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    right_paddle = Paddle(WIDTH - 20 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    
    # Create ball
    ball = Ball()
    
    # Show controls before starting
    show_controls()
    
    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Get keyboard input
        keys = pygame.key.get_pressed()
        
        # Player 1 controls (W, S)
        if keys[pygame.K_w]:
            left_paddle.move_up()
        if keys[pygame.K_s]:
            left_paddle.move_down()
        
        # Player 2 controls (Up, Down arrows)
        if keys[pygame.K_UP]:
            right_paddle.move_up()
        if keys[pygame.K_DOWN]:
            right_paddle.move_down()
        
        # Update ball position
        ball.update(left_paddle, right_paddle)
        
        # Check for winner
        if left_paddle.score >= WINNING_SCORE:
            show_winner(1)
            # Reset scores and ball
            left_paddle.score = 0
            right_paddle.score = 0
            ball.reset()
        elif right_paddle.score >= WINNING_SCORE:
            show_winner(2)
            # Reset scores and ball
            left_paddle.score = 0
            right_paddle.score = 0
            ball.reset()
        
        # Clear the screen
        screen.fill(BLACK)
        
        # Draw court elements
        draw_court()
        draw_scores(left_paddle.score, right_paddle.score)
        
        # Draw paddles and ball
        left_paddle.draw()
        right_paddle.draw()
        ball.draw()
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

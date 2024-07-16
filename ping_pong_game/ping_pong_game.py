import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 80
FPS = 60

# Set up the display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 100, 0)  # Darker green color for the background
BLACK = (0, 0, 0)

# Font for displaying scores
FONT = pygame.font.Font(None, 36)

# Ball
ball_x = WIDTH / 2
ball_y = HEIGHT / 2
ball_dx = 4  # Faster movement
ball_dy = 4  # Faster movement

# Paddles
paddle_a_x = 0
paddle_a_y = HEIGHT / 2
paddle_b_x = WIDTH - PADDLE_WIDTH
paddle_b_y = HEIGHT / 2

# Scores
score_a = 0
score_b = 0

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update paddle positions based on user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_a_y -= 5
    if keys[pygame.K_s]:
        paddle_a_y += 5
    if keys[pygame.K_UP]:
        paddle_b_y -= 5
    if keys[pygame.K_DOWN]:
        paddle_b_y += 5

    # Limit paddle movement
    paddle_a_y = max(0, min(paddle_a_y, HEIGHT - PADDLE_HEIGHT))
    paddle_b_y = max(0, min(paddle_b_y, HEIGHT - PADDLE_HEIGHT))

    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Check for collisions with paddles
    if (ball_x + BALL_RADIUS >= paddle_a_x and
            ball_x - BALL_RADIUS <= paddle_a_x + PADDLE_WIDTH and
            ball_y + BALL_RADIUS >= paddle_a_y and
            ball_y - BALL_RADIUS <= paddle_a_y + PADDLE_HEIGHT):
        ball_dx *= -1
    elif (ball_x + BALL_RADIUS >= paddle_b_x and
          ball_x - BALL_RADIUS <= paddle_b_x + PADDLE_WIDTH and
          ball_y + BALL_RADIUS >= paddle_b_y and
          ball_y - BALL_RADIUS <= paddle_b_y + PADDLE_HEIGHT):
        ball_dx *= -1

    # Check for ball hitting the top/bottom of the screen
    if ball_y - BALL_RADIUS < 0 or ball_y + BALL_RADIUS > HEIGHT:
        ball_dy *= -1

    # Check for ball going off-screen horizontally
    if ball_x - BALL_RADIUS < 0:
        score_b += 1
        ball_x = WIDTH / 2
        ball_y = HEIGHT / 2
        ball_dx *= -1
    elif ball_x + BALL_RADIUS > WIDTH:
        score_a += 1
        ball_x = WIDTH / 2
        ball_y = HEIGHT / 2
        ball_dx *= -1

    # Draw everything
    screen.fill(GREEN)  # Fill with the darker green color
    pygame.draw.rect(screen, WHITE, (paddle_a_x, paddle_a_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (paddle_b_x, paddle_b_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), BALL_RADIUS)

    # Display scores
    score_text_a = FONT.render(f"Player A: {score_a}", True, BLACK)
    score_text_b = FONT.render(f"Player B: {score_b}", True, BLACK)
    screen.blit(score_text_a, (10, 10))  # Position at the top-left corner
    screen.blit(score_text_b, (WIDTH - score_text_b.get_width() - 10, 10))  # Right-aligned

    pygame.display.flip()

pygame.quit()
sys.exit()

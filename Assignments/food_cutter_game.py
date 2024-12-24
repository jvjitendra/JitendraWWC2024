import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Food Cutter Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Game variables
food_images = ["apple.png", "banana.png", "carrot.png"]  # Replace with actual image paths
foods = []
score = 0
lives = 30
clock = pygame.time.Clock()
FPS = 60
# Load food images
def load_food_images():
    return [pygame.image.load(img) for img in food_images]

food_sprites = load_food_images()

# Create a food object
def create_food():
    food = {
        "image": random.choice(food_sprites),
        "x": random.randint(50, WIDTH - 50),
        "y": -50,
        "speed": random.randint(1, 3),  # Slower dropping speed
        "scale": random.uniform(0.4, 0.6)  # Smaller size for the food
    }
    food["image"] = pygame.transform.scale(food["image"], (int(food["image"].get_width() * food["scale"]), int(food["image"].get_height() * food["scale"])))
    return food

# Game loop
def game_loop():
    global foods, score, lives

    # Main loop
    running = True
    while running:
        screen.fill(WHITE)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for food in foods[:]:
                    food_rect = pygame.Rect(food["x"], food["y"], food["image"].get_width(), food["image"].get_height())
                    if food_rect.collidepoint(mouse_x, mouse_y):
                        foods.remove(food)
                        score += 1

        # Update food positions
        for food in foods[:]:
            food["y"] += food["speed"]
            if food["y"] > HEIGHT:
                foods.remove(food)
                lives -= 1

        # Add new food
        if random.randint(1, 20) == 1:  # Adjust spawn rate
            foods.append(create_food())

        # Draw food
        for food in foods:
            screen.blit(food["image"], (food["x"], food["y"]))

        # Draw score and lives
        score_text = font.render(f"Score: {score}", True, BLACK)
        lives_text = font.render(f"Lives: {lives}", True, RED)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WIDTH - 120, 10))

        # Check game over
        if lives <= 0:
            game_over_text = font.render("Game Over! Press Esc to Quit", True, RED)
            screen.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2 - 20))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False

        # Update screen
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# Run the game
if __name__ == "__main__":
    game_loop()

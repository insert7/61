#Simple ball animation program
import pygame
import sys

def main():
    # Initialize Pygame
    pygame.init()
    # Set screen dimensions
    screen_width, screen_height = 800, 600
    # Define colors
    white, red = (255, 255, 255), (255, 0, 0)
    # Set ball properties
    ball_pos = [screen_width // 2, screen_height // 2]
    ball_radius, ball_speed = 20, [2, 2]

    # Create the screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Simple Ball Animation")
    clock = pygame.time.Clock()  # Create a clock object to control the frame rate

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update ball position
        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]

        # Check for collisions with the screen edges and reverse direction
        if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > screen_width:
            ball_speed[0] = -ball_speed[0]
        if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > screen_height:
            ball_speed[1] = -ball_speed[1]

        # Render the ball on the screen
        screen.fill(white)  # Fill the screen with white color
        pygame.draw.circle(screen, red, ball_pos, ball_radius)  # Draw the ball
        pygame.display.flip()  # Update the screen
        clock.tick(60)  # Limit the frame rate to 60 FPS

if __name__ == "__main__":
    main()

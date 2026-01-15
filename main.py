import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    print(f"Starting Asteroids with pygame version : {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # Log the game state
        log_state()

        # Process the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Draw
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        # Limit FPS to 60 and calculate delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

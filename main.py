import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

pygame.init()


running = True

def main():
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x, y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
    player_ship = Player(x, y)
    while running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player_ship.draw(screen)
        player_ship.update(dt)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()

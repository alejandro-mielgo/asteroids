import pygame
from src.player import Player
from src.asteroid import Asteroid
from src.asteroidfield import AsteroidField
from src.shot import Shot
from src.constants import *


def main():
    print('Starting Asteroids!')

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable  = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    Shot.containers = (shots,drawable,updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField((updatable,))

    running:bool = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        screen.fill("black")
        
        for asteroid in asteroids:
            if player.check_collision(asteroid) == True:
                print('collision detected')
                running=False
            
            for shot in shots:
                if shot.check_collision(asteroid) == True:
                    asteroid.split()
                    shot.kill()

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    
    pygame.quit()


if __name__=="__main__":
    main()
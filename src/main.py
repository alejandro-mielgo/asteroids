import pygame
from src.player import Player
from src.asteroid import Asteroid
from src.asteroidfield import AsteroidField
from src.shot import Shot, Bomb, Barrier
from src.constants import *


def main():

    print('Starting Asteroids!')

    pygame.init()
    pygame.mixer.init()
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
    Bomb.containers = (shots,drawable,updatable)
    Barrier.containers = (shots,drawable,updatable)

    Shot.load_sound()
    Bomb.load_sound()
    Barrier.load_sound()

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
                player.health-=1
                print(f"health down to {player.health}")
                if player.health<=0:
                    running=False
            
            for shot in shots:
                if shot.check_collision(asteroid) == True:
                    asteroid.split()
                    if type(shot) is Shot:
                        shot.kill()


        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    
    pygame.quit()
    return 0


if __name__=="__main__":
    main()
    
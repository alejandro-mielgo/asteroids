import pygame
from src.player import Player
from src.asteroid import Asteroid
from src.asteroidfield import AsteroidField
from src.shot import Shot, Bomb, Barrier
from src.constants import *


def load_sounds() -> None:

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("./assets/music.mp3")
    pygame.mixer.music.set_volume(0.5)  
    pygame.mixer.music.play(-1)  

    Shot.load_sound("./assets/shot.mp3")
    Bomb.load_sound("./assets/bomb.mp3")
    Barrier.load_sound("./assets/barrier.mp3")
    Asteroid.load_sound("./assets/asteroid_explossion.mp3")

    
def create_containers()->tuple:
    updatable  = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    Shot.containers = (shots,drawable,updatable)
    Bomb.containers = (shots,drawable,updatable)
    Barrier.containers = (shots,drawable,updatable)
    AsteroidField.containers = (updatable,)

    return updatable,drawable, asteroids, shots


def main():

    print('Starting Asteroids!')
    load_sounds()        

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable,drawable, asteroids, shots = create_containers()
    player:Player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    running:bool = True
    paused:bool = False
    exp:int = 0

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
        
        if paused:
            screen.fill("black")
            print('paused game')
            pygame.display.flip()
            dt = clock.tick(5) / 1000
            continue  


        updatable.update(dt,exp)
        
 
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid) == True:
                    asteroid.split()
                    exp+=1
                    print(exp)
                    if isinstance(shot,Shot):
                        shot.kill()

            if player.check_collision(asteroid) == True:
                player.health-=1
                print(f"health down to {player.health}")
                if player.health<=0:
                    running=False
            

        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    
    pygame.quit()


if __name__=="__main__":
    main()
    
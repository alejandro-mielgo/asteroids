import pygame
from src.player import Player
from src.asteroid import Asteroid
from src.asteroidfield import AsteroidField
from src.shot import Shot, Bomb, Barrier
from src.constants import *
from src.uimanager import UIManager


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
    proyectiles = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (proyectiles, drawable, updatable)
    Bomb.containers = (proyectiles, drawable, updatable)
    Barrier.containers = (proyectiles, drawable, updatable)
    AsteroidField.containers = (updatable,)


    return updatable,drawable, asteroids, proyectiles


def main():

    print('Starting Asteroids!')
    load_sounds()        

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable, drawable, asteroids, proyectiles = create_containers()
    player:Player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    ui=UIManager(player=player)

    running:bool = True
    paused:bool = False
    exp:int = 0
    level:int=0

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
        ui.update(dt,exp,level) #la ui despues!
        
 
        for asteroid in asteroids:
            for proyectile in proyectiles:
                if proyectile.check_collision(asteroid) == True:
                    asteroid.split()
                    proyectile.manage_collision()
                    exp+=1
                    level = exp // XP_PER_LEVEL
                   

            if player.check_collision(asteroid) == True:
                if player.take_damage():
                    return
                
                
            
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        ui.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    
    pygame.quit()


if __name__=="__main__":
    main()
    
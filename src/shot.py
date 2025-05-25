import pygame
from src.circleshape import CircleShape
from src.constants import SHOT_RADIUS, BARRIER_RADIUS, BARRIER_DURATION
# from src.player import Player


class Shot(CircleShape):
    sound = None

    @classmethod
    def load_sound(cls,path = "./assets/shot.mp3"):
        cls.sound = pygame.mixer.Sound(path)

    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)
        if Shot.sound:
            Shot.sound.play()

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt


class Bomb(CircleShape):
        
    @classmethod
    def load_sound(cls,path = "./assets/bomb.mp3"):
        cls.sound = pygame.mixer.Sound(path)


    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)
        if Bomb.sound:
            Bomb.sound.play()
    
    def draw(self,screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.radius += dt*200
        if self.radius>380:
            self.kill()


class Barrier(CircleShape):

    @classmethod
    def load_sound(cls,path = "./assets/barrier.mp3"):
        cls.sound = pygame.mixer.Sound(path)
    

    def __init__(self, player):
        x=player.position[0]
        y=player.position[1]
        super().__init__(x,y,BARRIER_RADIUS)
        self.player = player
        self.duration = BARRIER_DURATION
        if Barrier.sound:
            Barrier.sound.play()
    
    def draw(self,screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 2)

    def update(self, dt):
        self.position = self.player.position
        self.duration -=dt
        if self.duration<=0:
            self.kill()


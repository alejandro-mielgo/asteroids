import pygame
from src.circleshape import CircleShape
from src.constants import SHOT_RADIUS, BARRIER_RADIUS, BARRIER_DURATION, SCREEN_WIDTH, SCREEN_HEIGHT
# from src.player import Player


class Shot(CircleShape):

    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)
        if Shot.sound:
            Shot.sound.play()

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, 0)

    def update(self, dt, exp):
        self.position += self.velocity * dt
        if (
            self.position.x < -self.radius
            or self.position.x > SCREEN_WIDTH + self.radius
            or self.position.y < -self.radius
            or self.position.y > SCREEN_HEIGHT + self.radius
        ):
            self.kill()  # removes from all sprite groups


class Bomb(CircleShape):
        
    @classmethod
    def load_sound(cls,path = "./assets/bomb.mp3"):
        cls.sound = pygame.mixer.Sound(path)


    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)
        if Bomb.sound:
            Bomb.sound.play()
        self.thickness = 5
    
    def draw(self,screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, int(self.thickness))

    def update(self, dt, exp):
        self.radius += dt*350
        self.thickness += dt*5
        if self.radius>450:
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
        self.thickness = 7
        if Barrier.sound:
            Barrier.sound.play()
    
    def draw(self,screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, int(self.thickness))

    def update(self, dt, exp):
        self.position = self.player.position
        self.duration -=dt
        self.thickness -= dt
        if self.duration<=0:
            self.kill()


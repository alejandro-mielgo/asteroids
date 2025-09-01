import pygame
from src.circleshape import CircleShape
from src.asteroid import Asteroid
from src.constants import SHOT_RADIUS, BARRIER_RADIUS, BARRIER_DURATION, SCREEN_WIDTH, SCREEN_HEIGHT,PLAYER_SHOOT_SPEED



class Shot(CircleShape):

    def __init__(self,x:float,y:float, player_rotation:float, piercing:bool, triple:bool, main:bool=True):
        super().__init__(x,y,SHOT_RADIUS)
        
        if Shot.sound and main:
            Shot.sound.play()
        
        self.piercing = piercing
        self.rotation = player_rotation
        
        if triple:
            shot_1 = Shot(x=x,y=y, player_rotation=player_rotation, piercing=piercing, triple=False, main=False)
            shot_1.velocity = pygame.Vector2(0, 1).rotate(self.rotation-10) * PLAYER_SHOOT_SPEED
            shot_2 = Shot(x=x,y=y, player_rotation=player_rotation, piercing=piercing, triple=False, main=False)
            shot_2.velocity = pygame.Vector2(0, 1).rotate(self.rotation+10) * PLAYER_SHOOT_SPEED

    
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

    def manage_collision(self):
        if self.piercing == False:
            self.kill()


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
    
    def manage_collision(self):
        pass


class Barrier(CircleShape):

    @classmethod
    def load_sound(cls,path = "./assets/barrier.mp3"):
        cls.sound = pygame.mixer.Sound(path)
    

    def __init__(self, player, duration:float=BARRIER_DURATION):
        x=player.position[0]
        y=player.position[1]
        super().__init__(x,y,BARRIER_RADIUS)
        self.player = player
        self.duration = duration
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

    def manage_collision(self):
        pass


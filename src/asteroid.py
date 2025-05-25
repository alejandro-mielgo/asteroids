import pygame
import random

from src.circleshape import CircleShape
from src.constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    
    def draw(self,screen):
        pygame.draw.circle(screen,'white',self.position,self.radius,2)
    
    def update(self,dt):
        self.position = self.position + dt * self.velocity

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20,50)
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1= Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = v1 * 1.2
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = v2 * 1.2
        




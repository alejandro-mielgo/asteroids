import pygame
import random

from src.circleshape import CircleShape
from src.constants import ASTEROID_MIN_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH


class Asteroid(CircleShape):

    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    
    def draw(self,screen):
        pygame.draw.circle(screen,'white',self.position,self.radius,2)
    
    def update(self, dt, exp):
        self.position += self.velocity * dt

        if (
            self.position.x < -self.radius
            or self.position.x > SCREEN_WIDTH + self.radius
            or self.position.y < -self.radius
            or self.position.y > SCREEN_HEIGHT + self.radius
        ):
            self.kill()  # removes from all sprite groups

     

    def split(self):
        
        self.kill()
        Asteroid.sound.play()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1= Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_1.velocity = v1 * 1.2
        asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_2.velocity = v2 * 1.2
        




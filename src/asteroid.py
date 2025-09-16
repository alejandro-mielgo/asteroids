import pygame
import random

from src.circleshape import CircleShape
from src.constants import ASTEROID_MIN_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH, POWERUP_CHANCE
from src.powerup import PowerUp


class Asteroid(CircleShape):

    def __init__(self,x,y,radius)->None:
        super().__init__(x,y,radius)
        self.image = pygame.image.load("./assets/sprites/asteroid.png").convert_alpha()
        self.radius = radius

    
    def draw(self,screen):
        rect = self.image.get_rect(center=self.position)
        scaled_image = pygame.transform.scale(self.image, (self.radius*2, self.radius*2))
        rect = scaled_image.get_rect(center=self.position)
        screen.blit(scaled_image, rect)
        # pygame.draw.circle(screen,'white',self.position,self.radius,3)

    
    def update(self, dt, exp):
        self.position += self.velocity * dt

        if (
            self.position.x < -self.radius
            or self.position.x > SCREEN_WIDTH + self.radius
            or self.position.y < -self.radius
            or self.position.y > SCREEN_HEIGHT + self.radius
        ):
            self.kill()  # removes from all sprite groups


    def spawn_powerup(self):
        if random.random() < POWERUP_CHANCE:
            power_up = PowerUp(self.position.x, self.position.y)
            power_up.velocity = self.velocity * 0.2
     
    def split(self):

        self.kill()
        self.spawn_powerup()
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
        




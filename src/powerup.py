import pygame
import random
from src.circleshape import CircleShape
from src.constants import POWERUP_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT

powerup_kinds = ['bomb', 'barrier', 'life', 'piercing_shot', 'triple_shot']
powerup_colours = {
    'bomb': 'red',
    'barrier': 'yellow',
    'life': 'white',
    'piercing_shot': 'green',
    'triple_shot': 'purple'
}

class PowerUp(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, POWERUP_RADIUS)
        self.kind = random.choice(powerup_kinds)
        self.colour = powerup_colours[self.kind]

    def draw(self,screen):
        pygame.draw.circle(screen,self.colour,self.position,self.radius,3)
    
    def powerup_effect(self, player):
        if self.kind == 'bomb':
            player.n_bombs += 1
        elif self.kind == 'barrier':
            player.n_barriers += 1
        elif self.kind == 'life':
            player.n_lifes += 1
        elif self.kind == 'piercing_shot':
            player.piercing_shot = True
        elif self.kind == 'triple_shot':
            player.triple_shoot = True

    def update(self, dt, exp):
        self.position += self.velocity * dt

        if (
            self.position.x < -self.radius
            or self.position.x > SCREEN_WIDTH + self.radius
            or self.position.y < -self.radius
            or self.position.y > SCREEN_HEIGHT + self.radius
        ):
            self.kill()  # removes from all sprite groups

            

import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...] = ()

    @classmethod
    def load_sound(cls,path:str):
        cls.sound = pygame.mixer.Sound(path)

    def __init__(self, x, y, radius):
        super().__init__(*self.containers)

        self.position:pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity:pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt,exp):
        # sub-classes must override
        pass

    def check_collision(self, other):
        distance = self.position.distance_to(other.position)
        collided = distance < (self.radius + other.radius)
        # if collided:
        #     print(f"[DEBUG] Collision detected: {self} <-> {other} | Distance: {distance:.2f} | Radii sum: {self.radius + other.radius}")
        #     print(f"coordinates:({self.position.x,self.position.y}), ({other.position.x},{other.position.y})")
        return collided

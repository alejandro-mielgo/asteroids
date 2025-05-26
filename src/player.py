import pygame
from src.circleshape import CircleShape
from src.shot import Shot,Bomb, Barrier
from src.constants import *



class Player(CircleShape):

    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation:float = 0
        self.shoot_cooldown:float = 0
        self.bomb_cooldown:float = 0
        self.barrier_cooldown:float = 0
        self.n_bombs:int = 5
        self.n_barriers:int = 2
        self.health:int = 1
        self.invulnerable:bool=False

        self.no_ammo_sound = pygame.mixer.Sound("./assets/no_ammo.mp3")

    def triangle(self)->list[pygame.Vector2]:
        visual_radius:float = self.radius + 10
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * visual_radius / 1.5

        a = pygame.Vector2(self.position + forward*1.4 * visual_radius)
        b = pygame.Vector2(self.position - forward/2 * visual_radius - right)
        c = pygame.Vector2(self.position - forward/2 * visual_radius + right)  
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), 2)
        pygame.draw.circle(screen,'white',self.position,self.radius,1)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        self.position.x = self.position.x % SCREEN_WIDTH
        self.position.y = self.position.y % SCREEN_HEIGHT
    
    def shot(self):
        if self.shoot_cooldown>0:
            return
        new_shot = Shot(self.position[0], self.position[1])
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

       
    def drop_bomb(self):

        if self.bomb_cooldown>0:
            return  
        if self.n_bombs<=0:
            print('no bombs available')
            pygame.mixer.Sound.play(self.no_ammo_sound)
            pygame.mixer.music.stop()
            return
 

        new_bomb = Bomb(self.position[0], self.position[1])
        new_bomb.velocity = pygame.Vector2(0, 0)
        self.bomb_cooldown = PLAYER_BOMB_COOLDOWN
        self.n_bombs -= 1

    def activate_barrier(self):
        if self.n_barriers<=0 or self.barrier_cooldown>0:
            return
        barrier = Barrier(player=self)
        barrier.velocity = pygame.Vector2(0, 0)
        self.barrier_cooldown = PLAYER_BARRIER_COOLDOWN
        self.n_barriers -=1


    def update(self, dt, exp):
            self.shoot_cooldown -= dt
            self.bomb_cooldown -= dt
            self.barrier_cooldown -= dt

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.rotate(-dt)
            
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.rotate(dt)
            
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self.move(dt)
            
            if keys[pygame.K_q]:
                self.drop_bomb()
            
            if keys[pygame.K_SPACE]:
                self.shot()
            
            if keys[pygame.K_e]:
                self.activate_barrier()

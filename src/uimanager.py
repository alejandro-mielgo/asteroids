import pygame

from src.player import Player

class UIManager():


    def __init__(self, player:Player):
        self.player:Player = player
        self.exp:int = 0
        self.level:int = 0
        self.font = pygame.font.SysFont(None, 25)

    def update(self,dt, exp, level):
        self.exp = exp
        self.level = level

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.exp} | Level { self.level }", True, (255, 255, 255))
        # lives_text = self.font.render(f"Lives: {self.player.health}", True, (255, 255, 255))
        bombs_text = self.font.render(f"Bombs: {self.player.n_bombs}  | cd {max(self.player.bomb_cooldown,0):.2f}", True, (255, 255, 255))
        barriers_text = self.font.render(f"Barriers: {self.player.n_barriers}  | cd {max(self.player.barrier_cooldown,0):.2f}", True, (255, 255, 255))
        
        screen.blit(score_text, (10, 10))
        screen.blit(bombs_text, (10, 35))
        screen.blit(barriers_text, (10, 60))
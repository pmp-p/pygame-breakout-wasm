import pygame
import constants as c

from .base import BaseObject


class Block(BaseObject):
    def __init__(self, block_type, pos, groups, obstacles):
        super(Block, self).__init__()
        self.type = block_type
        self.pos = pos
        self.health = int(self.type)
        self.color = c.COLOR_LEGEND[self.type]
        self.image = pygame.Surface((c.BLOCK_WIDTH, c.BLOCK_HEIGHT))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.old_rect = self.rect.copy()
        self.groups = groups
        self.obstacles = obstacles

    def update(self):
        self.old_rect = self.rect.copy()
        self.color = c.COLOR_LEGEND[self.type]
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=self.pos)

    def draw(self, window):
        pygame.draw.rect(window, pygame.Color(self.color), self.rect)

    def damage(self):
        if self.health > 0:
            self.health -= 1
            self.type = str(self.health)

        if self.health == 0:
            self.kill()


def damage_block(block):
    if block.health > 0:
        block.health -= 1
        block.type = str(block.health)

    if block.health == 0:
        block.kill()

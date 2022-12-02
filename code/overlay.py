import pygame

from settings import *


class Overlay:
    def __init__(self,player):
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.tool_surf = {tool:pygame.image.load(f'{OVERLAY_PATH}{tool}.png').convert_alpha() for tool in player.tools}

    def display(self):
        tool_surf = self.tool_surf[self.player.selected_tool]
        tool_rect = tool_surf.get_rect(midbottom = OVERLAY_POSITIONS['tool'])
        self.display_surface.blit(tool_surf,tool_rect)
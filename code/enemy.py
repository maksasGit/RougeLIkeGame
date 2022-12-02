import pygame
from settings import *
from support import *
from timer import Timer
from player import Player

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)

        self.import_assets()
        self.status = 'down_idle';
        self.frame_index = 0

        #setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)

            # movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 100

            #timers
        self.timers = {
            'tool_use': Timer(350,self.use_tool),
            'tool_switch': Timer(200)
        }

            # tools
        self.tools = ['hoe', 'water' , 'axe']
        self.tool_index = 0
        self.selected_tool = self.tools[self.tool_index]


            #

    def use_tool(self):
      #  print(self.selected_tool)
        it = 1

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def animate(self,dt):
        self.frame_index += 4 * dt
        if (self.frame_index >= len(self.animations[self.status])):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

    def import_assets(self):
        self.animations = {'up': [],'down': [],'left': [],'right': [],
						   'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
						   'right_hoe':[],'left_hoe':[],'up_hoe':[],'down_hoe':[],
						   'right_axe':[],'left_axe':[],'up_axe':[],'down_axe':[],
						   'right_water':[],'left_water':[],'up_water':[],'down_water':[]}

        for animation in self.animations.keys():
            full_path = 'C:/Users/imaks/PycharmProjects/pythonProject/graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)

    def go_to(self,playerPosX,playerPosY):

        pos_int_x = round(self.pos.x)
        pos_int_y = round(self.pos.y)
        pos_player_x = round(playerPosX)
        pos_player_y = round(playerPosY)


        if pos_int_y < pos_player_y:
            self.direction.y = 1
            self.status = 'down'
        elif pos_int_y > pos_player_y:
            self.direction.y = -1
            self.status = 'up'
        else:
            self.direction.y = 0


        if pos_int_x < pos_player_x:
            self.direction.x = 1
            self.status = 'right'
        elif pos_int_x > pos_player_x:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0





    def get_status(self):

            #idle
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'

            #tool use
        if self.timers['tool_use'].active:
            self.status = self.status.split('_')[0] + '_' + self.selected_tool

    def move(self, dt):
            # normalize vecttor
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

            #horizontal move
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
            #vertical move
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.get_status()
        self.update_timers()
        self.move(dt)
        self.animate(dt)


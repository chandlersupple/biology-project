import sys 
import pygame 
import random 
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1000,500)) 
pygame.display.set_caption('Natural Selection, Chandler Supple')

orange_brown = (255, 153, 0) 
brown = (153, 51, 0) 
light_backing = (255, 255, 102) 
dark_brown = (77, 57, 0) 
white = (255,255,255) 
black = (0,0,0) 
blue = (0, 102, 204) 
red = (255,0,0) 
orange = (255, 204, 0)
grey = (214, 214, 194)
dark_grey = (61, 61, 41)
lime = (0,255,0)
purple = (102, 0, 235)
yellow = (255, 255, 0)
green = (0, 204, 0)
sand = (255, 219, 77)
light_blue = (0, 153, 204)

x = random.randint(200, 800) 
y = random.randint(100, 400) 
begin = 0
cont_pressed = 0

direct = 'up'
enemy_count = 7
enemy_size = 20
enemy_speed = 3
ready = 750 
once = 0 
i = 0 
none = None
bigger = 1

sprite_size = 10
sprite_speed = 5
sprite_sprint_length = 250
power = 0

food_count = 10
j = 0 
consumed_count = 0 
score = 0

score = 0
power = 0 
time = 0
health = 0

has_rolled = 0
rolls = [0,1,2,3,4,5]
player_roll = 0

verdana_font = pygame.font.SysFont("verdana", 42) 
score_font = pygame.font.SysFont("verdana", 15) 
title_in_verdana = verdana_font.render("Natural Selection", False, (brown))
gameover_title = verdana_font.render("Gameover", False, (brown))

clock = pygame.time.Clock()

def gameboard(roll):

    for i in range(0, 12):
        pygame.draw.rect(screen, orange_brown, (0, ((i * 20) + (i * 20) + 20), 20, 20), 0)
        pygame.draw.rect(screen, brown, (980, ((i * 20) + (i * 20) + 20), 20, 20), 0)
        pygame.draw.rect(screen, brown, (0, ((i * 20) + (i * 20)), 20, 20), 0)
        pygame.draw.rect(screen, orange_brown, (980, ((i * 20) + (i * 20)), 20, 20), 0)

    for i in range(0, 25):
        pygame.draw.rect(screen, orange_brown, (((i * 20) + (i * 20) + 20), 0, 20, 20), 0)
        pygame.draw.rect(screen, orange_brown, (((i * 20) + (i * 20) + 20), 480, 20, 20), 0)
        pygame.draw.rect(screen, brown, (((i * 20) + (i * 20)), 0, 20, 20), 0)
        pygame.draw.rect(screen, brown, (((i * 20) + (i * 20)), 480, 20, 20), 0)

        pygame.draw.rect(screen, light_backing, (20, 20, 960, 460), 0)

        screen.blit(title_in_verdana, (38, 420))

    for i in range(0, 5):
        pygame.draw.rect(screen, dark_brown, ((((150 * i) + ((i * 30) + 65)), (145 + (((-1)**i) * (50))), 150, 210)), 0)
        pygame.draw.rect(screen, orange_brown, ((((150 * i) + ((i * 30) + 65)), (145 + (((-1)**i) * (50))), 150, 210)), 3)

    pygame.draw.rect(screen, white, (850, 70, 80, 80), 0)
    pygame.draw.rect(screen, brown, (850, 70, 80, 80), 3)

    dice_number = verdana_font.render(str(roll), False, (brown))
    screen.blit(dice_number, (876, 83))    
    
def gameover():
    for i in range(0, 12):
        pygame.draw.rect(screen, orange_brown, (0, ((i * 20) + (i * 20) + 20), 20, 20), 0)
        pygame.draw.rect(screen, brown, (980, ((i * 20) + (i * 20) + 20), 20, 20), 0)
        pygame.draw.rect(screen, brown, (0, ((i * 20) + (i * 20)), 20, 20), 0)
        pygame.draw.rect(screen, orange_brown, (980, ((i * 20) + (i * 20)), 20, 20), 0)

    for i in range(0, 25):
        pygame.draw.rect(screen, orange_brown, (((i * 20) + (i * 20) + 20), 0, 20, 20), 0)
        pygame.draw.rect(screen, orange_brown, (((i * 20) + (i * 20) + 20), 480, 20, 20), 0)
        pygame.draw.rect(screen, brown, (((i * 20) + (i * 20)), 0, 20, 20), 0)
        pygame.draw.rect(screen, brown, (((i * 20) + (i * 20)), 480, 20, 20), 0)

    screen.blit(gameover_title, (500, 250))  
    
def env(color):

    for i in range(0, 12):
        pygame.draw.rect(screen, black, (0, ((i * 20) + (i * 20) + 20), 20, 20), 0)
        pygame.draw.rect(screen, white, (980, ((i * 20) + (i * 20) + 20), 20, 20), 0)
        pygame.draw.rect(screen, white, (0, ((i * 20) + (i * 20)), 20, 20), 0)
        pygame.draw.rect(screen, black, (980, ((i * 20) + (i * 20)), 20, 20), 0)

    for i in range(0, 25):
        pygame.draw.rect(screen, black, (((i * 20) + (i * 20) + 20), 0, 20, 20), 0)
        pygame.draw.rect(screen, black, (((i * 20) + (i * 20) + 20), 480, 20, 20), 0)
        pygame.draw.rect(screen, white, (((i * 20) + (i * 20)), 0, 20, 20), 0)
        pygame.draw.rect(screen, white, (((i * 20) + (i * 20)), 480, 20, 20), 0)

        pygame.draw.rect(screen, color, (20, 20, 960, 460), 0)

class Sprite: 
    def __init__(self, sprite_size, sprite_speed, sprite_sprint_length, direction): 
        global x, y, direct, ready 
        self.sprite_size = sprite_size 
        self.sprite_speed = sprite_speed 
        self.sprite_sprint_length = sprite_sprint_length 
        self.x = x 
        self.y = y 
        self.direction = direction

        if direction[pygame.K_UP]:
            self.y = self.y - self.sprite_speed
            direct = 'up'
        if direction[pygame.K_DOWN]:
            self.y = self.y + self.sprite_speed
            direct = 'down'            
        if direction[pygame.K_RIGHT]:
            self.x = self.x + self.sprite_speed
            direct = 'right'            
        if direction[pygame.K_LEFT]:
            self.x = self.x - self.sprite_speed
            direct = 'left'        

        if direction[pygame.K_SPACE]:
            if (ready >= 765):
                if (direct == 'up'):
                    self.y = self.y - (self.sprite_sprint_length)
                if (direct == 'down'):
                    self.y = self.y + (self.sprite_sprint_length)
                if (direct == 'right'):
                    self.x = self.x + (self.sprite_sprint_length)
                if (direct == 'left'):
                    self.x = self.x - (self.sprite_sprint_length)        
                ready = 0
        if (ready < 765):
            ready = ready + 1

        if (self.x > 1000):
            self.x = 1000
        if (self.x < 0):
            self.x = 0
        if (self.y > 500):
            self.y = 500
        if (self.y < 0):
            self.y = 0

        x = self.x
        y = self.y

        sprite = pygame.draw.circle(screen, blue, (self.x, self.y), sprite_size, 0)
        
class Enemy: 
    def __init__(self, enemy_size_range, enemy_speed_range, color): 
        global x, y, i, once, enemy_x_dict, enemy_y_dict, enemy_count, health, bigger, sprite_size

        self.enemy_size_range = enemy_size_range
        self.enemy_speed_range = enemy_speed_range
        self.color = color

        dist_x = enemy_x_dict.get('enemy_x%s' % i) - x
        dist_y = enemy_y_dict.get('enemy_y%s' % i) - y
        
        if (self.enemy_size_range > sprite_size):
            bigger = 1
        if (self.enemy_size_range <= sprite_size):
            bigger = 0
        
        if (dist_x > 5 and dist_x <= 400):
            enemy_x_dict[('enemy_x%s' % i).format(i)] = enemy_x_dict.get('enemy_x%s' % i) - self.enemy_speed_range
        if (dist_x < -5 and dist_y >= -400):
            enemy_x_dict[('enemy_x%s' % i).format(i)] = enemy_x_dict.get('enemy_x%s' % i) + self.enemy_speed_range
        if (dist_y > 5 and dist_y <= 250):
            enemy_y_dict[('enemy_y%s' % i).format(i)] = enemy_y_dict.get('enemy_y%s' % i) - self.enemy_speed_range
        if (dist_y < -5 and dist_y >= -250):
            enemy_y_dict[('enemy_y%s' % i).format(i)] = enemy_y_dict.get('enemy_y%s' % i) + self.enemy_speed_range
            
        pygame.draw.circle(screen, self.color, (enemy_x_dict.get('enemy_x%s' % i), enemy_y_dict.get('enemy_y%s' % i)), self.enemy_size_range, 0)
        
        if (abs(dist_x) <= 15 and abs(dist_y) <= 15 and bigger == 1):
            health = health + 5
        
        i = i + 1
        if (i >= enemy_count):
            i = 0
        
class Food: 
    def __init__(self, color): 
        global food_x_dict, food_y_dict, x, y, j, food_count, consumed_count, score
        self.color = color 

        if (abs(x - food_x_dict.get('food_x%s' % j)) <= 15 and abs(y - food_y_dict.get('food_y%s' % j)) <= 15):
            consumed_count = consumed_count + 1
            score = score + 1
            if (j <= food_count):
                j = j + 1
            if (j >= food_count):
                j = 0
                
        pygame.draw.circle(screen, self.color, (food_x_dict.get('food_x%s' % j), food_y_dict.get('food_y%s' % j)), 10, 0)

        if (j >= food_count):
            j = 0
        j = j + 1
        
def profile(score, health, ready):
    global power, time
    
    pygame.draw.rect(screen, white, (5, 5, 600, 80), 0)
    pygame.draw.rect(screen, dark_grey, (5, 5, 600, 80), 2)
    
    pygame.draw.rect(screen, dark_grey, (15, 15, 515, 14), 2)
    pygame.draw.rect(screen, dark_grey, (15, 32, 515, 14), 2)
    pygame.draw.rect(screen, dark_grey, (15, 49, 515, 14), 2)
    
    if (score < 300):
        pygame.draw.rect(screen, lime, (18, 18, (round(int(score * 1.7))), 9), 0)
    if (score >= 300):
        pygame.draw.rect(screen, lime, (18, 18, 510, 9), 0)
    if (ready < 750):
        pygame.draw.rect(screen, yellow, (18, 35, (round(int(ready / 1.5))), 9), 0)
    if (ready >= 750):
        pygame.draw.rect(screen, yellow, (18, 35, 510, 9), 0)
    if (health < 60):
        pygame.draw.rect(screen, red, (18, 52, (510 - (health * 5)), 9), 0)
    if (health >= 60):
        pygame.draw.rect(screen, red, (18, 52, 0, 9), 0)
        
    score_font_rendered = score_font.render(("Score: %s" % score), False, (dark_grey)) 
    screen.blit(score_font_rendered, (14, 63))
    
def upgrade_info():
    global sprite_size, sprite_speed, sprite_sprint_length, power
    pygame.draw.rect(screen, white, (0,0,1000,500), 0)
    for i in range(0, 12):
        pygame.draw.rect(screen, black, (0, ((i * 20) + (i * 20) + 20), 20, 20), 0)
        pygame.draw.rect(screen, white, (980, ((i * 20) + (i * 20) + 20), 20, 20), 0)
        pygame.draw.rect(screen, white, (0, ((i * 20) + (i * 20)), 20, 20), 0)
        pygame.draw.rect(screen, black, (980, ((i * 20) + (i * 20)), 20, 20), 0)

    for i in range(0, 25):
        pygame.draw.rect(screen, black, (((i * 20) + (i * 20) + 20), 0, 20, 20), 0)
        pygame.draw.rect(screen, black, (((i * 20) + (i * 20) + 20), 480, 20, 20), 0)
        pygame.draw.rect(screen, white, (((i * 20) + (i * 20)), 0, 20, 20), 0)
        pygame.draw.rect(screen, white, (((i * 20) + (i * 20)), 480, 20, 20), 0)
        
    speed_text = score_font.render("Speed:", False, (dark_grey)) 
    size_text = score_font.render("Size:", False, (dark_grey)) 
    sprint_length_text = score_font.render("Sprint Length:", False, (dark_grey)) 
        
    screen.blit(speed_text, (150, 80))
    screen.blit(size_text, (150, 180))
    screen.blit(sprint_length_text, (150, 280))
        
    pygame.draw.rect(screen, black, (150, 100, 100, 50), 0)
    speed_plus = pygame.Rect(150, 100, 100, 50)
            
    pygame.draw.rect(screen, black, (150, 200, 100, 50), 0)
    size_plus = pygame.Rect(150, 200, 100, 50)
            
    pygame.draw.rect(screen, black, (150, 300, 100, 50), 0)
    sprint_plus = pygame.Rect(150, 300, 100, 50)
        
    pygame.draw.rect(screen, black, (450, 100, 400, 300), 3)
    pygame.draw.circle(screen, blue, (650,250), sprite_size, 0)
    
    if (power >= 1):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.button == 1):
                if (speed_plus.collidepoint(event.pos)):
                    sprite_speed = sprite_speed + 1
                    power = power - 1
            if (event.button == 1):
                if (size_plus.collidepoint(event.pos)):
                    sprite_size = sprite_size + 2
                    power = power - 1
            if (event.button == 1):
                if (sprint_plus.collidepoint(event.pos)):
                    sprite_sprint_length = sprite_sprint_length + 50
                    power = power - 1

try:
    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.display.quit()

        if (begin == 2 and has_rolled == 0):
            upgrade_info()
            cont = pygame.key.get_pressed()
            if cont[pygame.K_c]:
                player_roll = 0

        if (player_roll == 0):
            if ((len(rolls) - 1) > 1):
                rolled = random.randint(1,(len(rolls) - 1))
            roll = rolls[rolled]

            start_roll = pygame.key.get_pressed()
            if start_roll[pygame.K_r]:
                has_rolled = 1
                player_roll = 1
                rolls.pop(rolled)

            gameboard(roll)

        start_space = pygame.key.get_pressed()
        if start_space[pygame.K_SPACE]:
            begin = 1

        if (begin == 1):
            direction = pygame.key.get_pressed()

            if (roll == 1): # grassy meadow
                enemy_count = 5
                enemy_size = 20
                enemy_speed = 3
                env_color = green
                food_color = orange
                enemy_color = yellow
                food_count = 15
            if (roll == 2): # flood
                enemy_count = 6
                enemy_size = 20
                enemy_speed = 4
                env_color = light_blue
                food_color = black
                enemy_color = dark_grey
                food_count = 8
            if (roll == 5): # famine
                enemy_count = 10
                enemy_size = 30
                enemy_speed = 5
                env_color = light_backing
                food_color = black
                enemy_color = sand
                food_count = 3
            if (roll == 3): # mudlside
                enemy_count = 7
                enemy_size = 20
                enemy_speed = 4
                env_color = brown
                food_color = orange_brown
                enemy_color = light_backing
                food_count = 5
            if (roll == 4): # smog
                enemy_count = 6
                enemy_size = 30
                enemy_speed = 5
                env_color = white
                food_color = black
                enemy_color = grey
                food_count = 10

            if (once == 0):

                enemy_x_dict = {}
                enemy_y_dict = {}
                enemy_speed_dict = {}    
                enemy_size_dict = {}
                enemy_dict = {}
                food_x_dict = {}
                food_y_dict = {}
                food_dict = {}

                for i in range(0, enemy_count):
                    x_init = random.randint(50, 950)
                    enemy_x_dict[('enemy_x%s' % i).format(i)] = x_init
                for i in range(0, enemy_count):
                    y_init = random.randint(50, 450)
                    enemy_y_dict[('enemy_y%s' % i).format(i)] = y_init
                for i in range(0, enemy_count):
                    enemy_dict[('enemy_class%s' % i).format(i)] = None
                for i in range(0, enemy_count):
                    size = random.randint(8, enemy_size)
                    enemy_size_dict[('enemy_size%s' % i).format(i)] = size
                for i in range(0, enemy_count):
                    speed = random.randint(1, enemy_speed)
                    enemy_speed_dict[('enemy_speed%s' % i).format(i)] = speed
                for j in range(0, food_count):
                    food_x_init = random.randint(50, 950)
                    food_x_dict[('food_x%s' % j).format(j)] = food_x_init
                for j in range(0, food_count):
                    food_y_init = random.randint(50, 450)
                    food_y_dict[('food_y%s' % j).format(j)] = food_y_init
                for j in range(0, food_count):
                    food_dict[('food_class%s' % j).format(j)] = None

                once = 1

            if (score >= 300 or health >= 60):
                if (health >= 60):
                    rolls.append(roll)
                if (score >= 300):
                    power = power + 1
                has_rolled = 0
                begin = 2
                player_roll = 1
                score = 0
                once = 0
                health = 0
                x = random.randint(200, 800) 
                y = random.randint(100, 400)
                ready = 765

            env(env_color)
            profile(score, health, ready)
            sprite = Sprite(sprite_size, sprite_speed, sprite_sprint_length, direction)
            for i in range(0, enemy_count):
                enemy_dict[('enemy_class%s' % i)] = Enemy(enemy_size_dict.get('enemy_size%s' % i), enemy_speed_dict.get('enemy_speed%s' % i), enemy_color) 
            for j in range(0, food_count):
                food_dict[('food_class%s' % j)] = Food(food_color) 

        pygame.display.flip()
        clock.tick(30)
    
except:
    print('Oops, it looks like an error occured...')

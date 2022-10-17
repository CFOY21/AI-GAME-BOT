import pygame 
from pygame.locals import *
import os
import sys
import math


pygame.init()

w, h = 800,447
window = pygame.display.set_mode((w,h))

background = pygame.image.load(os.path.join('images','pumpkins.png')).convert()
backgroundx = 0
backgroundx2 = background.get_width()
#backgroundx2 = 10


speed = 30
run = True

clock = pygame.time.Clock()







class player2(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#self.image = pygame.Surface((10,10))
		self.image =  pygame.image.load(os.path.join('images','candy_small.png')).convert()
		#self.image.fill((0,0,0))
		self.rect = self.image.get_rect()
		#self.rect.left =25
		self.rect.x = 150
		#self.rect.move(200,200)
		self.rect.y = 300
		self.dx = 200
		self.dy = 0

	def update(self):
		self.dx =0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_w]:
			self.dx = 3
			self.image = pygame.image.load(os.path.join('images','pumpkin.png')).convert()
		if keystate[pygame.K_s]:
			self.dx = -3
			self.image = pygame.image.load(os.path.join('images', 'ghost_small.png'))
		self.rect.x += self.dx 
		#self.image = pygame.image.load(os.path.join('images', 'ghost_small.png'))

		# starting coordinate for ghost 
		self.dy = 200
		if keystate[pygame.K_UP]:
			# this controls how far the character would go up
			self.dy = 290
		if keystate[pygame.K_DOWN]:
			self.dy = 285
		self.rect.y =self.dy 





class pumpkin(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join('images', 'pumkin_small.png')).convert()
		self.rect = self.image.get_rect()
		# sets how fast the object moves
		self.dx = -1
		self.dy = 150
		self.rect.y =200
		self.rect.x = 400


	def update(self):

		self.rect.x += self.dx

		

		#deletes object as it leaves screen
		if self.rect.x ==0:
			self.rect.x =800

			# this will control the frame rate
		if self.rect.x%5 ==0:
			self.image = pygame.image.load(os.path.join('images', 'ghost_small.png')).convert()
		else:
			self.image = pygame.image.load(os.path.join('images', 'pumkin_small.png')).convert()

		collision = pygame.sprite.spritecollideany(pumpkin_enemy,all_sprites)

		if collision:
				print('collision detected')
		#self.rect.


class Score():
	def __init__(self):
		self.score = 0 
		self.score_font = pygame.font.SysFont(None,50)

	def update(self):


		#if pumpkin_enemy.rect.x < play1.rect.x:
		if pumpkin_enemy.rect.x < 2:
			self.score += 1 

		self.player_score = self.score_font.render(str(self.score), True,(255,0,0))


	def draw(self):
		window.blit(self.player_score,(30,40))


def redraw():
	#check this for x and y coordinates
	# coordinates of scrolling background
	window.blit(background,(backgroundx,-200))
	window.blit(background,(backgroundx2,-200))


	all_sprites.update()
	all_sprites.draw(window)
	pumpkin_sprite.update()
	pumpkin_sprite.draw(window)
	score.update()
	score.draw()


	#platform
	rect = Rect(0, 350, 2000, 50)
	pygame.draw.rect(window,(20,0,0), rect)

	

	#player_list.update()
	
	pygame.display.update()

all_sprites = pygame.sprite.Group()
play1 = player2()
all_sprites.add(play1)

pumpkin_sprite = pygame.sprite.GroupSingle()
pumpkin_enemy = pumpkin()
pumpkin_sprite.add(pumpkin_enemy)

score =Score()
score.__init__()
#
while run:
	redraw()
	clock.tick(speed)
	#player_list.draw(window)

	rect = Rect(100, 150, 200, 50)
	pygame.draw.rect(window,(0,0,0), rect)

	

	
	backgroundx -=1.4
	backgroundx2-=1.4
	if backgroundx < background.get_width() * -1:
		backgroundx = background.get_width()
	if backgroundx2 < background.get_width() * -1:
		backgroundx2 = background.get_width()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
			quit()
	#all_sprites.update()
	#all_sprites.draw(window)

import pygame 
from pygame.locals import *
import os
import sys
import math


w, h = 800,447
window = pygame.display.set_mode((w,h))

background = pygame.image.load(os.path.join('images','pumpkins.png')).convert()
backgroundx = 0
backgroundx2 = background.get_width()


speed = 30
run = True

clock = pygame.time.Clock()




# ghost sprite class
class Player(pygame.sprite.Sprite):

	def  __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.images = []

		img = pygame.image.load(os.path.join('images','ghost_small.png')).convert()
		self.images.append(img)
		self.image = self.images[0]
		self.rect = self.image.get_rect()
		self.x = 0

	def update():
		self.dx = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_w]:
			self.dx = 3
		if keystate[pygame.K_s]:
			self.dx = -3
		self.rect.x = self.dx 


class player2(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#self.image = pygame.Surface((10,10))
		self.image =  pygame.image.load(os.path.join('images','ghost_small.png')).convert()
		#self.image.fill((0,0,0))
		self.rect = self.image.get_rect()
		#self.rect.left =25
		#self.rect.x = 150
		self.rect.move(200,200)
		self.rect.y = 4
		self.dx = 200
		self.dy = 200

	def update(self):
		self.dx =0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_w]:
			self.dx = 3
		if keystate[pygame.K_s]:
			self.dx = -3
		self.rect.x += self.dx 
		self.dy = 0
		if keystate[pygame.K_UP]:
			self.dy = 3
		if keystate[pygame.K_DOWN]:
			self.dy = -3
		self.rect.y =self.dy 





def redraw():
	window.blit(background,(backgroundx,0))
	window.blit(background,(backgroundx2,0))

	#ghost drawing
	player = Player()   # spawn player
	player.rect.x = 200   # go to x
	player.rect.y = 30  # go to y
	player_list = pygame.sprite.Group()
	player_list.add(player)
	player_list.draw(window)

	all_sprites.update()
	all_sprites.draw(window)


	#platform
	rect = Rect(100, 150, 200, 50)
	pygame.draw.rect(window,(0,0,0), rect)

	collide = pygame.Rect.colliderect(rect,play1)

	#player_list.update()
	#runner.draw(window)
	pygame.display.update()

all_sprites = pygame.sprite.Group()
play1 = player2()
all_sprites.add(play1)

#
while run:
	redraw()
	clock.tick(speed)
	#player_list.draw(window)

	rect = Rect(100, 150, 200, 50)
	pygame.draw.rect(window,(0,0,0), rect)

	collide = pygame.Rect.colliderect(rect,play1)

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

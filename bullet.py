import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""represent the bullet"""
	def __init__(self,game):
		"""initialize the bullet's attributes"""
		super().__init__()
		self.settings=game.settings
		self.screen=game.screen
		#make the rect.
		self.rect=pygame.Rect(
			0,0,self.settings.bullet_width,self.settings.bullet_height)
		#set the position.
		self.rect.midright=game.ship.rect.midright
		self.x=float(self.rect.x)


	def update(self):
		"""update the position of the bullet"""	
		self.x+=self.settings.bullet_speed
		self.rect.x=self.x

	def draw_bullet(self):
		"""draw the bullet to the screen"""
		pygame.draw.rect(self.screen,self.settings.bullet_color,self.rect)

import pygame
from pygame import font

class Button:
	"""manage the button of the game"""
	def __init__(self,game,msg):
		"""initialize the attributes of the button"""
		self.settings=game.settings
		self.screen=game.screen
		#set the properties of the button.
		self.button_color=(0,50,0)
		self.width,self.height=200,50
		self.font=pygame.font.SysFont(None,48)
		self.text_color=(255,255,255)
		self.rect=pygame.Rect(0,0,self.width,self.height)
		#set the position.
		self.rect.center=self.screen.get_rect().center
		#prepare the message only once.
		self._prep_msg(msg)

	def _prep_msg(self,msg):
		"""turn msg into an image and put it on the button"""
		self.image=self.font.render(
			msg,True,self.text_color,self.button_color)
		self.image_rect=self.image.get_rect()
		self.image_rect.center=self.rect.center

	def draw_button(self):
		"""draw the msg and the button on the screen"""
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.image,self.image_rect)


import pygame
import json

class ScoreBoard:
	"""manage the score board"""
	def __init__(self,game):
		"""initialize the attributes of the score board"""
		self.settings=game.settings
		self.screen=game.screen
		#set the properties.
		self.width,self.height=200,50
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.centerx=self.screen.get_rect().centerx
		self.text_color=(0,250,0)
		self.text_color2=(250,0,0)
		self.text_color3=(200,200,0)
		self.font=pygame.font.SysFont(None,48)
		self.high_score=self.get_saved_high_score()
		self.prep_score()
		self.prep_high_score()
		self.prep_misses()
		self.prep_level()


	def prep_score(self):
		"""render the score into an image"""
		score_str=str(self.settings.score)
		self.score_img=self.font.render(
			score_str,None,self.text_color,self.settings.bg_color)
		self.score_rect=self.score_img.get_rect()
		self.score_rect.centerx=self.rect.centerx + 20

	def check_high_score(self):
		"""check if there is a new high score"""
		if self.settings.score>self.high_score:
			self.high_score=self.settings.score
			self.prep_high_score()

	def get_saved_high_score(self):
		"""return the saved high score from the file if it exists"""
		try:
			with open("high_score.json") as file:
				saved_high_score=json.load(file)
		except FileNotFoundError:
			return 0
		else:
			return saved_high_score

	def prep_high_score(self):
		"""render the high score into an image"""
		high_score_str=str(self.high_score)
		self.high_score_img=self.font.render(
			high_score_str,None,self.text_color,self.settings.bg_color)
		self.high_score_rect=self.high_score_img.get_rect()
		self.high_score_rect.left=self.rect.left

	def prep_misses(self):
		"""render the misses into an image"""
		misses_str=str(self.settings.misses)
		self.misses_img=self.font.render(
			misses_str,None,self.text_color2,self.settings.bg_color)
		self.misses_rect=self.misses_img.get_rect()
		self.misses_rect.right=self.rect.right

	def prep_level(self):
		"""render the level into an image"""
		level_str=str(self.settings.level)
		self.level_img=self.font.render(
			level_str,None,self.text_color3,self.settings.bg_color)
		self.level_rect=self.level_img.get_rect()
		self.level_rect.centerx=self.rect.centerx - 30

	def draw_score(self):
		"""draw the score to the screen"""
		self.screen.blit(self.score_img,self.score_rect)
		self.screen.blit(self.high_score_img,self.high_score_rect)
		self.screen.blit(self.misses_img,self.misses_rect)
		self.screen.blit(self.level_img,self.level_rect)
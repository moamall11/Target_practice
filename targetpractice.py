import pygame
import sys
import json

from FB_settings import Settings
from ship import Ship
from bullet import Bullet
from rectangle import Rectangle
from button import Button
from FB_stats import Stats
from score_board import ScoreBoard

class FiringBullets:
	"""a class to manage the game's assets and attributes"""
	def __init__(self):
		"""initialize the attributes of the game"""
		pygame.init()
		self.settings=Settings()
		self.screen=pygame.display.set_mode(
			(self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption("shoot the target")
		self.play_button=Button(self,"Play")
		self.ship=Ship(self)
		self.bullets=pygame.sprite.Group()
		self.rectangle=Rectangle(self)
		self.stats=Stats(self)
		self.sb=ScoreBoard(self)


	def run_game(self):
		"""the main loop for the game"""
		while True:
			self._check_events()
			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self.rectangle.update()
			self._update_screen()

	def _close_game(self):
		"""save the high score and close the game"""
		saved_high_score=self.sb.get_saved_high_score()
		if self.sb.high_score>saved_high_score:
			with open("high_score.json",'w') as file:
				json.dump(self.sb.high_score,file)
		sys.exit()

	def _check_events(self):
		"""check and respond to keypresses and keyreleases"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self._close_game()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos=pygame.mouse.get_pos()
				self._click_play_button(mouse_pos)

	def _click_play_button(self,mouse_pos):
		"""respond when the player clicks the play button"""
		button_clicked=self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			self._start_game()

	def _start_game(self):
		"""start the game"""
		#reset the settings.
		self.settings.initialize_dynamic_settings()
		self.bullets.empty()
		self.sb.prep_score()
		self.sb.prep_misses()
		self.sb.prep_level()
		self.stats.game_active=True
			

	def _check_keydown_events(self,event):
		"""respond to keys pressed by the player"""
		if event.key == pygame.K_q:
			self._close_game()
		elif event.key == pygame.K_UP:
			self.ship.moving_up=True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down=True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif event.key == pygame.K_p:
			self._start_game()

	def _check_keyup_events(self,event):
		"""respond to keys released by the player"""
		if event.key == pygame.K_UP:
			self.ship.moving_up=False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down=False

	def _fire_bullet(self):
		"""add a bullet to the group of bullets"""
		if len(self.bullets.sprites()) < self.settings.bullet_limit:
			bullet=Bullet(self)
			self.bullets.add(bullet)
			

	def _update_bullets(self):
		"""update the positions of bullets"""
		self.bullets.update()
		#detect collisions of the bullets with the rectangle.
		collisions=pygame.sprite.spritecollideany(self.rectangle,self.bullets)
		for bullet in self.bullets.copy():
			if bullet.rect.left >= self.screen.get_rect().right:
				self.bullets.remove(bullet)
				self.settings.misses+=1
				self.sb.prep_misses()
			elif collisions:
				self.bullets.remove(bullet)
				self.settings.score+=1
				self.sb.prep_score()
				self.sb.check_high_score()
				if self.settings.score % 5 == 0:
					self.settings.increase_spead()
					self.settings.level+=1
					self.sb.prep_level()
				break
		if self.settings.misses >= 3:
			self.stats.game_active=False


	def _update_screen(self):
		"""update the screen"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.rectangle.draw_rect()
		if not self.stats.game_active:
			self.play_button.draw_button()
		self.sb.draw_score()
		pygame.display.flip()


if __name__=='__main__':
	game=FiringBullets()
	game.run_game()
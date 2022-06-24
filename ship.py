import pygame

class Ship:
    """manage the ship's assets and behavior"""
    def __init__(self,game):
        """initialize the ship's attributes"""
        self.settings=game.settings
        self.screen=game.screen
        self.screen_rect=self.screen.get_rect()
        #set the image and rect.
        self.image=pygame.image.load("ship.bmp")
        self.rect=self.image.get_rect()
        #set the position.
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.rect.midleft=self.screen_rect.midleft
        #store the decimal value of the y rect of the ship.
        self.y=float(self.rect.y)
        #movement flags.
        self.moving_up=False
        self.moving_down=False


    def update(self):
        """update the position of the ship depending on the movement flags"""
        if self.moving_up and self.rect.top >= 0:
            self.y-=self.settings.ship_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y+=self.settings.ship_speed
        self.rect.y=self.y

    def blitme(self):
        """put the ship on the screen in its current position"""
        self.screen.blit(self.image,self.rect)
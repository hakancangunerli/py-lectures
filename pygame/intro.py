# intro to pygame, 

# we must import and initiliaze for all projects 
import pygame
pygame.init()
# we of course need to add extra things to make a screen, and a background as well. 

screen = pygame.display.set_mode((640,480)) # Set screen size of pygame window
background = pygame.Surface(screen.get_size())  # Create empty pygame surface
background.fill((255,255,255))    #rgb 
background = background.convert()  
#we have to do something called blitting, which would PAINT the screen, 
screen.blit(background, (0, 0))

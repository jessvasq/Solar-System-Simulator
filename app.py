import pygame
import math

#initialize the module 
pygame.init()

#set up pygame window
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#set up the title
pygame.display.set_caption("SOLAR SYSTEM SIMULATOR")

#create a loop to run the game
def main():
    run=True
    #create a loop to run the game
    while run:
        #iterate through all the events
        for event in pygame.event.get():
            #if the user clicks the close button, the game will stop
            if event.type == pygame.QUIT:
                run=False
    #use pygame.quit() to stop the game
    pygame.quit()

#call the main function
main()
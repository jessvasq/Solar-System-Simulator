import pygame
import math

#initialize the module 
pygame.init()

#set up pygame window
WIDTH, HEIGHT = 1200, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#set up the title
pygame.display.set_caption("SOLAR SYSTEM SIMULATOR")

#create a class for Planet

class Planet:
    #AU (astronomical units) is the distance from the sun to the earth
    AU = 149.6e6 * 1000 #we're multiplying by 1000 to get the value in meters
    #gravity constant will be used to calculate the force of gravity between the planets 
    G = 6.67428e-11
    #astronomical unit will be scaled down to fit the pygame window, update this number to make the planets bigger or smaller
    SCALE = 180 / AU  #1AU = 100pixels
    #time step will be used to calculate the orbit of the planet
    TIMESTEP = 36000*24 #represents 1 day, 36000 = #of seconds in an hour
    
    #use draw method to draw the planet
    def draw(self, win):
        #take the planet's value and draw it to scale 
        x = self.x * self.SCALE + WIDTH / 2 
        y = self.y*self.SCALE + WIDTH / 2
        #pass in the window, the color, the x and y coordinates, and the radius of the planet. This will draw the planet
        pygame.draw.circle(win, self.color, (x,y), self.radius)
         
        
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        #each planet will have an orbit. This will be a list of tuples that will contain the x and y coordinates of the orbit
        self.orbit = []
        #check if the planet is the sun. If it is, it will be the center of the solar system
        self.sun = False
        #if the planet is the sun, it will have a distance of 0 to the sun
        self.distance_to_sun = 0
        #each planet will have a x and y velocity. This will be used to calculate the orbit by moving x and y which will create a circle path
        self.x_vel = 0
        self.y_val = 0
        

#create a loop to run the game
def main():
    run=True
    #set up the clock
    clock = pygame.time.Clock()
    
    #initialize the planets
    #the sun will be the center of the solar system
                     #radius,  color,   mass                     
    sun = Planet(0, 0, 50, (255, 255, 0), 1.98892 * 10 ** 30)
    sun.sun = True ##we set the sun to true so that it will be the center of the solar system and dont have to calculate the distance to the sun
                #-1 indicates the planet will be on the left side of the sun
                        #Planet.AU is the distance from the sun to the earth, we're accessing the AU variable from the Planet class
    
    mercury = Planet(-0.387 * Planet.AU, 0, 8, (80, 78, 81), 3.30 * 10 ** 23)
    venus = Planet(-0.723 * Planet.AU, 0, 14, (255, 153, 51), 4.87 * 10 ** 24)
    earth = Planet(-1 * Planet.AU, 0, 16, (100, 149, 237), 5.97219 * 10 ** 24)
    mars = Planet(-1.524 * Planet.AU, 0, 12, (188, 39, 50), 6.41 * 10 ** 23)
    # jupiter = Planet(-5.203 * Planet.AU, 0, 40, (194, 150, 56), 1.898 * 10 ** 27)
    # saturn = Planet(-9.537 * Planet.AU, 0, 35, (179, 165, 136), 5.683 * 10 ** 26)
    # uranus = Planet(-19.191 * Planet.AU, 0, 25, (215, 242, 252), 8.681 * 10 ** 25)
    # neptune = Planet(-30.069 * Planet.AU, 0, 20, (19, 77, 212), 1.024 * 10 ** 26)
    # pluto = Planet(-39.482 * Planet.AU, 0, 10, (204, 84, 65), 1.309 * 10 ** 22)

    #add the planets to a list    
    planets = [sun, mercury, venus, earth, mars]
    
    #create a loop to run the game
    while run:
        #clock.tick() will make sure the game runs at the same speed on all computers
        clock.tick(60)
        #update the background color
        # WIN.fill((255, 255, 255))
        # #update the display
        # pygame.display.update()
        
        #iterate through all the events
        for event in pygame.event.get():
            #if the user clicks the close button, the game will stop
            if event.type == pygame.QUIT:
                run=False
                
        #calculate the force of gravity between the planets
        for planet in planets:
            planet.draw(WIN)
            
        #update the display after drawing the planets    
        pygame.display.update()
        
    #use pygame.quit() to stop the game
    pygame.quit()

#call the main function
main()
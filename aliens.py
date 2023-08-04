import pygame

def main():
    #initialize pygame module
    pygame.init()
    #load and set the logo
    logo = pygame.image.load("BG.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    #create surface on screen that has the size 240 x 180
    screen = pygame.display.set_mode((240,180))
    #variable for main loop
    running = True

    #main loop
    while running:
        #event handling, gets all events from event queue
        for event in pygame.event.get():
            #check if event type is quit
            if event.type == pygame.QUIT:
                running = False

if __name__=="__main__":
    main()
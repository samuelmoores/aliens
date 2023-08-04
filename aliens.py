import pygame

def main():
    #initialize pygame module
    pygame.init()
    #load and set the logo
    logo = pygame.image.load("Logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Aliens")
    #create surface on screen and set size
    screen = pygame.display.set_mode((1024,720))
    #variable for main loop
    running = True
    #load background image
    image_bg = pygame.image.load("BG.png")
    screen.blit(image_bg, (0, 0))
    pygame.display.flip()

    #load player image
    image_player = pygame.image.load("Player.png")
    image_player.set_alpha(128)
    screen.blit(image_player, (50, 50))
    pygame.display.flip()

    #set move player values
    xpos = 50
    ypos = 50
    step_x = 1
    step_y = 1

    #main loop
    while running:
        #event handling, gets all events from event queue
        for event in pygame.event.get():
            #check if event type is quit
            if event.type == pygame.QUIT:
                running = False
        
        #move player
        if xpos > 1024 - 50 or xpos < 0:
            step_x = -step_x
        if ypos > 720 - 50 or ypos < 0:
            step_y = -step_y
        xpos += step_x
        ypos += step_y
        screen.blit(image_bg, (0,0))
        screen.blit(image_player, (xpos, ypos))
        pygame.display.flip()

    


if __name__=="__main__":
    main()
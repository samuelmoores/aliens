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

    #main loop
    while running:
        #event handling, gets all events from event queue
        for event in pygame.event.get():
            #check if event type is quit
            if event.type == pygame.QUIT:
                running = False

if __name__=="__main__":
    main()
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((500, 650))
pygame.display.set_caption('Z Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Fonts/ShortBaby-Mg2w.ttf', 50)

test_surface = pygame.Surface((500, 650))
test_surface.fill('Pink')
sky_surface = pygame.image.load('Graphics/bluesky.png')
ground_surface = pygame.image.load('Graphics/ground.png')
house_surface = pygame.image.load('Graphics/house.png')
text_surface = test_font.render('Zoe Dollie', False, 'Coral')

doll_surface = pygame.image.load('Doll/clara.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface, (0, 0))
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, -60))
    screen.blit(house_surface, (180, 160))
    screen.blit(text_surface, (20, 170))
    screen.blit(doll_surface, (60, 290))

    pygame.display.update()
    clock.tick(60)



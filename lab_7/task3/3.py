import pygame
pygame.init()

display = pygame.display.set_mode((800, 600))
back_color = (255, 255, 255)
red = (255 ,0 ,0 )
clock = pygame.time.Clock()
FPS = 60
x = 30
y = 30
runn =True
speed = 20 
while runn:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            runn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x+ 25 + speed <=800: 
        x += 20
    if keys[pygame.K_LEFT] and x - 25 - speed >= 0: 
        x -= 20
    if keys[pygame.K_DOWN] and y + 25 + speed <= 600:
        y += 20
    if keys[pygame.K_UP] and y - 25 - speed >= 0:
        y -= 20
    
    display.fill(back_color)
    
    pygame.draw.circle(display , red , (x, y ) , 25)

    clock.tick(FPS)
    pygame.display.flip()
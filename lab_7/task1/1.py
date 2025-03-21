import pygame
import time
pygame.init()

display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("miki-rurk")
clock = pygame.time.Clock()
image_miki = pygame.image.load(r"C:\vscode\labs\.vscode\.vscode\lab_7\task1\clock.png")
image_min =  pygame.image.load(r"C:\vscode\labs\.vscode\.vscode\lab_7\task1\min_hand.png")
image_sec = pygame.image.load(r"C:\vscode\labs\.vscode\.vscode\lab_7\task1\sec_hand.png")
sec = image_sec.get_rect(center=(400 , 300))
minute = image_min.get_rect(center=(400,300))
angle1 = 60
angle2 = -49.5
FPS = 60

runn = True
while runn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            runn = False
    rat_sec = pygame.transform.rotate(image_sec, angle1)
    sec_rect = image_sec.get_rect(center=(400, 300))
    rot_rect = rat_sec.get_rect(center=sec_rect.center)
    rat_min = pygame.transform.rotate(image_min , angle2)
    rotan_min= rat_min.get_rect(center=minute.center)

    display.blit(image_miki, (0, 0))

    display.blit(rat_sec, rot_rect.topleft)
    display.blit(rat_min, rotan_min.topleft)

    time.sleep(1)  
    angle2 -= 0.5
    angle1 -= 6
    pygame.display.flip()
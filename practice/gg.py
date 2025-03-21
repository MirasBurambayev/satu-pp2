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
angle = 60
FPS = 60

runn = True
while runn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            runn = False
    rat_sec = pygame.transform.rotate(image_sec, angle)
    sec_rect = image_sec.get_rect(center=(400, 300))
    rot_rect = rat_sec.get_rect(center=sec_rect.center)

    display.blit(image_miki, (0, 0))
    display.blit(image_min, (0, 0))
    display.blit(rat_sec, rot_rect.topleft)

    time.sleep(1)  

    angle -= 6
    pygame.display.flip()
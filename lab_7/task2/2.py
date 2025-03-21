import pygame
import os

pygame.init()
pygame.mixer.init()

tracks = [
    r"lab_7\task2\music\Король и Шут - Дурак и молния.mp3",
    r"lab_7\task2\music\Король и Шут - Лесник.mp3",
    r"lab_7\task2\music\Король и Шут - Прыгну Со Скалы.mp3"
]
current = 0 
pygame.mixer.music.load(tracks[current])
pygame.mixer.music.play()


display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("player")
back_color = (169, 171, 170)

image_back =pygame.image.load(r"C:\vscode\labs\.vscode\.vscode\lab_7\task2\knopki\back 1.png")
image_next = pygame.image.load(r"C:\vscode\labs\.vscode\.vscode\lab_7\task2\knopki\back 2.png")
image_pause =pygame.image.load(r"C:\vscode\labs\.vscode\.vscode\lab_7\task2\knopki\pause 1.png")
image_play = pygame.image.load(r"C:\vscode\labs\.vscode\.vscode\lab_7\task2\knopki\play 1.png")
back = image_back.get_rect(center=(250, 300))
pause = image_pause.get_rect(center=(350, 300))
play = image_play.get_rect(center=(450, 300))
next = image_next.get_rect(center=(550, 300))
clock = pygame.time.Clock()
FPS = 60






runn = True
while runn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            runn = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play.collidepoint(event.pos):
                pygame.mixer.music.play()
            if pause.collidepoint(event.pos):
                pygame.mixer.music.pause()
            if next.collidepoint(event.pos):
                current +=1
                if current >= len(tracks):
                    current = 0
                pygame.mixer.music.load(tracks[current])
                pygame.mixer.music.play()
            if back.collidepoint(event.pos):
                current -=1
                if current >= len(tracks):
                    current = 0
                pygame.mixer.music.load(tracks[current])
                pygame.mixer.music.play()
        
    display.fill(back_color)

    display.blit(image_back, back)
    display.blit(image_pause, pause)
    display.blit(image_play, play)
    display.blit(image_next, next)


    clock.tick(FPS)
    pygame.display.flip()
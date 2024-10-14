import pygame
pygame.init()

width = 480
height = 640

screen = pygame.display.set_mode((width, height))
button = pygame.Rect(width // 4, height // 4, 200, 100)

score_font = pygame.font.SysFont('comicsansms', 40)
scores = 0

def show_scores():
    scores_screen = score_font.render(str(scores), True, 'blue')
    screen.blit(scores_screen, [5, 0])

run_game = True

while run_game:
    screen.fill('white')
    pygame.draw.rect(screen, 'green', button)
    show_scores()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if button.x <= event.pos[0] <= button.x + button.width:
                    scores += 1
        if event.type == pygame.QUIT:
            run_game = False
    pygame.display.flip()
pygame.quit()


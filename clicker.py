import pygame, sys, time
pygame.init()

width_screen = 800
height_screen = 600

screen = pygame.display.set_mode((width_screen, height_screen))

background = pygame.image.load('background.jpg')

class Button():
    def __init__(self):
        self.button_image = pygame.image.load('button.png')
        self.x = width_screen // 3.3
        self.y = height_screen // 3.3
        self.width = self.button_image.get_width()
        self.height = self.button_image.get_height()
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

score_font = pygame.font.SysFont('comicsansms', 40)
scores = 0

def show_scores():
    scores_screen = score_font.render(str(scores), True, 'blue')
    screen.blit(scores_screen, [5, 0])

run_game = True

sck=0.3

while run_game:
    screen.blit(background, (0, 0))
    button = Button()
    screen.blit(button.button_image, (width_screen // 3.3, height_screen // 3.3))
    show_scores()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button.hitbox.collidepoint(event.pos):
                start_time = time.time()
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            end_time = time.time()
            time_passed = (end_time - start_time) * 100
            print(time_passed)
            scores = round(scores + time_passed*sck)
        if event.type == pygame.QUIT:
            run_game = False
    pygame.display.flip()
pygame.quit()

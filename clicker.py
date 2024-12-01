import pygame, sys, time
pygame.init()

width_screen = 800
height_screen = 600

screen = pygame.display.set_mode((width_screen, height_screen))

background = pygame.image.load('background.jpg')
button_not_clicked_image = pygame.image.load('button_not_clicked.png')
button_clicked_image = pygame.image.load('button_clicked.png')


class Button():
    def __init__(self, image):
        self.image = image
        self.x = width_screen // 3
        self.y = height_screen // 2.5
        self.width = self.image.get_width() // 1.2
        self.height = self.image.get_height() // 1.8
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

score_font = pygame.font.SysFont('comicsansms', 40)
scores = 0

def show_scores():
    scores_screen = score_font.render(str(scores), True, 'blue')
    screen.blit(scores_screen, [5, 0])

run_game = True

scores_multiplier = 0.3
start_time = 0
end_time = 0
button_pressed = False

button = Button(button_not_clicked_image)

while run_game:
    screen.blit(background, (0, 0))
    screen.blit(button.image, (width_screen // 3.3, height_screen // 3.3))
    show_scores()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button.hitbox.collidepoint(event.pos):
                start_time = time.time()
                button.image = button_clicked_image
                button_pressed = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and button_pressed:
            end_time = time.time()
            button.image = button_not_clicked_image
            button_pressed = False
            time_passed = (end_time - start_time) * 100
            print(time_passed)
            scores = round(scores + time_passed * scores_multiplier)
        if event.type == pygame.QUIT:
            run_game = False
    pygame.display.flip()
pygame.quit()

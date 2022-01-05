import pygame, os, Button

#init
pygame.init()

#root
root = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
FPS = 60
WIDTH,HEIGHT = root.get_width(), root.get_height()

#fonts
header_font = pygame.font.SysFont("comicsans", 100, bold=True)
second_font = pygame.font.SysFont("comicsans", 70, bold=True)

#colours
BLACK = (0, 0, 0)

#variables
player1 = 1
f = [0, 0, 0, 0, 0, 0, 0, 0, 0]
w = WIDTH/5
h = HEIGHT/5

#images
background = pygame.transform.scale(pygame.image.load(os.path.join("Include", "background.png")), (WIDTH, HEIGHT))
exit_image = pygame.transform.scale(pygame.image.load(os.path.join("Include", "exit.png")), (70, 70))
cross_image = pygame.transform.scale(pygame.image.load(os.path.join("Include", "cross.png")), (w, h))
circle_image = pygame.transform.scale(pygame.image.load(os.path.join("Include", "cicle.png")), (w, h))
backgound_winner = pygame.transform.scale(pygame.image.load(os.path.join("Include", "background_winner.png")), (WIDTH, HEIGHT))


#widgets
EXIT_BUTTON = Button.Button(WIDTH-120, 50, exit_image, 1)
BORDER_1 = pygame.Rect(2 * w, 1 * h, 10, 3 * h)
BORDER_2 = pygame.Rect(3 * w, 1 * h, 10, 3 * h)
BORDER_3 = pygame.Rect(w, 2 * h, 3 * WIDTH / 5, 10)
BORDER_4 = pygame.Rect(w, 3 * h, 3 * w, 10)
B1 = pygame.Rect(w, h, w, h)
RESTART_TEXT = second_font.render("Restart game", True, BLACK)
RESTART_BUTTON = Button.Button(WIDTH/2-RESTART_TEXT.get_width()/2, 2*h, RESTART_TEXT, 1)
QUIT_TEXT = second_font.render("Quit game", True, BLACK)
QUIT_BUTTON = Button.Button(WIDTH/2-QUIT_TEXT.get_width()/2, 2.6*h, QUIT_TEXT, 1)


def show_window():
    root.blit(background, (0, 0))
    if EXIT_BUTTON.draw(root):
        quit()
    pygame.draw.rect(root, BLACK, BORDER_1)
    pygame.draw.rect(root, BLACK, BORDER_2)
    pygame.draw.rect(root, BLACK, BORDER_3)
    pygame.draw.rect(root, BLACK, BORDER_4)
    check_fields()
    check_won(player1)

    pygame.display.update()

def check_won(x):
    global f
    global player1
    if f[1]==f[2]==f[0]!=0 or f[4]==f[5]==f[3]!=0 or f[7]==f[8]==f[6]!=0 or f[1]==f[4]==f[7]!=0 or f[2]==f[5]==f[8]!=0 or f[0]==f[3]==f[6]!=0 or f[0]==f[4]==f[8]!=0 or f[2]==f[4]==f[6]!=0:
        root.blit(backgound_winner, (0, 0))
        winner = True
        if RESTART_BUTTON.draw(root):
            f = [0, 0, 0, 0, 0, 0, 0 , 0 ,0]
            player1 = 1
        if QUIT_BUTTON.draw(root):
                quit()
        if x:
            root.blit(header_font.render("Player 2 won", True, BLACK), (WIDTH/2 - 300, 1*h))
        else:
            root.blit(header_font.render("Player 1 won", True, BLACK), (WIDTH/2 - 300, h))
    elif 0 not in f:
        root.blit(backgound_winner, (0, 0))
        if RESTART_BUTTON.draw(root):
            f = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            player1 = 1
        if QUIT_BUTTON.draw(root):
            quit()
        root.blit(header_font.render("It's a draw", True, BLACK), (WIDTH / 2 - 300, 1 * h))

def check_fields():
    if f[0] == 1:
        root.blit(cross_image, (w, h))
    elif f[0] == 2:
        root.blit(circle_image, (w,h))
    if f[1] == 1:
        root.blit(cross_image, (2*w, h))
    elif f[1] == 2:
        root.blit(circle_image, (2*w,h))
    if f[2] == 1:
        root.blit(cross_image, (3*w, h))
    elif f[2] == 2:
        root.blit(circle_image, (3*w,h))
    if f[3] == 1:
        root.blit(cross_image, (w, 2*h))
    elif f[3] == 2:
        root.blit(circle_image, (w,2*h))
    if f[4] == 1:
        root.blit(cross_image, (2*w, 2*h))
    elif f[4] == 2:
        root.blit(circle_image, (2*w,2*h))
    if f[5] == 1:
        root.blit(cross_image, (3*w, 2*h))
    elif f[5] == 2:
        root.blit(circle_image, (3*w,2*h))
    if f[6] == 1:
        root.blit(cross_image, (w, 3*h))
    elif f[6] == 2:
        root.blit(circle_image, (w,3*h))
    if f[7] == 1:
        root.blit(cross_image, (2*w, 3*h))
    elif f[7] == 2:
        root.blit(circle_image, (2*w,3*h))
    if f[8] == 1:
        root.blit(cross_image, (3*w, 3*h))
    elif f[8] == 2:
        root.blit(circle_image, (3*w,3*h))


def check_button():
    global player1
    global f
    pos = pygame.mouse.get_pos()
    if pos[0]  >= w and pos[0] <= 2*w and pos[1] >= h and pos[1] <=2*h and f[0] == 0:
        if player1:
            f[0] = 1
            player1 = False
        else:
            f[0] = 2
            player1 = True
    if pos[0]  >= 2*w and pos[0] <= 3*w and pos[1] >= h and pos[1] <=2*h and f[1] == 0:
        if player1:
            f[1] = 1
            player1 = False
        else:
            f[1] = 2
            player1 = True
    if pos[0]  >= 3*w and pos[0] <= 4*w and pos[1] >= h and pos[1] <=2*h and f[2] == 0:
        if player1:
            f[2] = 1
            player1 = False
        else:
            f[2] = 2
            player1 = True
    if pos[0]  >= w and pos[0] <= 2*w and pos[1] >= 2*h and pos[1] <=3*h and f[3] == 0:
        if player1:
            f[3] = 1
            player1 = False
        else:
            f[3] = 2
            player1 = True
    if pos[0]  >= 2*w and pos[0] <= 3*w and pos[1] >= 2*h and pos[1] <=3*h and f[4] == 0:
        if player1:
            f[4] = 1
            player1 = False
        else:
            f[4] = 2
            player1 = True
    if pos[0]  >= 3*w and pos[0] <= 4*w and pos[1] >= 2*h and pos[1] <=3*h and f[5] == 0:
        if player1:
            f[5] = 1
            player1 = False
        else:
            f[5] = 2
            player1 = True
    if pos[0]  >= w and pos[0] <= 2*w and pos[1] >= 3*h and pos[1] <=4*h and f[6] == 0:
        if player1:
            f[6] = 1
            player1 = False
        else:
            f[6] = 2
            player1 = True
    if pos[0]  >= 2*w and pos[0] <= 3*w and pos[1] >= 3*h and pos[1] <=4*h and f[7] == 0:
        if player1:
            f[7] = 1
            player1 = False
        else:
            f[7] = 2
            player1 = True
    if pos[0]  >= 3*w and pos[0] <= 4*w and pos[1] >= 3*h and pos[1] <=4*h and f[8] == 0:
        if player1:
            f[8] = 1
            player1 = False
        else:
            f[8] = 2
            player1 = True

def quit():
    pygame.display.quit()
    exit()

def main():
    run = True
    while run:
        pygame.time.Clock().tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0]:
                check_button()
        show_window()
    quit()

if __name__ == "__main__":
    main()
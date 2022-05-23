import pygame
import pygame.freetype
import random
pygame.init()
pygame.freetype.init()

WIDTH, HEIGHT = 740, 540

BLOCK_SIZE = 20
game_height, game_width = 500 / 20, 700 / 20 


clock = pygame.time.Clock()

display = pygame.display.set_mode((740, 590))

timer = 0

pressed = pygame.key.get_pressed()
font = pygame.freetype.SysFont(None, 40)

score_font = pygame.freetype.SysFont(None, 30)

coors = [(random.randint(0, game_width - 1), random.randint(0, game_height - 1))]

apple = (random.randint(0, game_width - 1), random.randint(0, game_height - 1))

while apple == coors[0]:
    apple = (random.randint(0, game_width - 1), random.randint(0, game_height - 1))


display.fill((0, 51, 102))

pygame.draw.rect(display, (0, 0, 0), pygame.Rect(20, 20, 700, 500))

changed = False
# snake head

pygame.draw.rect(display, (0, 255, 0), pygame.Rect(20 + coors[0][0] * BLOCK_SIZE + 1, 20 + coors[0][1] * BLOCK_SIZE + 1, BLOCK_SIZE - 2, BLOCK_SIZE - 2))

# apple


pygame.draw.rect(display, (255, 0, 0), pygame.Rect(apple[0] * BLOCK_SIZE + 21, apple[1] * BLOCK_SIZE + 21, BLOCK_SIZE - 2, BLOCK_SIZE - 2))

pygame.display.update()

moving_direction = (0, 0)

game_lost = False

furled = 0

size = 1
update_score = True

done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and moving_direction != (-1, 0) and moving_direction != (1, 0):
                moving_direction = (1, 0)
                changed = True
                
            if event.key == pygame.K_LEFT and moving_direction != (1, 0) and moving_direction != (-1, 0):
                moving_direction = (-1, 0)
                changed = True
                
            if event.key == pygame.K_UP and moving_direction != (0, 1) and moving_direction != (0, -1):
                moving_direction = (0, -1)
                changed = True
                
            if event.key == pygame.K_DOWN and moving_direction != (0, -1) and moving_direction != (0, 1):
                moving_direction = (0, 1)
                changed = True
            pygame.mouse.set_visible(False)
        if event.type == pygame.MOUSEMOTION:
            pygame.mouse.set_visible(True)
    
    if moving_direction != (0, 0) and (changed or timer >= 100):
        pygame.draw.rect(display, (0, 255, 0), pygame.Rect(20 + (coors[0][0] + moving_direction[0]) * BLOCK_SIZE + 1, 20 + 1 + (coors[0][1] + moving_direction[1]) * BLOCK_SIZE, BLOCK_SIZE - 2, BLOCK_SIZE - 2))
        coors.insert(0, (coors[0][0] + moving_direction[0], coors[0][1] + moving_direction[1]))
        if furled == 0:
            pygame.draw.rect(display, (0, 0, 0), pygame.Rect(20 + coors[-1][0] * BLOCK_SIZE, 20 + coors[-1][1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        else:
            furled -= 1
        timer = 0
        coors.pop(-1)
        changed = False
        pygame.display.update()

    if coors[0] == apple:
        size += 4
        update_score = True
        furled += 4
        apple = (random.randint(0, game_width - 1), random.randint(0, game_height - 1))
        while apple in coors:
            apple = (random.randint(0, game_width - 1), random.randint(0, game_height - 1))
            
        for _ in range(4):
            coors.append(coors[-1])
        pygame.draw.rect(display, (255, 0, 0), pygame.Rect(apple[0] * BLOCK_SIZE + 21, apple[1] * BLOCK_SIZE + 21, BLOCK_SIZE - 2, BLOCK_SIZE - 2))
        
    for coor_index in range(1, len(coors) - furled):
        if coors[0] == coors[coor_index]:
            game_lost = True
            done = True

    if coors[0][0] < 0 or coors[0][0] >= game_width or coors[0][1] < 0 or coors[0][1] >= game_height:
        game_lost = True
        done = True
    
    timer += clock.get_time()

    if update_score is True:
        update_score = False
        pygame.draw.rect(display, (0, 51, 102), pygame.Rect(20, HEIGHT, 180, 50))
        score_rect = score_font.get_rect(f"Length: {size}")
        score_font.render_to(display, (100 - score_rect.width // 2, HEIGHT + 25 - score_rect.height // 2), f"Length: {size}")
        pygame.display.update()



if game_lost:
    pygame.draw.rect(display, (0, 0, 0), pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 - 40, 150, 80))

    
    pygame.draw.rect(display, (255, 255, 255), pygame.Rect(20 + coors[0][0] * BLOCK_SIZE + 1, 20 + coors[0][1] * BLOCK_SIZE + 1, BLOCK_SIZE - 2, BLOCK_SIZE - 2))


    
    font.fgcolor = (255, 255, 255)
    
    finished_length = font.get_rect("Length: {}".format(len(coors)))    
    game_over_text = font.get_rect("Game Over")

    font.render_to(display, (WIDTH // 2 - finished_length.width // 2, HEIGHT // 2 - finished_length.height // 2 - 25), "Length: {}".format(len(coors)))

    font.render_to(display, (WIDTH // 2 - game_over_text.width // 2, HEIGHT // 2 - finished_length.height // 2 + 25), "Game Over")
    
    pygame.display.update()


    
    ending = True



    
    while ending:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ending = False
                
            
            
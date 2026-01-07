import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600,400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Wooffie's Bones Adventure!")

level = 0
score = 0
checkpoint = 0
clock = pygame.time.Clock()

#color template
white = (255, 255, 255)
black = (0, 0, 0)
brown = (139,69,19)


wooffie_width, wooffie_height = 75, 80
wooffie_x = WIDTH // 2 - wooffie_width // 2
wooffie_y = HEIGHT - wooffie_height - 10
wooffie_speed = 6

bone_width = 32
bone_height = 21
bone_x = random.randint(0,WIDTH-bone_width)
bone_y = -bone_height
bone_speed = 4 + level*(score/10)

choco_width = 27
choco_height = 36
choco_x = random.randint(0,WIDTH-choco_width)
choco_y = -choco_height
choco_speed = 2 + level*(score/7)

wooffie_img = pygame.image.load ("wooffie.png")
wooffie_img = pygame.transform.scale (wooffie_img, (wooffie_width, wooffie_height))

bone_img = pygame.image.load ("bone.png")
bone_img = pygame.transform.scale(bone_img, (bone_width,bone_height))

choco_img = pygame.image.load("chocolate.png")
choco_img = pygame.transform.scale (choco_img, (choco_width, choco_height))

waffles_img = pygame.image.load("waffles.png")
waffles_img = pygame.transform.scale(waffles_img, (68,84))

font = pygame.font.SysFont(None, 36)

MENU = "menu"
PLAYING = "playing"
GAME_OVER = "game_over"
CONTINUE = "continue"
THE_END = "the_end"
STORY1 = "opening"
STORY2 = "story"
STORY3 = "story3"
RULE = "rule"
READY = "ready"
THE_END2 = "the_end2"

game_state = MENU



running = True
while running:
    clock.tick(60)
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_state == MENU:
                game_state = STORY1

            elif event.key == pygame.K_SPACE and game_state == STORY1:
                game_state = STORY2

            elif event.key == pygame.K_SPACE and game_state == STORY2:
                game_state = STORY3

            elif event.key == pygame.K_SPACE and game_state == STORY3:
                game_state = RULE
            
            elif event.key == pygame.K_SPACE and game_state == RULE:
                game_state = READY
            
            elif event.key == pygame.K_SPACE and game_state == READY:
                game_state = PLAYING
                level = 1

            elif event.key == pygame.K_SPACE and game_state == THE_END:
                game_state = THE_END2

            elif event.key == pygame.K_SPACE and game_state == THE_END2:
                running = False
                

            if game_state == GAME_OVER and event.key == pygame.K_r:
                score = checkpoint
                wooffie_x = WIDTH // 2 - wooffie_width // 2
                bone_y = -bone_height
                choco_y = -choco_height
                game_state = PLAYING 
            
            if game_state == CONTINUE and event.key == pygame.K_h:
                wooffie_x = WIDTH // 2 - wooffie_width // 2
                bone_y = -bone_height
                choco_y = -choco_height
                level += 1
                checkpoint = score
                game_state = PLAYING 

    if game_state == MENU:
        screen.fill((222,184,135))
        tittle = font.render("Wooffie the Bone Collector", True, (139,69,19))
        start = font.render ("Press SPACE to start!", True, (139,69,19))
        screen.blit (tittle, (120,150))
        screen.blit (start, (160, 220))
    
    if game_state == STORY1:
        screen.fill ((255,235,205))
        intro_text = font.render ("Hi, I'm Wooffie!", True, (139,69,19))
        intro2 = font.render ("I like to giving gift to my friends", True, brown )
        skip = font.render ("click SPACE to continue", True, (210,180,140))
        screen.blit (intro_text, (140, 150))
        screen.blit (intro2, (140, 180) )
        screen.blit (wooffie_img, (20 , HEIGHT // 2 - wooffie_height))
        screen.blit (skip, (140, 260))

    if game_state == STORY2:
        screen.fill ((255,235,205))
        intro_text = font.render ("This is one of my friend, Waffles", True, (139,69,19))
        intro2 = font.render ("Today is his birthday", True, brown )
        gift = font.render ("I want to give him many bones as a special gift!", True, brown)
        skip = font.render ("click SPACE to continue", True, (210,180,140))
        screen.blit (intro_text, (40, 110))
        screen.blit (intro2, (40, 150) )
        screen.blit (gift, (20, 210))
        screen.blit (skip, (120, 270))
        screen.blit (waffles_img, (WIDTH - 130, HEIGHT // 2 - wooffie_height - 10))

    if game_state == STORY3:
            screen.fill ((255,235,205))
            intro_text = font.render ("Help me to collect the bones!", True, (139,69,19))
            skip = font.render ("click SPACE to continue", True, (210,180,140))
            screen.blit (intro_text, (120, 100))
            screen.blit (wooffie_img, (WIDTH / 2 - wooffie_width + 20, HEIGHT - wooffie_height - 150))
            screen.blit (skip, (160, HEIGHT - 90))

    if game_state == RULE:
            screen.fill ((255,235,205))
            intro_text = font.render ("Catch the Bones and avoid the Chocolates", True, (139,69,19))
            skip = font.render ("click SPACE to continue", True, (210,180,140))
            screen.blit (intro_text, (55, 100))
            screen.blit (wooffie_img, (WIDTH / 2 - wooffie_width + 20, HEIGHT - wooffie_height - 150))
            screen.blit (skip, (160, HEIGHT - 90))
            screen.blit (bone_img, (110, HEIGHT - wooffie_height - 100))
            screen.blit (choco_img, (WIDTH - 140, HEIGHT - wooffie_height - 100))
    
    if game_state == READY:
            screen.fill ((255,235,205))
            intro_text = font.render ("READY?", True, (139,69,19))
            skip = font.render ("click SPACE to start", True, (210,180,140))
            screen.blit (intro_text, (250, 100))
            screen.blit (wooffie_img, (WIDTH / 2 - wooffie_width + 20, HEIGHT - wooffie_height - 150))
            screen.blit (skip, (160, HEIGHT - 90))
        

    elif game_state == PLAYING:
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and wooffie_x > 0:
            wooffie_x -= wooffie_speed

        if keys[pygame.K_RIGHT] and wooffie_x < WIDTH - wooffie_width:
            wooffie_x += wooffie_speed

        bone_y += bone_speed
        if bone_y > HEIGHT:
            bone_y = -bone_height
            bone_x = random.randint(0,WIDTH-bone_width)

        choco_y += choco_speed
        if choco_y > HEIGHT:
            choco_y = -choco_height
            choco_x = random.randint(0,WIDTH-choco_width)

        dog_rect = pygame.Rect (wooffie_x, wooffie_y, wooffie_width, wooffie_height)
        bone_rect = pygame.Rect (bone_x, bone_y, bone_width, bone_height)
        choco_rect = pygame.Rect (choco_x, choco_y, choco_width, choco_height)

        if dog_rect.colliderect(bone_rect):
            score += 1
            bone_y = -bone_height
            bone_x = random.randint(0,WIDTH-bone_width)
        
        if dog_rect.colliderect(choco_rect):
            game_state = GAME_OVER
        
        screen.blit(wooffie_img, dog_rect)
        screen.blit(bone_img, bone_rect)
        screen.blit(choco_img, choco_rect)
            
        score_text = font.render (f"Your scores: {score}", True, black)
        screen.blit (score_text, (10,10))

        if score == 15*level and score > 0:
            game_state = CONTINUE
        
        if score == 45:
            game_state = THE_END

    if game_state == CONTINUE:
        screen.fill(((255,235,205)))

        achievement_text = font.render(f"Yeay! We've collected {score} bones!", True, brown)
        happy_text = font.render ("but I want to give more...", True, brown)
        continue_text = font.render ("press H to help Wooffie!", True, brown)

        achievement_rect = achievement_text.get_rect(center=(WIDTH // 2, 150))
        happy_rect = happy_text.get_rect(center=(WIDTH // 2, 200))
        continue_rect = continue_text.get_rect(center=(WIDTH // 2, 250))


        screen.blit(achievement_text, achievement_rect)
        screen.blit (happy_text, happy_rect)
        screen.blit(continue_text, continue_rect)
        screen.blit(wooffie_img, dog_rect)


    if game_state == GAME_OVER:
        screen.fill((230,230,250))

        game_over_text = font.render ("I'm not feeling well...", True, (112,128,144))
        score_text = font.render (f"Bones collected: {score}", True, (112,128,144))
        restart_text = font.render ("Press R to try again", True, (112,128,144))

        screen.blit(game_over_text, (170,140))
        screen.blit (score_text, (180,190))
        screen.blit(restart_text, (175,240))


    if game_state == THE_END2:
        screen.fill ((255,235,205))
        intro_text = font.render ("Waffles must be like it", True, (139,69,19))
        happy = font.render ("I'm going to give it to him", True, (139,69,19))
        skip = font.render ("click SPACE to quit", True, (210,180,140))
        bye = font.render ("Bye byee ~", True, (139,69,19))
        screen.blit (intro_text, (160, 90))
        screen.blit (happy, (140, 120))
        screen.blit (bye, (200, HEIGHT - 110 ))
        screen.blit (wooffie_img, (WIDTH / 2 - wooffie_width + 20, HEIGHT - wooffie_height - 150))
        screen.blit (skip, (170, HEIGHT - 60))

    if game_state == THE_END:
        screen.fill ((255,235,205))
        intro_text = font.render ("We did it! 45 bones!", True, (139,69,19))
        happy = font.render ("Thanks for helping me!", True, (139,69,19))
        skip = font.render ("click SPACE to continue", True, (210,180,140))
        screen.blit (intro_text, (170, 100))
        screen.blit (happy, (160, 130))
        screen.blit (wooffie_img, (WIDTH / 2 - wooffie_width + 20, HEIGHT - wooffie_height - 150))
        screen.blit (skip, (160, HEIGHT - 90))
       
    
    pygame.display.update()

pygame.quit()
sys.exit()

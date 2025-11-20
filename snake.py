import pygame
import random
import sys

pygame.init()

width = 600
height = 600
snake_size = 20
FPS = 10

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
white = (255,255,255)

font = pygame.font.SysFont("Arial", 20)

#Snake body
def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, green,(x,y,snake_size, snake_size))

#Food generation
def generate_food(snake_list):
    while True:
        x = random.randrange(0,width,snake_size)
        y = random.randrange(0,height, snake_size)

        #Checking food for not appearing on the snake
        if (x,y) not in snake_list:
            return x,y
        

def main():
    global FPS

    #Snake parameters
    snake_x = width // 2
    snake_y = height // 2
    snake_list = [(snake_x, snake_y)]
    snake_length = 1

    dx = 0
    dy = 0

    score = 0
    level = 1
    foods_to_next_level = 4 #Level up

    food_x, food_y = generate_food(snake_list)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #To control
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT  and dx == 0:
                    dx = -snake_size
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = snake_size 
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -snake_size
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = snake_size

        #Update position
        snake_x += dx
        snake_y += dy

        #Collision check
        if snake_x < 0 or snake_x >= width or snake_y < 0 or snake_y >= height:
            #Game over if snake go out of borders
            pygame.quit()
            sys.exit()

        snake_list.append((snake_x, snake_y))
        if len(snake_list) > snake_length:
            snake_list.pop(0)


        if (snake_x, snake_y) in snake_list[:-1]:
            pygame.quit()
            sys.exit()

        #Eating
        if snake_x == food_x and snake_y == food_y:
            score += 1
            snake_length += 1

            food_x, food_y = generate_food(snake_list)

            if score % foods_to_next_level == 0:
                level += 1
                FPS += 2

        screen.fill(black)

        pygame.draw.rect(screen, red, (food_x, food_y, snake_size, snake_size))
        draw_snake(snake_list)

        score_text = font.render(f"Score: {score}", True, white)
        level_text = font.render(f"Level: {level}", True, white)
        screen.blit(score_text, (10,10))
        screen.blit(level_text, (500,1))

        pygame.display.update()
        clock.tick(FPS)

main()
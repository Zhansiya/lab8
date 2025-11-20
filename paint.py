import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

radius = 10
color = (0, 0, 255)
tool = "brush"
start_pos = None
drawing = False

def draw_rectangle(screen, start, end, color, width = 2):
    x1, y1 = start
    x2, y2 = end
    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(screen, color, rect, width)

def draw_circle(screen, start, end, color, width = 2):
    x1, y1 = start
    x2, y2 = end
    radius = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
    pygame.draw.circle(screen, color, start, radius, width)

def main():
    global color, radius, tool, start_pos, drawing

    canvas = pygame.Surface(screen.get_size())
    canvas.fill((0,0,0))

    while True:
        screen.blit(canvas, (0,0))
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    tool = "brush"
                elif event.key == pygame.K_2:
                    tool = "rect"
                elif event.key == pygame.K_3:
                    tool = "circle"
                elif event.key == pygame.K_4:
                    tool = "eraseer"

                elif event.key == pygame.K_r:
                    color = (255,0,0)
                elif event.key == pygame.K_g:
                    color = (0,255,0)
                elif event.key == pygame.K_b:
                    color = (0,0,255)
                elif event.key == pygame.K_w:
                    color = (255,255,255)
                elif event.key == pygame.K_k:
                    color = (0,0,0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                if tool == "rect":
                    draw_rectangle(canvas, start_pos, event.pos, color, 3)
                elif tool == "circle":
                    draw_circle(canvas, start_pos, event.pos, color, 3)
                drawing = False

        if drawing:
            if tool == "brush":
                pygame.draw.circle(canvas, color, mouse, radius)
            elif tool == "eraser":
                pygame.draw.circle(canvas, (0,0,0), mouse, radius)

        if drawing and tool in ["rect", "circle"]:
            temp = canvas.copy()
            if tool == "rect":
                draw_rectangle(temp, start_pos, mouse, color, 2)
            elif tool == "circle":
                draw_circle(temp, start_pos, mouse, color, 2)
            screen.blit(temp, (0,0))

        show_text = pygame.font.SysFont("Arial", 20).render(f"Tool: {tool.upper()} | Press 1-Brush 2-Rect 3-Circle 4-Eraser | Colors: R,G,B,W,K", True, (255,255,255))
        screen.blit(show_text, (10,10))

        pygame.display.update()
        clock.tick(60)

main()
import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Balls")

# Warna
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (128, 0, 128)]
black = (0, 0, 0)
white = (255, 255, 255)

# Kelas Bola
class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = random.choice([-5, 5])
        self.dy = random.choice([-5, 5])

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # Pantulan dinding
        if self.x - self.radius < 0 or self.x + self.radius > screen_width:
            self.dx = -self.dx
        if self.y - self.radius < 0 or self.y + self.radius > screen_height:
            self.dy = -self.dy

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Membuat bola
balls = [Ball(random.randint(50, screen_width-50), random.randint(50, screen_height-50), 20, colors[i]) for i in range(5)]
purple_ball = Ball(screen_width//2, screen_height//2, 20, colors[5])
balls.append(purple_ball)

# Fungsi untuk menampilkan teks
font = pygame.font.SysFont(None, 36)
hit_count = 0

def display_text(text, x, y):
    img = font.render(text, True, white)
    screen.blit(img, (x, y))

# Main loop
running = True
purple_ball_mode = "bounce"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                purple_ball.dx = -10
                purple_ball.dy = 0
            if event.key == pygame.K_RIGHT:
                purple_ball.dx = 10
                purple_ball.dy = 0
            if event.key == pygame.K_UP:
                purple_ball.dx = 0
                purple_ball.dy = -10
            if event.key == pygame.K_DOWN:
                purple_ball.dx = 0
                purple_ball.dy = 10
            if event.key == pygame.K_SPACE:
                purple_ball_mode = "stop" if purple_ball_mode == "bounce" else "bounce"

    screen.fill(black)
    pygame.draw.rect(screen, white, (0, 0, screen_width, screen_height), 5)

    for ball in balls:
        ball.move()
        ball.draw()

    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            if (balls[i].x - balls[j].x)**2 + (balls[i].y - balls[j].y)**2 < (balls[i].radius + balls[j].radius)**2:
                balls[i].dx, balls[j].dx = balls[j].dx, balls[i].dx
                balls[i].dy, balls[j].dy = balls[j].dy, balls[i].dy
                if balls[i] == purple_ball or balls[j] == purple_ball:
                    hit_count += 1
                if purple_ball_mode == "stop":
                    purple_ball.dx, purple_ball.dy = 0, 0

    display_text(f'Score: {hit_count}', 10, 10)

    pygame.display.flip()
    pygame.time.delay(20)

pygame.quit()




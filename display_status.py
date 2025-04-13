import pygame
import requests
import time

# Settings
SERVER_URL = "http://localhost:5000/status"
POLL_INTERVAL = 5 # seconds

# Colors
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)

# Setup the screen
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Status Display")
clock = pygame.time.Clock()

# Setup the font
pygame.font.init()
font = pygame.font.SysFont("Arial", 100)  # (family, size)

def draw_text(text, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center = (screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text_surface, text_rect)

def show_red_screen():
    screen.fill((255, 0, 0))
    draw_text("IN MEETING!", WHITE)
    pygame.display.flip()

def show_green_screen():
    screen.fill((0, 255, 0))
    draw_text("FREE!", BLACK)
    pygame.display.flip()

# Main Loop
try:
    while True:
        try:
            response = requests.get(SERVER_URL)
            if response.status_code == 200:
                status = response.json()
                if status.get("inMeeting"):
                    show_red_screen()
                else:
                    show_green_screen()
        except requests.RequestException:
            print("Failed to talk to Flask Server!")

        # Handle Quit Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()

        time.sleep(POLL_INTERVAL)
        clock.tick(60)

except KeyboardInterrupt:
    pygame.quit()

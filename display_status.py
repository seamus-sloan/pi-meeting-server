import pygame
import requests
import threading

# Settings
SERVER_URL = "http://localhost:5000/status"
POLL_INTERVAL = 5 # seconds
current_status = None

# Colors
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)

# Setup the screen
pygame.init()
window_size = (800, 600)  # Width, Height
screen = pygame.display.set_mode(window_size)
# screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Status Display")
clock = pygame.time.Clock()

# Setup the font
pygame.font.init()
font_large = pygame.font.SysFont("Arial", 100)
font_small = pygame.font.SysFont("Arial", 36)

def draw_text(text, color):
    text_surface = font_large.render(text, True, color)
    text_rect = text_surface.get_rect(center = (screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text_surface, text_rect)

def show_header(status):
    lines = [
        f"{'VIDEO ON' if status.get('videoOn') else 'VIDEO OFF'}"
        f"{'DRONE ON' if status.get('droneOn') else 'DRONE OFF'}"
    ]

    for i, line in enumerate(lines):
        text_surface = font_small.render(line, True, WHITE)
        text_rect = text_surface.get_rect(center = (screen.get_width() / 2, 200 + i * 40))
        screen.blit(text_surface, text_rect)

def show_red_screen(status):
    screen.fill((255, 0, 0))
    draw_text("IN MEETING!", WHITE)
    show_header(status)
    pygame.display.flip()

def show_green_screen(status):
    screen.fill((0, 255, 0))
    draw_text("FREE!", BLACK)
    show_header(status)
    pygame.display.flip()

def fetch_status():
    global current_status
    while True:
        try:
            response = requests.get(SERVER_URL)
            if response.status_code == 200:
                current_status = response.json()
        except requests.RequestException:
            print("Failed to talk to Flask Server!")

        pygame.time.wait(POLL_INTERVAL * 1000) # Wait before next request...

# Fetch status in separate thread
status_thread = threading.Thread(target=fetch_status)
status_thread.daemon = True
status_thread.start()

# Main Loop
try:
    while True:
        if current_status:
            if current_status.get("inMeeting"):
               show_red_screen(current_status)
            else:
                show_green_screen(current_status)


        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()

        # Control the frame rate (higher frame rate for smoother performance)
        clock.tick(30)  # 30 FPS for smoother graphics

except KeyboardInterrupt:
    pygame.quit()
import os
import pygame
import requests
import threading

DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# Settings
SERVER_URL = "http://localhost:5000/status"
POLL_INTERVAL = 5 # seconds
current_status = {
    "droneOn": False,
    "inMeeting": False,
    "videoOn": False
}

# Colors
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# See fetch_status
running = True

# Setup the screen
pygame.init()
if DEBUG:
    window_size = (800, 600)  # Width, Height
    screen = pygame.display.set_mode(window_size)
else:
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

pygame.display.set_caption("Status Display")
clock = pygame.time.Clock()

# Setup the fonts
font_large = pygame.font.SysFont("Arial", 100)
font_small = pygame.font.SysFont("Arial", 36)


def center_surface(surface, x_offset = 0, y_offset = 0):
    return surface.get_rect(center = (
        screen.get_width() / 2 + x_offset, 
        screen.get_height() / 2 + y_offset))

def draw_large_text(text, color):
    text_surface = font_large.render(text, True, color)
    text_rect = center_surface(text_surface)
    screen.blit(text_surface, text_rect)

def draw_small_text(text, y_offset):
    text_surface = font_small.render(text, True, BLACK)
    text_rect = center_surface(text_surface, 0, y_offset)
    screen.blit(text_surface, text_rect)

def show_status(status):
    in_meeting = status.get("inMeeting")
    if in_meeting:
        screen.fill(RED)
        draw_large_text("IN MEETING", WHITE)
    else:
        screen.fill(GREEN)
        draw_large_text("FREE", BLACK)
    
    video_status = status.get('videoOn')
    video_text = "VIDEO ON" if video_status else "VIDEO OFF"
    draw_small_text(video_text, 100)

    drone_status = status.get('droneOn')
    drone_text = "DRONE ON" if drone_status else "DRONE OFF"
    draw_small_text(drone_text, 140)

    pygame.display.flip()

def fetch_status():
    global current_status
    while running:
        try:
            response = requests.get(SERVER_URL)
            if response.status_code == 200:
                current_status = response.json()
        except requests.RequestException as e:
            print(f"Request failed: {e}")

        pygame.time.wait(POLL_INTERVAL * 1000) # Wait before next request...



# Fetch status in separate thread
status_thread = threading.Thread(target=fetch_status)
status_thread.daemon = True
status_thread.start()



# Main Loop
try:
    while True:
        show_status(current_status)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()

        # Control the frame rate (higher frame rate for smoother performance)
        clock.tick(30)  # 30 FPS for smoother graphics

except KeyboardInterrupt:
    running = False
    pygame.quit()
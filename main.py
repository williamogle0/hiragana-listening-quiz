import os
import random
import pygame
from pygame.locals import K_SPACE, QUIT, K_RETURN

# Initialize pygame mixer and pygame
pygame.mixer.init()
pygame.init()

# Set up the screen (needed to capture events)
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Random Sound Player')

# Path to the folder with .mp3 files
sounds_folder = "sounds"

currentSound = ""

# Function to play a random mp3 file
def play_random_sound():
    # Get list of .mp3 files in the folder
    mp3_files = [f for f in os.listdir(sounds_folder) if f.endswith('.mp3')]
    
    if mp3_files:
        # Choose a random file and play it
        random_file = random.choice(mp3_files)
        currentSound = random_file
        file_path = os.path.join(sounds_folder, random_file)
        print(f"Playing: {random_file}")
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

def replay_sound():
    pygame.mixer.music.play()

# Play the first random sound
play_random_sound()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == K_SPACE:
            # Play a new random sound when the spacebar is pressed
            play_random_sound()
        elif event.type == pygame.KEYDOWN and event.key == K_RETURN:
            replay_sound()
            

# Quit pygame when done
pygame.quit()

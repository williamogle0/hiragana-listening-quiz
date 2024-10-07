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

currentSoundPath = ""

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

X = 400
Y = 300

font = pygame.font.Font('freesansbold.ttf', 32)
display_surface = pygame.display.set_mode((X, Y))
text = font.render('GeeksForGeeks', True, green, blue)
# create a rectangular object for the
# text surface object
textRect = text.get_rect()
 
# set the center of the rectangular object.
textRect.center = (X // 2, Y // 2)

# Function to play a random mp3 file
def play_random_sound():
    # Get list of .mp3 files in the folder
    mp3_files = [f for f in os.listdir(sounds_folder) if f.endswith('.mp3')]
    
    if mp3_files:
        # Choose a random file and play it
        random_file = random.choice(mp3_files)
        file_path = os.path.join(sounds_folder, random_file)
        print(random_file)
        currentSoundPath = random_file
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
    # print(currentSoundPath)
    text = font.render(currentSoundPath, True, green, blue)
    # text = font.render('GeeksForGeeks', True, green, blue)
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
    
    # set the center of the rectangular object.
    textRect.center = (X // 2, Y // 2)
    display_surface.fill(white)
    display_surface.blit(text, textRect)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == K_SPACE:
            # Play a new random sound when the spacebar is pressed
            play_random_sound()
        elif event.type == pygame.KEYDOWN and event.key == K_RETURN:
            replay_sound()
        pygame.display.update()
            

# Quit pygame when done
pygame.quit()

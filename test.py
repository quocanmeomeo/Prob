import pygame
import time
import pygame_textinput

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Input Text Box Example")
# Use a font that supports Vietnamese characters
font = pygame.font.Font('TH Grisly Beast.ttf', 32)  # Replace with the path to your font
clock = pygame.time.Clock()

# Define colors
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
COLOR_TEXT = pygame.Color('black')
BACKGROUND_COLOR = pygame.Color('white')

# Text box rectangle
input_box = pygame.Rect(300, 200, 200, 32)
color = COLOR_INACTIVE

# Variables to manage input
active = False
text = ''
total_spending = ''
cursor_visible = True
last_blink_time = time.time()

# Dummy function for restart_game()
def restart_game():
    print("Game restarted!")

# Initialize text input object
textinput = pygame_textinput.TextInputVisualizer()
textinput.font_object = font

running = True
while running:
    screen.fill(BACKGROUND_COLOR)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the click is inside the input box
            if input_box.collidepoint(event.pos):
                active = not active
                textinput.value = '' if active else text  # Clear text if activating the input box
            else:
                active = False
            color = COLOR_ACTIVE if active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if active and event.key == pygame.K_RETURN:
                total_spending = textinput.value
                textinput.value = ''
                restart_game()

    # Handle cursor blinking
    if time.time() - last_blink_time > 0.5:  # Change cursor visibility every 0.5 seconds
        cursor_visible = not cursor_visible
        last_blink_time = time.time()

    # Update and draw the text input
    if active:
        textinput.update(events)
        screen.blit(textinput.surface, (input_box.x + 5, input_box.y + 5))

    # Render the current text.
    else:
        txt_surface = font.render('Your name', True, COLOR_TEXT)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

    pygame.draw.rect(screen, color, input_box, 2)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

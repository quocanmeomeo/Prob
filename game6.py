import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 3090
SCREEN_HEIGHT = 1600
CARD_RATIO = (int(250.1 * 1.5), int(416.8 * 1.5))  # Increased size by 1.5
PACK_RATIO = (274.7*1.5, 121.4*1.5)
BG_IMAGE = 'BG.png'
TITLE_IMAGE = 'Title.png'
CARD_IMAGES = ['card0.png', 'card1.png', 'card2.png', 'card3.png', 'card4.png', 'card5.png']
PACK_IMAGES = ['Pack1.png', 'Pack3.png', 'Pack5.png']
PACK_PRICES = [10, 25, 40]
TARGET_SPENDING = 115
VOUCHER_IMAGE = 'voucher.png'
VOUCHER_IMAGES_B = ['b1.png', 'b2.png', 'b3.png', 'b4.png', 'b5.png']
VOUCHER_IMAGES_C = ['c1.png', 'c2.png', 'c3.png', 'c4.png', 'c5.png']
WIN = 'win.png'
LOSE = 'lose.png'
REPLAY = 'replay.png'

# Colors
WHITE = (255, 255, 255)
BLACK = (68, 40, 29)
GRAY = (200, 200, 200)
TRANSPARENT = (0, 0, 0, 0)

# Load images
bg_image = pygame.image.load(BG_IMAGE)
title_image = pygame.image.load(TITLE_IMAGE)
card_images = [pygame.image.load(img) for img in CARD_IMAGES]
pack_images = [pygame.image.load(img) for img in PACK_IMAGES]
voucher_image = pygame.image.load(VOUCHER_IMAGE)
voucher_images_b = [pygame.image.load(img) for img in VOUCHER_IMAGES_B]
voucher_images_c = [pygame.image.load(img) for img in VOUCHER_IMAGES_C]
win_image = pygame.image.load(WIN)
lose_image = pygame.image.load(LOSE)
replay_image = pygame.image.load(REPLAY)

# Scale images
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
title_image = pygame.transform.scale(title_image, (401.6*1.5, 121.4*1.5))
card_images = [pygame.transform.scale(img, CARD_RATIO) for img in card_images]
pack_images = [pygame.transform.scale(img, PACK_RATIO) for img in pack_images]
voucher_image = pygame.transform.scale(voucher_image, (540, 1240))
voucher_images_b = [pygame.transform.scale(img, (268.2*2*1.2, 121.1*2*1.2)) for img in voucher_images_b]
voucher_images_c = [pygame.transform.scale(img, (268.2*2*1.2, 121.1*2*1.2)) for img in voucher_images_c]
win_image = pygame.transform.scale(win_image, (274.9*2.7, 247.6*2.7))
lose_image = pygame.transform.scale(lose_image, (274.9*2.7, 247.6*2.7))
replay_image = pygame.transform.scale(replay_image, (334*1.5, 121.5*1.5))

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Kitty Gacha")

# Card counters
card_counters = [0, 0, 0, 0, 0]

# Spending
total_spending = 0

# Previous game
game_data = []
mean_spending = 0
sum_spending = 0

# Font
FONT_PATH = 'TH Grisly Beast.ttf'  # Path to the font file
font = pygame.font.Font(FONT_PATH, 37)

# Calculate new pack positions
pack1_x = 150 + int(1 * 300 * 1.5) - PACK_RATIO[0]// 2 - 115
pack3_x = 150 + int(2.5 * 300 * 1.5) - PACK_RATIO[0] // 2 - 115
pack5_x = 150 + int(4 * 300 * 1.5) - PACK_RATIO[0] // 2 - 115
pack_y = 800 + int(CARD_RATIO[1] * 0.3) +100

# Variables to manage card slots and timing
slots = [None, None, None, None, None]
displayed_cards = False
start_time = None
flip_start_time = None
flip_duration = 0.5  # Reduced flip duration to 0.5 seconds
transitioning = False



# Text box colors
COLOR_INACTIVE = BLACK
COLOR_ACTIVE = BLACK
COLOR_TEXT = BLACK
BACKGROUND_COLOR = WHITE

# Input box rectangle
input_box = pygame.Rect(1350, 1019.1 + 200, 300, 50)
color = COLOR_INACTIVE

# Variables to manage input
input_active = False
input_text = 'Your name'
cursor_visible = True
last_blink_time = time.time()

def draw_interface():
    screen.blit(bg_image, (0, 0))
    screen.blit(title_image, (0, 0))

    # Draw spending bar
    bar_length = pack5_x + CARD_RATIO[0] + 200
    pygame.draw.rect(screen, BLACK, (50, 150, bar_length, 60), 2)
    spending_bar_length = min(bar_length, int(bar_length * total_spending / TARGET_SPENDING))
    pygame.draw.rect(screen, (150, 75, 0), (50, 150, spending_bar_length, 60))

    # Draw spending text
    spending_text = font.render(f"Total spending: {total_spending}", True, BLACK)
    mean_text = font.render(f"Mean spending: {mean_spending}", True, BLACK)
    target_text = font.render(f"Target spending: {TARGET_SPENDING}", True, BLACK)
    screen.blit(spending_text, (50, 240))
    screen.blit(target_text, (bar_length - 350, 240))
    if (mean_spending <10):
        screen.blit(mean_text, (((bar_length - 350 - 50) / 2) + 90, 240))
    elif (mean_spending <100):
        screen.blit(mean_text, (((bar_length - 350 - 50) / 2) + 80, 240))
    else:
        screen.blit(mean_text, (((bar_length - 350 - 50) / 2) + 75, 240))

    # Draw card slots only if cards are selected
    for i in range(5):
        if slots[i] is not None:
            card_x = 150 + int(i * 300 * 1.5) -70
            card_y = 350
            draw_flip_animation(screen, card_x, card_y, slots[i])

    # Check win/lose condition
    game_over = all(c > 0 for c in card_counters)

    if not game_over:
        # Draw packs
        screen.blit(pack_images[0], (pack1_x, pack_y))
        screen.blit(pack_images[1], (pack3_x, pack_y))
        screen.blit(pack_images[2], (pack5_x, pack_y))

        # Draw pack prices
        price_text1 = font.render(f"Price {PACK_PRICES[0]}", True, BLACK)
        price_text_rect1 = price_text1.get_rect(center=(pack1_x + PACK_RATIO[0] // 2, pack_y + PACK_RATIO[1] + 40))
        screen.blit(price_text1, price_text_rect1.topleft)

        price_text2 = font.render(f"Price {PACK_PRICES[1]}", True, BLACK)
        price_text_rect2 = price_text2.get_rect(center=(pack3_x + PACK_RATIO[0] // 2, pack_y + PACK_RATIO[1] + 40))
        screen.blit(price_text2, price_text_rect2.topleft)

        price_text3 = font.render(f"Price {PACK_PRICES[2]}", True, BLACK)
        price_text_rect3 = price_text3.get_rect(center=(pack5_x + PACK_RATIO[0] // 2, pack_y + PACK_RATIO[1] + 40))
        screen.blit(price_text3, price_text_rect3.topleft)

    # Draw voucher images and move counters next to them
    voucher_y = (SCREEN_HEIGHT - 1240*1.2) // 2
    voucher_positions = [
        (2350, voucher_y + 0 * 248*1.2),
        (2350, voucher_y + 1 * 248*1.2 - 9),
        (2350, voucher_y + 2 * 248*1.2 - 19),
        (2350, voucher_y + 3 * 248*1.2 - 28),
        (2350, voucher_y + 4 * 248*1.2 - 36)
    ]
    for i, pos in enumerate(voucher_positions):
        voucher_img = voucher_images_b[i] if card_counters[i] == 0 else voucher_images_c[i]
        screen.blit(voucher_img, pos)
        if card_counters[i] > 0:
            counter_text = font.render(str(card_counters[i]), True, BLACK)
            counter_text_rect = counter_text.get_rect(
                center=(pos[0] + voucher_img.get_width() + 40, pos[1] + voucher_img.get_height() // 2))
            screen.blit(counter_text, counter_text_rect.topleft)

    if game_over:
        if total_spending <= TARGET_SPENDING:
            screen.blit(win_image, (((150 + int(1 * 300 * 1.5) -70) - (150 + int(0 * 300 * 1.5) -70))/2, 925))
        else:
            screen.blit(lose_image, (((150 + int(1 * 300 * 1.5) -70) - (150 + int(0 * 300 * 1.5) -70))/2, 925))

        # Draw input box
        pygame.draw.rect(screen, BACKGROUND_COLOR, input_box)
        text_surface = font.render(input_text, True, BLACK)
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        # Draw the cursor if the input box is active and the cursor is visible
        if input_active and cursor_visible:
            cursor_x = input_box.x + 5 + text_surface.get_width()
            cursor_y = input_box.y + 5
            cursor_height = text_surface.get_height()
            pygame.draw.line(screen, COLOR_TEXT, (cursor_x, cursor_y), (cursor_x, cursor_y + cursor_height), 2)

        # Draw replay image
        screen.blit(replay_image, (1350, 1069.1 + 250))



def handle_pack_selection(pack_index):
    global total_spending, displayed_cards, start_time, slots, flip_start_time, transitioning
    if not transitioning:  # Prevent interaction during transition
        total_spending += PACK_PRICES[pack_index]
        repeat_count = [1, 3, 5][pack_index]
        slots = [None] * 5  # Reset the slots

        # Display placeholders
        for i in range(repeat_count):
            slots[2 - repeat_count // 2 + i] = 0  # Aligning the middle slot

        displayed_cards = True
        start_time = time.time()
        flip_start_time = None
        transitioning = True

def update_slots():
    global displayed_cards, slots, flip_start_time, transitioning
    if displayed_cards and time.time() - start_time >= 1:  # Reduced wait time to 1 second
        for i in range(5):
            if slots[i] == 0:
                slots[i] = random.randint(1, 5)
                card_counters[slots[i] - 1] += 1
        displayed_cards = False
        flip_start_time = time.time()

    # End the transition after flip duration
    if flip_start_time and time.time() - flip_start_time >= flip_duration:
        transitioning = False

def draw_flip_animation(screen, x, y, card_index):
    global flip_start_time
    if flip_start_time:
        elapsed_time = time.time() - flip_start_time
        if elapsed_time < flip_duration:
            scale = abs((elapsed_time / flip_duration) * 2 - 1)
            if scale > 0.5:
                card_image = pygame.transform.scale(card_images[card_index], (int(CARD_RATIO[0] * (1 - scale)), CARD_RATIO[1]))
            else:
                card_image = pygame.transform.scale(card_images[0], (int(CARD_RATIO[0] * scale), CARD_RATIO[1]))
            screen.blit(card_image, (x + (CARD_RATIO[0] - card_image.get_width()) // 2, y))
        else:
            screen.blit(card_images[card_index], (x, y))
    else:
        screen.blit(card_images[card_index], (x, y))

def restart_game():
    global total_spending, card_counters, slots, displayed_cards, start_time, flip_start_time, transitioning, \
        mean_spending,game_data, sum_spending

    for i in range (len(game_data)):
        sum_spending += game_data[i][1]
    mean_spending = int(sum_spending/len(game_data))
    # Resetting game variables
    total_spending = 0
    card_counters = [0, 0, 0, 0, 0]
    slots = [None] * 5
    displayed_cards = False
    start_time = None
    flip_start_time = None
    transitioning = False

# Main loop
running = True
game_over_displayed = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                input_active = not input_active
                if input_active:
                    input_text = ''
            else:
                input_active = False
                input_text = 'Your name'
            color = COLOR_ACTIVE if input_active else COLOR_INACTIVE
            mouse_x, mouse_y = event.pos
            # Check for pack selection
            if pack1_x <= mouse_x <= pack1_x + PACK_RATIO[0] and pack_y <= mouse_y <= pack_y + PACK_RATIO[1] and (0 in card_counters):
                handle_pack_selection(0)
            elif pack3_x <= mouse_x <= pack3_x + PACK_RATIO[0] and pack_y <= mouse_y <= pack_y + PACK_RATIO[1] and (0 in card_counters):
                handle_pack_selection(1)
            elif pack5_x <= mouse_x <= pack5_x + PACK_RATIO[0] and pack_y <= mouse_y <= pack_y + PACK_RATIO[1] and (0 in card_counters):
                handle_pack_selection(2)
            # Check for replay button click to restart the game
            elif (1350 <= mouse_x <= 1350 + replay_image.get_width() and
                  1069.1 + 250 <= mouse_y <= 1069.1 + 250 + replay_image.get_height()):
                if (0 in card_counters):
                    continue
                else:
                    game_data.append(["", total_spending])
                    restart_game()
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                if input_text.strip() and (input_text != 'Your name'):
                    # Store the input text with total_spending
                    game_data.append([input_text, total_spending])
                else:
                    game_data.append(["", total_spending])
                restart_game()
                print(game_data)
                game_over_displayed = False
                end_game_time = None
                input_active = False
                input_text = 'Your name'
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    # Handle cursor blinking
    if time.time() - last_blink_time > 0.5:  # Change cursor visibility every 0.5 seconds
        cursor_visible = not cursor_visible
        last_blink_time = time.time()


    update_slots()
    draw_interface()
    pygame.display.flip()

pygame.quit()

import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 2800
SCREEN_HEIGHT = 1440
CARD_RATIO = (int(250 * 1.3), int(420 * 1.3))  # Increased size by 1.3
PACK_RATIO = (270, 120)
BG_IMAGE = 'BG.png'
TITLE_IMAGE = 'Title.png'
CARD_IMAGES = ['card0.png', 'card1.png', 'card2.png', 'card3.png', 'card4.png', 'card5.png']
PACK_IMAGES = ['Pack1.png', 'Pack3.png', 'Pack5.png']
PACK_PRICES = [10, 25, 40]
TARGET_SPENDING = 50
VOUCHER_IMAGE = 'voucher.png'
VOUCHER_IMAGES_B = ['b1.png', 'b2.png', 'b3.png', 'b4.png', 'b5.png']
VOUCHER_IMAGES_C = ['c1.png', 'c2.png', 'c3.png', 'c4.png', 'c5.png']

# Colors
WHITE = (255, 255, 255)
BLACK = (68,40,29)

# Load images
bg_image = pygame.image.load(BG_IMAGE)
title_image = pygame.image.load(TITLE_IMAGE)
card_images = [pygame.image.load(img) for img in CARD_IMAGES]
pack_images = [pygame.image.load(img) for img in PACK_IMAGES]
voucher_image = pygame.image.load(VOUCHER_IMAGE)
voucher_images_b = [pygame.image.load(img) for img in VOUCHER_IMAGES_B]
voucher_images_c = [pygame.image.load(img) for img in VOUCHER_IMAGES_C]

# Scale images
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
title_image = pygame.transform.scale(title_image, (600, 200))
card_images = [pygame.transform.scale(img, CARD_RATIO) for img in card_images]
pack_images = [pygame.transform.scale(img, PACK_RATIO) for img in pack_images]
voucher_image = pygame.transform.scale(voucher_image, (540, 1240))
voucher_images_b = [pygame.transform.scale(img, (540, 248)) for img in voucher_images_b]
voucher_images_c = [pygame.transform.scale(img, (540, 248)) for img in voucher_images_c]

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Kitty Gacha")

# Card counters
card_counters = [0, 0, 0, 0, 0]

# Spending
total_spending = 0

# Font
FONT_PATH = 'TH Grisly Beast.ttf'  # Path to the font file
font = pygame.font.Font(FONT_PATH, 37)

# Calculate new pack positions
pack1_x = 50 + int(1 * 300 * 1.3) - PACK_RATIO[0] // 2 - 20
pack3_x = 50 + int(2.5 * 300 * 1.3) - PACK_RATIO[0] // 2 -25
pack5_x = 50 + int(4 * 300 * 1.3) - PACK_RATIO[0] // 2 - 20
pack_y = 800 + int(CARD_RATIO[1] * 0.3) -25

# Variables to manage card slots and timing
slots = [None, None, None, None, None]
displayed_cards = False
start_time = None
flip_start_time = None
flip_duration = 0.5  # Reduced flip duration to 0.5 seconds
transitioning = False

def draw_interface():
    screen.blit(bg_image, (0, 0))
    screen.blit(title_image, (0 , 0))

    # Draw spending bar
    bar_length = pack5_x + CARD_RATIO[0] + 75
    pygame.draw.rect(screen, BLACK, (50, 150, bar_length, 60), 2)
    spending_bar_length = min(bar_length, int(bar_length * total_spending / TARGET_SPENDING))
    pygame.draw.rect(screen, (150, 75, 0), (50, 150, spending_bar_length, 60))

    # Draw spending text
    spending_text = font.render(f"Total spending: {total_spending}", True, BLACK)
    target_text = font.render(f"Target spending: {TARGET_SPENDING}", True, BLACK)
    screen.blit(spending_text, (50, 240))
    screen.blit(target_text, (bar_length - 350, 240))

    # Draw card slots only if cards are selected
    for i in range(5):
        if slots[i] is not None:
            card_x = 50 + int(i * 300 * 1.3)
            card_y = 300
            draw_flip_animation(screen, card_x, card_y, slots[i])

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
    voucher_y = (SCREEN_HEIGHT - 1240) // 2
    voucher_positions = [
        (2100, voucher_y + 0 * 248),
        (2100, voucher_y + 1 * 248 - 2),
        (2100, voucher_y + 2 * 248 - 4),
        (2100, voucher_y + 3 * 248 - 6),
        (2100, voucher_y + 4 * 248 - 6)
    ]
    for i, pos in enumerate(voucher_positions):
        voucher_img = voucher_images_b[i] if card_counters[i] == 0 else voucher_images_c[i]
        screen.blit(voucher_img, pos)
        if card_counters[i] > 0:
            counter_text = font.render(str(card_counters[i]), True, BLACK)
            counter_text_rect = counter_text.get_rect(center=(pos[0] + voucher_img.get_width() + 40, pos[1] + voucher_img.get_height() // 2))
            screen.blit(counter_text, counter_text_rect.topleft)

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
    global total_spending, card_counters, slots, displayed_cards, start_time, flip_start_time, transitioning

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
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            # Check for pack selection
            if pack1_x <= mouse_x <= pack1_x + PACK_RATIO[0] and pack_y <= mouse_y <= pack_y + PACK_RATIO[1]:
                handle_pack_selection(0)
            elif pack3_x <= mouse_x <= pack3_x + PACK_RATIO[0] and pack_y <= mouse_y <= pack_y + PACK_RATIO[1]:
                handle_pack_selection(1)
            elif pack5_x <= mouse_x <= pack5_x + PACK_RATIO[0] and pack_y <= mouse_y <= pack_y + PACK_RATIO[1]:
                handle_pack_selection(2)
            # Check for title click to restart the game
            elif 0 <= mouse_x <= title_image.get_width() and 0 <= mouse_y <= title_image.get_height():
                restart_game()

    update_slots()
    draw_interface()
    pygame.display.flip()

pygame.quit()

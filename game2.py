import pygame
import random

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
PACK_PRICES = [50, 70, 90]
TARGET_SPENDING = 700
VOUCHER_IMAGE = 'voucher.png'
VOUCHER_IMAGES_B = ['b1.png', 'b2.png', 'b3.png', 'b4.png', 'b5.png']
VOUCHER_IMAGES_C = ['c1.png', 'c2.png', 'c3.png', 'c4.png', 'c5.png']

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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
title_image = pygame.transform.scale(title_image, (600, 200))  # Adjust size as needed
card_images = [pygame.transform.scale(img, CARD_RATIO) for img in card_images]
pack_images = [pygame.transform.scale(img, PACK_RATIO) for img in pack_images]
voucher_image = pygame.transform.scale(voucher_image, (540, 1240))  # Increased size by 1.5
voucher_images_b = [pygame.transform.scale(img, (540, 248)) for img in voucher_images_b]  # Adjust size for each small image
voucher_images_c = [pygame.transform.scale(img, (540, 248)) for img in voucher_images_c]  # Adjust size for each small image

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Kitty Gacha")

# Card counters
card_counters = [0, 0, 0, 0, 0]

# Spending
total_spending = 0

# Font
font = pygame.font.Font(None, 60)

# Calculate new pack positions (defined outside the functions to be accessible globally)
pack1_x = 50 + int(1 * 300 * 1.3) - PACK_RATIO[0] // 2  # Middle of card1 and card2
pack3_x = 50 + int(2.5 * 300 * 1.3) - PACK_RATIO[0] // 2  # Middle of card3
pack5_x = 50 + int(4 * 300 * 1.3) - PACK_RATIO[0] // 2  # Middle of card4 and card5
pack_y = 800 + int(CARD_RATIO[1] * 0.3)  # Adjusted spacing between cards and packs by 1.3, moved 50px down from original 750

def draw_interface():
    screen.blit(bg_image, (0, 0))
    screen.blit(title_image, (0 , 0))

    # Draw spending bar
    bar_length = pack5_x + CARD_RATIO[0] + 75   # Extend the bar by 20px to the right
    pygame.draw.rect(screen, BLACK, (50, 150, bar_length, 60), 2)  # Adjusted length to reach the right of card 5
    spending_bar_length = min(bar_length, int(bar_length * total_spending / TARGET_SPENDING))
    pygame.draw.rect(screen, (150, 75, 0), (50, 150, spending_bar_length, 60))

    # Draw spending text
    spending_text = font.render(f"Total spending: {total_spending}", True, BLACK)
    target_text = font.render(f"Target spending: {TARGET_SPENDING}", True, BLACK)
    screen.blit(spending_text, (50, 240))
    screen.blit(target_text, (bar_length - 370, 240))  # Adjusted position

    # Draw card slots with increased spacing and centered counters
    for i in range(5):
        if card_counters[i] > 0:  # Only display if the counter is greater than 0
            card_image = card_images[i + 1]
            card_x = 50 + int(i * 300 * 1.3)  # Increased spacing by 1.3
            card_y = 300  # Moved 50px down from original 250
            screen.blit(card_image, (card_x, card_y))  # Adjusted spacing
            counter_text = font.render(str(card_counters[i]), True, BLACK)
            counter_text_rect = counter_text.get_rect(center=(card_x + CARD_RATIO[0] // 2, card_y + CARD_RATIO[1] + 40))
            screen.blit(counter_text, counter_text_rect.topleft)  # Centered below the card

    # Draw packs with increased spacing and centered prices
    screen.blit(pack_images[0], (pack1_x, pack_y))  # Pack1 between card1 and card2
    screen.blit(pack_images[1], (pack3_x, pack_y))  # Pack3 in the middle of card3
    screen.blit(pack_images[2], (pack5_x, pack_y))  # Pack5 between card4 and card5

    # Draw pack prices
    price_text1 = font.render(f"Price {PACK_PRICES[0]}", True, BLACK)
    price_text_rect1 = price_text1.get_rect(center=(pack1_x + PACK_RATIO[0] // 2, pack_y + PACK_RATIO[1] + 40))
    screen.blit(price_text1, price_text_rect1.topleft)  # Centered below the pack

    price_text2 = font.render(f"Price {PACK_PRICES[1]}", True, BLACK)
    price_text_rect2 = price_text2.get_rect(center=(pack3_x + PACK_RATIO[0] // 2, pack_y + PACK_RATIO[1] + 40))
    screen.blit(price_text2, price_text_rect2.topleft)  # Centered below the pack

    price_text3 = font.render(f"Price {PACK_PRICES[2]}", True, BLACK)
    price_text_rect3 = price_text3.get_rect(center=(pack5_x + PACK_RATIO[0] // 2, pack_y + PACK_RATIO[1] + 40))
    screen.blit(price_text3, price_text_rect3.topleft)  # Centered below the pack

    # Draw voucher images
    if all(counter > 0 for counter in card_counters):
        screen.blit(voucher_image, (2100, (SCREEN_HEIGHT - 1240) // 2))  # Center voucher vertically
    else:
        voucher_y = (SCREEN_HEIGHT - 1240) // 2  # Center vertically
        voucher_positions = [
            (2100, voucher_y + 0 * 248),  # Position for voucher 1
            (2100, voucher_y + 1 * 248 - 2),  # Position for voucher 2
            (2100, voucher_y + 2 * 248 - 4),  # Position for voucher 3
            (2100, voucher_y + 3 * 248 - 6),  # Position for voucher 4
            (2100, voucher_y + 4 * 248 - 6)   # Position for voucher 5
        ]
        for i, pos in enumerate(voucher_positions):
            voucher_img = voucher_images_b[i] if card_counters[i] == 0 else voucher_images_c[i]
            screen.blit(voucher_img, pos)

def handle_pack_selection(pack_index):
    global total_spending
    total_spending += PACK_PRICES[pack_index]
    repeat_count = [1, 3, 5][pack_index]
    for _ in range(repeat_count):
        card_index = random.randint(1, 5) - 1
        card_counters[card_index] += 1


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            # Adjust mouse detection for new pack positions
            if pack1_x <= mouse_x <= pack1_x + PACK_RATIO[0] and pack_y <= mouse_y <= pack_y + PACK_RATIO[1]:
                handle_pack_selection(0)
            elif pack3_x <= mouse_x <= pack3_x + PACK_RATIO[0] and pack_y <= mouse_y <= pack_y + PACK_RATIO[1]:
                handle_pack_selection(1)
            elif pack5_x <= mouse_x <= pack5_x + PACK_RATIO[0] and pack_y <= mouse_y <= pack_y + PACK_RATIO[1]:
                handle_pack_selection(2)

    draw_interface()
    pygame.display.flip()

pygame.quit()

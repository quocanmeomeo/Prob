import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1440
CARD_RATIO = (250, 420)
PACK_RATIO = (270, 120)
BG_IMAGE = 'BG.png'
TITLE_IMAGE = 'Title.png'
VOUCHER_IMAGE = 'voucher.png'
CARD_IMAGES = ['card0.png', 'card1.png', 'card2.png', 'card3.png', 'card4.png', 'card5.png']
PACK_IMAGES = ['Pack1.png', 'Pack3.png', 'Pack5.png']
PACK_PRICES = [50, 70, 90]
TARGET_SPENDING = 200

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
bg_image = pygame.image.load(BG_IMAGE)
title_image = pygame.image.load(TITLE_IMAGE)
voucher_image = pygame.image.load(VOUCHER_IMAGE)
card_images = [pygame.image.load(img) for img in CARD_IMAGES]
pack_images = [pygame.image.load(img) for img in PACK_IMAGES]

# Scale images
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
title_image = pygame.transform.scale(title_image, (400, 150))  # Adjust size as needed
voucher_image = pygame.transform.scale(voucher_image, (400, 800))  # Adjust size as needed
card_images = [pygame.transform.scale(img, CARD_RATIO) for img in card_images]
pack_images = [pygame.transform.scale(img, PACK_RATIO) for img in pack_images]

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Kitty Gacha")

# Card counters
card_counters = [0, 0, 0, 0, 0]

# Spending
total_spending = 0

# Font
font = pygame.font.Font(None, 36)


def draw_interface():
    screen.blit(bg_image, (0, 0))
    screen.blit(title_image, (50, 20))

    # Draw spending bar
    pygame.draw.rect(screen, BLACK, (50, 150, 1000, 30), 2)  # Double the bar length
    spending_bar_length = min(1000, int(1000 * total_spending / TARGET_SPENDING))
    pygame.draw.rect(screen, (150, 75, 0), (50, 150, spending_bar_length, 30))

    # Draw spending text
    spending_text = font.render(f"Total spending: {total_spending}", True, BLACK)
    target_text = font.render(f"Target spending: {TARGET_SPENDING}", True, BLACK)
    screen.blit(spending_text, (50, 200))
    screen.blit(target_text, (300, 200))

    # Draw card slots with increased spacing and centered counters
    for i in range(5):
        card_image = card_images[0] if card_counters[i] == 0 else card_images[i + 1]
        card_x = 50 + i * 300
        card_y = 250
        screen.blit(card_image, (card_x, card_y))  # Adjusted spacing
        counter_text = font.render(str(card_counters[i]), True, BLACK)
        counter_text_rect = counter_text.get_rect(center=(card_x + CARD_RATIO[0] // 2, card_y + CARD_RATIO[1] + 20))
        screen.blit(counter_text, counter_text_rect.topleft)  # Centered below the card

    # Draw packs with increased spacing and centered prices
    for i in range(3):
        pack_x = 50 + i * 540
        pack_y = 750
        screen.blit(pack_images[i], (pack_x, pack_y))  # Adjusted spacing
        price_text = font.render(f"Price {PACK_PRICES[i]}", True, BLACK)
        price_text_rect = price_text.get_rect(center=(pack_x + PACK_RATIO[0] // 2, pack_y + PACK_RATIO[1] + 20))
        screen.blit(price_text, price_text_rect.topleft)  # Centered below the pack

    # Draw voucher
    screen.blit(voucher_image, (1800, 250))


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
            for i in range(3):
                if 50 + i * 540 <= mouse_x <= 50 + (i + 1) * 540 and 750 <= mouse_y <= 750 + PACK_RATIO[1]:
                    handle_pack_selection(i)
                    break

    draw_interface()
    pygame.display.flip()

pygame.quit()

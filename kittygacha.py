import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Setup the display to fullscreen and get dimensions
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
pygame.display.set_caption("Kitty Gacha")

# Define original dimensions to calculate scaling factors
ORIGINAL_WIDTH = 3090
ORIGINAL_HEIGHT = 1600
scale_w = SCREEN_WIDTH / ORIGINAL_WIDTH
scale_h = SCREEN_HEIGHT / ORIGINAL_HEIGHT

# --- Constants (Scaled) ---
CARD_RATIO = (int(250.1 * 1.5 * scale_w), int(416.8 * 1.5 * scale_h))
PACK_RATIO = (int(274.7 * 1.5 * scale_w), int(121.4 * 1.5 * scale_h))
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
title_image = pygame.transform.scale(title_image, (int(401.6 * 1.5 * scale_w), int(121.4 * 1.5 * scale_h)))
card_images = [pygame.transform.scale(img, CARD_RATIO) for img in card_images]
pack_images = [pygame.transform.scale(img, PACK_RATIO) for img in pack_images]
voucher_image = pygame.transform.scale(voucher_image, (int(540 * scale_w), int(1240 * scale_h)))
voucher_images_b = [pygame.transform.scale(img, (int(268.2 * 2 * 1.2 * scale_w), int(121.1 * 2 * 1.2 * scale_h))) for img in voucher_images_b]
voucher_images_c = [pygame.transform.scale(img, (int(268.2 * 2 * 1.2 * scale_w), int(121.1 * 2 * 1.2 * scale_h))) for img in voucher_images_c]
win_image = pygame.transform.scale(win_image, (int(274.9 * 2.7 * scale_w), int(247.6 * 2.7 * scale_h)))
lose_image = pygame.transform.scale(lose_image, (int(274.9 * 2.7 * scale_w), int(247.6 * 2.7 * scale_h)))
replay_image = pygame.transform.scale(replay_image, (int(334 * 1.5 * scale_w), int(121.5 * 1.5 * scale_h)))


# Card counters
card_counters = [0, 0, 0, 0, 0]

# Spending
total_spending = 0

# Previous game
game_data = []
mean_spending = 0
sum_spending = 0

# Font (Scaled)
FONT_PATH = 'TH Grisly Beast.ttf'
font = pygame.font.Font(FONT_PATH, max(1, int(37 * scale_h)))
bigfont = pygame.font.Font(FONT_PATH, max(1, int(100 * scale_h)))
rankfont = pygame.font.Font(FONT_PATH, max(1, int(70 * scale_h)))

# Calculate new pack positions (Scaled)
pack1_x = int(150 * scale_w) + int(1 * 300 * 1.5 * scale_w) - PACK_RATIO[0] // 2 - int(115 * scale_w)
pack3_x = int(150 * scale_w) + int(2.5 * 300 * 1.5 * scale_w) - PACK_RATIO[0] // 2 - int(115 * scale_w)
pack5_x = int(150 * scale_w) + int(4 * 300 * 1.5 * scale_w) - PACK_RATIO[0] // 2 - int(115 * scale_w)
pack_y = int(800 * scale_h) + int(CARD_RATIO[1] * 0.3) + int(100 * scale_h)

# Variables to manage card slots and timing
slots = [None, None, None, None, None]
displayed_cards = False
start_time = None
flip_start_time = None
flip_duration = 0.5
transitioning = False

# Additional state to manage the screen
show_leaderboard = False

# Text box colors
COLOR_INACTIVE = BLACK
COLOR_ACTIVE = BLACK
COLOR_TEXT = BLACK
BACKGROUND_COLOR = WHITE

# Input box rectangle (Scaled)
input_box = pygame.Rect(int(1350 * scale_w), int((1019.1 + 200) * scale_h), int(500 * scale_w), int(100 * scale_h))
color = COLOR_INACTIVE

# Variables to manage input
active = False
input_text = 'Your name'
cursor_visible = True
last_blink_time = time.time()
input_active = False # Explicitly define input_active

def draw_interface():
    if not show_leaderboard:
        screen.blit(bg_image, (0, 0))
        screen.blit(title_image, (0, 0))

        # Draw spending bar (Scaled)
        bar_length = pack5_x + CARD_RATIO[0] + int(200 * scale_w)
        pygame.draw.rect(screen, BLACK, (int(50 * scale_w), int(150 * scale_h), bar_length, int(60 * scale_h)), 2)
        spending_bar_length = min(bar_length, int(bar_length * total_spending / TARGET_SPENDING))
        pygame.draw.rect(screen, (150, 75, 0), (int(50 * scale_w), int(150 * scale_h), spending_bar_length, int(60 * scale_h)))

        # Draw spending text (Scaled)
        spending_text = font.render(f"Total spending: {total_spending}", True, BLACK)
        mean_text = font.render(f"Mean spending: {mean_spending}", True, BLACK)
        target_text = font.render(f"Target spending: {TARGET_SPENDING}", True, BLACK)
        screen.blit(spending_text, (int(50 * scale_w), int(240 * scale_h)))
        screen.blit(target_text, (bar_length - int(350 * scale_w), int(240 * scale_h)))
        if (mean_spending < 10):
            screen.blit(mean_text, (((bar_length - int(350 * scale_w) - int(50 * scale_w)) / 2) + int(90 * scale_w), int(240 * scale_h)))
        elif (mean_spending < 100):
            screen.blit(mean_text, (((bar_length - int(350 * scale_w) - int(50 * scale_w)) / 2) + int(80 * scale_w), int(240 * scale_h)))
        else:
            screen.blit(mean_text, (((bar_length - int(350 * scale_w) - int(50 * scale_w)) / 2) + int(75 * scale_w), int(240 * scale_h)))

        # Draw card slots (Scaled)
        for i in range(5):
            if slots[i] is not None:
                card_x = int(150 * scale_w) + int(i * 300 * 1.5 * scale_w) - int(70 * scale_w)
                card_y = int(350 * scale_h)
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
            price_text_rect1 = price_text1.get_rect(center=(pack1_x + PACK_RATIO[0] // 2, pack_y + PACK_RATIO[1] + int(40 * scale_h)))
            screen.blit(price_text1, price_text_rect1.topleft)

            price_text2 = font.render(f"Price {PACK_PRICES[1]}", True, BLACK)
            price_text_rect2 = price_text2.get_rect(center=(pack3_x + PACK_RATIO[0] // 2, pack_y + PACK_RATIO[1] + int(40 * scale_h)))
            screen.blit(price_text2, price_text_rect2.topleft)

            price_text3 = font.render(f"Price {PACK_PRICES[2]}", True, BLACK)
            price_text_rect3 = price_text3.get_rect(center=(pack5_x + PACK_RATIO[0] // 2, pack_y + PACK_RATIO[1] + int(40 * scale_h)))
            screen.blit(price_text3, price_text_rect3.topleft)

        # Draw voucher images (Scaled)
        voucher_y = (SCREEN_HEIGHT - int(1240 * 1.2 * scale_h)) // 2
        voucher_positions = [
            (int(2350 * scale_w), voucher_y + int(0 * 248 * 1.2 * scale_h)),
            (int(2350 * scale_w), voucher_y + int(1 * 248 * 1.2 * scale_h - 9 * scale_h)),
            (int(2350 * scale_w), voucher_y + int(2 * 248 * 1.2 * scale_h - 19 * scale_h)),
            (int(2350 * scale_w), voucher_y + int(3 * 248 * 1.2 * scale_h - 28 * scale_h)),
            (int(2350 * scale_w), voucher_y + int(4 * 248 * 1.2 * scale_h - 36 * scale_h))
        ]
        for i, pos in enumerate(voucher_positions):
            voucher_img = voucher_images_b[i] if card_counters[i] == 0 else voucher_images_c[i]
            screen.blit(voucher_img, pos)
            if card_counters[i] > 0:
                counter_text = font.render(str(card_counters[i]), True, BLACK)
                counter_text_rect = counter_text.get_rect(
                    center=(pos[0] + voucher_img.get_width() + int(40 * scale_w), pos[1] + voucher_img.get_height() // 2))
                screen.blit(counter_text, counter_text_rect.topleft)

        if game_over:
            win_lose_x_pos = ((int(150 * scale_w) + int(1 * 300 * 1.5 * scale_w) - int(70 * scale_w)) - (int(150 * scale_w) + int(0 * 300 * 1.5 * scale_w) - int(70 * scale_w))) / 2 + int(150 * scale_w) - win_image.get_width()/4
            win_lose_y_pos = int(925 * scale_h)
            if total_spending <= TARGET_SPENDING:
                screen.blit(win_image, (win_lose_x_pos, win_lose_y_pos))
            else:
                screen.blit(lose_image, (win_lose_x_pos, win_lose_y_pos))

            # Draw input box
            pygame.draw.rect(screen, BACKGROUND_COLOR, input_box)
            text_surface = font.render(input_text, True, BLACK)
            screen.blit(text_surface, (input_box.x + int(5 * scale_w), input_box.y + int(15 * scale_h)))
            pygame.draw.rect(screen, color, input_box, 2)

            # Draw the cursor (Scaled)
            if input_active and cursor_visible:
                cursor_x = input_box.x + int(5 * scale_w) + text_surface.get_width()
                cursor_y = input_box.y + int(15 * scale_h)
                cursor_height = text_surface.get_height()
                pygame.draw.line(screen, COLOR_TEXT, (cursor_x, cursor_y), (cursor_x, cursor_y + cursor_height), 2)

            # Draw replay image (Scaled)
            screen.blit(replay_image, (int(1350 * scale_w), int((1069.1 + 250) * scale_h)))
    else:
        # Leaderboard screen
        screen.blit(bg_image, (0, 0))
        screen.blit(title_image, (0, 0))

        # Draw spending bar (Scaled)
        bar_length = pack5_x + CARD_RATIO[0] + int(200 * scale_w)
        pygame.draw.rect(screen, BLACK, (int(50 * scale_w), int(150 * scale_h), bar_length, int(60 * scale_h)), 2)
        spending_bar_length = min(bar_length, int(bar_length * total_spending / TARGET_SPENDING))
        pygame.draw.rect(screen, (150, 75, 0), (int(50 * scale_w), int(150 * scale_h), spending_bar_length, int(60 * scale_h)))

        # Draw spending text (Scaled)
        spending_text = font.render(f"Total spending: {total_spending}", True, BLACK)
        mean_text = font.render(f"Mean spending: {mean_spending}", True, BLACK)
        target_text = font.render(f"Target spending: {TARGET_SPENDING}", True, BLACK)
        screen.blit(spending_text, (int(50 * scale_w), int(240 * scale_h)))
        screen.blit(target_text, (bar_length - int(350 * scale_w), int(240 * scale_h)))
        if (mean_spending < 10):
            screen.blit(mean_text, (((bar_length - int(350 * scale_w) - int(50 * scale_w)) / 2) + int(90 * scale_w), int(240 * scale_h)))
        elif (mean_spending < 100):
            screen.blit(mean_text, (((bar_length - int(350 * scale_w) - int(50 * scale_w)) / 2) + int(80 * scale_w), int(240 * scale_h)))
        else:
            screen.blit(mean_text, (((bar_length - int(350 * scale_w) - int(50 * scale_w)) / 2) + int(75 * scale_w), int(240 * scale_h)))

        # Draw voucher images (Scaled)
        voucher_y = (SCREEN_HEIGHT - int(1240 * 1.2 * scale_h)) // 2
        voucher_positions = [
            (int(2350 * scale_w), voucher_y + int(0 * 248 * 1.2 * scale_h)),
            (int(2350 * scale_w), voucher_y + int(1 * 248 * 1.2 * scale_h - 9 * scale_h)),
            (int(2350 * scale_w), voucher_y + int(2 * 248 * 1.2 * scale_h - 19 * scale_h)),
            (int(2350 * scale_w), voucher_y + int(3 * 248 * 1.2 * scale_h - 28 * scale_h)),
            (int(2350 * scale_w), voucher_y + int(4 * 248 * 1.2 * scale_h - 36 * scale_h))
        ]
        for i, pos in enumerate(voucher_positions):
            voucher_img = voucher_images_c[i]
            screen.blit(voucher_img, pos)
            if card_counters[i] > 0:
                counter_text = font.render(str(card_counters[i]), True, BLACK)
                counter_text_rect = counter_text.get_rect(
                    center=(pos[0] + voucher_img.get_width() + int(40 * scale_w), pos[1] + voucher_img.get_height() // 2))
                screen.blit(counter_text, counter_text_rect.topleft)

        # Draw Leaderboard title (Scaled)
        leaderboard_text = bigfont.render("Leaderboard", True, BLACK)
        screen.blit(leaderboard_text, ((SCREEN_WIDTH - int(700 * scale_w)) // 2 - leaderboard_text.get_width() // 2, int(350 * scale_h)))

        # Draw Leaderboard entries (Scaled)
        if len(leaderboard) > 0:
            for i in range(len(leaderboard)):
                entry_text = rankfont.render(f"#{i + 1}: {leaderboard[i][0]} - {leaderboard[i][1]}", True, BLACK)
                screen.blit(entry_text, ((SCREEN_WIDTH - int(700 * scale_w)) // 2 - entry_text.get_width() // 2, int(550 * scale_h) + (i * int(100 * scale_h))))


def handle_pack_selection(pack_index):
    global total_spending, displayed_cards, start_time, slots, flip_start_time, transitioning
    if not transitioning:
        total_spending += PACK_PRICES[pack_index]
        repeat_count = [1, 3, 5][pack_index]
        slots = [None] * 5

        for i in range(repeat_count):
            slots[2 - repeat_count // 2 + i] = 0

        displayed_cards = True
        start_time = time.time()
        flip_start_time = None
        transitioning = True

def update_slots():
    global displayed_cards, slots, flip_start_time, transitioning
    if displayed_cards and time.time() - start_time >= 1:
        for i in range(5):
            if slots[i] == 0:
                slots[i] = random.randint(1, 5)
                card_counters[slots[i] - 1] += 1
        displayed_cards = False
        flip_start_time = time.time()

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
        mean_spending, game_data, sum_spending

    if len(game_data) > 0:
        for i in range(len(game_data)):
            sum_spending += game_data[i][1]
        mean_spending = int(sum_spending / len(game_data))
        sum_spending = 0
    sort_leaderboard()

    total_spending = 0
    card_counters = [0, 0, 0, 0, 0]
    slots = [None] * 5
    displayed_cards = False
    start_time = None
    flip_start_time = None
    transitioning = False

leaderboard = []
def sort_leaderboard():
    global leaderboard, game_data
    filtered_data = [item for item in game_data if item[0] != '']
    sorted_data = sorted(filtered_data, key=lambda x: x[1], reverse=False)
    leaderboard = sorted_data[:5]
    print(leaderboard)

# Main loop
running = True
game_over_displayed = False
while running:
    # Define clickable rects for collision detection in the loop
    pack1_rect = pygame.Rect(pack1_x, pack_y, PACK_RATIO[0], PACK_RATIO[1])
    pack3_rect = pygame.Rect(pack3_x, pack_y, PACK_RATIO[0], PACK_RATIO[1])
    pack5_rect = pygame.Rect(pack5_x, pack_y, PACK_RATIO[0], PACK_RATIO[1])
    replay_rect = pygame.Rect(int(1350 * scale_w), int((1069.1 + 250) * scale_h), replay_image.get_width(), replay_image.get_height())
    title_rect = title_image.get_rect()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if input_box.collidepoint(event.pos) and not (0 in card_counters):
                input_active = not input_active
                if input_active:
                    input_text = ''
            else:
                input_active = False
                if not input_text.strip(): # if empty or just spaces
                    input_text = 'Your name'
            color = COLOR_ACTIVE if input_active else COLOR_INACTIVE

            if title_rect.collidepoint(event.pos):
                show_leaderboard = not show_leaderboard
                continue

            if show_leaderboard:
                continue

            if not all(c > 0 for c in card_counters):
                if pack1_rect.collidepoint(mouse_x, mouse_y):
                    handle_pack_selection(0)
                elif pack3_rect.collidepoint(mouse_x, mouse_y):
                    handle_pack_selection(1)
                elif pack5_rect.collidepoint(mouse_x, mouse_y):
                    handle_pack_selection(2)

            if all(c > 0 for c in card_counters) and replay_rect.collidepoint(mouse_x, mouse_y):
                game_data.append(["", total_spending])
                restart_game()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Allow quitting with ESC
                 running = False
            if input_active:
                if event.key == pygame.K_RETURN:
                    if input_text.strip() and (input_text != 'Your name'):
                        game_data.append([input_text, total_spending])
                    else:
                        game_data.append(["", total_spending])
                    restart_game()
                    game_over_displayed = False
                    input_active = False
                    input_text = 'Your name'
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    if time.time() - last_blink_time > 0.5:
        cursor_visible = not cursor_visible
        last_blink_time = time.time()

    update_slots()
    draw_interface()
    pygame.display.flip()

pygame.quit()
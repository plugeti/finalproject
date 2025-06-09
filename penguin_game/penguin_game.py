import pygame
import random
import os
import sys

# 경로 설정 함수
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# 초기화
pygame.init()
WIDTH, HEIGHT = 600, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Penguin Ice Adventure (Final v2)")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 폰트
font = pygame.font.SysFont("Arial", 28)
big_font = pygame.font.SysFont("Arial", 48)

# 이미지 로드
bg_img = pygame.image.load(resource_path(os.path.join("assets", "snow_bg.png")))
penguin_img = pygame.image.load(resource_path(os.path.join("assets", "penguin.png")))
penguin_img = pygame.transform.scale(penguin_img, (50, 50))

rock_img = pygame.image.load(resource_path(os.path.join("assets", "rock.png")))
rock_img = pygame.transform.scale(rock_img, (60, 60))

fish_img = pygame.image.load(resource_path(os.path.join("assets", "fish.png")))
fish_img = pygame.transform.scale(fish_img, (40, 40))

# 난이도 설정
difficulty_settings = {
    "Easy": {"rock_speed": 4, "spawn_interval": 80, "fish_spawn_interval": 180},
    "Normal": {"rock_speed": 5, "spawn_interval": 60, "fish_spawn_interval": 200},
    "Hard": {"rock_speed": 7, "spawn_interval": 40, "fish_spawn_interval": 150}
}

# 로비(메인 메뉴) 화면
def draw_main_menu():
    win.blit(bg_img, (0, 0))
    title = big_font.render("Penguin Ice Adventure", True, BLACK)
    tip1 = font.render("1: Start Game", True, BLACK)
    tip2 = font.render("2: Quit", True, BLACK)
    win.blit(title, (WIDTH//2 - title.get_width()//2, 200))
    win.blit(tip1, (WIDTH//2 - tip1.get_width()//2, 300))
    win.blit(tip2, (WIDTH//2 - tip2.get_width()//2, 350))
    pygame.display.update()

# 난이도 선택 화면
def draw_difficulty_menu():
    win.blit(bg_img, (0, 0))
    title = big_font.render("Select Difficulty", True, BLACK)
    tip1 = font.render("1: Easy", True, BLACK)
    tip2 = font.render("2: Normal", True, BLACK)
    tip3 = font.render("3: Hard", True, BLACK)
    win.blit(title, (WIDTH//2 - title.get_width()//2, 200))
    win.blit(tip1, (WIDTH//2 - tip1.get_width()//2, 300))
    win.blit(tip2, (WIDTH//2 - tip2.get_width()//2, 350))
    win.blit(tip3, (WIDTH//2 - tip3.get_width()//2, 400))
    pygame.display.update()

# 시작 화면
def draw_start():
    win.blit(bg_img, (0, 0))
    title = big_font.render("Penguin Ice Adventure", True, BLACK)
    tip = font.render("Press SPACE to Start!", True, BLACK)
    win.blit(title, (WIDTH//2 - title.get_width()//2, 200))
    win.blit(tip, (WIDTH//2 - tip.get_width()//2, 300))
    pygame.display.update()

# 최고 점수 (유지)
high_score = 0

# ====== 메인 전체 루프 ======
while True:

    # --- 로비 메뉴 ---
    main_menu = True
    while main_menu:
        draw_main_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    main_menu = False
                elif event.key == pygame.K_2:
                    pygame.quit()
                    exit()

    # --- 난이도 선택 ---
    difficulty = "Normal"
    difficulty_menu = True
    while difficulty_menu:
        draw_difficulty_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = "Easy"
                    difficulty_menu = False
                elif event.key == pygame.K_2:
                    difficulty = "Normal"
                    difficulty_menu = False
                elif event.key == pygame.K_3:
                    difficulty = "Hard"
                    difficulty_menu = False

    # 난이도 적용
    rock_speed = difficulty_settings[difficulty]["rock_speed"]
    spawn_interval = difficulty_settings[difficulty]["spawn_interval"]
    fish_spawn_interval = difficulty_settings[difficulty]["fish_spawn_interval"]

    # --- 시작 화면 ---
    menu = True
    while menu:
        draw_start()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            menu = False

    # ====== 변수 초기화 ======
    penguin_x = WIDTH // 2 - 25
    penguin_y_ground = HEIGHT - 120
    penguin_y = penguin_y_ground
    penguin_speed = 7
    is_jumping = False
    jump_velocity = 0
    jump_power = 15
    gravity = 1

    rock_list = []
    fish_list = []
    frame_count = 0
    level = 1
    level_threshold = 10
    hp = 3
    max_hp = 3
    score = 0

    # ====== 게임 루프 ======
    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        frame_count += 1
        win.blit(bg_img, (0, 0))

        # 이벤트
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # 키 입력
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and penguin_x > 0:
            penguin_x -= penguin_speed
        if keys[pygame.K_RIGHT] and penguin_x < WIDTH - 50:
            penguin_x += penguin_speed
        if keys[pygame.K_SPACE]:
            if not is_jumping:
                is_jumping = True
                jump_velocity = -jump_power

        # 점프 처리
        if is_jumping:
            penguin_y += jump_velocity
            jump_velocity += gravity
            if penguin_y >= penguin_y_ground:
                penguin_y = penguin_y_ground
                is_jumping = False

        # 펭귄 그리기
        win.blit(penguin_img, (penguin_x, penguin_y))
        penguin_rect = pygame.Rect(penguin_x, penguin_y, 50, 50)

        # 바위 생성
        if frame_count % spawn_interval == 0:
            rock_x = random.randint(0, WIDTH - 60)
            rock_y = -60
            rock_list.append(pygame.Rect(rock_x, rock_y, 60, 60))

        # 생선 생성
        if frame_count % fish_spawn_interval == 0:
            fish_x = random.randint(0, WIDTH - 40)
            fish_y = -40
            fish_list.append(pygame.Rect(fish_x, fish_y, 40, 40))

        # 바위 이동
        for rock in rock_list[:]:
            rock.y += rock_speed
            win.blit(rock_img, (rock.x, rock.y))
            if rock.colliderect(penguin_rect) and not is_jumping:
                hp -= 1
                rock_list.remove(rock)
                if hp <= 0:
                    if score > high_score:
                        high_score = score
                    running = False  # 죽으면 → 게임 루프 탈출 → while True → 로비 복귀
            elif rock.y > HEIGHT:
                rock_list.remove(rock)
                score += 1
                if score % level_threshold == 0:
                    level += 1
                    rock_speed += 1

        # 생선 이동
        for fish in fish_list[:]:
            fish.y += rock_speed
            win.blit(fish_img, (fish.x, fish.y))
            if fish.colliderect(penguin_rect):
                score += 5
                fish_list.remove(fish)
            elif fish.y > HEIGHT:
                fish_list.remove(fish)

        # UI 표시
        score_text = font.render(f"Score: {score}", True, BLACK)
        level_text = font.render(f"Level: {level}", True, BLACK)
        hp_text = font.render(f"HP: {hp}", True, BLACK)
        hi_score_text = font.render(f"High Score: {high_score}", True, BLACK)
        diff_text = font.render(f"Difficulty: {difficulty}", True, BLACK)

        win.blit(score_text, (10, 10))
        win.blit(level_text, (10, 50))
        win.blit(hp_text, (10, 90))
        win.blit(hi_score_text, (WIDTH - 250, 10))
        win.blit(diff_text, (WIDTH - 250, 50))

        pygame.display.update()

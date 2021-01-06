import os
import random
import sys

import pygame

pygame.init()
size = width, height = 789, 500
screen = pygame.display.set_mode(size)
start = pygame.mixer.Sound('data/Ring05.wav')


def terminate():
    print(x)
    pygame.quit()
    sys.exit()


def star_screen_info():
    screen = pygame.display.set_mode((789, 500))
    start.play()
    pygame.display.set_caption("Инициализация игры")
    fon = pygame.transform.scale(load_image('start_screen.png'), (789, 500))
    screen.blit(fon, (0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (204, 133, 429, 94), width=2)
    choose = [200, 133]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if choose[1] == 133:
                        choose[1] += 42 + 90
                    else:
                        choose[1] = 133
                elif event.key == pygame.K_UP:
                    if choose[1] == 133 + 42 + 90:
                        choose[1] = 133
                    else:
                        choose[1] = 133 + 42 + 90
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    if choose[1] == 133:
                        return 0
                    else:
                        return 1
            if event.type == pygame.MOUSEMOTION:
                if 204 <= event.pos[0] <= 204 + 425 and 133 <= event.pos[1] <= 133 + 90:
                    choose[1] = 133
                elif 204 <= event.pos[0] <= 204 + 425 and 133 + 90 + 40 <= event.pos[1] <= 133 + 40 + 2 * 90:
                    choose[1] = 133 + 42 + 90
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 204 <= event.pos[0] <= 204 + 425 and 133 <= event.pos[1] <= 133 + 90:
                    return 0
                elif 204 <= event.pos[0] <= 204 + 425 and 133 + 90 + 40 <= event.pos[1] <= 133 + 40 + 2 * 90:
                    return 1
        screen.fill((0, 0, 0))
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (0, 255, 0), (choose[0], choose[1], 429, 94), width=6)
        pygame.display.flip()


def start_screen():
    screen = pygame.display.set_mode((710, 500))
    pygame.display.set_caption("Инициализация игры")
    fon = pygame.transform.scale(load_image('Fone.png'), (710, 500))
    screen.blit(fon, (0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (160, 125, 420, 66), width=2)
    choose = [160, 125]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
                return 0, 0, 0, 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if choose[1] != 125 + 2 * 66 + 25 * 2:
                        choose[1] += 66 + 25
                    else:
                        choose[1] = 125
                elif event.key == pygame.K_UP:
                    if choose[1] != 125:
                        choose[1] -= 66 + 25
                    else:
                        choose[1] = 125 + 2 * 66 + 25 * 2
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    if choose[1] == 125:
                        return 1, 2000, 30, 3
                    elif choose[1] == 125 + 66 + 25:
                        return 3, 1500, 30, 2
                    elif choose[1] == 125 + 2 * 66 + 25 * 2:
                        return 5, 1000, 50, 1
            if event.type == pygame.MOUSEMOTION:
                if 160 <= event.pos[0] <= 160 + 420 and 125 <= event.pos[1] <= 125 + 66:
                    choose[1] = 125
                elif 160 <= event.pos[0] <= 160 + 420 and 125 + 66 + 25 <= event.pos[1] <= 125 + 66 + 25 + 66:
                    choose[1] = 125 + 66 + 25
                elif 160 <= event.pos[0] <= 160 + 420 and 125 + 2 * 66 + 25 * 2 <= event.pos[
                    1] <= 125 + 3 * 66 + 2 * 25:
                    choose[1] = 125 + 2 * 66 + 2 * 25
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 160 <= event.pos[0] <= 160 + 420 and 125 <= event.pos[1] <= 125 + 66:
                    return 1, 2000, 30, 3
                elif 160 <= event.pos[0] <= 160 + 420 and 125 + 66 + 25 <= event.pos[1] <= 125 + 66 + 25 + 66:
                    return 3, 1500, 30, 2
                elif 160 <= event.pos[0] <= 160 + 420 and 125 + 2 * 66 + 25 * 2 <= event.pos[
                    1] <= 125 + 3 * 66 + 2 * 25:
                    return 5, 1000, 50, 1
        screen.fill((0, 0, 0))
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (choose[0], choose[1], 420, 66), width=2)
        pygame.display.flip()
        clock.tick(FPS)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    # прозрачный цвет
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def mission_screen():
    screen = pygame.display.set_mode((788, 500))
    pygame.display.set_caption("Инициализация игры")
    fon = pygame.transform.scale(load_image('mission_screen.png'), (788, 500))
    screen.blit(fon, (0, 0))

    font = pygame.font.Font('data/B_font.ttf', 80)
    text_coord = [140, 120]
    col = 1
    for i in range(3):
        for j in range(5):
            if i == 0:
                color = (100, 160, 100)
            elif i == 1:
                color = (200, 200, 0)
            else:
                color = (255, 0, 0)
            x = text_coord[0] + 100 * j
            y = text_coord[1] + 100 * i
            pygame.draw.rect(screen, color, (x, y, 80, 80), width=9)
            string_rendered = font.render(str(col), True, color)
            col += 1
            #     intro_rect = string_rendered.get_rect()
            #     text_coord += 10
            #     intro_rect.top = text_coord
            #     intro_rect.x = 10
            #     text_coord += intro_rect.height
            screen.blit(string_rendered, (x + 4, y + 4))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
                col = 1
                for i in range(3):
                    for j in range(5):
                        if i == 0:
                            color = (100, 160, 100)
                        elif i == 1:
                            color = (200, 200, 0)
                        else:
                            color = (255, 0, 0)
                        x = text_coord[0] + 100 * j
                        y = text_coord[1] + 100 * i
                        pygame.draw.rect(screen, color, (x, y, 80, 80), width=9)
                        col += 1
                        if text_coord[0] + 100 * j <= event.pos[0] <= text_coord[0] + 100 * j + 80 and text_coord[
                            1] + 100 * i <= event.pos[1] <= text_coord[1] + 100 * i + 80:
                            x = text_coord[0] + 100 * j
                            y = text_coord[1] + 100 * i
                            pygame.draw.rect(screen, (255, 255, 255), (x, y, 80, 80), width=9)
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                return col
                                run = False

        pygame.display.flip()


def lose_screen():
    screen = pygame.display.set_mode((300, 300))
    intro_text = ["Вы проиграли", f"Набрано {x} очков"]
    pygame.display.set_caption("Итоги игры")

    fon = pygame.Surface((300, 300))
    fon.fill((200, 200, 200))

    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 40)
    text_coord = 30
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    line = "Начать заново"
    rip = pygame.transform.scale(load_image("rip.jpg"), (200, 150))
    screen.blit(rip, (50, 100))

    pygame.draw.rect(screen, (255, 255, 255), (50, 250, 200, 40), width=3)
    font = pygame.font.Font(None, 30)
    string_rendered = font.render(line, True, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 265
    intro_rect.x = 70

    screen.blit(string_rendered, intro_rect)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 50 <= event.pos[0] <= 250 and 250 <= event.pos[1] <= 290:
                    global running
                    running = False
                    run = False
            elif event.type == pygame.MOUSEMOTION:
                if 50 <= event.pos[0] <= 250 and 250 <= event.pos[1] <= 290:
                    pygame.draw.rect(screen, (255, 200, 200), (50, 250, 200, 40), width=3)
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (50, 250, 200, 40), width=3)

        pygame.display.flip()
        clock.tick(FPS)


def victory():
    screen = pygame.display.set_mode((300, 300))
    intro_text = ["Вы выйграли", f"Набрано {x} очков"]
    pygame.display.set_caption("Итоги игры")

    fon = pygame.Surface((300, 300))
    fon.fill((200, 200, 200))

    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 40)
    text_coord = 30
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    line = "Начать заново"
    pygame.draw.rect(screen, (255, 255, 255), (50, 250, 200, 40), width=3)
    font = pygame.font.Font(None, 30)
    string_rendered = font.render(line, True, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 265
    intro_rect.x = 70

    screen.blit(string_rendered, intro_rect)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 50 <= event.pos[0] <= 250 and 250 <= event.pos[1] <= 290:
                    global running
                    running = False
                    run = False
            elif event.type == pygame.MOUSEMOTION:
                if 50 <= event.pos[0] <= 250 and 250 <= event.pos[1] <= 290:
                    pygame.draw.rect(screen, (255, 200, 200), (50, 250, 200, 40), width=3)
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (50, 250, 200, 40), width=3)

        pygame.display.flip()
        clock.tick(FPS)



class Mountain(pygame.sprite.Sprite):
    mountains = ["mountains.png", "mountains_2.png", "mountains_3.png", "mountains_4.png"]
    image = pygame.transform.scale(load_image(random.choice(mountains)), (789, 500))

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = height


class Landing(pygame.sprite.Sprite):
    image = load_image("pt.png")

    def __init__(self, pos):
        super().__init__(mobs)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.HP = HP

    def update(self):
        self.rect = self.rect.move(0, 1)
        if not pygame.sprite.spritecollideany(self, horizontal_borders):
            self.rect = self.rect.move(0, mob_speed)
        else:
            health.play()
            self.kill()
            global HP
            HP -= 1
            if HP == 0:
                lose_screen()


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class GunCar(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x=width // 2, y=height - 5 - 44, weigh=32, heigh=44):
        super().__init__(gun_car)
        self.image = pygame.transform.scale(load_image("cannon.png"), (weigh, heigh))
        # self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        # pygame.draw.circle(self.image, pygame.Color("red"), (radius, radius), radius)
        self.rect = self.image.get_rect().move(x, y)

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(load_image("bullet.png"), (30, 60))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()


while True:
    x = 0
    y = star_screen_info()
    screen = pygame.display.set_mode(size)
    gun_car = pygame.sprite.Group()
    gun = GunCar()
    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    horizontal_borders = pygame.sprite.Group()
    vertical_borders = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Border(0, height - 6, width, height - 6)
    mountain = Mountain()
    font = pygame.font.Font('data/B_font.ttf', 40)

    FPS = 100

    MYEVENTTYPE = pygame.USEREVENT + 1
    hp_image = pygame.transform.scale(load_image("health.png"), (40, 40))

    pygame.key.set_repeat(200, 70)
    clock = pygame.time.Clock()
    if y == 1:
        mob_speed, takt, STEP, HP = start_screen()
    else:
        mob_col = 10 + mission_screen() * 2
        if mob_col <= 20:
            mob_speed, takt, STEP, HP = 1, 2000, 30, 3
        elif mob_col <= 30:
            mob_speed, takt, STEP, HP = 3, 1500, 30, 2
        else:
            mob_speed, takt, STEP, HP = 5, 1000, 50, 1

    pygame.time.set_timer(MYEVENTTYPE, takt)
    running = True
    pygame.display.set_caption("Поймай диверсантов")
    bom = pygame.mixer.Sound('data/Pop_up.wav')
    health = pygame.mixer.Sound("data/health.wav")
    if y == 1:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    terminate()
                if event.type == MYEVENTTYPE:
                    Landing((random.randrange(width - 200), 0))
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if gun.rect.x < width + 32:
                            gun.rect.x += STEP
                        else:
                            gun.rect.x = 0
                    if event.key == pygame.K_LEFT:
                        if gun.rect.x > 0 - 32:
                            gun.rect.x -= STEP
                        else:
                            gun.rect.x = width - 32
                    if event.key == pygame.K_SPACE:
                        gun.shoot()
                        bom.play()
            hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
            if hits:
                x += 10
            screen.fill((0, 0, 0))

            all_sprites.draw(screen)
            all_sprites.update()
            gun_car.draw(screen)
            mobs.draw(screen)

            string_rendered = font.render(str(x), True, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            intro_rect.x = 600
            intro_rect.y = 50
            screen.blit(string_rendered, intro_rect)

            mobs.update()
            for i in range(HP):
                screen.blit(hp_image, (50 + i * 50, 50))
            pygame.display.flip()
            clock.tick(50)
    else:
        running = True
        while mob_col != 0 and running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    terminate()
                if event.type == MYEVENTTYPE:
                    Landing((random.randrange(width - 200), 0))

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if gun.rect.x < width + 32:
                            gun.rect.x += STEP
                        else:
                            gun.rect.x = 0
                    if event.key == pygame.K_LEFT:
                        if gun.rect.x > 0 - 32:
                            gun.rect.x -= STEP
                        else:
                            gun.rect.x = width - 32
                    if event.key == pygame.K_SPACE:
                        gun.shoot()
                        bom.play()
            hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
            if hits:
                x += 10
                mob_col -= 1
            screen.fill((0, 0, 0))

            all_sprites.draw(screen)
            all_sprites.update()
            gun_car.draw(screen)
            mobs.draw(screen)

            string_rendered = font.render(str(x), True, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            intro_rect.x = 600
            intro_rect.y = 50
            screen.blit(string_rendered, intro_rect)

            mobs.update()
            for i in range(HP):
                screen.blit(hp_image, (50 + i * 50, 50))
            pygame.display.flip()
            clock.tick(50)
        victory()

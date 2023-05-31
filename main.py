import pygame
import random
from settings import *
from words import *
from buttons import *

'''Виселица 2.0
Игра «Виселица» реализованая с помощью pygame.

Виселица - игра, в которой вам нужно угадывать различные слова на заданные темы.

Ход игры:
Вы выбираете язык и тему.
Получаете количество букв в слове.
Угадываете слово по буквам.
Если ошибетесь 8 раз - проиграете.
Удачной игры!

История версий:
v0.1 - угадывание слова в терминале.
v0.2 - добавлена графическая оболочка и словарь RUS.
v0.3 - словарь и настройки выделены в отдельный файл, доработан интерфейс.
v0.4 - добавлены счетчики, игра зациклена.
v0.5 - реализован выбор языка, добавлены словари ENG, EST (тема - компьютерные термины).

v1.0 - реализовано управление мышкой, добавления доска с использованными буквы.
v1.5 - добавлены тематические словари с возможностью их выбора.
v1.6 - реализована графику классической игры "Виселица".
v1.7 - добавлена подсказка.
v1.8 - Обновлены все файлы.
v2.0 - Полноценная игра.

Перед запуском программы нужно установить библиотеки:
pygame - pip install pygame;

OLEKSANDR LOZENKO  - https://github.com/OleksandrLozenko'''

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Виселица 2.0 + Update")
background_image = pygame.image.load("Images/background.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
###
font = pygame.font.SysFont(FONT_TEXT, FONT_SIZE)
textbox = pygame.Surface((TEXTBOX_WIDTH, TEXTBOX_HEIGHT))
textbox.fill((200, 200, 200))
textbox_rect = textbox.get_rect(center=(WIDTH/2, HEIGHT/2 + 100))
pygame.draw.rect(textbox, WHITE, textbox.get_rect(), 2)
cross_image = pygame.image.load("Images/cross.png") # Загрузка картинки 'Крестик'.
Logo_image = pygame.image.load("Images/Logo.png") # Загрузка картинки 'Логотип'.
draw_cross = {'button1': False, 'button2': False}
hang_man = {i: pygame.image.load(f"Images/hangman{i}.png") for i in range(9)} # Загрузка картинок и присвоение каждой картинке свой ключ.
###
ALPHABET = ALPHABET_RUS
menu_or_game = ' '
button_width, button_height = 50, 50 # Ширина и висота кнопки.
gap = 10  # расстояние между кнопками.
x, y = gap, gap  # начальная позиция кнопок.
# Создание кнопок из букв алфавита и размещение их в строках по 11 кнопок в каждой.
rows = [] # Список строк.
current_row = [] # Текущая строка.
for letter in ALPHABET:
    current_row.append(letter)
    if len(current_row) == 11:  # Если текущая строка заполнилась.
        rows.append(current_row)  # Добавляем ее в список строк.
        current_row = []  # Обнуляем текущую строку для следующей.
if current_row: # Если последняя строка не пуста.
    rows.append(current_row)
# Создание кнопок на основе строк и их размещение на экране.
buttons = [] # Список кнопок.
for row in rows:
    row_width = button_width * len(row) + gap * (len(row) - 1) # Ширина строки.
    x = (WIDTH - row_width) // 2 # Позиция по горизонтали.
    y += button_height + gap # Переходим на следующую строку по вертикали.
    for letter in row:
        button_rect = pygame.Rect(x, y, button_width, button_height)
        button_text = font.render(letter, True, BLACK)
        buttons.append((button_rect, button_text))
        x += button_width + gap # Переходим к следующей кнопке по горизонтали.

def draw_buttons():
    '''Функция для отображения кнопок на экране.'''
    for i, (button_rect, button_text) in enumerate(buttons):
        letter = ALPHABET[i]  # Получаем символ кнопки из алфавита
        if letter in button_colors:
            color = button_colors[letter]  # Используем сохраненный цвет кнопки из словаря
        else:
            if letter in guessed_letters:
                if letter in word:
                    if current_letter == letter:
                        color = GREEN  # Зеленый цвет для кнопки, если угадана с использованием кнопки с буквой.
                    else:
                        color = YELLOW  # Желтый цвет для кнопки, если угадана с использованием clue_button.
                else:
                    color = RED  # Красный цвет для кнопки, если угадана неверная буква.
            else:
                color = WHITE  # Белый цвет для неактивных кнопок.
        pygame.draw.rect(win, color, button_rect)
        text_surface = font.render(letter, True, BLACK)
        text_rect = text_surface.get_rect(center=button_rect.center)
        win.blit(text_surface, text_rect)

def handle_button_click(pos):
    global hang_man_count, current_letter, guessed_letters, no_word, remaining_attempts, buttons, button_colors
    if clue_button.collidepoint(pos):
        while True:
            random_letter = random.choice(ALPHABET)
            if random_letter not in guessed_letters and random_letter in word:
                guessed_letters.append(random_letter)
                break
    for i, (button_rect, button_text) in enumerate(buttons):
        if button_rect.collidepoint(pos): # Если нажата кнопка button_rect.
            current_letter = ALPHABET[i]
            if current_letter not in guessed_letters:
                guessed_letters.append(current_letter) # Добавить буквы в использованые.
                if current_letter not in word:
                    remaining_attempts -= 1 # Изменить кол-во попыток.
                    hang_man_count += 1 # Изменить счестчик картинок.
                    if current_letter not in button_colors:
                        button_colors[current_letter] = RED  # Установка цвета кнопки в красный.
                else:
                    if current_letter not in button_colors:
                        button_colors[current_letter] = GREEN  # Установка цвета кнопки в зеленый.
            break
    draw_buttons()

# Игровые переменные
guessed_letters = [] # Угаданные буквы.
current_letter = "" # Текущая выбранная буква.
no_word = [] # Список слов, которые были использованы.
remaining_attempts = 8 # Попытки.
hang_man_count = 0 # Начальная картинка.
button_colors = {}  # Словарь для хранения цветов кнопок.

def draw_word():
    '''Функция отображает текущее состояние угадываемого слова, рисуя его на экране в окне игры.'''
    global no_word
    if word not in no_word: # Если текущее слово не входит в список использованных слов.
        no_word.append(word) # Добавить в список использованных слов.
    display_word = ""
    for i, letter in enumerate(word):
        if i in no_word:
            display_word += letter # Добавляем букву в строку
        elif letter in guessed_letters:
            display_word += letter # Добавляем угаданную букву в строку
        else:
            display_word += ENCRYPTION # Добавляем символ шифрования вместо неугаданной буквы

    if display_word:  # Проверка на пустую строку
        font = pygame.font.SysFont(FONT_TEXT, 50)
        text = font.render(display_word, True, BLACK)
        win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2 + 10))

    # Проверяем, угаданы ли все буквы и рисуем сообщение о угадонном слове.
    if all(letter in guessed_letters for letter in word): # Если все буквы угаданы.
        message_surface = pygame.Surface((300, 100)) # Размеры
        message_surface.fill(WHITE)
        message_rect = message_surface.get_rect(center=(WIDTH/2, HEIGHT/2))
        pygame.draw.rect(message_surface, GREEN, message_surface.get_rect(), 5)
        message_font = pygame.font.SysFont(FONT_TEXT, 40)
        message_text = message_font.render(word, True, GREEN)
        message_surface.blit(message_text, (message_surface.get_width()/2 - message_text.get_width()/2, message_surface.get_height()/2 - message_text.get_height()/2))
        win.blit(message_surface, message_rect)
        pygame.display.update()
        pygame.time.delay(1000)
        get_new_word() # Получить новое слово, если все буквы были угаданы.

def get_new_word():
    '''Функция для получения нового слова.'''
    global word, guessed_letters, remaining_attempts, no_word, hang_man_count,hide_message
    hide_message = False
    if len(no_word) == len(WORDS) and not hide_message: # Если длина использованных и слова совпадают сгенерировать новое слово
        message_surface = pygame.Surface((300, 100)) # Размеры
        message_surface.fill(WHITE)
        message_rect = message_surface.get_rect(center=(WIDTH/2, HEIGHT/2))
        pygame.draw.rect(message_surface, GREEN, message_surface.get_rect(), 5)
        message_font = pygame.font.SysFont(FONT_TEXT, 50)
        message_text = message_font.render(victory, True, GREEN)
        message_surface.blit(message_text, (message_surface.get_width()/2 - message_text.get_width()/2, message_surface.get_height()/2 - message_text.get_height()/2))
        win.blit(message_surface, message_rect)
        pygame.display.update()
        win.blit(again_button_text_img, again_button_hovered_img_rect)
        win.blit(exit_button_text_img, exit_button_hovered_img_rect)
        pygame.display.update()
        pygame.time.delay(1000)

    while True: 
        word = random.choice(WORDS) # Выбор нового слова
        if word not in no_word:
            no_word.append(word)
            guessed_letters = [] # Обновляем список угаданых букв
            remaining_attempts = 8 # Попытки
            hang_man_count = 0
            button_colors.clear() # Вернуть изначальную картинку
            return word

count_language = 'RUS' # Язык
# Нарисовать текстовое поле для ввода
#def draw_textbox():
#    win.blit(textbox, (WIDTH/2 - TEXTBOX_WIDTH/2, HEIGHT/2+ 70))
#    text = font.render(current_letter, True, BLACK)
#    win.blit(text, (WIDTH/2 - TEXTBOX_WIDTH/4 + 25, HEIGHT/2 + 70 + TEXTBOX_HEIGHT/4 - FONT_SIZE/4))

def language():
    '''Функция для нарисования текста в текущем языке.'''
    rect = pygame.Rect(0, 5, 220, 50)
    pygame.draw.rect(win, WHITE, rect)
    pygame.draw.rect(win, BLACK, rect, 2)
    text_2 = font.render(f"{menu_language}: {count_language}", True, BLACK)
    win.blit(text_2, (10, 10))

def draw_topic():
    ''''Функция для отрисовки текущей темы'''
    rect = pygame.Rect(0, 60, 260, 50)
    pygame.draw.rect(win, WHITE, rect)
    pygame.draw.rect(win, BLACK, rect, 2)
    if selected_index is not None:
        topic_text = f"Topic: {ITEMS[selected_index]}" # если тема была выбранна игроком.
    else:
        topic_text = f"{topic_language}: {selected_item}" # Если тема была выбранна рандомно.
    text_2 = font.render(topic_text, True, BLACK)
    win.blit(text_2, (10, 65))

def draw_used_letters():
    '''Функция для нарисования использованных букв'''
    rect = pygame.Rect(0, 545, WIDTH, 50)
    pygame.draw.rect(win, WHITE, rect)
    pygame.draw.rect(win, BLACK, rect, 2)
    text_2 = font.render(f"{' , '.join(guessed_letters)}", True, BLACK)
    win.blit(text_2, (5, 550))

def choose_your_language():
    '''Сообщение "Выберите язык."'''
    font = pygame.font.SysFont(FONT_TEXT, 50)
    text_2 = font.render(f"{choose_language}:", True, BLACK)
    win.blit(text_2, (250, 220))

def check_remaining_attempts():
    '''Функция проверки количество попыток и вывод сообщения о проигрыше.'''
    global remaining_attempts, hide_message, again_button
    hide_message = False
    if remaining_attempts <= 0 and not hide_message and hang_man_count == 8: # если попыток = 0 и Сообщение скрыто
        win.blit(hang_man[hang_man_count], (200 , 50))
        message_surface = pygame.Surface((300, 100))
        message_surface.fill(WHITE)
        message_rect = message_surface.get_rect(center=(WIDTH/2, HEIGHT/2))
        pygame.draw.rect(message_surface, RED, message_surface.get_rect(), 5)
        message_font = pygame.font.SysFont(FONT_TEXT, 50)
        message_text = message_font.render(word, True, RED)
        message_surface.blit(message_text, (message_surface.get_width()/2 - message_text.get_width()/2, message_surface.get_height()/2 - message_text.get_height()/2))
        win.blit(message_surface, message_rect)
        # Нарисовать кнопки 'выход' и 'снова'.
        win.blit(again_button_text_img, again_button_hovered_img_rect)
        win.blit(exit_button_text_img, exit_button_hovered_img_rect)
        pygame.display.update()
        pygame.time.delay(1000)

def draw_dropdown():
    '''Фукция отображения содержимого выпадающего списка.'''
    pygame.draw.rect(win, WHITE, (DROPDOWN_X, DROPDOWN_Y, DROPDOWN_WIDTH, DROPDOWN_HEIGHT), 0)

    for i, item in enumerate(ITEMS):
        item_rect = pygame.Rect(DROPDOWN_X, DROPDOWN_Y + i * BUTTON_HEIGHT, DROPDOWN_WIDTH, BUTTON_HEIGHT)
        pygame.draw.rect(win, WHITE, item_rect, 0)

        item_text = pygame.font.SysFont(None, 24).render(item, True, BLACK)
        item_text_rect = item_text.get_rect(center=item_rect.center)
        win.blit(item_text, item_text_rect)

def draw_button():
    '''Функция отрисовки кнопки.'''
    pygame.draw.rect(win, RED, (BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT), 0)

    if selected_index is not None:
        button_text = pygame.font.SysFont(None, 24).render(ITEMS[selected_index], True, WHITE)
    else:
        button_text = pygame.font.SysFont(None, 24).render(choose_topic, True, WHITE)
    
    button_text_rect = button_text.get_rect(center=(BUTTON_X + BUTTON_WIDTH // 2, BUTTON_Y + BUTTON_HEIGHT // 2))
    win.blit(button_text, button_text_rect) 

def draw_screen():
    '''Функция отрисовки кнопок с языками.'''
    if pygame.display.get_init():
        win.blit(rus_button_text_img, rus_button_img_rect)
        win.blit(eng_button_text_img, eng_button_img_rect)
        win.blit(est_button_text_img, est_button_img_rect)
        pygame.display.update()

def Logo():
    '''Функция для отрисовки Логотипа'''
    win.blit(Logo_image, (40 ,-200))

def draw_clue_text():
    '''Функция для отрисовки сообщения "Подсказка"'''
    font = pygame.font.SysFont(FONT_TEXT, 45)
    text_2 = font.render(f"{clue_text}?", True, BLACK)
    win.blit(text_2, (280, 100))

def play():
    '''Функция отрисовки кнопки "Старт".'''
    win.blit(button_img, button_img_rect)

def draw_settings():
    '''Фунция отрисовки кнопки "Настройки."'''
    win.blit(setting_button_text_img,setting_button_img_rect)

menu_running = True
game_running = False
topic_selection = False
setting_running = False
while True:
    # Меню
    if menu_running:
        menu_or_game = 'menu'
        for event in pygame.event.get():
            # Анимация кнопок
            if event.type == pygame.MOUSEMOTION:
                if rus_button.collidepoint(event.pos):
                    rus_button_img_rect = rus_button_hovered_img_rect
                else:
                    rus_button_img_rect = rus_button_img.get_rect(center=rus_button.center)
                if eng_button.collidepoint(event.pos):
                    eng_button_img_rect = eng_button_hovered_img_rect
                else:
                    eng_button_img_rect = eng_button_img.get_rect(center=eng_button.center)
                if est_button.collidepoint(event.pos):
                    est_button_img_rect = est_button_hovered_img_rect
                else:
                    est_button_img_rect = est_button_img.get_rect(center=est_button.center)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rus_button.collidepoint(event.pos):
                    ALPHABET =  ALPHABET_RUS
                    ITEMS = ['ИТ', 'ЕДА', 'ТРАНСПОРТ']
                    count_language, menu_language, choose_language, remaining_tries,choose_topic,topic_language,clue_text = "RUS", 'Язык','Выберите язык', 'Попытки','Выберите тему','Тема','Подсказка'
                    victory = 'Молодец!'
                if eng_button.collidepoint(event.pos):
                    ALPHABET = ALPHABET_ENG
                    ITEMS = ['IT','FOOD','TRANSPORT']
                    count_language,menu_language,choose_language, remaining_tries,choose_topic,topic_language,clue_text = "ENG",'Language','Choose language', 'Attempts','Choose a theme','Topic','Clue'
                    victory = 'Well done!'
                if est_button.collidepoint(event.pos):
                    ALPHABET = ALPHABET_EST
                    ITEMS = ['IT', 'TOIT', 'TRANSPORT']
                    count_language,menu_language,choose_language, remaining_tries,choose_topic,topic_language,clue_text = "EST",'Keel','Valige keel', 'Katsed',"Vali teema",'Teema','Viim'
                    victory =  "Hästi tehtud!"
                if setting_button.collidepoint(event.pos):
                    menu_running = False
                    setting_running = True
                elif button.collidepoint(event.pos):
                    menu_running = False
                    topic_selection = True
                    current_letter = ""
                    guessed_letters = []
                    remaining_attempts = 8
                    hang_man_count = 0
                    button_colors.clear()
    # Отрисовка всех элементов
            pygame.time.delay(100)
            win.blit(background_image, (0, 0))
            Logo()
            draw_screen()
            choose_your_language()
            language()
            play()
            draw_settings()
            pygame.display.update()

    # Игра
    if game_running:
        menu_or_game = 'game'
        # Нарисовать кнопки с положением
        buttons = []
        for i, letter in enumerate(ALPHABET):
            button_rect = pygame.Rect(140 + i % 11 * 50, 360 + i // 11 * 50, 40, 40) # Размещения кнопок
            button_text = font.render(letter, True, BLACK)
            buttons.append((button_rect, button_text))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if setting_button.collidepoint(event.pos):
                    game_running = False
                    setting_running = True
                pressed_letter = handle_button_click(event.pos)
                if again_button.collidepoint(event.pos) and remaining_attempts <= 0: # Работает когда нажата кнопка и попыток 0.
                    hide_message = True
                    current_letter = ""
                    guessed_letters = []
                    no_word.clear()
                    remaining_attempts = 8
                    hang_man_count = 0
                    button_colors.clear()
                    word = random.choice(WORDS)
                if exit_button.collidepoint(event.pos) and remaining_attempts <= 0:
                    game_running = False
                    menu_running = True
                    hang_man_count = 0
                    selected_index = None
    # ВВОД С КЛАВИАТУРИ
    #        elif event.type == pygame.KEYDOWN:
    #            if (event.unicode.isalpha() and len(current_letter) == 1 and event.unicode.upper() in ALPHABET) \
    #    or event.key in ENGLISH_KEY_CODES \
    #    or event.key in ESTONIAN_KEY_CODES \
    #    or event.unicode in ['õ','ü','ä','ö']:
    #                current_letter = event.unicode.upper()
    #            elif event.key == pygame.K_BACKSPACE:
    #                current_letter = ""
    #            elif event.key == pygame.K_RETURN:
    #                if current_letter not in guessed_letters:
    #                    guessed_letters.add(current_letter)
    #                   if current_letter not in word:
    #                        remaining_attempts -= 1
    #                current_letter = ""
    # Отрисовка всех элементов
        for button_rect, button_text in buttons:
            pygame.draw.rect(win, BLACK, button_rect, 1)
            win.blit(button_text, button_rect)
        win.blit(background_image, (0, 0))
        check_remaining_attempts()
        if remaining_attempts != 0: # Если попыток не равно 0 рисовать эти элементы.
            win.blit(hang_man[hang_man_count], (200 , 50))
            language()
    #       draw_textbox()
            draw_buttons()
            draw_word()
            draw_used_letters()
            draw_settings()
            draw_topic()
            if draw_cross['button1'] == True:
                win.blit(clue_button_text_img, clue_button_img_rect)
            pygame.display.update()

    # Настройки
    if setting_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect1.collidepoint(mouse_pos):
                    draw_cross['button1'] = not draw_cross['button1']  # Инвертируем рисования крестика на первой кнопке
                elif button_rect2.collidepoint(mouse_pos):
                    draw_cross['button2'] = not draw_cross['button2']  # Инвертируем рисования крестика на второй кнопке
                if exit_button.collidepoint(event.pos):
                    setting_running = False
                    menu_running = True
                # Работает когда нажата кнопка и Выбрано окно game.
                if again_button.collidepoint(event.pos) and menu_or_game == 'game': 
                    setting_running = False
                    game_running = True
                    current_letter = ""
                    guessed_letters = []
                    no_word.clear()
                    remaining_attempts = 8
                    hang_man_count = 0
                    button_colors.clear()
                    selected_item = random.choice(ITEMS)
                    word = random.choice(WORDS)
                if button.collidepoint(event.pos) and menu_or_game == 'game':
                    setting_running = False
                    menu_running = False
                    game_running = True
                    print(word)

        win.blit(background_image, (0, 0))
        win.blit(exit_button_text_img, exit_button_hovered_img_rect)
        # Отрисовка первой кнопки
        pygame.draw.rect(win, border_color1, (button_x1 - border_width1, button_y1 - border_width1,
                                            button_width1 + border_width1 * 2, button_height1 + border_width1 * 2))
        pygame.draw.rect(win, button_color1, (button_x1, button_y1, button_width1, button_height1))

        # Отрисовка второй кнопки
        pygame.draw.rect(win, border_color2, (button_x2 - border_width2, button_y2 - border_width2,
                                            button_width2 + border_width2 * 2, button_height2 + border_width2 * 2))
        pygame.draw.rect(win, button_color2, (button_x2, button_y2, button_width2, button_height2))

        if menu_or_game == 'game':
            win.blit(again_button_text_img, again_button_hovered_img_rect)
            play()
        for button_id, is_drawn in draw_cross.items():
            if is_drawn: # Рассположение крестика.
                if button_id == 'button1':
                    cross_x = button_x1 + (button_width1 - cross_image.get_width()) // 2
                    cross_y = button_y1 + (button_height1 - cross_image.get_height()) // 2
                elif button_id == 'button2':
                    cross_x = button_x2 + (button_width2 - cross_image.get_width()) // 2
                    cross_y = button_y2 + (button_height2 - cross_image.get_height()) // 2
                win.blit(cross_image, (cross_x, cross_y))

        draw_clue_text()
        pygame.display.update()


# Тема
    if topic_selection:
        topic = 0 
        if count_language == 'RUS':
            WORDS = WORDS_FOOD_UPPER[topic] if selected_index == 1 else WORDS_IT_UPPER[topic] if selected_index == 0 else WORDS_TRANSPORT_UPPER[topic]
        elif count_language == 'ENG':
            WORDS = WORDS_FOOD_UPPER[1] if selected_index == 1 else WORDS_IT_UPPER[1] if selected_index == 0 else WORDS_TRANSPORT_UPPER[1]
        elif count_language == 'EST':
            WORDS = WORDS_FOOD_UPPER[2] if selected_index == 1 else WORDS_IT_UPPER[2] if selected_index == 0 else WORDS_TRANSPORT_UPPER[2]

        ALPHABET = ALPHABET_RUS if count_language == 'RUS' else ALPHABET_ENG if count_language == 'ENG' else ALPHABET_EST

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка мыши
                    mouse_pos = pygame.mouse.get_pos()

                    # Проверяем, нажали ли на кнопку
                    if BUTTON_X <= mouse_pos[0] <= BUTTON_X + BUTTON_WIDTH and BUTTON_Y <= mouse_pos[1] <= BUTTON_Y + BUTTON_HEIGHT:
                        # Переключаем флаг открытия/закрытия выпадающего списка
                        dropdown_open = not dropdown_open
                    # Проверяем, нажали ли внутри выпадающего списка
                    elif dropdown_open and DROPDOWN_X <= mouse_pos[0] <= DROPDOWN_X + DROPDOWN_WIDTH and DROPDOWN_Y <= mouse_pos[1] <= DROPDOWN_Y + DROPDOWN_HEIGHT:
                        # Определяем выбранный элемент
                        selected_index = (mouse_pos[1] - DROPDOWN_Y) // BUTTON_HEIGHT
                        if 0 <= selected_index < len(ITEMS):
                            dropdown_open = False  # Закрытие выпадающего списка
                            if ITEMS[selected_index] == 'ИТ':
                                WORDS = WORDS_IT_UPPER[topic] if count_language == 'RUS' else WORDS_IT_UPPER[1] if count_language == 'ENG' else WORDS_IT_UPPER[2]
                            elif ITEMS[selected_index] == 'ЕДА':
                                WORDS = WORDS_FOOD_UPPER[topic] if count_language == 'RUS' else WORDS_FOOD_UPPER[1] if count_language == 'ENG' else WORDS_FOOD_UPPER[2]
                            elif ITEMS[selected_index] == 'ТРАНСПОРТ':
                                WORDS = WORDS_TRANSPORT_UPPER[topic] if count_language == 'RUS' else WORDS_TRANSPORT_UPPER[1] if count_language == 'ENG' else WORDS_TRANSPORT_UPPER[2]

                    if button.collidepoint(event.pos):
                        topic_selection = False
                        game_running = True
                        current_letter = ""
                        guessed_letters = []
                        remaining_attempts = 8
                        hang_man_count = 0
                        button_colors.clear()

                    if selected_index is not None:
                        # Если выбранная тема существует, использовать ее
                        selected_item = ITEMS[selected_index]
                        if selected_item == 'ИТ':
                            WORDS = WORDS_IT_UPPER[topic] if count_language == 'RUS' else WORDS_IT_UPPER[1] if count_language == 'ENG' else WORDS_IT_UPPER[2]
                        elif selected_item == 'ЕДА':
                            WORDS = WORDS_FOOD_UPPER[topic] if count_language == 'RUS' else WORDS_FOOD_UPPER[1] if count_language == 'ENG' else WORDS_FOOD_UPPER[2]
                        elif selected_item == 'ТРАНСПОРТ':
                            WORDS = WORDS_TRANSPORT_UPPER[topic] if count_language == 'RUS' else WORDS_TRANSPORT_UPPER[1] if count_language == 'ENG' else WORDS_TRANSPORT_UPPER[2]
                        word = random.choice(WORDS)
                    else:
                        # Если выбранная тема не существует, выбрать случайную тему
                        selected_item = random.choice(ITEMS)
                        if selected_item == 'ИТ':
                            WORDS = WORDS_IT_UPPER[topic] if count_language == 'RUS' else WORDS_IT_UPPER[1] if count_language == 'ENG' else WORDS_IT_UPPER[2]
                        elif selected_item == 'ЕДА':
                            WORDS = WORDS_FOOD_UPPER[topic] if count_language == 'RUS' else WORDS_FOOD_UPPER[1] if count_language == 'ENG' else WORDS_FOOD_UPPER[2]
                        elif selected_item == 'ТРАНСПОРТ':
                            WORDS = WORDS_TRANSPORT_UPPER[topic] if count_language == 'RUS' else WORDS_TRANSPORT_UPPER[1] if count_language == 'ENG' else WORDS_TRANSPORT_UPPER[2]
                        word = random.choice(WORDS)

        win.blit(background_image, (0, 0))
        draw_button()
        play()
        if dropdown_open:
            draw_dropdown()
        pygame.display.update()

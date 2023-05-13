import pygame
import random
from settings import *
from words import *
from buttons import *

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Виселица 1.0")
background_image = pygame.image.load("Images/background.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
###
font = pygame.font.SysFont(FONT_TEXT, FONT_SIZE)
textbox = pygame.Surface((TEXTBOX_WIDTH, TEXTBOX_HEIGHT))
textbox.fill((200, 200, 200))
textbox_rect = textbox.get_rect(center=(WIDTH/2, HEIGHT/2 + 100))
pygame.draw.rect(textbox, WHITE, textbox.get_rect(), 2)
###
hang_man = {0: pygame.image.load('Images/hangman.png'),
            1: pygame.image.load('Images/hangman1.png'),
            2: pygame.image.load('Images/hangman2.png'),
            3: pygame.image.load('Images/hangman3.png'),
            4: pygame.image.load('Images/hangman4.png'),
            5: pygame.image.load('Images/hangman5.png'),
            6 : pygame.image.load('Images/hangman6.png'),
            7 : pygame.image.load('Images/hangman7.png'),
            8 : pygame.image.load('Images/hangman8.png'),
}
button_width, button_height = 50, 50
gap = 10  # расстояние между кнопками
x, y = gap, gap  # начальная позиция кнопок
# Создание кнопок из букв алфавита и размещение их в строках по 11 кнопок в каждой
rows = []
current_row = []
for letter in ALPHABET:
    current_row.append(letter)
    if len(current_row) == 11:
        rows.append(current_row)
        current_row = []
if current_row:
    rows.append(current_row)
# Создание кнопок на основе строк и их размещение на экране
buttons = []
button_width, button_height = 50, 50
gap = 10
x, y = gap, gap
for row in rows:
    row_width = button_width * len(row) + gap * (len(row) - 1)
    x = (800 - row_width) // 2
    y += button_height + gap
    for letter in row:
        button_rect = pygame.Rect(x, y, button_width, button_height)
        button_text = font.render(letter, True, BLACK)
        buttons.append((button_rect, button_text))
        x += button_width + gap
hang_man_count = 0
def draw_buttons():
    ''' Функция для отображения кнопок на экране '''
    # Проходит по всем кнопкам и рисует их на экране
    for button_rect, button_text in buttons:
        pygame.draw.rect(win, WHITE, button_rect)
        win.blit(button_text, button_text.get_rect(center=button_rect.center))

def handle_button_click(pos):
    ''' Функция для обработки нажатий кнопок на экране '''
    global hang_man_count
    # Принимает координаты щелчка мыши на экране (pos)
    global current_letter, guessed_letters, no_word, remaining_attempts, buttons
    for i, (button_rect, button_text) in enumerate(buttons):
        # Если координаты щелчка находятся в пределах кнопки
        if button_rect.collidepoint(pos):
            current_letter = ALPHABET[i] # Получаем текущую букву, соответствующую этой кнопке
            if current_letter not in guessed_letters:
                # Если текущая буква не присутствует в слове
                if current_letter not in word:
                    remaining_attempts -= 1
                    hang_man_count += 1
                    guessed_letters.append(current_letter)
                else:
                    guessed_letters.append(current_letter)
    draw_buttons()

# Игровые переменные
guessed_letters = [] # Угаданные буквы.
current_letter = "" # Текущая выбранная буква.
no_word = [] # Список слов, которые были использованы.
remaining_attempts = 8
def draw_word():
    '''Функция отображает текущее состояние угадываемого слова, рисуя его на экране в окне игры. '''
    global no_word
    if word not in no_word: # Если текущее слово не входит в список использованных слов.
        no_word.append(word) # Добавить в список использованных слов.
    display_word = ""
    for i, letter in enumerate(word):
        if i in no_word:
            display_word += letter # добавляем букву в строку
        elif letter in guessed_letters:
            display_word += letter # добавляем угаданную букву в строку
        else:
            display_word += ENCRYPTION # добавляем символ шифрования вместо неугаданной буквы

    if display_word:  # Проверка на пустую строку
        font = pygame.font.SysFont(FONT_TEXT, 50)
        text = font.render(display_word, True, COlOR_ENCRYPTED_WORD)
        win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2 + 10))

    # Проверяем, угаданы ли все буквы и рисуем сообщение о угадонном слове.
    if all(letter in guessed_letters for letter in word):
        get_new_word() # Получить новое слово, если все буквы были угаданы.
        message_surface = pygame.Surface((300, 100))
        message_surface.fill(WHITE)
        message_rect = message_surface.get_rect(center=(WIDTH/2, HEIGHT/2))
        pygame.draw.rect(message_surface, GREEN, message_surface.get_rect(), 5)
        message_font = pygame.font.SysFont(FONT_TEXT, 40)
        message_text = message_font.render(f"Вы угадали!", True, GREEN)
        message_surface.blit(message_text, (message_surface.get_width()/2 - message_text.get_width()/2, message_surface.get_height()/2 - message_text.get_height()/2))
        win.blit(message_surface, message_rect)
        pygame.display.update()
        pygame.time.delay(1000)
def get_new_word():
    '''Функция для получения нового слова'''
    global word, guessed_letters, remaining_attempts, no_word, hang_man_count
    if len(no_word) == len(WORDS): # Если длина использованных и слова совпадают сгенерировать новое слово
        message_surface = pygame.Surface((300, 100))
        message_surface.fill(WHITE)
        message_rect = message_surface.get_rect(center=(WIDTH/2, HEIGHT/2))
        pygame.draw.rect(message_surface, GREEN, message_surface.get_rect(), 5)
        message_font = pygame.font.SysFont(FONT_TEXT, 50)
        message_text = message_font.render("Молодец!", True, GREEN)
        message_surface.blit(message_text, (message_surface.get_width()/2 - message_text.get_width()/2, message_surface.get_height()/2 - message_text.get_height()/2))
        win.blit(message_surface, message_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        quit()
    while True: 
        word = random.choice(WORDS) # Выбор нового слова
        if word not in no_word:
            no_word.append(word)
            guessed_letters = []
            remaining_attempts = 8
            hang_man_count = 0 # Попытки
            return word

count_language = 'RUS'
# Нарисовать текстовое поле для ввода
#def draw_textbox():
#    win.blit(textbox, (WIDTH/2 - TEXTBOX_WIDTH/2, HEIGHT/2+ 70))
#    text = font.render(current_letter, True, BLACK)
#    win.blit(text, (WIDTH/2 - TEXTBOX_WIDTH/4 + 25, HEIGHT/2 + 70 + TEXTBOX_HEIGHT/4 - FONT_SIZE/4))

def language():
    '''Функция для нарисования текста о текущем языке'''
    rect = pygame.Rect(0, 5, 220, 50)
    pygame.draw.rect(win, WHITE, rect)
    pygame.draw.rect(win, BLACK, rect, 2)
    text_2 = font.render(f"{menu_language}: {count_language}", True, BLACK)
    win.blit(text_2, (10, 10))

def draw_used_letters():
    rect = pygame.Rect(400, 5, 400, 50)
    pygame.draw.rect(win, WHITE, rect)
    pygame.draw.rect(win, BLACK, rect, 2)
    text_2 = font.render(f"{' , '.join(guessed_letters)}", True, BLACK)
    win.blit(text_2, (410, 10))

def choose_your_language():
    '''Сообщение "Выберите язык"'''
    font = pygame.font.SysFont(FONT_TEXT, 50)
    text_2 = font.render(f"{choose_language}:", True, BLACK)
    win.blit(text_2, (250, 220))

def check_remaining_attempts():
    '''Функция проверки количество попыток и вывод сообщения о проигрыше'''
    global remaining_attempts, hide_message, again_button
    hide_message = False
    if remaining_attempts <= 0 and not hide_message and hang_man_count == 8: # если попыток = 0 и сообщение не скрыто
        win.blit(hang_man[hang_man_count], (200 , 50))
        message_surface = pygame.Surface((300, 100))
        message_surface.fill(WHITE)
        message_rect = message_surface.get_rect(center=(WIDTH/2, HEIGHT/2))
        pygame.draw.rect(message_surface, RED, message_surface.get_rect(), 5)
        message_font = pygame.font.SysFont(FONT_TEXT, 50)
        message_text = message_font.render("Вы проиграли!", True, RED)
        message_surface.blit(message_text, (message_surface.get_width()/2 - message_text.get_width()/2, message_surface.get_height()/2 - message_text.get_height()/2))
        win.blit(message_surface, message_rect)
        win.blit(again_button_text_img, again_button_hovered_img_rect)
        win.blit(exit_button_text_img, exit_button_hovered_img_rect)
        pygame.display.update()
        pygame.time.delay(1000)
 
def draw_screen():
    '''Функция отрисовки кнопок с языками'''
    if pygame.display.get_init():
        win.blit(button_img, button_img_rect)
        win.blit(rus_button_text_img, rus_button_img_rect)
        win.blit(eng_button_text_img, eng_button_img_rect)
        win.blit(est_button_text_img, est_button_img_rect)
        pygame.display.update()
def draw_settings():
    win.blit(setting_button_text_img,setting_button_img_rect)
# Цикл меню
game_running = False
menu_running = True
setting_running = False
while True:
    if menu_running:
        for event in pygame.event.get():
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
                    WORDS, ALPHABET = WORDS_RUS, ALPHABET_RUS
                    word = random.choice(WORDS)
                    count_language, menu_language, choose_language, remaining_tries = "RUS", 'Язык','Выберите язык', 'Попытки'
                if eng_button.collidepoint(event.pos):
                    WORDS, ALPHABET = WORDS_ENG, ALPHABET_ENG
                    word = random.choice(WORDS)
                    count_language,menu_language,choose_language, remaining_tries = "ENG",'Language','Choose language', 'Attempts'
                if est_button.collidepoint(event.pos):
                    WORDS, ALPHABET = WORDS_EST, ALPHABET_EST
                    word = random.choice(WORDS)
                    count_language,menu_language,choose_language, remaining_tries = "EST",'Keel','Valige keel', 'Katsed'
                if button.collidepoint(event.pos):
                    menu_running = False
                    game_running = True
                    current_letter = ""
                    guessed_letters = []
                    remaining_attempts = 8
                    hang_man_count = 0
                    word = random.choice(WORDS)
    # Отрисовка всех элементов
            pygame.time.delay(100)
            win.blit(background_image, (0, 0))
            draw_screen()
            choose_your_language()
            language()
            draw_settings()
            pygame.display.update()

# Цикл игры
    if game_running:
        # Нарисовать кнопки с положением
        buttons = []
        for i, letter in enumerate(ALPHABET):
            button_rect = pygame.Rect(140 + i % 11 * 50, 360 + i // 11 * 50, 40, 40)
            button_text = font.render(letter, True, BLACK)
            buttons.append((button_rect, button_text))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pressed_letter = handle_button_click(event.pos)
                if again_button.collidepoint(event.pos) and remaining_attempts <= 0:
                    hide_message = True
                    current_letter = ""
                    guessed_letters = []
                    no_word.clear()
                    remaining_attempts = 8
                    hang_man_count = 0
                    word = random.choice(WORDS)
                if exit_button.collidepoint(event.pos) and remaining_attempts <= 0:
                    game_running = False
                    menu_running = True
                    hang_man_count = 0
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
        if remaining_attempts != 0: # Если попыток не равно 0 рисовать эти элементи.
            win.blit(hang_man[hang_man_count], (200 , 50))
            language()
    #       draw_textbox()
            draw_buttons()
            draw_word()
            draw_used_letters()
            draw_settings()
            pygame.display.update()
    if setting_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_settings()
import pygame
import random
from settings import *
from words import *
from buttons import *

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Виселица 2.0")
background_image = pygame.image.load("Images/background.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
###
font = pygame.font.SysFont(FONT_TEXT, FONT_SIZE)
textbox = pygame.Surface((TEXTBOX_WIDTH, TEXTBOX_HEIGHT))
textbox.fill((200, 200, 200))
textbox_rect = textbox.get_rect(center=(WIDTH/2, HEIGHT/2 + 100))
pygame.draw.rect(textbox, WHITE, textbox.get_rect(), 2)
# Загрузка картинок и присвоение каждой картинке свой ключ.
hang_man = {0: pygame.image.load('Images/hangman.png'),
            1: pygame.image.load('Images/hangman1.png'),
            2: pygame.image.load('Images/hangman2.png'),
            3: pygame.image.load('Images/hangman3.png'),
            4: pygame.image.load('Images/hangman4.png'),
            5: pygame.image.load('Images/hangman5.png'),
            6 : pygame.image.load('Images/hangman6.png'),
            7 : pygame.image.load('Images/hangman7.png'),
            8 : pygame.image.load('Images/hangman8.png')}
button_width, button_height = 50, 50
gap = 10  # расстояние между кнопками
x, y = gap, gap  # начальная позиция кнопок
# Создание кнопок из букв алфавита и размещение их в строках по 11 кнопок в каждой.
rows = [] # Список строк
current_row = [] # Текущая строка
for letter in ALPHABET:
    current_row.append(letter)
    if len(current_row) == 11:  # Если текущая строка заполнилась
        rows.append(current_row)  # Добавляем ее в список строк
        current_row = []  # Обнуляем текущую строку для следующей
if current_row: # Если последняя строка не пуста
    rows.append(current_row)
# Создание кнопок на основе строк и их размещение на экране
buttons = [] # Список кнопок
for row in rows:
    row_width = button_width * len(row) + gap * (len(row) - 1) # Ширина строки
    x = (WIDTH - row_width) // 2 # Позиция по горизонтали
    y += button_height + gap # Переходим на следующую строку по вертикали
    for letter in row:
        button_rect = pygame.Rect(x, y, button_width, button_height)
        button_text = font.render(letter, True, BLACK)
        buttons.append((button_rect, button_text))
        x += button_width + gap # Переходим к следующей кнопке по горизонтали

hang_man_count = 0 # Начальная картинка.

def draw_buttons():
    ''' Функция для отображения кнопок на экране.'''
    # Проходит по всем кнопкам и рисует их на экране
    for i, (button_rect, button_text) in enumerate(buttons):
        letter = ALPHABET[i]  # Получаем символ кнопки из алфавита
        if letter in guessed_letters:
            if letter in word:
                pygame.draw.rect(win, GREEN, button_rect)
            else:
                pygame.draw.rect(win, RED, button_rect)
        else:
            pygame.draw.rect(win, WHITE, button_rect)
        text_surface = font.render(letter, True, BLACK)
        text_rect = text_surface.get_rect(center=button_rect.center)
        win.blit(text_surface, text_rect)

def handle_button_click(pos):
    ''' Функция для обработки нажатий кнопок на экране.'''
    global hang_man_count
    global current_letter, guessed_letters, no_word, remaining_attempts, buttons

    for i, (button_rect, button_text) in enumerate(buttons):
        # Если координаты щелчка находятся в пределах кнопки
        if button_rect.collidepoint(pos):
            current_letter = ALPHABET[i] # Получаем текущую букву, соответствующую этой кнопке
            if current_letter not in guessed_letters: # Если текущая буква еще не угадана
                guessed_letters.append(current_letter)
                if current_letter not in word: # Если текущая буква не присутствует в загаданном слове
                    remaining_attempts -= 1 # Уменьшаем количество оставшихся попыток
                    hang_man_count += 1 # Увеличиваем счетчик картинок
                    button_text_color = RED # Цвет текста кнопки - красный (неправильная буква)
                else:
                    button_text_color = GREEN # Цвет текста кнопки - зеленый (правильная буква)
            else:
                # Буква уже угадана
                button_text_color = WHITE
            
            pygame.draw.rect(win, button_text_color, button_rect)
            text_surface = font.render(ALPHABET[i], True, BLACK)
            text_rect = text_surface.get_rect(center=button_rect.center)
            win.blit(text_surface, text_rect)

# Игровые переменные
guessed_letters = [] # Угаданные буквы.
current_letter = "" # Текущая выбранная буква.
no_word = [] # Список слов, которые были использованы.
remaining_attempts = 8 # Попытки

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
        text = font.render(display_word, True, COlOR_ENCRYPTED_WORD)
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
            hang_man_count = 0 # Вернуть изначальную картинку
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

def draw_used_letters():
    '''Функция для нарисования использованных букв'''
    rect = pygame.Rect(400, 5, 400, 50)
    pygame.draw.rect(win, WHITE, rect)
    pygame.draw.rect(win, BLACK, rect, 2)
    text_2 = font.render(f"{' , '.join(guessed_letters)}", True, BLACK)
    win.blit(text_2, (410, 10))

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
                    count_language, menu_language, choose_language, remaining_tries,choose_topic = "RUS", 'Язык','Выберите язык', 'Попытки','Выберите тему'
                    game_over,victory = 'Вы проиграли!','Молодец!'
                if eng_button.collidepoint(event.pos):
                    ALPHABET = ALPHABET_ENG
                    ITEMS = ['IT','FOOD','TRANSPORT']
                    count_language,menu_language,choose_language, remaining_tries,choose_topic = "ENG",'Language','Choose language', 'Attempts','Choose a theme'
                    victory = 'Well done!'
                if est_button.collidepoint(event.pos):
                    ALPHABET = ALPHABET_EST
                    ITEMS = ['IT', 'TOIT', 'TRANSPORT']
                    count_language,menu_language,choose_language, remaining_tries,choose_topic = "EST",'Keel','Valige keel', 'Katsed',"Vali teema"
                    victory =  "Hästi tehtud!"
                if button.collidepoint(event.pos):
                    menu_running = False
                    topic_selection = True
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
            play()
            draw_settings()
            pygame.display.update()

    # Игра
    if game_running:
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
                pressed_letter = handle_button_click(event.pos)
                if again_button.collidepoint(event.pos) and remaining_attempts <= 0: # Работает когда нажата кнопка и попыток 0.
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
        if remaining_attempts != 0: # Если попыток не равно 0 рисовать эти элементы.
            win.blit(hang_man[hang_man_count], (200 , 50))
            language()
    #       draw_textbox()
            draw_buttons()
            draw_word()
            draw_used_letters()
            draw_settings()
            pygame.display.update()
    # Настройки
    if setting_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_settings()
    # Тема
    if topic_selection:
        topic = 0
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
                            dropdown_open = False #Закритие выпадающего списка
                            if ITEMS[selected_index] == 'ИТ':
                                WORDS = WORDS_IT_UPPER[topic] if count_language == 'RUS' else WORDS_IT_UPPER[1] if count_language == 'ENG' else WORDS_IT_UPPER[2]
                            if ITEMS[selected_index] == 'ЕДА':
                                WORDS = WORDS_FOOD_UPPER[topic] if count_language == 'RUS' else WORDS_FOOD_UPPER[1] if count_language == 'ENG' else WORDS_FOOD_UPPER[2]
                            if ITEMS[selected_index] == 'ТРАНСПОРТ':
                                WORDS = WORDS_TRANSPORT_UPPER[topic] if count_language == 'RUS' else WORDS_TRANSPORT_UPPER[1] if count_language == 'ENG' else WORDS_TRANSPORT_UPPER[2]

                if button.collidepoint(event.pos):
                    topic_selection = False
                    game_running = True
                    current_letter = ""
                    guessed_letters = []
                    remaining_attempts = 8
                    hang_man_count = 0
                    word = random.choice(WORDS)
        win.blit(background_image, (0, 0))
        draw_button()
        play()
        if dropdown_open:
            draw_dropdown()
        pygame.display.update()

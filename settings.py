import pygame
from words import *
# Окно.
pygame.init()
WIDTH = 800
HEIGHT = 600
# Допустимые символы.
ENCRYPTION = "_" + ' '

# Шрифт и размер.
FONT_SIZE = 32
FONT_TEXT = "Arial"
TEXTBOX_WIDTH = 150
TEXTBOX_HEIGHT = 40
COlOR_ENCRYPTED_WORD = (0, 0, 0)

# Слова
WORDS = WORDS_IT # Слова по умолчанию
ALPHABET = ALPHABET_RUS # Буквы по умолчанию

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0, 255, 0)
RED = (255,0,0)
YELLOW = (255, 255, 0)

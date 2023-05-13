import pygame
pygame.init()
font = pygame.font.SysFont('Arial', 50)
menu_language, choose_language,remaining_tries  = 'Язык', 'Выберите язык', 'Попытки'
language_surface = font.render(menu_language, True, (0, 0, 0))
choose_language_surface = font.render(choose_language, True, (0, 0, 0))
WORDS_RUS = ['мама', 'папа', 'дед']
WORDS_ENG = ['mom', 'dad', 'grandfather']
WORDS_EST = ['ema', 'isa', 'vend','vanaisa','õde']
ALPHABET_RUS = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]
ALPHABET_ENG = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
ALPHABET_EST = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "Š", "Z", "Ž", "T", "U", "V", "W", "Õ", "Ä", "Ö", "Ü", "X", "Y"]
ENGLISH_KEY_CODES = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z]
ESTONIAN_KEY_CODES = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z, pygame.K_SEMICOLON, pygame.K_PLUS, pygame.K_KP_MULTIPLY, pygame.K_QUOTE, pygame.K_COMMA, pygame.K_o, pygame.K_PERIOD, pygame.K_u, pygame.K_ASTERISK, pygame.K_o]

WORDS = []
WORDS_RUS = [word.upper() for word in WORDS_RUS]
WORDS_ENG = [word.upper() for word in WORDS_ENG]
WORDS_EST = [word.upper() for word in WORDS_EST]

WORDS.extend(WORDS_RUS)
WORDS.extend(WORDS_ENG)
WORDS.extend(WORDS_EST)




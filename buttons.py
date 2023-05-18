import pygame
from settings import *

pygame.init()
###
button = pygame.Rect(WIDTH/2-100, HEIGHT/2+100, 200, 70)
button_img = pygame.image.load('Images/Start.png')
button_img_rect = button_img.get_rect(center=button.center)
button_hovered_img_rect = button_img_rect.inflate(0, 30)
###
rus_button = pygame.Rect(180, 300, 180, 50)
rus_button_img = pygame.image.load('Images/RUS.png')
rus_button_text_img = pygame.Surface(rus_button_img.get_size(), pygame.SRCALPHA)
rus_button_text_img.blit(rus_button_img, (0, 0))
rus_button_img_rect = rus_button_img.get_rect(center=rus_button.center)
rus_button_hovered_img_rect = rus_button_img_rect.inflate(0, 30)
###
eng_button = pygame.Rect(320, 300, 170, 50)
eng_button_img = pygame.image.load('Images/ENG.png')
eng_button_text_img = pygame.Surface(eng_button_img.get_size(), pygame.SRCALPHA)
eng_button_text_img.blit(eng_button_img, (0, 0))
eng_button_img_rect = eng_button_img.get_rect(center=eng_button.center)
eng_button_hovered_img_rect = eng_button_img_rect.inflate(0, 30)
###
est_button = pygame.Rect(460, 300, 170, 50)
est_button_img = pygame.image.load('Images/EST.png')
est_button_text_img = pygame.Surface(est_button_img.get_size(), pygame.SRCALPHA)
est_button_text_img.blit(est_button_img, (0, 0))
est_button_img_rect = est_button_img.get_rect(center=est_button.center)
est_button_hovered_img_rect = est_button_img_rect.inflate(0, 30)
###
again_button = pygame.Rect(400, 400, 200, 70)
again_button_img = pygame.image.load('Images/Again.png')
again_button_text_img = pygame.Surface(again_button_img.get_size(), pygame.SRCALPHA)
again_button_text_img.blit(again_button_img, (0, 0))
again_button_img_rect = again_button_img.get_rect(center=again_button.center)
again_button_hovered_img_rect = again_button_img_rect.inflate(0, 30)
###
exit_button = pygame.Rect(200, 400, 200, 70)
exit_button_img = pygame.image.load('Images/Exit_to_menu.png')
exit_button_text_img = pygame.Surface(exit_button_img.get_size(), pygame.SRCALPHA)
exit_button_text_img.blit(exit_button_img, (0, 0))
exit_button_img_rect = exit_button_img.get_rect(center=exit_button.center)
exit_button_hovered_img_rect = exit_button_img_rect.inflate(0, 30)
###
setting_button = pygame.Rect(200, 400, 1100, -600)
setting_button_img = pygame.image.load('Images/Settings.png')
setting_button_text_img = pygame.Surface(setting_button_img.get_size(), pygame.SRCALPHA)
setting_button_text_img.blit(setting_button_img, (0, 0))
setting_button_img_rect = setting_button_img.get_rect(center=setting_button.center)
setting_button_hovered_img_rect = setting_button_img_rect.inflate(0, 30)
###
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 40

# Определение размеров выпадающего списка
DROPDOWN_WIDTH = BUTTON_WIDTH
DROPDOWN_HEIGHT = BUTTON_HEIGHT * 3
# Определение координат кнопки
BUTTON_X = (WIDTH - BUTTON_WIDTH) // 2
BUTTON_Y = (HEIGHT - BUTTON_HEIGHT - DROPDOWN_HEIGHT) // 2
# Определение координат выпадающего списка
DROPDOWN_X = BUTTON_X
DROPDOWN_Y = BUTTON_Y + BUTTON_HEIGHT
ITEMS = ['ИТ', 'ЕДА', 'ТРАНСПОРТ']

# Флаг для отслеживания открытия/закрытия выпадающего списка
dropdown_open = False

# Индекс выбранного элемента
selected_index = None



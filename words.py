import pygame
pygame.init()
font = pygame.font.SysFont('Arial', 50)
menu_language, choose_language, remaining_tries, choose_topic, topic_language, clue_text, quantity = 'Язык', 'Выберите язык', 'Попытки', 'Выберите тему', 'Тема', 'Подсказка', 'Количество попыток'
victory = 'Молодец!'
language_surface = font.render(menu_language, True, (0, 0, 0))
choose_language_surface = font.render(choose_language, True, (0, 0, 0))
ALPHABET_RUS = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н",
                "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]
ALPHABET_ENG = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
ALPHABET_EST = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
                "P", "Q", "R", "S", "Š", "Z", "Ž", "T", "U", "V", "W", "Õ", "Ä", "Ö", "Ü", "X", "Y"]
ENGLISH_KEY_CODES = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l,
                     pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z]
ESTONIAN_KEY_CODES = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s,
                      pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z, pygame.K_SEMICOLON, pygame.K_PLUS, pygame.K_KP_MULTIPLY, pygame.K_QUOTE, pygame.K_COMMA, pygame.K_o, pygame.K_PERIOD, pygame.K_u, pygame.K_ASTERISK, pygame.K_o]

WORDS = {
    'RUS': {
        'ИТ': ["Программирование", "Алгоритм", "Кодирование", "Разработка", "Код", "Интернет", "Компьютер", "Сервер", "Кибербезопасность"],
        'ЕДА': ["Яблоко", "Помидор", "Апельсин", "Банан", "Морковь", "Огурец", "Груша", "Персик", "Киви", "Свекла"],  
        'ТРАНСПОРТ': ["Автомобиль", "Поезд", "Самолет", "Велосипед", "Мотоцикл", "Автобус", "Трамвай", "Такси", "Корабль", "Грузовик"],
        'БЛЮДА': ["Пицца", "Спагетти", "Суши", "Стейк", "Салат", "Бургер", "Паста", "Роллы", "Суп", "Рыба"]
    },
    'ENG': {
        'IT': ["Programming", "Algorithm", "Coding", "Development", "Website", "Database", "Internet", "Computer", "Server", "Cybersecurity"],
        'FOOD': ["Apple", "Tomato", "Orange", "Banana", "Carrot", "Cucumber", "Pear", "Peach", "Kiwi", "Beetroot"],  
        'TRANSPORT': ["Car", "Train", "Airplane", "Bicycle", "Motorcycle", "Bus", "Tram", "Taxi", "Ship", "Truck"],
        'DISHES': ["Pizza", "Spaghetti", "Sushi", "Steak", "Salad", "Burger", "Pasta", "Rolls", "Soup", "Fish"]
    },
    'EST': {
        'IT': ["Programmeerimine", "Algoritm", "Kodeerimine", "Arendus", "Veebileht", "Andmebaas", "Internet", "Arvuti", "Server", "Küberkaitse"],
        'TOIT': ["Õun", "Tomat", "Apelsin", "Banaan", "Porgand", "Kurk", "Pirn", "Virsik", "Kiivi", "Punapeet"],  
        'TRANSPORT': ["Auto", "Rong", "Lennuk", "Jalgratas", "Mootorratas", "Buss", "Tramm", "Taks", "Laev", "Veoauto"],
        'NÕUD': ["Pizza", "Spagetid", "Sushi", "Steik", "Salat", "Burger", "Pasta", "Rullid", "Supp", "Kala"]
    }
}

#WORDS_FOOD = {
#    0: ["Яблоко", "Помидор", "Апельсин", "Банан", "Морковь", "Огурец", "Груша", "Персик", "Киви", "Свекла"],
#    1: ["Apple", "Tomato", "Orange", "Banana", "Carrot", "Cucumber", "Pear", "Peach", "Kiwi", "Beetroot"],
#    2: ["Õun", "Tomat", "Apelsin", "Banaan", "Porgand", "Kurk", "Pirn", "Virsik", "Kiivi", "Punapeet"]
#}

#WORDS_TRANSPORT = {
#    0: ["Автомобиль", "Поезд", "Самолет", "Велосипед", "Мотоцикл", "Автобус", "Трамвай", "Такси", "Корабль", "Грузовик"],
#    1: ["Car", "Train", "Airplane", "Bicycle", "Motorcycle", "Bus", "Tram", "Taxi", "Ship", "Truck"],
#    2: ["Auto", "Rong", "Lennuk", "Jalgratas", "Mootorratas", "Buss", "Tramm", "Taks", "Laev", "Veoauto"]
#}

#WORDS_IT = {
#    0: ["Программирование", "Алгоритм", "Кодирование", "Разработка", "Веб-сайт", "Код", "Интернет", "Компьютер", "Сервер", "Кибербезопасность"],
#    1: ["Programming", "Algorithm", "Coding", "Development", "Website", "Database", "Internet", "Computer", "Server", "Cybersecurity"],
#    2: ["Programmeerimine", "Algoritm", "Kodeerimine", "Arendus", "Veebileht", "Andmebaas", "Internet", "Arvuti", "Server", "Küberkaitse"]
#}

#WORDS_DISHES = {
#    0: ["Пицца", "Спагетти", "Суши", "Стейк", "Салат", "Бургер", "Паста", "Роллы", "Суп", "Рыба"],
#    1: ["Pizza", "Spaghetti", "Sushi", "Steak", "Salad", "Burger", "Pasta", "Rolls", "Soup", "Fish"],
#    2: ["Pizza", "Spagetid", "Sushi", "Steik", "Salat", "Burger", "Pasta", "Rullid", "Supp", "Kala"]
#}
# Объединение всех слов в один список
def upper(dictionary):
    for lang in dictionary.values():
        for category in lang.values():
            for i in range(len(category)):
                category[i] = category[i].upper()
upper(WORDS)

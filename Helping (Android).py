# HELPING — Android / Pydroid FULL
# Python 3.13 | Offline | One file | Anonymous

import hashlib
from datetime import datetime

# ===================== BANNER =====================

BANNER = """
==============================
        HELPING
 Offline Emergency Helper
==============================
"""

# ===================== LANG =====================

LANG = {
    "ua": {
        "menu": "Оберіть дію:",
        "options": [
            "Обстріл / бомбардування",
            "Укриття та підвал",
            "Евакуація",
            "Перша медична допомога",
            "Блокпост",
            "Полон",
            "Відсутній зв'язок",
            "Тривожний рюкзак",
            "SOS-лог (анонімно)",
            "Вийти"
        ]
    },
    "ru": {
        "menu": "Выберите действие:",
        "options": [
            "Обстрел / бомбардировка",
            "Укрытие и подвал",
            "Эвакуация",
            "Первая медицинская помощь",
            "Блокпост",
            "Плен",
            "Нет связи",
            "Тревожный рюкзак",
            "SOS-лог (анонимно)",
            "Выход"
        ]
    },
    "en": {
        "menu": "Choose an action:",
        "options": [
            "Shelling / bombing",
            "Shelter / basement",
            "Evacuation",
            "First aid",
            "Checkpoint",
            "Captivity",
            "No connection",
            "Emergency backpack",
            "SOS log (anonymous)",
            "Exit"
        ]
    }
}

# ===================== FULL GUIDES =====================

GUIDES = {

"shelling": {
"ua": """
• Негайно лягти або сховатися
• Подалі від вікон, дзеркал, техніки
• Рот злегка відкрити (зменшує тиск)
• Руки прикривають голову і шию
• Не бігти під час вибухів
• Не користуватися ліфтом
• Після тиші чекати 5–10 хв
• Обережно виходити (можливі повторні удари)
""",
"ru": """
• Немедленно лечь или укрыться
• Держаться подальше от окон
• Рот слегка приоткрыт
• Прикрыть голову и шею
• Не бежать во время взрывов
• Не пользоваться лифтом
• После тишины ждать 5–10 минут
• Возможны повторные удары
""",
"en": """
• Immediately get down or take cover
• Stay away from windows and glass
• Keep mouth slightly open
• Protect head and neck
• Do not run during explosions
• Do not use elevators
• Wait 5–10 minutes after silence
• Secondary strikes possible
"""
},

"shelter": {
"ua": """
• Найкраще: метро, бетонний підвал
• Без вікон і з двома виходами
• Не ховатися під авто
• Тримати воду і аптечку
• Сидіти подалі від входу
""",
"ru": """
• Лучшее: метро, бетонный подвал
• Без окон, два выхода
• Не прятаться под авто
• Иметь воду и аптечку
• Держаться подальше от входа
""",
"en": """
• Best: metro, concrete basement
• No windows, two exits
• Do not hide under vehicles
• Keep water and first aid
• Stay away from entrances
"""
},

"evac": {
"ua": """
• Документи, гроші, телефон
• Повідомити рідних
• Вдягти зручний одяг
• Взяти мінімум речей
• Слідувати офіційним маршрутам
• Не сперечатися з військовими
""",
"ru": """
• Документы, деньги, телефон
• Сообщить близким
• Удобная одежда
• Минимум вещей
• Следовать официальным маршрутам
• Не спорить с военными
""",
"en": """
• Documents, money, phone
• Inform relatives
• Comfortable clothes
• Take minimal items
• Follow official routes
• Do not argue with military
"""
},

"aid": {
"ua": """
• Кровотеча — турнікет / тиск
• Поранення — не діставати уламки
• Опік — вода 10–15 хв
• Перелом — іммобілізація
• Шок — тепло, спокій
• Не давати алкоголь
""",
"ru": """
• Кровотечение — жгут / давление
• Ранение — не извлекать осколки
• Ожог — вода 10–15 минут
• Перелом — фиксация
• Шок — тепло и покой
• Не давать алкоголь
""",
"en": """
• Bleeding — tourniquet / pressure
• Wounds — do not remove fragments
• Burns — cool 10–15 minutes
• Fractures — immobilize
• Shock — warmth and calm
• No alcohol
"""
},
"checkpoint": {
"ua": """
• Повільно підійти
• Руки на видноті
• Не робити різких рухів
• Відповідати чітко
• Телефон сховати
""",
"ru": """
• Медленно подходить
• Руки на виду
• Без резких движений
• Отвечать кратко
• Телефон убрать
""",
"en": """
• Approach slowly
• Keep hands visible
• No sudden moves
• Answer clearly
• Put phone away
"""
},

"captivity": {
"ua": """
• Зберігати спокій
• Не сперечатися
• Запам'ятовувати деталі
• Не провокувати
• Думати про виживання
""",
"ru": """
• Сохранять спокойствие
• Не спорить
• Запоминать детали
• Не провоцировать
• Думать о выживании
""",
"en": """
• Stay calm
• Do not argue
• Memorize details
• Do not provoke
• Focus on survival
"""
},

"noconn": {
"ua": """
• Економити заряд
• Увімкнути режим енергоощадження
• Домовитися про офлайн-план
• Записувати інформацію
""",
"ru": """
• Экономить заряд
• Включить энергосбережение
• Договориться об офлайн-плане
• Записывать информацию
""",
"en": """
• Save battery
• Enable power saving
• Agree on offline plan
• Write down information
"""
},

"bag": {
"ua": """
• Документи + копії
• Вода (2–3 л)
• Аптечка
• Ліхтарик
• Павербанк
• Теплий одяг
• Ніж / мультитул
""",
"ru": """
• Документы + копии
• Вода (2–3 л)
• Аптечка
• Фонарик
• Пауэрбанк
• Тёплая одежда
• Нож / мультитул
""",
"en": """
• Documents + copies
• Water (2–3 L)
• First aid kit
• Flashlight
• Power bank
• Warm clothes
• Knife / multitool
"""
}
}

KEYS = ["shelling","shelter","evac","aid","checkpoint","captivity","noconn","bag"]

# ===================== UTILS =====================

def clear():
    print("\n" * 40)

def pause():
    input("\n[ENTER]")

def hash_pass(p):
    return hashlib.sha256(p.encode()).hexdigest()

# ===================== SOS LOG =====================

def sos_log():
    clear()
    print("=== SOS LOG ===\n")
    text = input("Write message:\n> ")

    protect = input("\nSet password? (y/n): ").lower()
    password = None
    if protect == "y":
        password = hash_pass(input("Password: "))

    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fname = f"sos_{ts}.txt"

    with open(fname, "w", encoding="utf-8") as f:
        if password:
            f.write("[PROTECTED]\nHASH:" + password + "\n\n")
        f.write("TIME: " + ts + "\n\n" + text)

    print("\nSaved locally:", fname)
    pause()

# ===================== MAIN =====================

def main():
    clear()
    print(BANNER)
    print("1 — Українська\n2 — Русский\n3 — English")

    choice = input("> ").strip()
    lang = "ua" if choice == "1" else "ru" if choice == "2" else "en"

    while True:
        clear()
        print(BANNER)
        print(LANG[lang]["menu"])
        for i, opt in enumerate(LANG[lang]["options"], 1):
            print(f"{i}. {opt}")

        c = input("> ").strip()

        if c.isdigit() and 1 <= int(c) <= 8:
            print(GUIDES[KEYS[int(c)-1]][lang])
            pause()
        elif c == "9":
            sos_log()
        elif c == "10":
            break

if __name__ == "__main__":
    main()

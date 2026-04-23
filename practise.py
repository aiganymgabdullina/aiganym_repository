import random
class Player:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.health = 100
        self.mood = 100

    def is_alive(self):
        return self.health > 0 and self.mood > 0

    def update_stats(self, m=0, h=0, mood=0):
        self.money += m
        self.health = min(max(self.health + h, 0), 100)
        self.mood = min(max(self.mood + mood, 0), 100)


def play_simulation():
    hero = Player("Айганым")
    events = [
        {"desc": "Вы нашли кошелек!", "m": 50, "h": 0, "mood": 10},
        {"desc": "Плохая еда в столовой...", "m": 0, "h": -20, "mood": -10},
        {"desc": "Премия на работе!", "m": 100, "h": -10, "mood": 20},
        {"desc": "Вы проспали всё на свете.", "m": -20, "h": 10, "mood": -10}
    ]

    for turn in range(1, 11):
        if not hero.is_alive():
            print(f"\nИгра окончена на {turn} ходу. Ресурсы исчерпаны.")
            break

        print(f"\n=== Ход {turn} ===")
        print(f"Статус: Деньги {hero.money}, Здоровье {hero.health}, Настроение {hero.mood}")
        event = random.choice(events)
        print(f"Событие: {event['desc']}")
        hero.update_stats(event['m'], event['h'], event['mood'])
        print("1. Работать (+++$, -HP) | 2. Отдыхать (-$, +HP, +Mood)")
        choice = input("Ваш ход: ")

        if choice == "1":
            hero.update_stats(m=40, h=-15, mood=-5)
        elif choice == "2":
            hero.update_stats(m=-30, h=20, mood=25)

    if hero.is_alive():
        print(f"\nВыживание успешно! Итоговый капитал: {hero.money}")
play_simulation()
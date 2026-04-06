#1 esep
from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)
#1 esep
class Player:
    def __init__(self, player_id: int, name: str, hp: int):
        self._id = player_id
        self._name = name.strip().title()
        self.inventory = Inventory()

        if hp < 0:
            self._hp = 0
        else:
            self._hp = hp

    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"

    def __del__(self):
        print(f"Player {self._name} удалён")

#2 esep
    @classmethod
    def from_string(cls, data: str):
        parts = data.split(',')

        if len(parts) != 3:
            raise ValueError("Неверный формат строки")

        try:
            player_id = int(parts[0].strip())
            name = parts[1].strip()
            hp = int(parts[2].strip())
        except:
            raise ValueError("Ошибка преобразования данных")

        return cls(player_id, name, hp)

@app.route('/')
def home():
    return "Сервер работает"
@app.route('/player')
def player_info():
    p = Player(1, " john ", 120)
    return str(p)
@app.route('/player-from-string')
def player_from_string():
    try:
        p = Player.from_string("2, alice , 90")
        return str(p)
    except ValueError as e:
        return f"Ошибка: {e}"

#3 esep
class Item:
    def __init__(self, item_id: int, name: str, power: int):
        self.id = item_id
        self.name = name.strip().title()
        self.power = power

    def __str__(self):
        return f"Item(id={self.id}, name='{self.name}', power={self.power})"

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

@app.route('/item')
def item_info():
    i = Item(1, " Sword ", 50)
    return str(i)

#4 esep
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        for i in self.items:
            if i.id == item.id:
                return
        self.items.append(item)

    def remove_item(self, item_id: int):
        self.items = [i for i in self.items if i.id != item_id]

    def get_items(self):
        return self.items

    def unique_items(self):
        return set(self.items)

    def to_dict(self):
        return {item.id: item for item in self.items}

    # 5 esep
    def get_strong_items(self, min_power: int):
        return ([item for item in self.items if item.power >= min_power])

@app.route('/inventory')
def inventory_test():
    inv = Inventory()
    inv.add_item(Item(1, "Sword", 50))
    inv.add_item(Item(2, "Shield", 30))
    result = ""
    for item in inv.get_items():
        result += str(item) + "\n"
    result += "Уникальных: " + str(len(inv.unique_items()))
    return result

@app.route('/strong-items')
def strong_items():
    inv = Inventory()
    inv.add_item(Item(1, "Sword", 50))
    inv.add_item(Item(2, "Shield", 30))
    inv.add_item(Item(3, "Axe", 70))

    return "<br>".join(str(i) for i in inv.get_strong_items(50))

#6 esep
from datetime import datetime
class Event:
    def __init__(self, event_type: str, data: dict):
        self.type = event_type
        self.data = data
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Event(type='{self.type}', data={self.data}, timestamp='{self.timestamp}')"

@app.route('/event')
def event_test():
    e = Event("ATTACK", {"damage": 20})
    return str(e)


#7 esep
class Warrior(Player):
    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            damage = int(damage * 0.9)  # -10%
            self._hp -= damage
        else:
            super().handle_event(event)


class Mage(Player):
    def handle_event(self, event):
        if event.type == "LOOT":
            item = event.data.get("item")
            if item:
                item.power = int(item.power * 1.1)  # +10%
                self.inventory.add_item(item)
        else:
            super().handle_event(event)

@app.route('/event-test')
def event_test_route():
    w = Warrior(1, "Aiganym", 100)
    m = Mage(2, "Akzhan", 100)

    attack = Event("ATTACK", {"damage": 50})
    loot = Event("LOOT", {"item": Item(1, "Sword", 50)})

    w.handle_event(attack)
    m.handle_event(loot)
    return f"Warrior HP: {w._hp}<br>Mage Item Power: {m.inventory.get_items()[0].power}"

#8 esep
class Logger:
    def log(self, event, player, filename: str):
        line = f"{event.timestamp};{player._id};{event.type};{event.data}\n"

        with open(filename, "a", encoding="utf-8") as f:
            f.write(line)
#9 esep
    def read_logs(self, filename: str):
        events = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(";")
                if len(parts) != 4:
                    continue

                timestamp = parts[0]
                player_id = int(parts[1])
                event_type = parts[2]
                data = eval(parts[3])
                e = Event(event_type, data)
                e.timestamp = timestamp
                events.append(e)

        return events

@app.route('/log-test')
def log_test():
    p = Player(1, "Aiganym", 100)
    e = Event("ATTACK", {"damage": 50})
    logger = Logger()
    logger.log(e, p, "log.txt")
    return "Событие записано"

@app.route('/read-logs')
def read_logs():
    logger = Logger()
    events = logger.read_logs("log.txt")
    result = ""
    for e in events:
        result += str(e) + "<br>"
    return result

if __name__ == '__main__':
    app.run(port=5001)
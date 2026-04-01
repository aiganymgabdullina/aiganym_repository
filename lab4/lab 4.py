#1 esep
from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

class Player:
    def __init__(self, player_id: int, name: str, hp: int):
        self._id = player_id
        self._name = name.strip().title()

        if hp < 0:
            self._hp = 0
        else:
            self._hp = hp

    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"

    def __del__(self):
        print(f"Player {self._name} удалён")
@app.route('/')
def home():
    return "Сервер работает"
@app.route('/player')
def player_info():
    p = Player(1, " john ", 120)
    return str(p)

#2 esep
class PlayerString(Player):
    @classmethod
    def from_string(cls, data: str):
        parts = data.split(',')

        if len(parts) != 3:
            return "Ошибка: неверный формат"

        try:
            player_id = int(parts[0].strip())
            name = parts[1].strip()
            hp = int(parts[2].strip())
        except:
            return "Ошибка: данные не корректны"

        return cls(player_id, name, hp)

@app.route('/player-from-string')
def player_from_string():
    p = PlayerString.from_string("2, alice , 90")
    return str(p)

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

if __name__ == '__main__':
    app.run(port=5001)
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

def create_player():
    return Player(1, " john ", 120)

@app.route('/')
def home():
    return "Сервер работает"

@app.route('/player')
def player_info():
    p = create_player()
    return str(p)

if __name__ == '__main__':
    app.run(port=5001)
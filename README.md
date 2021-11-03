# Battleship-API
SphereMall Assignment: Battleship API v1

# Design

To design the battleship API I started off by modelling the game by using Class-responsibility-collaboration (CRC) cards as a brainstorming tool.
We have the following cards: Board, Player, Game

## Board
Responsibility:
The board should represent the state of the board.
The board should validate the board.

Collaboration:
A board has players

## Player
Responsibility:
The player ties the game and the board together

Collaboration:
A player has a game

## Game
Responsibility:
Couple players and their action
When both players are in a game, they shoot in turns untill one of the players has no ships.
At first game is a NEW State. After another player joins in, it is in PLAYING state. When one of the players has no ships left it switches to the FINISHED state.

Collaboration:
A game has a Player

# Enity Diagrams
![enitity-diagram](https://user-images.githubusercontent.com/15825757/140053838-186432c3-1872-40d6-aa6a-2bed2f47ba40.png)

# How to run
requirements:
Python3.X
pip


Start API
```
git clone https://github.com/BugOrFeature/Battleship-API.git
cd Battleship-API

pip install virtualenv
virtualenv venv
source ./venv/bin/activate

pip install -r requirements.txt
flask db init
flask db migrate
flask db upgrade

flask run
```
Run tests

Make sure the API is running locally with flask run
```
python -m pytest tests
```

# Routes / Examples
api.create_game   POST     /api/games/
api.game_status   GET      /api/games/
api.make_move     PATCH    /api/games/
auth.login        GET      /login
auth.login_post   POST     /login
auth.logout       GET      /logout
auth.signup       GET      /signup
auth.signup_post  POST     /signup
main.index        GET      /
main.profile      GET      /profile
static            GET      /static/<path:filename>

example:
player 1 starts a game
```
grid = "CCCCC.....BBBB......RRR.......SSS.......DD.........................................................."
data = {'name': 'player1',
        'grid': str(grid)}
create_game_response = requests.post("http://127.0.0.1:5000/api/games/", json=data)
```

player 2 joins a started game
```
grid = "..........BBBB......RRR.......SSS.......DD.....................................................CCCCC"
data = {'name': 'player2',
        'grid': str(grid)}
create_game_response = requests.post("http://127.0.0.1:5000/api/games/", json=data)
```

player 1 asks for game_status
```
data = {'name': 'player1', 'game_id': 1}
game_status_response = session.get("http://127.0.0.1:5000/api/games/", json=data)
```

player 1 attacks the board
```
data = {'name': 'player1', 'game_id': 1, 'x': 0, 'y': 0}
game_attack = session.patch("http://127.0.0.1:5000/api/games/", json=data)
api_game_attack_response = json.loads(game_attack.content)
```

from app import db
from enum import Enum, auto


class Grid(db.Model):
    __tablename__ = 'grids'
    id = db.Column(db.Integer, primary_key=True)

    start_grid = db.Column(db.String(100))
    game_grid = db.Column(db.String(100))

    player = db.relationship('Player', back_populates='grid')
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))

    def __init__(self, start_grid):
        self.validate_game_grid(start_grid)

        super().__init__(start_grid=start_grid,
                         game_grid=start_grid)

    def can_attack(self):
        pass

    def attack(self):
        pass

    def validate_game_grid(self, grid):
        pass


class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    grid = db.relationship('Grid', back_populates='player', uselist=False)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    game = db.relationship('Game', back_populates='players')


class GameState(Enum):
    """ The states that represent the progression of the game.
    At the start when a player creates a game it is waiting for another player to join.
    After a second player joins the state should become IN_PROGRESS
    When the game is finished the state should be FINISHED.
    """
    WAITING = auto()
    IN_PROGRESS = auto()
    FINISHED = auto()


class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.Enum(GameState))
    players = db.relationship('Player', back_populates='game', order_by='Player.id')

    def __init__(self):
        super().__init__()
        self.state = GameState.WAITING

    def save(self):
        db.session.add(self)
        db.session.commit()

    def join(self, player):
        pass

    def attack(self, player_name, x, y):
        pass

    def winner(self):
        pass

    def save_to_db(self):
        pass

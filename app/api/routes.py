from flask import current_app
from flask import jsonify, request

from app.api import bp
from app.api.models import Game, Board, Player


@bp.route('/games/', methods=['POST'])
def create_game():
    data = request.json
    name, grid = data['name'], data['grid']
    g = Game.get_new_game()
    try:
        b = Board(grid)
    except ValueError as e:
        raise ValueError(str(e))

    p = Player(name=name, board=b)
    g.join(p)
    g.save_to_db()
    current_app.logger.info(f'Player {name} joined game {g.id}')
    return jsonify({'message': 'game created!', 'game_id': str(g.id)})


@bp.route('/games/', methods=['PATCH'])
def make_move():
    data = request.json
    game_id, name = data['game_id'], data['name']
    x, y = data['x'], data['y']
    g = Game.query.get(game_id)
    return jsonify({'result': str(g.shoot(player_name=name, x=x, y=y))})


@bp.route('/games/', methods=['GET'])
def game_status():
    data = request.json
    g = Game.query.get(data['game_id'])
    name = data['name']
    asking, other = (g.current, g.other) if g.current.name == name else (g.other, g.current)

    return jsonify({'state': str(g.state),
                    'your_board': asking.board.grid,
                    'enemy_board': other.board.enemy_view()})


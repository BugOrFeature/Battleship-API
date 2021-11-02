import pytest

from app.api.models import Grid, Player


@pytest.fixture(scope='module')
def app():
    from app import create_app

    app = create_app()

    ctx = app.app_context()
    ctx.push()

    yield app
    ctx.pop()


@pytest.fixture(scope='module')
def db(app):
    from app import db as _db
    _db.create_all()
    yield _db
    _db.drop_all()


@pytest.fixture()
def session(db):
    connection = db.engine.connect()
    transaction = connection.begin()

    session = db.create_scoped_session(options={'bind': connection, 'binds': {}})
    db.session = session

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope='module')
def test_client(app):
    return app.test_client()


@pytest.fixture
def player1(grid_factory):
    return Player(name='player1', grid=grid_factory())


@pytest.fixture
def player2(grid_factory):
    return Player(name='player2', grid=grid_factory())


@pytest.fixture
def grid_factory():
    empty_grid = [[0 for i in range(10)] for j in range(10)]
    test_grid = add_ship("Carrier", grid=empty_grid, start=(0, 0))
    test_grid = add_ship("Battleship", grid=test_grid, start=(0, 1))
    test_grid = add_ship("Cruiser", grid=test_grid, start=(0, 2))
    test_grid = add_ship("Submarine", grid=test_grid, start=(0, 3))
    test_grid = add_ship("Destroyer", grid=test_grid, start=(0, 4))

    grid_str = grid_to_string(test_grid)

    def create(grid=None):
        if grid is None:
            grid = grid_str
        return Grid(grid)

    return create


def grid_to_string(grid):
    flattend = [y for x in grid for y in x]
    return ''.join(map(str, flattend))


def add_ship(ship_name, grid, start, vertical=True):
    x, y = start
    ships_length = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
    ship_encoding = {'Carrier': 1, 'Battleship': 2, 'Cruiser': 3, 'Submarine': 4, 'Destroyer': 5}
    if vertical:
        for i in range(0, ships_length[ship_name]):
            grid[x + i][y] = ship_encoding[ship_name]
    if not vertical:
        for i in range(0, ships_length[ship_name]):
            grid[x][y + i] = ship_encoding[ship_name]

    return grid

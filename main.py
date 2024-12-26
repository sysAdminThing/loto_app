from .game import *
from . import *


main = Blueprint('/', __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/pick_number", methods=["POST"])
def pick_number_route():
    # Retrieve numbers from session, or initialize if not present
    if 'taken_numbers' not in session:
        session['taken_numbers'] = []
    return jsonify({"data": pick_number()})


@main.route("/show_all_picked", methods=["GET"])
def show_all_picked_route():
    # Retrieve numbers from session
    if 'taken_numbers' not in session:
        session['taken_numbers'] = []
    return show_all_picked()


@main.route("/show_last_number", methods=["GET"])
def show_last_number_route():
    # Retrieve numbers from session
    if 'taken_numbers' not in session:
        session['taken_numbers'] = []
    return show_last_number()


@main.route("/clear_number", methods=["POST"])
def clear_number_route():
    clear_number()
    return jsonify({"message": "Numbers cleared"})


@main.route("/start_new_game", methods=["POST"])
def start_new_game_route():
    start_new_game()
    return jsonify({"message": "New game started"})


from .game import *
from . import *


main = Blueprint('/', __name__)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('/.login'))
        return f(*args, **kwargs)
    return decorated_function

@main.route("/")
@login_required
def index():
    return render_template("index.html")

@main.route("/pick_number", methods=["POST"])
@login_required
def pick_number_route():
    # Retrieve numbers from session, or initialize if not present
    if 'taken_numbers' not in session:
        session['taken_numbers'] = []
    return jsonify({"data": pick_number()})

@main.route("/show_all_picked", methods=["GET"])
@login_required
def show_all_picked_route():
    # Retrieve numbers from session
    if 'taken_numbers' not in session:
        session['taken_numbers'] = []
    return show_all_picked()


@main.route("/show_last_number", methods=["GET"])
@login_required
def show_last_number_route():
    # Retrieve numbers from session
    if 'taken_numbers' not in session:
        session['taken_numbers'] = []
    return show_last_number()


@main.route("/clear_number", methods=["POST"])
@login_required
def clear_number_route():
    clear_number()
    return jsonify({"message": "Numbers cleared"})

@main.route("/start_new_game", methods=["POST"])
@login_required
def start_new_game_route():
    start_new_game()
    return jsonify({"message": "New game started"})


@main.route('/login', methods=['POST','GET'])
def login():
    if 'username' in session:
        print('true')
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username=='loto_game' and password=='loto_game123!':
            session['username'] = username
            return redirect(url_for('/.index'))
        else:
            pass
    return render_template("login.html")



from . import os, json, random, jsonify



# Path to the file where numbers will be saved
data_file = "taken_numbers.json"

def load_data():
    # Check if the file exists, and load the data if it does
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    # Save the data back to the file
    with open(data_file, "w") as f:
        json.dump(data, f)

# Initialize taken_numbers by loading the saved data
taken_numbers = load_data()

def show_all_picked():
    return jsonify({"data": taken_numbers})

def show_last_number():
    if taken_numbers:
        return jsonify({"data": taken_numbers[-1]})
    else:
        return jsonify({"data": "no data"})

def pick_number():
    while True:
        random_number = random.randint(1, 90)
        if random_number not in taken_numbers:
            taken_numbers.append(random_number)
            save_data(taken_numbers)  # Save data to file after every pick
            return taken_numbers
        else:
            continue

def clear_number():
    taken_numbers.clear()
    save_data(taken_numbers)  # Clear data in the file as well

def start_new_game():
    clear_number()  # Clear the numbers and reset the game

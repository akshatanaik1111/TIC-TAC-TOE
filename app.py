from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

board = [""] * 9
current_player = "X"

def check_winner():
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] != "":
            return board[cond[0]]
    return None

@app.route("/", methods=["GET", "POST"])
def index():
    global current_player

    winner = check_winner()

    if request.method == "POST" and not winner:
        move = int(request.form["move"])
        if board[move] == "":
            board[move] = current_player
            current_player = "O" if current_player == "X" else "X"

    winner = check_winner()

    return render_template("index.html", board=board, winner=winner)

@app.route("/reset")
def reset():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
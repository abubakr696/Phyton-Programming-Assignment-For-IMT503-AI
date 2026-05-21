from flask import Flask, render_template, request, session
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=["GET", "POST"])
def game():
    message = ""
    game_over = False
    
    # Start new game if needed
    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["attempts"] = 0
    
    if request.method == "POST":
        # Reset game
        if "reset" in request.form:
            session.clear()
            return render_template("index.html", message="New game started! Guess 1-100.")
        
        # Process guess
        try:
            guess = int(request.form["guess"])
            session["attempts"] += 1
            
            if guess < session["number"]:
                message = "Too low!"
            elif guess > session["number"]:
                message = "Too high!"
            else:
                message = f"Correct! You got it in {session['attempts']} attempts."
                game_over = True
                
        except ValueError:
            message = "Enter a valid number between 1 and 100."
    
    return render_template("index.html", 
                           message=message, 
                           attempts=session.get("attempts", 0),
                           game_over=game_over)

if __name__ == "__main__":
    app.run(debug=True)
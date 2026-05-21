from flask import Flask, render_template, request

app = Flask(__name__)

def encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted += new_char
        else:
            encrypted += char
    return encrypted

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    message = ""
    shift = ""
    action = ""
    
    if request.method == "POST":
        message = request.form["message"]
        shift = int(request.form["shift"])
        action = request.form["action"]
        
        if action == "decrypt":
            shift = -shift
        
        result = encrypt(message, shift)
    
    return render_template("index.html", 
                           result=result, 
                           message=message, 
                           shift=shift if shift != "" else "",
                           action=action)

if __name__ == "__main__":
    app.run(debug=True)
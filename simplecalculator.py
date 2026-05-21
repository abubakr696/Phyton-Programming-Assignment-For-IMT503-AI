from flask import Flask, render_template, request

app = Flask(__name__)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    num1 = num2 = choice = ""
    
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            choice = request.form["choice"]
            
            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)
            else:
                result = "Invalid choice!"
                
        except ValueError:
            result = "Error! Please enter valid numbers."
    
    return render_template("index.html", 
                           result=result, 
                           num1=num1, 
                           num2=num2, 
                           choice=choice)

if __name__ == "__main__":
    app.run(debug=True)
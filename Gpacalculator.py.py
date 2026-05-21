from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "gpa_secret_key"

def get_grade(score):
    if score >= 70:
        return "A", 5
    elif score >= 60:
        return "B", 4
    elif score >= 50:
        return "C", 3
    elif score >= 45:
        return "D", 2
    elif score >= 40:
        return "E", 1
    else:
        return "F", 0

@app.route("/", methods=["GET", "POST"])
def index():
    courses = session.get("courses", [])
    gpa = None
    error = None
    
    if request.method == "POST":
        if "add" in request.form:
            try:
                name = request.form["course_name"]
                score = int(request.form["score"])
                credit = int(request.form["credit"])
                
                if 0 <= score <= 100 and credit > 0:
                    grade, point = get_grade(score)
                    courses.append({"name": name, "score": score, "credit": credit, "grade": grade, "point": point})
                    session["courses"] = courses
                else:
                    error = "Score must be 0-100 and credit > 0"
            except ValueError:
                error = "Enter valid numbers only"
        
        elif "calc" in request.form and courses:
            total_points = sum(c["point"] * c["credit"] for c in courses)
            total_credits = sum(c["credit"] for c in courses)
            gpa = round(total_points / total_credits, 2)
        
        elif "reset" in request.form:
            session.clear()
            courses = []
    
    return render_template("index.html", courses=courses, gpa=gpa, error=error)

if __name__ == "__main__":
    app.run(debug=True)
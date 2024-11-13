from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated database for requests
outing_requests = {}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/student')
def student_portal():
    return render_template("student_portal.html")

@app.route('/teacher')
def teacher_portal():
    return render_template("teacher_portal.html", outing_requests=outing_requests)

@app.route('/submit_request', methods=["POST"])
def submit_request():
    student_name = request.form.get("name")
    if student_name:
        outing_requests[student_name] = "Pending"
    return redirect(url_for("home"))

@app.route('/approve/<student>')
def approve(student):
    outing_requests[student] = "Approved"
    return redirect(url_for("teacher_portal"))

@app.route('/deny/<student>')
def deny(student):
    outing_requests[student] = "Denied"
    return redirect(url_for("teacher_portal"))

if __name__ == "__main__":
    app.run(debug=True)

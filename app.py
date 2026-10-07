from flask import Flask, jsonify, render_template

app = Flask(__name__)

employees = [
    {
        "id": 1,
        "name": "Anas Qureshi",
        "role": "DevOps Engineer",
        "department": "Cloud & DevOps",
        "status": "Active"
    },
    {
        "id": 2,
        "name": "Rahul Sharma",
        "role": "Python Developer",
        "department": "Engineering",
        "status": "Active"
    },
    {
        "id": 3,
        "name": "Priya Patil",
        "role": "Cloud Engineer",
        "department": "Cloud",
        "status": "Active"
    },
    {
        "id": 4,
        "name": "Arjun Mehta",
        "role": "Software Engineer",
        "department": "Engineering",
        "status": "On Leave"
    }
]


@app.route("/")
def home():
    return render_template("index.html", employees=employees)


@app.route("/employees")
def get_employees():
    return jsonify(employees)


@app.route("/employees/<int:employee_id>")
def get_employee(employee_id):

    for employee in employees:
        if employee["id"] == employee_id:
            return jsonify(employee)

    return jsonify({"error": "Employee not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
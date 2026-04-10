from flask import Flask, request, jsonify
from flask_cors import CORS   # ✅ ADD THIS

app = Flask(__name__)
CORS(app)   # ✅ ADD THIS

students = []

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    students.append(data)
    return {"message": "Student added"}
@app.route('/students/<int:index>', methods=['DELETE'])
def delete_student(index):
    if index < len(students):
        students.pop(index)
        return {"message": "Deleted"}
    return {"error": "Invalid index"}

if __name__ == '__main__':
    app.run(debug=True)
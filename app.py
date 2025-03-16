from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 메모리 내 할 일 목록
todos = []

# 메인 페이지
@app.route("/")
def index():
    return render_template("index.html", todos=todos)

# 할 일 추가
@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    new_todo = {"id": len(todos) + 1, "content": data["content"]}
    todos.append(new_todo)
    return jsonify({"message": "추가 완료!"})

# 할 일 삭제
@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    global todos
    todos = [todo for todo in todos if todo["id"] != id]  # 해당 ID를 가진 할 일 삭제
    return jsonify({"message": "삭제 완료!"})

if __name__ == "__main__":
    app.run(debug=True)


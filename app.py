from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

# 데이터베이스 모델
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

# 데이터베이스 초기화
with app.app_context():
    db.create_all()

# 메인 페이지
@app.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)

# 할 일 추가
@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    new_todo = Todo(content=data["content"])
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({"message": "추가 완료!"})

# 할 일 삭제
@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    todo = Todo.query.get(id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return jsonify({"message": "삭제 완료!"})

if __name__ == "__main__":
    app.run(debug=True)

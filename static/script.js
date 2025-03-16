document.getElementById("todo-form").addEventListener("submit", function(event) {
    event.preventDefault();
    const todoInput = document.getElementById("todo-input");
    const todoText = todoInput.value.trim();

    if (todoText !== "") {
        fetch("/add", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ content: todoText })
        })
        .then(response => response.json())
        .then(() => {
            location.reload();  // 새로고침해서 리스트 업데이트
        });
    }

    todoInput.value = "";  // 입력 필드 비우기
});

function deleteTodo(id) {
    fetch(`/delete/${id}`, { method: "POST" })
    .then(response => response.json())
    .then(() => {
        location.reload();  // 삭제 후 새로고침
    });
}
